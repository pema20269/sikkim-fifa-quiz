import streamlit as st
import time

st.set_page_config(page_title="Cute Cartoon Quiz", page_icon="🧸", layout="centered")

st.markdown("""
<style>
.stApp {background: linear-gradient(180deg, #FFD1DC 0%, #ADD8E6 100%);}
h1, h2, h3, p {color: white; text-shadow: 2px 2px 4px #FF69B4; font-family: 'Comic Sans MS', cursive; text-align: center;}
.stButton>button {background-color: #FF69B4; color: white; font-size: 20px; font-weight: bold; border-radius: 30px; padding: 14px; border: 3px solid white; width: 100%;}
.stButton>button:hover {background-color: #FF1493; border: 3px solid #FFD1DC;}
.stRadio > label {color: white !important; font-size: 18px; font-family: 'Comic Sans MS', cursive;}
</style>
""", unsafe_allow_html=True)

if 'quiz_started' not in st.session_state: st.session_state.quiz_started = False
if 'current_question' not in st.session_state: st.session_state.current_question = 0
if 'score' not in st.session_state: st.session_state.score = 0

# ALL 10 QUESTIONS
questions = [
    {"q": "🏔️ 1. What is the Capital of Sikkim?", "cartoon": "https://media.giphy.com/media/3o7btPCcdNniyf0ArS/giphy.gif", "options": ["Gangtok", "Namchi", "Geyzing", "Mangan"], "answer": "Gangtok"},
    {"q": "🧸 2. What is the State Animal of Sikkim?", "cartoon": "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif", "options": ["Red Panda", "Snow Leopard", "Tiger", "Deer"], "answer": "Red Panda"},
    {"q": "🎁 3. What is the Highest Peak in Sikkim?", "cartoon": "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif", "options": ["Khangchendzonga", "Mount Everest", "Nanda Devi", "K2"], "answer": "Khangchendzonga"},
    {"q": "⚽ 4. Which 3 countries will host FIFA World Cup 2026?", "cartoon": "https://media.giphy.com/media/3o7aCTfyhYawdOXcFW/giphy.gif", "options": ["USA, Canada, Mexico", "India, Japan, Korea", "Brazil, Argentina, Chile", "Germany, France, Spain"], "answer": "USA, Canada, Mexico"},
    {"q": "🏆 5. What is the Jersey number of Erling Haaland ?", "cartoon": "https://media.giphy.com/media/xTkcEQACH24SMPxIQg/giphy.gif", "options": ["7", "9", "10", "11"], "answer": "9"},
    {"q": "🎀 6. What is the jersey number of mbappe?", "cartoon": "https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif", "options": ["7", "9", "10", "11"], "answer": "10"},
    {"q": "🌈 7. Who has scored the most World Cup goals EVER?", "cartoon": "https://media.giphy.com/media/3o7aCTfyhYawdOXcFW/giphy.gif", "options": ["Lionel Messi", "Cristiano Ronaldo", "Miroslav Klose", "Kylian Mbappe"], "answer": "Miroslav Klose"},
    {"q": "🎈 8. Who won FIFA World Cup 2022?", "cartoon": "https://media.giphy.com/media/xTkcEQACH24SMPxIQg/giphy.gif", "options": ["France", "Brazil", "Argentina", "Croatia"], "answer": "Argentina"},
    {"q": "🚂 9. Where will the World Cup 2026 Final be played?", "cartoon": "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif", "options": ["MetLife Stadium, New Jersey", "Wembley Stadium", "Maracana Stadium", "Azteca Stadium"], "answer": "MetLife Stadium, New Jersey"},
    {"q": "🧩 10. What is the official slogan for World Cup 2026?", "cartoon": "https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif", "options": ["Unity", "We Are 26", "Passion", "Victory"], "answer": "We Are 26"},
]

# START SCREEN
if not st.session_state.quiz_started:
    st.markdown("<h1>👋 Hello There! 🌸 Are You Ready to Play? 🎉</h1>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif", width=200)
    st.markdown("#### 🏔️ 3 Questions about Sikkim")
    st.markdown("#### ⚽ 7 Questions about FIFA World Cup 2026")
    if st.button("🚀 Start Quiz"):
        st.session_state.quiz_started = True
        st.rerun()
    st.stop()

# QUIZ SCREEN
if st.session_state.current_question < len(questions):
    q = questions[st.session_state.current_question]
    st.progress((st.session_state.current_question + 1) / 10)
    st.markdown(f"<h2>Question {st.session_state.current_question + 1} / 10 🧸</h2>", unsafe_allow_html=True)
    st.image(q["cartoon"], width=240)
    st.subheader(q["q"])
    st.write(f"**⭐ Live Score: {st.session_state.score} / 10 ⭐**")
    choice = st.radio("Choose your answer:", q["options"], key=st.session_state.current_question)
    
    if st.button("Submit Answer ✅"):
        if choice == q["answer"]:
            st.success("🎉 CORRECT! YAY! 👏")
            st.image("https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif", width=180)
            st.session_state.score += 1
        else:
            st.error("❌ WRONG! Oops!")
            st.image("https://media.giphy.com/media/3o7btPCcdNniyf0ArS/giphy.gif", width=180)
            st.info(f"💡 Correct Answer: **{q['answer']}**")
        time.sleep(2)
        st.session_state.current_question += 1
        st.rerun()
        
# FINAL SCREEN
else:
    st.markdown("<h1>🎊 Quiz Finished! 🎊</h1>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif", width=200)
    st.markdown(f"<h2>🏆 Final Score: {st.session_state.score} / 10 🏆</h2>", unsafe_allow_html=True)
    
    if st.session_state.score == 10: st.success("🏆 PERFECT!")
    elif st.session_state.score >= 8: st.success(f"🌟 Excellent! Congratulations!")
    elif st.session_state.score >= 6: st.success(f"👏 Great Job!")
    elif st.session_state.score >= 4: st.info(f"😊 Good Effort!")
    else: st.warning(f"💪 Keep Practicing!")
    
    st.markdown("<h3>👏 Thank You for Playing! 👏</h3>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/xTkcEQACH24SMPxIQg/giphy.gif", width=180)
    
    if st.button("🔄 Play Again"):
        st.session_state.quiz_started = False
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.rerun()
