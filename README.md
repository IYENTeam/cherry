# Cherry

LLM 요약 품질 평가 프레임워크. 골든 데이터셋과 G-Eval 기반 커스텀 메트릭으로 프롬프트별 요약 성능을 비교합니다.

## 구조

```
evaluate.py          # 평가 파이프라인 (프롬프트 v1/v2/v3 비교)
metrics.py           # G-Eval 커스텀 메트릭 5종 (축약성·정확성·가독성·완결성·객관성)
golden_dataset.py    # 골든 데이터셋 17개 (뉴스·기술블로그·오픈소스·AI/ML)
```

## 평가 메트릭

| 메트릭 | 기준 |
|--------|------|
| 축약성 | 핵심만 간결하게 압축했는가 |
| 정확성 | 원본 내용 왜곡·날조 없는가 |
| 가독성 | 읽기 쉬운 구조와 흐름인가 |
| 완결성 | 중요 정보 누락 없는가 |
| 객관성 | 편향 없이 사실만 전달하는가 |

## 설치

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 설정

`.env.example`을 `.env`로 복사하고 API 키를 입력합니다.

```bash
cp .env.example .env
```

```env
ANTHROPIC_API_KEY=sk-ant-your-key
EVAL_MODEL=claude-sonnet-4-5-20250929
GENERATION_MODEL=claude-sonnet-4-5-20250929
```

## 실행

```bash
python evaluate.py
```

3개 프롬프트 버전(v1, v2, v3)으로 골든 데이터셋의 요약을 생성하고, 5개 메트릭으로 각각 평가한 뒤 전체/카테고리별 점수표를 출력합니다.
