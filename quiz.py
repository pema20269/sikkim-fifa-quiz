import streamlit as st
import time

st.set_page_config(page_title="Cute Pink Quiz", page_icon="💗", layout="centered")

st.markdown("""
<style>
.stApp {background: linear-gradient(180deg, #FFB6C1 0%, #FF69B4 100%);}
h1, h2, h3, p {color: white; text-shadow: 2px 2px 4px #FF1493;}
.stButton>button {background-color: #FF1493; color: white; font-size: 20px; font-weight: bold; border-radius: 25px; padding: 12px; border: 2px solid white;}
.stButton>button:hover {background-color: #FF69B4; transform: scale(1.05);}
</style>
""", unsafe_allow_html=True)

if 'quiz_started' not in st.session_state: st.session_state.quiz_started = False
if 'current_question' not in st.session_state: st.session_state.current_question = 0
if 'score' not in st.session_state: st.session_state.score = 0

questions = [
    {"q": "🏔️ 1. Capital of Sikkim?", "img": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Gangtok%2C_Sikkim.jpg", "options": ["Gangtok", "Namchi", "Geyzing", "Mangan"], "answer": "Gangtok"},
    {"q": "🐼 2. State animal of Sikkim?", "img": "https://upload.wikimedia.org/wikipedia/commons/2/2f/RedPandaFullBody.jpg", "options": ["Red Panda", "Snow Leopard", "Tiger", "Deer"], "answer": "Red Panda"},
    {"q": "❄️ 3. Highest peak in Sikkim?", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Kangchenjunga_from_Singalila_Ridge.jpg", "options": ["Khangchendzonga", "Mount Everest", "Nanda Devi", "K2"], "answer": "Khangchendzonga"},
    {"q": "⚽ 4. Where will FIFA World Cup 2026 be held?", "img": "https://upload.wikimedia.org/wikipedia/commons/7/7b/2026_FIFA_World_Cup_logo.svg.png", "options": ["USA, Canada, Mexico", "India", "Brazil", "Germany"], "answer": "USA, Canada, Mexico"},
    {"q": "🏆 5. How many teams in World Cup 2026?", "img": "https://upload.wikimedia.org/wikipedia/commons/e3/Football_Icon.svg", "options": ["32", "48", "24", "64"], "answer": "48"},
    {"q": "📅 6. First FIFA World Cup year?", "img": "https://upload.wikimedia.org/wikipedia/commons/0/0e/FIFA_World_Cup_Trophy.jpg", "options": ["1930", "1950", "1920", "1942"], "answer": "1930"},
    {"q": "🌟 7. Most World Cup goals?", "img": "https://upload.wikimedia.org/wikipedia/commons/8/8c/Miroslav_Klose_2018.jpg", "options": ["Lionel Messi", "Cristiano Ronaldo", "Miroslav Klose", "Kylian Mbappe"], "answer": "Miroslav Klose"},
    {"q": "🇦🇷 8. FIFA World Cup 2022 Winner?", "img": "https://upload.wikimedia.org/wikipedia/commons/c1/Argentina_national_football_team.jpg", "options": ["France", "Brazil", "Argentina", "Croatia"], "answer": "Argentina"},
    {"q": "🏟️ 9. World Cup 2026 Final stadium?", "img": "https://upload.wikimedia.org/wikipedia/commons/9/9b/MetLife_Stadium.jpg", "options": ["MetLife Stadium", "Wembley", "Maracana", "Azteca"], "answer": "MetLife Stadium"},
    {"q": "⚡ 10. World Cup 2026 theme?", "img": "https://upload.wikimedia.org/wikipedia/commons/e3/Football_Icon.svg", "options": ["Unity", "Diversity", "Passion", "Victory"], "answer": "Unity"},
]

if not st.session_state.quiz_started:
    st.balloons()
    st.title("💗 Hello there! 💗")
    st.image("https://media.giphy.com/media/3o7btPCcdNniyf0ArS/giphy.gif", use_container_width=True)
    st.image("https://upload.wikimedia.org/wikipedia/commons/e3/Football_Icon.svg", width=150)
    st.markdown("### ✨ Are you ready for the Quiz? ✨")
    st.markdown("#### 3 Questions about Sikkim 🏔️")
    st.markdown("#### 7 Questions about World Cup 2026 ⚽")
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("🚀 Let's Start Our Quiz", use_container_width=True):
            st.session_state.quiz_started = True
            st.rerun()
    st.stop()

if st.session_state.current_question < len(questions):
    q = questions[st.session_state.current_question]
    st.progress((st.session_state.current_question) / len(questions))
    st.title(f"Question {st.session_state.current_question + 1} / 10 🥰")
    st.subheader(q["q"])
    st.image(q["img"], use_container_width=True)
    st.write(f"**Your Score: {st.session_state.score} ⭐**")
    choice = st.radio("Choose your answer:", q["options"], key=st.session_state.current_question)
    if st.button("Submit Answer ✅"):
        if choice == q["answer"]:
            st.success(f"🎉 Right! Well done! 👏")
            st.image("https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif", width=200)
            st.markdown(f"**Answer: {q['answer']}** ✅")
            st.session_state.score += 1
            st.balloons()
        else:
            st.error(f"❌ Oops! Try next one!")
            st.image("https://media.giphy.com/media/3o7btPCcdNniyf0ArS/giphy.gif", width=200)
            st.info(f"**Correct Answer: {q['answer']}** 💡")
        time.sleep(2.5)
        st.session_state.current_question += 1
        st.rerun()
else:
    st.balloons()
    st.title("🎊 Quiz Finished! 🎊")
    st.image("https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif", use_container_width=True)
    st.markdown(f"### Your Final Score: **{st.session_state.score} / 10** ⭐")
    if st.session_state.score == 10:
        st.success("🏆 CONGRATULATIONS!!! Perfect Score! 🏆🎉👏")
    elif 6 <= st.session_state.score <= 9:
        st.success(f"👏 Good Job! {st.session_state.score}/10 🎉 You did great! 🥳")
    elif st.session_state.score == 5:
        st.warning(f"😊 You can try again! {st.session_state.score}/10 💪 Keep practicing!")
    else:
        st.info(f"💗 Don't give up! {st.session_state.score}/10 🌟 Try again!")
    st.markdown("### 💗 Thank you for playing! 💗")
    if st.button("🔄 Play Again"):
        st.session_state.quiz_started = False
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.rerun()
