import streamlit as st
import time

st.set_page_config(page_title="Football Teddy Quiz", page_icon="🧸", layout="centered")

st.markdown("""
<style>
.stApp {background: linear-gradient(180deg, #90EE90 0%, #98FB98 100%);}
h1, h2, h3, p {color: white; text-shadow: 2px 2px 4px #228B22; font-family: 'Comic Sans MS', cursive; text-align: center;}
.stButton>button {background-color: #32CD32; color: white; font-size: 20px; font-weight: bold; border-radius: 30px; padding: 14px; border: 3px solid white;}
</style>
""", unsafe_allow_html=True)

if 'quiz_started' not in st.session_state: st.session_state.quiz_started = False
if 'current_question' not in st.session_state: st.session_state.current_question = 0
if 'score' not in st.session_state: st.session_state.score = 0

# ALL FOOTBALL TEDDY/TOY GIFS - TEDDY WITH BALLS!
questions = [
    {"q": "🏔️ 1. What is the Capital of Sikkim?", "cartoon": "https://media.giphy.com/media/3o7btPCcdNniyf0ArS/giphy.gif", "options": ["Gangtok", "Namchi", "Geyzing", "Mangan"], "answer": "Gangtok"}, # teddy
    {"q": "🧸 2. What is the State Animal of Sikkim?", "cartoon": "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif", "options": ["Red Panda", "Snow Leopard", "Tiger", "Deer"], "answer": "Red Panda"}, # cute animal
    {"q": "🎁 3. What is the Highest Peak in Sikkim?", "cartoon": "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif", "options": ["Khangchendzonga", "Mount Everest", "Nanda Devi", "K2"], "answer": "Khangchendzonga"}, # mountain sparkles
    {"q": "⚽ 4. Where will FIFA World Cup 2026 be held?", "cartoon": "https://media.giphy.com/media/3o7aCTfyhYawdOXcFW/giphy.gif", "options": ["USA, Canada, Mexico", "India", "Brazil", "Germany"], "answer": "USA, Canada, Mexico"}, # bouncing football
    {"q": "🏆 5. How many teams will play in World Cup 2026?", "cartoon": "https://media.giphy.com/media/xTkcEQACH24SMPxIQg/giphy.gif", "options": ["32", "48", "24", "64"], "answer": "48"}, # trophy
    {"q": "🎀 6. In which year was the first FIFA World Cup?", "cartoon": "https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif", "options": ["1930", "1950", "1920", "1942"], "answer": "1930"}, # confetti ball
    {"q": "🌈 7. Who has scored the most World Cup goals?", "cartoon": "https://media.giphy.com/media/3o7aCTfyhYawdOXcFW/giphy.gif", "options": ["Lionel Messi", "Cristiano Ronaldo", "Miroslav Klose", "Kylian Mbappe"], "answer": "Miroslav Klose"}, # football juggling
    {"q": "🎈 8. Who won FIFA World Cup 2022?", "cartoon": "https://media.giphy.com/media/3o7aCTfyhYawdOXcFW/giphy.gif", "options": ["France", "Brazil", "Argentina", "Croatia"], "answer": "Argentina"}, # celebration with ball
    {"q": "🚂 9. Where will World Cup 2026 Final be played?", "cartoon": "https://media.giphy.com/media/xTkcEQACH24SMPxIQg/giphy.gif", "options": ["MetLife Stadium", "Wembley", "Maracana", "Azteca"], "answer": "MetLife Stadium"}, # stadium trophy
    {"q": "🧩 10. What is the theme for World Cup 2026?", "cartoon": "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif", "options": ["Unity", "Diversity", "Passion", "Victory"], "answer": "Unity"}, # hearts unity
]

if not st.session_state.quiz_started:
    st.markdown("<h1>🧸⚽ Football Teddy Quiz! ⚽🧸</h1>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/3o7aCTfyhYawdOXcFW/giphy.gif", width=220) # teddy with ball
    st.image("https://media.giphy.com/media/xTkcEQACH24SMPxIQg/giphy.gif", width=180) # trophy
    st.markdown("<h3>✨ Teddys are playing football! ✨</h3>", unsafe_allow_html=True)
    st.markdown("#### 🏔️ 3 Questions about Sikkim")
    st.markdown("#### ⚽ 7 Questions about World Cup 2026")
    if st.button("🚀 Let's Start"):
        st.session_state.quiz_started = True
        st.rerun()
    st.stop()

if st.session_state.current_question < len(questions):
    q = questions[st.session_state.current_question]
    st.progress((st.session_state.current_question + 1) / 10)
    st.markdown(f"<h2>Question {st.session_state.current_question + 1} / 10 🧸</h2>", unsafe_allow_html=True)
    st.image(q["cartoon"], width=240)
    st.subheader(q["q"])
    st.write(f"**⭐ Your Score: {st.session_state.score} / 10 ⭐**")
    choice = st.radio("Choose your answer:", q["options"], key=st.session_state.current_question)
    
    if st.button("Submit Answer ✅"):
        if choice == q["answer"]:
            st.success("🎉 GOAL!!! Correct! 👏")
            st.image("https://media.giphy.com/media/3o7aCTfyhYawdOXcFW/giphy.gif", width=180) # teddy celebrating with ball
            st.session_state.score += 1
        else:
            st.error("❌ Missed the goal!")
            st.image("https://media.giphy.com/media/3o7btPCcdNniyf0ArS/giphy.gif", width=180) # sad teddy
            st.info(f"💡 Correct Answer: **{q['answer']}**")
        time.sleep(2)
        st.session_state.current_question += 1
        st.rerun()
else:
    st.markdown("<h1>🎊 Match Finished! 🎊</h1>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/xTkcEQACH24SMPxIQg/giphy.gif", width=200) # trophy
    st.markdown(f"<h2>⭐ Final Score: {st.session_state.score} / 10 ⭐</h2>", unsafe_allow_html=True)
    
    if st.session_state.score == 10: st.success("🏆 CHAMPION!!! 10/10 Teddy is proud! 🏆")
    elif st.session_state.score >= 8: st.success(f"🎉 AMAZING! {st.session_state.score}/10 Great player! 🎉")
    elif st.session_state.score >= 6: st.success(f"👏 GOOD JOB! {st.session_state.score}/10 Keep playing! 👏")
    else: st.info(f"🌟 PRACTICE MORE! {st.session_state.score}/10 You got this! 🌟")
    
    st.markdown("<h3>💗 Thank you for playing with the teddys! 💗</h3>", unsafe_allow_html=True)
    st.markdown("### Play again? 🧸⚽")
    
    if st.button("🔄 Play Again"):
        st.session_state.quiz_started = False
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.rerun()
 
