import streamlit as st

st.set_page_config(page_title="MBTI 대학 추천기", page_icon="🎓")

st.title("🎓 MBTI 기반 대학 추천기")
st.write("당신의 MBTI에 맞는 대학을 추천해드립니다!")

mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

mbti = st.selectbox("당신의 MBTI 유형을 선택하세요", mbti_types)

# 각 MBTI에 해당하는 대학 추천 (샘플 데이터)
university_recommendations = {
    "INTJ": ["서울대학교", "KAIST", "포스텍"],
    "INTP": ["KAIST", "UNIST", "서울대학교"],
    "ENTJ": ["연세대학교", "서울대학교", "고려대학교"],
    "ENTP": ["한양대학교", "연세대학교", "KAIST"],
    "INFJ": ["이화여자대학교", "서울대학교", "서강대학교"],
    "INFP": ["홍익대학교", "성균관대학교", "서울대학교"],
    "ENFJ": ["숙명여자대학교", "중앙대학교", "연세대학교"],
    "ENFP": ["경희대학교", "홍익대학교", "고려대학교"],
    "ISTJ": ["국방대학교", "서울대학교", "경북대학교"],
    "ISFJ": ["부산대학교", "덕성여자대학교", "서울과학기술대학교"],
    "ESTJ": ["고려대학교", "건국대학교", "세종대학교"],
    "ESFJ": ["중앙대학교", "한양대학교", "서울시립대학교"],
    "ISTP": ["한국기술교육대학교", "한밭대학교", "경상국립대학교"],
    "ISFP": ["청주대학교", "단국대학교", "동국대학교"],
    "ESTP": ["경기대학교", "세종대학교", "한국체육대학교"],
    "ESFP": ["상명대학교", "명지대학교", "국민대학교"]
}

if mbti:
    st.subheader(f"🧠 {mbti}에게 어울리는 대학 추천:")
    recommendations = university_recommendations.get(mbti, ["추천할 데이터 없음"])
    for idx, uni in enumerate(recommendations, start=1):
        st.write(f"{idx}. {uni}")
