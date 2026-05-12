"""
평가 파이프라인: 골든 데이터셋 → 프롬프트로 요약 생성 → 메트릭 평가 → 결과 비교.

사용법:
    python evaluate.py

환경변수 (.env 파일):
    ANTHROPIC_API_KEY  - Anthropic API 키
    EVAL_MODEL         - 평가용 모델 (기본: claude-sonnet-4-5-20250929)
    GENERATION_MODEL   - 요약 생성용 모델 (기본: claude-sonnet-4-5-20250929)
"""

import os
import sys
from collections import defaultdict

from deepeval.models import AnthropicModel
from dotenv import load_dotenv

from golden_dataset import load_golden_dataset
from metrics import create_metrics

load_dotenv()

# Force unbuffered output
sys.stdout.reconfigure(line_buffering=True)

PROMPT_V1 = """다음 글을 3문장으로 요약해주세요.

{input}"""

PROMPT_V2 = """다음 글을 한국어 3문장으로 요약하세요.

규칙:
- 정확히 3문장으로 작성
- 1번째 문장: 이 글이 다루는 대상이 무엇인지 정의
- 2번째 문장: 핵심 메커니즘이나 특징
- 3번째 문장: 사용자/독자가 얻는 가치 또는 활용 관점
- 객관적이고 담담한 어조 (감탄사, 수식어 자제)
- 원본에 없는 내용 추가 금지

글:
{input}"""

PROMPT_V3 = """당신은 기술 콘텐츠를 명확하게 압축하는 편집자입니다.
다음 글을 한국어 3문장으로 요약하세요.

요약 구조 (반드시 이 순서):
1. **정의 문장**: "[이름]은(는) [무엇을 하는 도구/연구/뉴스]입니다." 형식으로 시작
2. **핵심 특징 문장**: 다른 것과 구별되는 메커니즘, 접근법, 또는 특별한 점
3. **가치 문장**: 어떤 사용자에게 어떤 의미가 있는지 (활용 관점)

작성 원칙:
- 정확히 3문장
- 각 문장은 서로 다른 정보를 담을 것 (반복 금지)
- 원본의 고유명사(제품명, 기술명)는 보존
- 추측, 평가, 감탄사 사용 금지
- "~한다"보다는 "~합니다" 어조 사용

예시 형식:
"[제품명]은 [한 줄 정의]입니다. [핵심 차별점]을 통해 [작동 방식]을 보여줍니다. [대상 사용자]에게 [구체적 가치]를 제공합니다."

글:
{input}"""


def generate_summary(
    prompt_template: str, input_text: str, model: "DeepEvalBaseLLM"
) -> str:
    prompt = prompt_template.format(input=input_text)
    return model.generate(prompt)


def run_evaluation():
    eval_model = AnthropicModel(
        model=os.environ.get("EVAL_MODEL", "claude-sonnet-4-5-20250929"),
    )
    gen_model = AnthropicModel(
        model=os.environ.get("GENERATION_MODEL", "claude-sonnet-4-5-20250929"),
    )

    dataset = load_golden_dataset()
    metrics = create_metrics(model=eval_model)

    prompts = {"v1": PROMPT_V1, "v2": PROMPT_V2, "v3": PROMPT_V3}
    # Track per-entry results with category metadata
    # results[version][(metric_name, category)] = [scores]
    results: dict[str, dict[tuple[str, str], list[float]]] = {
        v: defaultdict(list) for v in prompts
    }

    for version, template in prompts.items():
        print(f"\n{'=' * 60}")
        print(f"프롬프트 {version} 평가 중...")
        print(f"{'=' * 60}")

        for i, golden in enumerate(dataset.goldens):
            summary = generate_summary(template, golden.input, gen_model)
            category = (
                golden.additional_metadata.get("category", "미분류")
                if golden.additional_metadata
                else "미분류"
            )

            if not summary or not summary.strip():
                print(f"\n[{i + 1}/{len(dataset.goldens)}] [{category}] 빈 응답, 스킵")
                for m in metrics:
                    results[version][(m.name, category)].append(0.0)
                continue

            print(
                f"\n[{i + 1}/{len(dataset.goldens)}] [{category}] 생성된 요약:\n{summary[:100]}..."
            )

            for metric in metrics:
                from deepeval.test_case import LLMTestCase

                test_case = LLMTestCase(
                    input=golden.input,
                    actual_output=summary,
                    expected_output=golden.expected_output,
                )
                metric.measure(test_case)
                results[version][(metric.name, category)].append(metric.score)
                print(f"  {metric.name}: {metric.score:.2f} - {metric.reason[:80]}...")

    metric_names = [m.name for m in metrics]
    categories = sorted({cat for v in results for (_, cat) in results[v]})

    print(f"\n{'=' * 60}")
    print("전체 결과 요약")
    print(f"{'=' * 60}")
    _print_score_table(metric_names, prompts, results, categories=None)

    for cat in categories:
        print(f"\n{'=' * 60}")
        print(f"카테고리: {cat}")
        print(f"{'=' * 60}")
        _print_score_table(metric_names, prompts, results, categories=[cat])

    best = max(
        results,
        key=lambda v: sum(s for scores in results[v].values() for s in scores),
    )
    print(f"\n최고 프롬프트: {best}")


def _print_score_table(
    metric_names: list[str],
    prompts: dict[str, str],
    results: dict[str, dict[tuple[str, str], list[float]]],
    categories: list[str] | None = None,
):
    header = f"{'메트릭':<12}" + "".join(
        f"{'v' + str(v):>10}" for v in range(1, len(prompts) + 1)
    )
    print(header)
    print("-" * len(header))

    for name in metric_names:
        row = f"{name:<12}"
        for version in prompts:
            if categories:
                vals = []
                for cat in categories:
                    vals.extend(results[version].get((name, cat), []))
            else:
                vals = [
                    s
                    for (mn, _), scores in results[version].items()
                    if mn == name
                    for s in scores
                ]
            avg = sum(vals) / len(vals) if vals else 0
            row += f"{avg:>10.2f}"
        print(row)

    total_row = f"{'평균':<12}"
    for version in prompts:
        all_scores: list[float] = []
        for (mn, cat), scores in results[version].items():
            if categories and cat not in categories:
                continue
            all_scores.extend(scores)
        avg = sum(all_scores) / len(all_scores) if all_scores else 0
        total_row += f"{avg:>10.2f}"
    print(total_row)


if __name__ == "__main__":
    run_evaluation()
