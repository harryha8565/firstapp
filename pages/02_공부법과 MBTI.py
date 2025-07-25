import streamlit as st

# MBTI별 공부법 사전 (200자 이상 설명)
mbti_study_tips = {
    "INTJ": "INTJ는 계획적이고 목표 지향적인 성격으로, 장기적인 전략을 세워 공부하는 것이 잘 맞습니다. 단기 성과보다는 전체 구조를 파악한 후 효율적인 루틴을 만들고 따라가는 방식이 좋습니다. 개념을 먼저 이해하고 문제풀이로 확장하는 '이해-적용-정리' 루틴이 효과적이며, 스스로 만든 요약본과 계획표를 통해 자기주도 학습을 강화할 수 있습니다.",
    "INTP": "INTP는 깊이 있는 사고와 분석을 즐기며, 논리적으로 연결된 지식을 선호합니다. 공부할 때 단순 암기보다는 원리를 파악하고 스스로 질문을 만들며 공부하는 방식이 좋습니다. 정형화된 방법보다는 자유롭게 탐구할 수 있는 환경이 필요하며, 다양한 예시와 실제 사례를 통해 개념을 연결하는 방식이 효과적입니다. 자기만의 사고 정리 노트를 만들어보세요.",
    "ENTJ": "ENTJ는 경쟁심과 조직력이 뛰어나기 때문에 목표 설정과 시간관리를 통한 체계적인 공부가 잘 맞습니다. '무엇을 언제까지 끝낸다'는 식의 구체적인 목표 설정과 관리가 중요하며, 성과를 숫자로 확인하며 동기부여를 받는 성향입니다. 이해 중심의 과목은 구조도를 그리며 정리하고, 암기 과목은 반복 학습과 테스트를 병행하면 효과적입니다.",
    "ENTP": "ENTP는 창의적이고 즉흥적인 면이 있지만 관심 있는 분야에 대한 몰입력이 뛰어납니다. 다양한 과목을 연결해보거나 설명하는 방식으로 공부하면 이해도가 높아집니다. 새로운 방식의 공부법이나 자료를 활용하는 데 두려움이 없기 때문에, 유튜브 강의, 퀴즈 앱, 스터디 그룹 등 다양한 방법을 적극 활용하는 것이 좋습니다. 단, 시간 관리를 꼭 병행해야 합니다.",
    "INFJ": "INFJ는 깊은 통찰력과 계획성을 가지고 있으며 의미 있는 목표를 위해 노력하는 유형입니다. 감성적이지만 논리적인 사고도 가능하기 때문에, 공부할 때 감정과 연결된 동기를 설정하면 집중력이 높아집니다. 조용하고 안정된 환경에서 혼자 정리하며 공부하는 것이 효과적이며, 큰 흐름을 파악한 뒤 세부 내용을 정리하는 방식을 추천합니다.",
    "INFP": "INFP는 감수성이 풍부하고 자기 내면의 동기에 따라 움직이는 경향이 있어, 과목에 대한 흥미를 느낄 수 있는 연결 고리를 만드는 것이 중요합니다. 감정적 피로를 줄이기 위해 짧고 집중된 시간 동안 공부하고, 감성적인 색감이나 문구가 담긴 노트 정리법이 동기부여에 도움을 줄 수 있습니다. 자신의 페이스를 존중하면서도 계획은 유연하게 구성하세요.",
    "ENFJ": "ENFJ는 타인을 도우며 성장하는 성향이 강하기 때문에, 친구에게 설명하거나 스터디 그룹을 이끄는 방식의 학습이 효과적입니다. 정리 능력과 전달력이 좋아서 요약 자료를 만들며 공부하는 것도 추천됩니다. 자기 동기화에 능하며, '목표를 향한 의미 있는 여정'으로 받아들일 때 집중력이 높아집니다. 일정표와 체크리스트도 효과적입니다.",
    "ENFP": "ENFP는 열정적이고 창의적이지만 산만해지기 쉬운 면도 있어, 짧은 시간 단위로 집중하고 휴식을 넣는 '포모도로 학습법'이 잘 맞습니다. 공부를 놀이처럼 받아들이고 감정적으로 몰입할 수 있는 환경을 조성하면 좋습니다. 다양한 학습 자료와 시각적인 콘텐츠를 통해 집중력을 높이고, 친구와 협업하거나 토론하는 방식도 도움이 됩니다.",
    "ISTJ": "ISTJ는 규칙적이고 책임감 있는 성격으로, 정해진 계획을 성실히 수행하는 데 강점을 지닙니다. 미리 학습 계획을 세우고 이를 하루 단위로 세분화하여 실천하는 것이 효과적입니다. 정리된 교재나 인강을 중심으로 한 반복 학습이 잘 맞으며, 실수를 철저히 분석하고 수정하는 루틴을 통해 점차 실력을 높여갑니다. 자기 점검을 자주 하세요.",
    "ISFJ": "ISFJ는 조용하고 성실하며 타인의 기대에 책임감 있게 반응하는 유형으로, 정해진 루틴에 따라 착실히 공부하는 것이 효과적입니다. 필기와 노트 정리를 중시하며, 배운 내용을 다시 써보거나 말로 설명하며 복습하는 방식이 좋습니다. 시각 자료를 활용해 암기력을 높이고, 감정적 스트레스를 줄이기 위해 학습 공간을 편안하게 꾸며보세요.",
    "ESTJ": "ESTJ는 계획적이고 효율을 중시하는 성향으로, 내신을 준비할 때 시간표와 진도표를 철저히 세우고 따르는 학습이 적합합니다. 경쟁 상황에서 동기부여가 되기 때문에 스터디 그룹이나 테스트 형식 학습도 추천됩니다. 암기 과목은 반복과 정리를 중심으로 하고, 이해 과목은 도식화와 개념 비교를 통해 학습하면 효과적입니다.",
    "ESFJ": "ESFJ는 조직적이고 타인을 배려하는 성격으로, 함께 공부하는 환경에서 집중력이 높아집니다. 노트 필기와 정리를 잘 하며, 친구에게 설명하거나 함께 문제를 풀어보는 활동을 통해 복습 효과를 극대화할 수 있습니다. 체크리스트와 일일 목표 설정이 잘 맞고, 칭찬이나 성취 경험이 큰 동기부여가 되므로 작은 성공을 자주 확인하세요.",
    "ISTP": "ISTP는 논리적이고 실용적인 성향으로, 이론보다는 실제 문제 해결에 집중할 때 학습 효과가 높습니다. 개념은 짧게 정리하고 문제풀이를 통해 반복 학습하는 방식이 잘 맞습니다. 시간 낭비를 싫어하기 때문에 공부 계획을 간결하게 구성하고, 필요한 부분만 집중적으로 학습하는 전략이 좋습니다. 실수를 분석하는 데 강점을 활용하세요.",
    "ISFP": "ISFP는 감각적이고 온화한 성향으로, 지나치게 압박이 있는 공부보다는 차분한 환경에서 스스로 학습할 때 더 좋은 성과를 냅니다. 시각 자료나 색깔이 들어간 정리 노트가 효과적이며, 실제 사례나 체험 기반 학습이 이해에 도움을 줍니다. 계획은 유연하게, 하지만 목표는 명확하게 잡아야 중간에 흐트러지지 않습니다.",
    "ESTP": "ESTP는 에너지 넘치고 현실적인 성향으로, 학습에 직접적인 목적과 결과가 보일 때 집중력이 높아집니다. 문제풀이와 테스트를 중심으로 한 실전형 공부 방식이 잘 맞으며, 짧은 시간 동안 고강도 학습을 반복하는 전략이 효과적입니다. 경쟁을 활용한 스터디나 시간제한 퀴즈 방식도 추천됩니다. 시각적인 자료를 적극 활용하세요.",
    "ESFP": "ESFP는 사교적이고 즐거움을 추구하는 성향으로, 학습을 재미있게 만드는 방식이 효과적입니다. 다양한 색상과 도식, 영상 콘텐츠를 활용하면 집중력이 향상됩니다. 누군가와 함께 학습하거나 경쟁이 아닌 협업 기반 스터디가 도움이 되며, 감정의 기복을 관리하기 위해 충분한 휴식과 자기 보상도 포함된 학습 계획을 세우는 것이 좋습니다.",
}

# Streamlit 앱 시작
st.set_page_config(page_title="MBTI 공부법 추천기", layout="centered")

st.title("📚 MBTI별 내신 공부법 추천기")
st.write("MBTI 유형을 선택하면 어울리는 공부법을 자세히 안내해드립니다!")

# MBTI 선택
mbti_options = list(mbti_study_tips.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_options)

# 결과 출력
if selected_mbti:
    st.subheader(f"✏️ {selected_mbti} 유형에게 어울리는 공부법")
    st.write(mbti_study_tips[selected_mbti])
