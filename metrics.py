"""
G-Eval 기반 커스텀 메트릭: "좋은 요약문"의 기준을 정의.

5개 차원으로 평가:
1. 축약성 (Concision) — 핵심만 간결하게
2. 정확성 (Accuracy) — 원본 내용 왜곡 없음
3. 가독성 (Readability) — 읽기 쉬운 구조와 흐름
4. 완결성 (Completeness) — 중요 정보 누락 없음
5. 객관성 (Objectivity) — 편향 없이 사실 전달
"""

from deepeval.metrics import GEval
from deepeval.test_case import SingleTurnParams

from deepeval.models import AnthropicModel, DeepEvalBaseLLM


def create_metrics(
    model: DeepEvalBaseLLM | None = None,
    threshold: float = 0.7,
) -> list[GEval]:
    model = model or AnthropicModel()

    params = [
        SingleTurnParams.INPUT,
        SingleTurnParams.ACTUAL_OUTPUT,
        SingleTurnParams.EXPECTED_OUTPUT,
    ]

    return [
        GEval(
            name="축약성",
            criteria="요약문이 원본의 핵심 내용을 효율적으로 압축했는가? 불필요한 반복과 장식적 표현은 없는가? 단, 핵심 정보를 전달하기 위해 필요한 분량은 허용한다.",
            evaluation_steps=[
                "요약문이 원본 대비 의미 있는 길이 축소를 이뤘는지 확인 (정보 밀도 관점)",
                "같은 의미가 불필요하게 반복되지 않았는지 확인",
                "핵심과 무관한 부연 설명, 예시, 수식어가 과도하게 포함되지 않았는지 확인",
                "expected_output(골든)의 분량과 압축 수준과 비슷한지 참고",
            ],
            evaluation_params=params,
            threshold=threshold,
            model=model,
        ),
        GEval(
            name="정확성",
            criteria="요약문의 모든 내용이 원본 텍스트에 근거하는가? 왜곡, 과장, 날조된 내용이 없는가?",
            evaluation_steps=[
                "요약문의 각 핵심 주장이 원본에서 확인 가능한지 검증",
                "수치, 이름, 날짜 등 구체적 정보가 정확한지 확인",
                "원본의 맥락을 왜곡하지 않았는지 확인",
            ],
            evaluation_params=params,
            threshold=threshold,
            model=model,
        ),
        GEval(
            name="가독성",
            criteria="요약문이 읽기 쉬운 구조와 흐름을 갖추고 있는가? 문장 간 연결이 자연스러운가?",
            evaluation_steps=[
                "문장 구조가 명확하고 간단한지 확인",
                "정보의 배치 순서가 논리적인지 확인",
                "문단/문장 간 전환이 자연스러운지 확인",
            ],
            evaluation_params=[
                SingleTurnParams.INPUT,
                SingleTurnParams.ACTUAL_OUTPUT,
            ],
            threshold=threshold,
            model=model,
        ),
        GEval(
            name="완결성",
            criteria="원본에서 중요한 핵심 정보가 누락되지 않았는가?",
            evaluation_steps=[
                "원본의 핵심 주장/사실 중 요약문에 빠진 것이 있는지 확인",
                "expected_output(골든)에 포함된 핵심 포인트가 actual_output에도 담겼는지 비교",
                "누락된 정보가 사소한지 중요한지 판단",
            ],
            evaluation_params=params,
            threshold=threshold,
            model=model,
        ),
        GEval(
            name="객관성",
            criteria="요약문이 편향 없이 사실을 전달하는가? 작성자의 의견이나 감정이 개입되지 않았는가?",
            evaluation_steps=[
                "주관적 판단이나 평가가 포함되었는지 확인",
                "원본에 없는 의견이나 추론이 추가되었는지 확인",
                "감정적 표현이나 선정적 표현이 있는지 확인",
            ],
            evaluation_params=[
                SingleTurnParams.INPUT,
                SingleTurnParams.ACTUAL_OUTPUT,
            ],
            threshold=threshold,
            model=model,
        ),
    ]
