"""
골든 데이터셋: "좋은 요약문"의 기준이 되는 17개 예시.

각 항목은 input(원본 텍스트)과 expected_output(좋은 요약문)의 쌍입니다.
additional_metadata에 category를 저장하여 카테고리별 분석에 활용합니다.
"""

from deepeval.dataset import EvaluationDataset, Golden

CATEGORIES = [
    "뉴스 요약",
    "기술 블로그",
    "오픈소스 도구",
    "AI/ML 연구",
]

SAMPLE_GOLDENS: list[Golden] = [
    Golden(
        input="""
삼성전자가 2025년 1분기 실적 발표에서 매출 79조원, 영업이익 6조 6000억원을 기록했다고 밝혔다.
이는 전년 동기 대비 매출은 10% 증가, 영업이익은 30% 증가한 수치다.
반도체 부문의 적자가 줄어들고 AI 관련 수요가 견조한 것이 주요 요인으로 분석됐다.
DS(메모리) 부문은 HBM 수요 증가로 인해 전 분기 대비 적자 폭을 대폭 축소했다.
스마트폰 부문은 갤럭시 S25 시리즈의 선방에 힘입어 견고한 실적을 유지했다.
""".strip(),
        expected_output="""
삼성전자 2025년 Q1 실적: 매출 79조원(+10% YoY), 영업이익 6.6조원(+30% YoY).
핵심 동력: 반도체 적자 축소(HBM 수요) + 갤럭시 S25 호조. AI 수요 견고함이 전반적인 개선을 견인.
""".strip(),
        additional_metadata={"category": "뉴스 요약"},
    ),
    Golden(
        input="""
React 19가 정식 출시되었다. 가장 큰 변화는 Server Components가 안정화되었고,
use() 훅이 추가되었다는 점이다. 이제 컴포넌트 내에서 직접 Promise와 Context를 읽을 수 있다.
또한 Actions 개념이 도입되어 폼 제출과 상태 업데이트가 간소화되었다.
useFormStatus, useActionState, useOptimistic 등의 새로운 훅이 추가되어
비동기 상태 관리가 훨씬 직관적으로 변했다. 기존 forwardRef가 더 이상 필요 없어졌고,
ref를 일반 prop으로 전달할 수 있게 되었다.
""".strip(),
        expected_output="""
React 19 핵심 변경점: Server Components 안정화, use() 훅(Promise/Context 직접 읽기) 추가.
Actions 도입으로 폼/비동기 상태 관리 간소화 (useFormStatus, useActionState, useOptimistic).
forwardRef 폐지, ref 일반 prop化.
""".strip(),
        additional_metadata={"category": "기술 블로그"},
    ),
    Golden(
        input="""OpenAI's revised Microsoft pact lets it sell AI models across multiple clouds, enabling a likely expansion with Amazon and broader enterprise distribution.

Why it matters: The shift ends OpenAI's effective cloud exclusivity, widening its reach to customers using AWS, Google Cloud or others — and intensifying AI platform competition.

Driving the news: A rewritten deal frees OpenAI to sell through any cloud, caps Microsoft's cut of OpenAI revenue and scraps a controversial provision that would have changed the companies' business relationship once artificial general intelligence (AGI) was achieved.

The revised Microsoft-OpenAI arrangement makes room for Amazon and likely AWS distribution. The revised pact changes revenue-sharing and cloud distribution terms. The article frames the move as part of a broader shift in the AI platform market and notes that both Microsoft and OpenAI gain different strategic benefits. Amazon and OpenAI are positioned to act quickly after the change.""",
        expected_output="""OpenAI와 Microsoft의 수정된 계약은 OpenAI가 여러 클라우드를 통해 모델을 판매할 수 있는 길을 열었습니다.
이 변화는 Amazon, AWS 등 다른 클라우드와의 협력 가능성을 키우며 AI 플랫폼 경쟁 구도를 넓힙니다.
핵심은 클라우드 독점 완화, 수익 배분 조정, AGI 관련 조항 변경으로 요약됩니다.""",
        additional_metadata={"category": "뉴스 요약"},
    ),
    Golden(
        input="""Anthropic Labs가 공개한 Claude Design은 Claude를 글쓰기나 코드 작성 보조 도구로만 보는 관점에서 한 걸음 더 나아간 실험적 제품입니다. 사용자는 Claude와 대화하면서 디자인 초안, 프로토타입, 슬라이드, 원페이저 같은 시각적 결과물을 함께 만들 수 있습니다. 즉, 프롬프트의 결과가 텍스트 답변이 아니라 바로 편집 가능한 디자인 아티팩트가 되는 흐름을 보여줍니다.

Claude Design은 Claude Opus 4.7 비전 모델을 기반으로 하며, 현재는 Claude Pro, Max, Team, Enterprise 구독자를 대상으로 한 리서치 프리뷰 형태로 제공됩니다. Anthropic이 Labs라는 이름으로 내놓은 만큼, 완성된 대중용 디자인 툴이라기보다는 Claude가 시각적 작업 공간에서 어떤 협업자가 될 수 있는지를 검증하는 성격이 강합니다.

특히 Canva, Brilliant, Datadog 같은 파트너사가 언급된 점은 이 제품의 지향점을 잘 보여줍니다. 단순히 예쁜 이미지를 생성하는 것이 아니라, 실제 팀이 아이디어를 시각화하고, 초안을 협업 가능한 산출물로 옮기고, 빠르게 공유하는 업무 흐름을 겨냥합니다. Claude가 문서와 코드의 영역을 넘어 디자인 협업 인터페이스로 확장되는 사례로 볼 수 있습니다.""",
        expected_output="""Claude Design은 Claude와 함께 디자인 시안, 프로토타입, 슬라이드 등을 만드는 Anthropic Labs의 실험적 도구입니다.
텍스트 요청을 바탕으로 시각적 결과물을 빠르게 만들고 수정하는 협업형 제작 흐름을 보여줍니다.
AI가 단순 답변 도구를 넘어 디자인 작업의 초기 반복과 시각화까지 맡는 사례로 볼 수 있습니다.""",
        additional_metadata={"category": "뉴스 요약"},
    ),
    Golden(
        input="""AI 코딩 에이전트를 잘 쓰기 위해 필요한 것은 더 긴 프롬프트가 아니라 더 좋은 스펙입니다. 많은 사용자가 기능 요구사항, 배경 설명, 예외 조건을 한 번에 몰아넣으면 에이전트가 더 똑똑하게 일할 것이라고 기대하지만, 실제로는 컨텍스트가 커질수록 모델의 주의가 분산되고 중요한 경계 조건을 놓치기 쉽습니다.

이 글의 핵심은 스마트 스펙 작성입니다. 먼저 고수준의 목표와 몇 가지 핵심 요구사항을 또렷하게 제시하고, 에이전트가 이를 바탕으로 상세 계획을 확장하도록 만듭니다. 이후 Claude Code의 Plan Mode처럼 읽기 전용으로 코드베이스를 분석하게 한 뒤, 아키텍처와 테스트 전략, 보안 위험을 검토하고 충분히 정제된 계획이 나왔을 때만 실행 단계로 넘어갑니다.

또한 좋은 스펙은 한 번 쓰고 버리는 문서가 아니라 프로젝트와 함께 진화하는 기준점이어야 합니다. SPEC.md 같은 파일로 남겨두면 에이전트를 재시작하거나 세션이 길어져도 같은 목표와 제약을 유지할 수 있습니다. 결국 스펙 기반 워크플로우의 목표는 AI에게 모든 것을 맡기는 것이 아니라, AI가 벗어나지 말아야 할 방향과 검증 기준을 명확히 제공하는 것입니다.

TL;DR: 명확한 명세, 큰 작업의 작은 단위 분해, 읽기 전용 계획 모드, 지속적 개선이 중요하다. 스마트 스펙은 에이전트를 명확히 안내하고, 컨텍스트 크기 내에 유지되며, 프로젝트와 함께 진화하는 문서다. 고수준 목표와 핵심 요구사항을 먼저 제시하고, 에이전트가 세부 스펙을 확장하게 하는 방식이 권장된다. Claude Code의 Plan Mode를 사용해 코드베이스 분석과 계획 수립을 먼저 수행하고, 계획이 충분히 정제된 후 실행한다. SPEC.md 같은 파일에 확정된 스펙을 저장해 세션 사이의 망각을 줄인다. Commands, Testing, Project Structure, Code Style, Git Workflow, Boundaries 같은 영역이 중요하다.""",
        expected_output="""이 글은 AI 에이전트에게 일을 맡길 때 좋은 스펙을 어떻게 작성해야 하는지 설명합니다.
목표, 범위, 제약, 성공 기준, 예외 상황을 명확히 적어야 에이전트가 중간에 길을 잃지 않습니다.
코딩 에이전트나 업무 자동화 도구를 쓸 때 프롬프트보다 '작업 명세서'가 중요하다는 관점을 제공합니다.""",
        additional_metadata={"category": "기술 블로그"},
    ),
    Golden(
        input="""Y Combinator의 Requests for Startups(RFS)는 단순한 트렌드 예측 목록이라기보다, "지금 창업자들이 시도하면 좋을 문제"를 공개적으로 던지는 신호에 가깝습니다. 2026년 여름 버전에서는 AI가 하나의 기능을 넘어 소프트웨어, 서비스, 반도체, 물리 세계를 다시 설계하는 기반 기술로 자리 잡고 있다는 점이 전면에 놓입니다.

이번 목록에서 특히 눈에 띄는 방향은 AI 에이전트를 기존 인간용 소프트웨어의 부가 기능으로 보는 관점에서 벗어난다는 점입니다. 에이전트가 버튼을 누르고 폼을 채우는 방식은 느리고 불안정합니다. 앞으로의 소프트웨어는 사람이 보는 대시보드뿐 아니라, 에이전트가 바로 이해하고 호출할 수 있는 API, MCP, CLI, 문서화된 작업 인터페이스를 갖춰야 합니다.

따라서 이 글은 "YC가 어떤 회사를 투자할 것인가"보다 넓은 의미를 갖습니다. 이미 자신이 고민하던 아이디어가 목록에 있다면, 그것은 시장의 방향과 문제의식이 맞닿아 있다는 신호가 될 수 있습니다. 반대로 아직 구체적인 아이디어가 없다면, AI 인프라와 에이전트 네이티브 소프트웨어가 앞으로 어떤 식으로 재구축될지 살펴보는 참고 자료가 됩니다.""",
        expected_output="""YC의 Requests for Startups 2026은 다음 세대 스타트업이 풀어볼 만한 문제들을 제안하는 목록입니다.
특히 에이전트 네이티브 소프트웨어, AI 운영체제, 업무 자동화처럼 AI가 제품 구조 자체를 바꾸는 영역이 강조됩니다.
창업 아이디어를 찾는 개발자에게 단순 트렌드가 아니라 문제 정의 관점의 참고 자료가 됩니다.""",
        additional_metadata={"category": "기술 블로그"},
    ),
    Golden(
        input="""[YOLO](https://pjreddie.com/darknet/yolo/) (You Only Look Once)는 가장 빠르고 인기 있는 객체 팀지 모델 중 하나입니다. [YOLOv5](https://github.com/ultralytics/yolov5)는 오픈 소스로 구현된 YOLO 최신 버전입니다(추론을 위해 PyTorch 허브에서 YOLOv5를 로드하는 빠른 테스트는 [여기](https://pytorch.org/hub/ultralytics_yolov5/) 참조). Object Detection with YOLOv5 Android 샘플 앱은 스크립트화된 PyTorch YOLOv5 모델을 사용하여 훈련된 80개 클래스의 객체를 감지합니다.

2021년 9월 30일 업데이트: YOLOv5 모델(전이 학습이라고도 함)을 미세 조정(fine-tune)하기 위해 사용자 지정 데이터 세트를 사용하는 섹션과 사용자 지정 모델을 사용하도록 Android 프로젝트를 변경하는 단계가 추가되었습니다.

전제조건: PyTorch 1.10.0, torchvision 0.11.1, Python 3.8, pytorch_android_lite 1.10.0, pytorch_android_torchvision_lite 1.10.0, Android Studio 4.0.1 이상. 빠른 시작은 모델 준비, Android 프로젝트 assets 폴더에 모델 배치, 앱 실행으로 이어진다. YOLOv5 저장소의 export.py를 수정해 TorchScript Lite 모델을 생성하는 과정이 안내된다. 커스텀 데이터셋을 활용한 전이 학습과 사용자 지정 모델을 Android 프로젝트에 반영하는 섹션이 있다. 예제로 aicook 데이터셋을 사용해 냉장고 재료 탐지를 미세 조정한다.""",
        expected_output="""이 글은 Android 앱에서 PyTorch Lite와 YOLOv5 모델을 이용해 객체 탐지를 실행하는 예제 프로젝트를 안내합니다.
COCO 80개 클래스 탐지부터 커스텀 데이터셋으로 fine-tune한 모델 적용까지 필요한 절차를 단계적으로 설명합니다.
모바일 환경에서 PyTorch 모델을 실제 앱으로 배포하려는 개발자에게 빠른 시작점이 됩니다.""",
        additional_metadata={"category": "기술 블로그"},
    ),
    Golden(
        input="""AI 코딩 에이전트(AI Coding Agent)들이 쏟아지고 있는 지금, 이들이 내부적으로 어떻게 설계되어 있는지 정확히 아는 사람은 많지 않습니다. 블로그 포스트나 공식 문서는 대개 기능 소개와 사용법에 집중하지만, 실제 소스코드 수준에서 어떤 아키텍처 패턴을 채택했는지, 어떤 설계 결정을 내렸는지는 직접 코드를 뜯어봐야 알 수 있습니다. Awesome AI Anatomy는 바로 이 작업을 체계적으로 수행하는 오픈소스 프로젝트입니다. Claude Code, Dify, Browser Use, OpenHands, Cline, DeerFlow, Goose, Codex CLI 등 현재 가장 주목받는 AI 에이전트들의 소스코드를 직접 분석하고, 아키텍처 다이어그램·설계 패턴·보안 분석을 문서화하여 주간 업데이트로 공개합니다.

일반적인 Awesome List와 달리 각 분석 문서는 아키텍처 다이어그램, 코드 수준 참조, 보안 자세 분석, 프로젝트 간 비교표를 포함한다. 저장소에는 COMPARISON.md, CROSS-CUTTING.md, knowledge/ 같은 구조화된 분석 자료가 있다. 분석 대상 예시는 Claude Code, Dify, Browser Use, DeerFlow, Pi Mono 등이며, 각 프로젝트의 내부 구조와 특이점을 코드 수준에서 다룬다. 교차 분석에서는 도구 호출 루프, 컨텍스트 창 관리, 오류 복구 같은 공통 패턴과 과도한 파일 시스템 권한, 입력 검증 부족, 컨텍스트 오버플로우 같은 안티패턴을 정리한다. MIT 라이선스로 공개되어 개인·상업적 사용이 가능하다.""",
        expected_output="""Awesome AI Anatomy는 Claude Code, Dify, Browser Use 등 주요 AI 코딩 에이전트의 내부 구조를 코드 수준에서 분석하는 오픈소스 프로젝트입니다.
공식 문서가 기능 소개에 머무는 반면, 이 프로젝트는 아키텍처 다이어그램, 설계 패턴, 보안 이슈까지 정리합니다.
AI 에이전트를 직접 만들거나 비교하려는 개발자에게 구현 패턴과 안티패턴을 빠르게 파악할 수 있는 참고 자료가 됩니다.""",
        additional_metadata={"category": "오픈소스 도구"},
    ),
    Golden(
        input="""기업들은 AI를 사용해 지원자를 필터링합니다. Career-Ops는 그 반대편에서 지원자가 AI를 사용해 기업을 필터링할 수 있도록 설계된 오픈소스 취업 탐색 자동화 시스템입니다. 이 프로젝트를 만든 개발자는 수개월간 수동으로 구직 활동을 한 끝에 스스로 이 시스템을 구축했고, 740개 이상의 채용 공고를 평가하고 100개 이상의 맞춤형 이력서를 생성하여 Applied AI 헤드 포지션을 얻었습니다.

Career-Ops는 Claude Code를 기반으로 하며, AI 코딩 CLI가 가진 에이전트 능력을 취업 탐색 파이프라인으로 전환합니다. 단순한 키워드 매칭이 아닌, 지원자의 CV와 채용 공고를 실제로 비교·추론하여 적합도를 A-F 등급(10개 가중 차원)으로 평가합니다. Playwright를 통해 Greenhouse, Ashby, Lever 등 주요 채용 플랫폼의 채용 공고 페이지를 에이전트가 직접 탐색하고, 결과를 데이터베이스에 구조화하여 추적합니다. 중요한 것은 이 시스템이 절대 자동으로 지원서를 제출하지 않는다는 점입니다.

핵심은 채용 공고를 6개 블록으로 구조화해 평가하는 시스템이다. 블록에는 역할 요약, CV 매칭 분석, 레벨 전략 등이 포함되며, 화려한 공고 문구에서 실제 역할과 기대 성과를 분리한다. 지원자의 직접 경험, 전이 가능한 역량, 역량 격차를 구분하고, 시니어리티와 포지션 레벨의 정합성을 분석한다. Playwright로 Greenhouse, Ashby, Lever 등 채용 플랫폼을 탐색하고 결과를 데이터베이스에 구조화한다. 자동 지원서 제출은 하지 않고, 평가·준비는 AI가 담당하되 최종 결정과 제출은 사람이 한다.""",
        expected_output="""Career-Ops는 지원자가 AI를 활용해 채용 공고를 평가하고 맞춤형 이력서를 준비하도록 돕는 오픈소스 취업 탐색 자동화 시스템입니다.
Claude Code와 Playwright를 이용해 공고를 탐색하고, CV와의 적합도를 여러 차원에서 분석합니다.
자동 지원은 하지 않고 최종 판단은 사람이 유지한다는 점에서, 구직 과정을 보조하는 실용적 에이전트로 설계되어 있습니다.""",
        additional_metadata={"category": "오픈소스 도구"},
    ),
    Golden(
        input="""AI 도구를 활용하다 보면 같은 작업을 반복적으로 재시도하는 데 시간과 비용을 낭비하는 경우가 많습니다. 의도를 모호하게 전달하거나 형식을 지정하지 않으면, 모델은 잘못된 가정을 세우고 엉뚱한 결과물을 생성합니다. 이렇게 쌓이는 낭비는 하루에 50개의 프롬프트를 작성할 경우 수십 번의 재시도로 이어지며, 실제 비용과 시간에 직접적인 영향을 미칩니다. Prompt Master는 이 문제를 해결하기 위해 설계된 Claude 스킬(Skill)로, 어떤 AI 도구에도 최적화된 프롬프트를 단번에 작성해 줍니다.

Prompt Master의 핵심 철학은 "가장 좋은 프롬프트는 가장 긴 프롬프트가 아니라, 모든 단어가 결과에 기여하는 프롬프트"입니다. 대부분의 프롬프트 생성 도구들이 프롬프트를 더 길게 만드는 방향으로 동작하는 것과 달리, Prompt Master는 프롬프트를 더 날카롭게(sharper) 만드는 데 집중합니다. 사용자의 요청을 9가지 차원(작업, 입력, 출력, 제약, 맥락, 청중, 기억, 성공 기준, 예시)으로 분해하고, 누락된 핵심 정보가 있을 때는 최대 3개의 명확화 질문만 요청합니다.

Prompt Master는 Claude, ChatGPT, Gemini, o1/o3, Cursor, Claude Code, GitHub Copilot, Midjourney, DALL-E, Stable Diffusion, Sora, ElevenLabs, Zapier, Make 등 18개 이상의 AI 도구 프로파일을 내장하고 있습니다. 각 도구의 특성에 맞는 9가지 프롬프트 프레임워크인 RTF, CO-STAR, RISEN, CRISPE, Chain of Thought, Few-Shot, File-Scope Template, ReAct, Visual Descriptor 등을 자동으로 선택하고, 35가지 일반적인 프롬프트 실수 패턴을 감지해 교정합니다. 모든 요청을 7단계 파이프라인으로 처리한다: 대상 도구 감지, 9가지 의도 차원 추출, 명확화 질문, 프레임워크 자동 선택, 안전한 기법 적용, 토큰 효율성 감사, 프롬프트 전달.""",
        expected_output="""Prompt Master는 여러 AI 도구에 맞는 프롬프트를 자동으로 설계해주는 Claude Skill입니다.
사용자의 요청을 작업, 입력, 출력, 제약, 맥락 등으로 분해하고 도구별 프레임워크를 선택해 재시도 비용을 줄입니다.
긴 프롬프트보다 결과에 기여하는 단어만 남기는 '날카로운 프롬프트'를 지향한다는 점이 핵심입니다.""",
        additional_metadata={"category": "오픈소스 도구"},
    ),
    Golden(
        input="""oh-my-claude-sisyphus는 Anthropic의 차세대 개발 도구인 Claude Code SDK를 기반으로 설계된 고도화된 멀티 에이전트 오케스트레이션(Multi-Agent Orchestration) 프레임워크입니다. 이 도구의 등장 배경에는 최근 Anthropic의 정책 변화와 AI 개발 도구 생태계의 지각 변동이 밀접하게 연관되어 있습니다.

oh-my-claude-sisyphus 프로젝트는 oh-my-opencode 플러그인을 Claude Code에서 재현하려는 것을 목표로 하고 있습니다. 즉, 단순히 코드를 대신 작성해주는 보조 도구를 넘어, 개발자가 의도한 목표를 달성할 때까지 멈추지 않고 스스로 작업을 수행하는 자율적 시스템을 지향합니다. 프로젝트의 이름인 oh-my-opencode 플러그인이 제공하는 메인 에이전트인 '시시포스(Sisyphus)'에서 영감을 받았습니다.

기존의 AI 코딩 어시스턴트들이 단발성 질문에 답변하거나 짧은 코드 스니펫을 생성하는 데 그쳤다면, oh-my-claude-sisyphus는 복잡한 개발 워크플로우 전체를 관장합니다. 사용자가 단 한 번의 프롬프트로 기능을 요청하면, 시스템 내부에 존재하는 11개의 전문화된 에이전트들이 유기적으로 협력하여 요구사항 분석부터 구현, 테스트, 그리고 리팩토링까지 수행합니다.

OpenCode 플러그인은 Bun 런타임과 다중 LLM 제공자를 전제로 하고, oh-my-claude-sisyphus는 Claude Agent SDK와 ~/.claude/agents 설정을 중심으로 한다. 설치는 npm install -g oh-my-claude-sisyphus 형태로 진행되며, Claude Code와 유효한 구독 또는 API Key가 필요하다. MIT 라이선스로 공개되어 무료 사용과 수정, 재배포가 가능하다.""",
        expected_output="""oh-my-claude-sisyphus는 Claude Code SDK 기반의 멀티 에이전트 오케스트레이션 프레임워크입니다.
단발성 코드 생성이 아니라 요구사항 분석, 구현, 테스트, 리팩토링까지 여러 전문 에이전트가 이어서 수행하도록 설계되었습니다.
개발자가 세세하게 지시하지 않아도 작업 완료 상태까지 밀고 가는 위임형 AI 개발 도구를 지향합니다.""",
        additional_metadata={"category": "오픈소스 도구"},
    ),
    Golden(
        input="""2026년 4월 공개된 Claude Design은 LLM이 단순히 문장을 작성하는 수준을 넘어, 프로토타입과 슬라이드, 원페이저 같은 시각적 산출물을 직접 만들어낼 수 있음을 보여주었습니다. 다만 이 흐름이 실제 팀의 워크플로우에 들어가려면 한 가지 문제가 남습니다. 클라우드 전용 제품에 묶이면 자체 배포, 사내 모델 연동, 도구 체인 커스터마이징이 모두 제한되기 때문입니다.

Open Design은 이 제약을 풀기 위해 등장한 오픈소스 AI 디자인 도구입니다. 사용자의 로컬 환경에서 데몬을 실행하고, 웹 앱을 통해 프롬프트와 결과물을 주고받으며, 필요하면 Vercel 같은 클라우드에도 배포할 수 있도록 설계되었습니다. 특히 특정 모델 제공자에 종속되는 대신 BYOK(Bring Your Own Key) 방식을 택해 Anthropic API뿐 아니라 사용자가 이미 쓰고 있는 Claude Code, Codex, Cursor Agent, Gemini CLI, OpenCode, Qwen 같은 코딩 에이전트를 디자인 엔진으로 활용합니다.

흥미로운 점은 Open Design이 "또 하나의 독립 AI 에이전트"가 되려 하지 않는다는 것입니다. 이미 개발자가 설치해 둔 CLI 에이전트를 감지하고, 여기에 스킬 기반 디자인 워크플로우를 연결합니다. 그 결과 사용자는 익숙한 코딩 에이전트 생태계를 유지하면서도, 19개의 디자인 스킬과 71개의 디자인 시스템을 조합해 웹 프로토타입, 랜딩 페이지, 대시보드, 모바일 앱, 발표 자료, 업무 문서까지 생성할 수 있습니다.""",
        expected_output="""Open Design은 Anthropic의 Claude Design과 유사한 AI 디자인 워크플로를 오픈소스로 구현하려는 프로젝트입니다.
클라우드 기반·비공개 서비스에 의존하지 않고 로컬 실행, 코드 수정, 투명한 확장을 가능하게 한다는 점을 강조합니다.
디자인 시안, 프로토타입, 프론트엔드 결과물을 AI와 함께 만들고 싶은 개발자에게 대안적 선택지를 제공합니다.""",
        additional_metadata={"category": "오픈소스 도구"},
    ),
    Golden(
        input="""Claude Skills는 Anthropic의 대화형 AI Claude에게 특정한 능력을 학습시키기 위한 일종의 확장 모듈입니다. 각 스킬은 폴더 단위로 구성되며, 내부에는 SKILL.md같은 설명 파일, 관련 코드, 그리고 실행 가능한 스크립트가 포함되어 있습니다. 이 스킬들은 Claude가 문서 생성, API 테스트, 데이터 분석 등과 같은 다양한 작업을 보다 전문적으로 수행할 수 있게 만들어 줍니다.

이번에 소개하는 VoltAgent/awesome-claude-skills 저장소는 VoltAgent가 Claude Skills를 한곳에 모아 정리한 오픈소스 큐레이션 프로젝트로, Anthropic이 공개한 공식 스킬부터 커뮤니티 제작 스킬까지 전반적인 Claude Skills를 아우르고 있습니다. 개발자나 AI 엔지니어는 이 저장소를 통해 원하는 기능을 빠르게 찾아 Claude에 적용할 수 있습니다.

Claude Skills의 가장 큰 특징은 필요한 스킬만 불러오는 지연 로드(Lazy Loading) 방식입니다. 필요한 스킬만 필요할 때에 불러오기 때문에, 수백 개의 스킬을 관리하더라도 토큰의 낭비나 성능 저하 없이 사용할 수 있습니다. 또 여러 스킬을 동시에 조합해 복잡한 업무 흐름을 자동화할 수 있으며, 이는 Claude를 단순한 대화형 모델에서 도메인 특화형 AI 에이전트로 발전시키는 핵심 요소입니다.""",
        expected_output="""awesome-claude-skills는 Anthropic 공식 스킬과 커뮤니티 제작 Claude Skills를 한곳에 모은 오픈소스 큐레이션 저장소입니다.
문서 작성, 웹앱 테스트, 데이터 분석처럼 특정 업무를 Claude가 더 전문적으로 수행하도록 돕는 스킬들을 탐색할 수 있습니다.
필요한 스킬만 불러오는 지연 로드 방식과 조합 가능성이 Claude를 도메인 특화 에이전트로 확장하는 핵심입니다.""",
        additional_metadata={"category": "오픈소스 도구"},
    ),
    Golden(
        input="""거대 모델 학습은 이제 단일 GPU 몇 장의 문제가 아니라, 수천·수만 개 가속기와 네트워크, 컴파일러, 분산 런타임이 하나로 맞물리는 시스템 문제가 되었습니다. Google은 오랫동안 TPU를 자사 AI 인프라의 핵심으로 사용해왔지만, PyTorch 사용자에게 TPU는 여전히 낯선 선택지였습니다. PyTorch/XLA가 경로를 제공하긴 했지만, lazy tensor, SPMD 중심 사고방식, 컴파일러 제약 때문에 평소 작성하던 PyTorch 코드를 그대로 가져가기에는 마찰이 있었습니다.

TorchTPU는 이 간극을 줄이기 위해 Google이 공개한 PyTorch 네이티브 TPU 백엔드입니다. 핵심은 기존 학습 루프를 대대적으로 고치지 않고도 device="tpu"에 가까운 경험으로 TPU를 사용할 수 있게 만드는 것입니다. 이를 위해 PyTorch 2.x의 PrivateUse1 백엔드 통합 지점을 활용하고, 별도의 텐서 래퍼나 특수 서브클래스 없이 일반 torch.Tensor가 TPU 위에서 동작하도록 설계되었습니다.

이 스택은 단순한 디바이스 어댑터에 그치지 않습니다. 디버깅을 위한 eager 모드, 성능을 위한 연산 fusion, torch.compile 기반 정적 컴파일, StableHLO/XLA 경로, Pallas와 JAX 커스텀 커널, DDP·FSDPv2·DTensor 기반 분산 학습까지 한 번에 묶습니다. TPU는 행렬 연산을 위해 설계된 ASIC이며 MXU, TensorCore, SparseCore, ICI, TPU Pod, TPU VM 같은 구조를 갖는다. TorchTPU의 설계 원칙은 "그냥 PyTorch처럼 느껴져야 한다"이며 PrivateUse1 인터페이스로 torch.Tensor를 TPU 디바이스에 올린다.""",
        expected_output="""TorchTPU는 Google TPU를 PyTorch에서 더 네이티브하게 다루기 위한 백엔드 프로젝트입니다.
기존 PyTorch/XLA 사용 시 생기던 그래프 변환과 디버깅 부담을 줄이고, PyTorch 코드 흐름에 가까운 TPU 활용을 목표로 합니다.
TPU를 연구·학습·추론 워크로드에 쓰는 개발자에게 접근성과 생산성을 높일 수 있는 변화로 소개됩니다.""",
        additional_metadata={"category": "AI/ML 연구"},
    ),
    Golden(
        input="""대규모 언어 모델을 실제 서비스에 올릴 때 가장 빠르게 커지는 비용 중 하나는 KV 캐시입니다. 컨텍스트가 길어질수록 각 레이어의 Key와 Value를 저장해야 하므로 메모리 사용량이 선형적으로 늘어나고, 이는 긴 문맥 추론과 동시 사용자 처리량을 직접 제한합니다. 단순히 모델 가중치를 줄이는 것만으로는 이 병목을 해결하기 어렵습니다.

turboquant-pytorch는 Google의 TurboQuant 논문 아이디어를 PyTorch로 처음부터 구현한 오픈소스 라이브러리입니다. 핵심은 KV 벡터 자체를 최대한 예쁘게 복원하는 것이 아니라, 어텐션 계산에서 중요한 내적의 정확도를 보존하는 데 있습니다. 벡터 재구성 오차가 남더라도, 쿼리와 KV 캐시 사이의 내적 추정이 편향 없이 유지된다면 실제 어텐션 품질은 충분히 보존될 수 있다는 접근입니다.

이를 위해 TurboQuant는 랜덤 회전과 Lloyd-Max 양자화로 1차 압축을 수행하고, QJL 기반 1비트 잔차 보정으로 내적 정확도를 다시 끌어올립니다. PyTorch 구현체는 실제 Qwen2.5-3B-Instruct KV 캐시를 사용한 검증 결과를 공개하며, 3비트 설정에서 큰 폭의 메모리 절감과 높은 어텐션 충실도를 동시에 보여줍니다. 3-bit 설정에서 289MB KV 캐시를 58MB로 압축하고 코사인 유사도 0.9945, Top-5 일치율 94%를 보인다.""",
        expected_output="""turboquant-pytorch는 LLM 추론에서 중요한 KV 캐시를 양자화해 메모리 사용량을 줄이는 PyTorch 구현체입니다.
Google의 TurboQuant 아이디어를 PyTorch 코드로 재현해, 대형 모델 추론의 비용과 효율 문제를 다룹니다.
긴 컨텍스트와 배치 추론을 다루는 개발자에게 메모리 병목을 완화할 수 있는 실험적 도구입니다.""",
        additional_metadata={"category": "AI/ML 연구"},
    ),
    Golden(
        input="""AI 에이전트가 점점 더 복잡한 업무를 맡게 되면서, 단순한 추론 능력만큼이나 중요한 문제가 드러나고 있습니다. 바로 과거 경험에서 배우는 능력입니다. 사람은 실패한 접근을 기억하고 다음에는 피하지만, 많은 에이전트는 매번 새로운 작업을 처음 보는 것처럼 처리합니다. 그 결과 같은 전략적 실수를 반복하고, 이전 실행에서 얻은 유용한 힌트를 버리게 됩니다.

ReasoningBank는 이 문제를 해결하기 위해 제안된 에이전트 추론 메모리 프레임워크입니다. 기존의 궤적 메모리는 클릭, 입력, 관찰 같은 행동 시퀀스를 너무 자세히 저장해 다른 상황으로 일반화하기 어렵고, 워크플로우 메모리는 주로 성공 사례만 요약해 실패에서 얻을 수 있는 교훈을 놓칩니다. ReasoningBank는 이 두 한계를 넘기 위해 행동 기록이 아니라 재사용 가능한 추론 전략을 저장합니다.

핵심은 "무엇을 했는가"보다 "왜 그 접근이 통했거나 실패했는가"를 기억하는 것입니다. 실패 경험에서도 예방적 규칙과 전략을 추출하고, 이를 테스트 시점 추론 과정에서 다시 활용합니다. Memory-aware Test-Time Scaling(MaTTS)을 통해 메모리와 테스트 시점 추론 확장을 결합한다. 실험에서 WebArena 성공률은 메모리 없는 에이전트 대비 8.3%, SWE-Bench-Verified는 4.6% 향상되었다.""",
        expected_output="""ReasoningBank는 AI 에이전트가 성공과 실패 경험을 저장하고 다음 추론에 활용하도록 돕는 메모리 프레임워크입니다.
단순 대화 기록이 아니라 어떤 전략이 효과적이었는지, 어떤 실수가 반복되었는지를 구조화합니다.
장기적으로 더 나은 판단을 하는 에이전트를 만들기 위한 경험 기반 학습 접근으로 소개됩니다.""",
        additional_metadata={"category": "AI/ML 연구"},
    ),
    Golden(
        input="""Google DeepMind의 Project Genie는 생성형 AI를 정적인 이미지나 영상 생성 도구로 보는 관점에서 벗어나, 사용자가 직접 탐험할 수 있는 세계를 만들어내려는 실험입니다. 핵심에는 Genie 3라는 범용 월드 모델이 있습니다. 기존 영상 생성 모델이 프롬프트에 맞는 장면을 렌더링하는 데 그쳤다면, Genie 3는 사용자의 행동에 반응하며 다음 장면을 계속 만들어내는 방식으로 동작합니다.

이 프로젝트가 흥미로운 이유는 결과물이 단순한 "영상"이 아니라 "환경"에 가깝기 때문입니다. 사용자는 자연어 프롬프트나 이미지를 통해 세계의 분위기와 구조를 정하고, 그 안에서 걷거나 날거나 운전하는 식으로 상호작용할 수 있습니다. Nano Banana Pro는 초기 세계의 시각적 방향을 잡고, Gemini는 사용자의 의도와 전체 논리를 조율하며, Genie 3는 실시간 탐험을 가능하게 하는 생성 엔진 역할을 합니다.

물론 현재의 Project Genie는 연구 단계의 프로토타입에 가깝습니다. 생성 길이, 지연 시간, 물리적 정확성, 프롬프트 반영도에는 아직 한계가 있습니다. Genie 3는 사용자 입력에 따라 다음 프레임을 실시간 생성해 게임 엔진에 가까운 경험을 만든다. 월드 리믹싱 기능으로 기존 세계를 변형하고 여정을 비디오로 저장할 수 있다.""",
        expected_output="""Project Genie는 Google DeepMind가 공개한 인터랙티브 세계 생성 연구 흐름을 소개하는 글입니다.
이미지나 간단한 입력에서 조작 가능한 환경을 만들고, 사용자가 그 안에서 상호작용할 수 있는 가능성을 탐색합니다.
게임, 시뮬레이션, 로봇 학습처럼 생성 모델이 정적인 콘텐츠를 넘어 동적인 세계 모델로 확장되는 방향을 보여줍니다.""",
        additional_metadata={"category": "AI/ML 연구"},
    ),
    Golden(
        input="""Apple은 WWDC 2025에서 iOS 26을 공개하며 디자인 언어를 대폭 손봤다. 가장 눈에 띄는 변화는 Liquid Glass라 불리는 반투명 소재 기반의 새 UI 시스템이다. 상단 바, 탭 바, 위젯, 알림 배너 등 거의 모든 시스템 UI 요소가 배경 콘텐츠를 투과하는 유리 질감으로 바뀌었다. 홈 화면 아이콘도 원형으로 변경되었고, 잠금 화면과 제어 센터 역시 새 디자인 언어를 따른다.

기능 면에서는 Siri가 대폭 개편되었다. Apple Intelligence를 기반으로 화면 컨텍스트를 이해하고 앱 간 작업을 연결하는 능력이 추가되었다. 예를 들어 메시지 앱에서 친구가 보낸 주소를 Siri가 읽고, 바로 지도 앱에서 경로를 안내하는 식이다. 또한 ChatGPT, Google Gemini 등 서드파티 모델과의 연동도 확대되었다.

그 밖에 메일 앱에 카테고리 자동 분류 기능이 추가되었고, Safari에는 Intelligent Search라는 AI 요약 기능이 들어갔다. 카메라 앱은 Visual Intelligence를 통해 실시간 객체 인식과 번역을 지원한다. Apple은 이번 업데이트가 2007년 이후 가장 큰 시각적 변화라고 표현했다.""",
        expected_output="""Apple은 WWDC 2025에서 Liquid Glass 디자인과 개편된 Siri를 핵심으로 하는 iOS 26을 공개했습니다.
반투명 유리 질감 UI가 시스템 전반에 적용되었고, Siri는 화면 맥락을 이해해 앱 간 작업을 연결하는 기능을 갖추었습니다.
메일 자동 분류, Safari AI 요약, 카메라 실시간 인식 등 Apple Intelligence 기반 기능이 여러 기본 앱에 확산되었습니다.""",
        additional_metadata={"category": "뉴스 요약"},
    ),
    Golden(
        input="""Cursor는 VS Code 포크 기반의 AI 코드 에디터로, 출시 이후 빠르게 개발자 사이에서 채택률이 높아지고 있다. 2025년 5월 기준 시리즈 C 라운드에서 9억 달러 기업가치를 인정받으며 약 1억 달러를 추가 유치했다. 투자는 Thrive Capital이 리드했고, Andreessen Horowitz, Stripe 공동 창업자 Patrick Collison 등이 참여했다.

Cursor의 핵심은 에디터 안에서 코드베이스 전체를 맥락으로 활용하는 AI 어시스턴트다. Tab 자동완성, 자연어 기반 코드 편집(Cmd+K), 그리고 에이전트 모드를 통해 멀티 파일 변경과 터미널 명령까지 자동 수행한다. 최근에는 Background Agent 기능을 도입해 클라우드에서 별도 샌드박스를 띄워 작업을 병렬 처리하는 방식도 실험 중이다.

경쟁 환경도 치열하다. GitHub Copilot이 에이전트 모드를 추가했고, Windsurf(구 Codeium)는 OpenAI가 인수를 발표했다. Google의 Project Jules, Amazon의 Q Developer Agent 등 대형 플랫폼들도 AI 코딩 에이전트 시장에 진입하고 있다. Cursor는 독립 에디터라는 위치에서 빠른 반복과 개발자 경험에 집중하는 전략으로 차별화를 시도하고 있다.""",
        expected_output="""Cursor는 VS Code 기반 AI 코드 에디터로, 시리즈 C에서 9억 달러 기업가치를 인정받으며 1억 달러를 유치했습니다.
코드베이스 전체를 맥락으로 쓰는 자동완성, 자연어 편집, 에이전트 모드가 핵심이며 클라우드 병렬 처리도 실험 중입니다.
Copilot, Windsurf, Project Jules 등 경쟁이 심화되는 가운데 독립 에디터로서 빠른 반복에 집중하는 전략을 취하고 있습니다.""",
        additional_metadata={"category": "뉴스 요약"},
    ),
    Golden(
        input="""Anthropic이 공개한 Model Context Protocol(MCP)은 LLM 애플리케이션이 외부 도구와 데이터 소스에 접근하는 방식을 표준화하려는 오픈 프로토콜이다. 기존에는 AI 에이전트가 웹 검색, 파일 시스템, 데이터베이스, API 등 외부 자원을 사용하려면 각 도구마다 개별적인 통합 코드를 작성해야 했다. MCP는 이 문제를 해결하기 위해 클라이언트-서버 아키텍처를 제안한다.

MCP 서버는 특정 기능(파일 읽기, GitHub PR 조회, 슬랙 메시지 전송 등)을 JSON-RPC 기반 인터페이스로 노출하고, MCP 클라이언트(Claude Desktop, Cursor, Zed 등)는 이 서버에 접속해 도구 목록을 가져오고 호출한다. 이 구조 덕분에 한 번 만든 MCP 서버는 MCP를 지원하는 모든 클라이언트에서 재사용할 수 있다.

현재 공식 SDK는 TypeScript와 Python으로 제공되며, 커뮤니티에서 Go, Rust, Java, C# 등의 SDK도 등장하고 있다. GitHub, Slack, Google Drive, PostgreSQL 등의 레퍼런스 서버가 이미 공개되어 있다. OpenAI, Google, Microsoft 등 다른 AI 기업들도 MCP 지원을 표명하면서 사실상 업계 표준으로 자리 잡는 흐름이다. 다만 보안 모델(인증, 권한 범위 제한, 샌드박싱)은 아직 초기 단계이며 프로덕션 배포에는 추가 설계가 필요하다.""",
        expected_output="""MCP는 Anthropic이 공개한 오픈 프로토콜로, LLM 앱이 외부 도구와 데이터에 접근하는 방식을 표준화합니다.
JSON-RPC 기반 클라이언트-서버 구조를 사용해 한 번 만든 도구 서버를 여러 AI 클라이언트에서 재사용할 수 있습니다.
TypeScript·Python SDK와 다수의 레퍼런스 서버가 공개되어 있으나 보안 모델은 아직 초기 단계입니다.""",
        additional_metadata={"category": "오픈소스 도구"},
    ),
]


def load_golden_dataset(goldens: list[Golden] | None = None) -> EvaluationDataset:
    return EvaluationDataset(goldens=goldens or SAMPLE_GOLDENS)
