import streamlit as st

# 1. 앱 제목 설정
st.title("🍿 영화관 세트 메뉴 골라보기")
st.write("원하는 팝콘과 음료를 선택하시면 조합된 세트 메뉴를 확인하실 수 있습니다.")

# 2. 데이터 정의
popcorn_options = ['기본', '카라멜', '어니언']
drink_options = ['생수', '탄산음료']

# 3. 사이드바 또는 메인 화면에 선택 박스 만들기
st.subheader("💡 직접 골라보기")
col1, col2 = st.columns(2)

with col1:
    selected_popcorn = st.selectbox("팝콘을 골라주세요", popcorn_options)

with col2:
    selected_drink = st.selectbox("음료를 골라주세요", drink_options)

# 선택된 조합 출력
st.info(f"선택하신 메뉴: **{selected_popcorn} 팝콘 + {selected_drink}** 세트")

st.write("---")

# 4. 기존 코드처럼 가능한 모든 조합 전체 보기 (확장 레이아웃 사용)
st.subheader("📋 전체 세트 메뉴 판")
with st.expander("모든 가능한 조합 보기"):
    for popcorn in popcorn_options:
        for drink in drink_options:
            st.write(f"• 세트 메뉴: **{popcorn}** 팝콘, **{drink}**")