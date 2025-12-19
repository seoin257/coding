import streamlit as st
import random

# ===== 세션 초기화 =====
if "history" not in st.session_state:
    st.session_state.history = []

if "com" not in st.session_state:
    nums = list(range(10))
    random.shuffle(nums)
    st.session_state.com = nums[:3]
    st.session_state.trycount = 0
    st.session_state.done = False


# ===== 새 게임 함수 =====
def new_game():
    nums = list(range(10))
    random.shuffle(nums)
    st.session_state.com = nums[:3]
    st.session_state.trycount = 0
    st.session_state.done = False
    st.session_state.history = []


st.title("숫자야구")

# ⭐ 새 게임 버튼
if st.button("리셋"):
    new_game()

com = st.session_state.com

base1_str = st.text_input("1 2 3처럼 띄어쓰기로 입력")

if st.button("제출") and not st.session_state.done:
    if not base1_str:
        st.warning("숫자 먼저 입력해")
        st.stop()

    try:
        base = list(map(int, base1_str.split()))
    except:
        st.error("숫자만 입력해")
        st.stop()

    if len(base) != 3:
        st.error("숫자 3개 입력해")
        st.stop()

    if len(set(base)) != 3:
        st.error("같은 숫자 입력 불가")
        st.stop()

    st.session_state.trycount += 1

    n = []
    for i in range(3):
        if base[i] == com[i]:
            n.append(1)
        elif base[i] in com:
            n.append(2)
        else:
            n.append(3)

    if n == [1, 1, 1]:
        msg = "성공!!!"
        st.success(msg)
        st.session_state.done = True
    else:
        result = []
        for x in sorted(n):
            if x == 1:
                result.append("스트라이크")
            elif x == 2:
                result.append("볼")
            else:
                result.append("아웃")
        msg = " / ".join(result)
        st.write(msg)

    st.session_state.history.append(
        f"{st.session_state.trycount}회차 | 입력: {base} | 결과: {msg}"
    )

    if st.session_state.trycount == 9 and not st.session_state.done:
        st.error("실패!!!")
        st.write("정답:", com)
        st.session_state.done = True


st.divider()
st.write("기록")
for h in st.session_state.history:
    st.write(h)
