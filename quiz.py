import streamlit as st
import time

st.set_page_config(page_title="Cute Cartoon Quiz", page_icon="💗", layout="centered")

st.markdown("""
<style>
.stApp {background: linear-gradient(180deg, #FFC0CB 0%, #FF69B4 100%);}
h1, h2, h3, p {color: white; text-shadow: 2px 2px 4px #FF1493; font-family: 'Comic Sans MS', cursive; text-align: center;}
.stButton>button {background-color: #FF1493; color: white; font-size: 20px; font-weight: bold; border-radius: 25px; padding: 12px; border: 3px solid white; box-shadow: 0 0 15px pink; display: block; margin: 0 auto;}
.stButton>button:hover {background-color: #FF69B4; transform: scale(1.1);}
.sparkle {animation: sparkle 1.5s infinite;}
@keyframes sparkle {0%,100% {opacity: 1;} 50% {opacity: 0.6;}}
</style>
""", unsafe_allow_html=True)

if 'quiz_started' not in st.session_state: st.session_state.quiz_started = False
if 'current_question' not in st.session_state: st.session_state.current_question = 0
if 'score' not in st.session_state: st.session_state.score = 0

# ALL CUTE STATIC CARTOON IMAGES - NO GIFS, NO HUMANS!
questions = [
    {"q": "🏔️ 1. What is the Capital of Sikkim?", "cartoon": "https://cdn-icons-png.flaticon.com/512/616/616408.png", "options": ["Gangtok", "Namchi", "Geyzing", "Mangan"], "answer": "Gangtok"},
    {"q": "🐼 2. What is the State Animal of Sikkim?", "cartoon": "https://cdn-icons-png.flaticon.com/512/616/616490.png", "options": ["Red Panda", "Snow Leopard", "Tiger", "Deer"], "answer": "Red Panda"},
    {"q": "❄️ 3. What is the Highest Peak in Sikkim?", "cartoon": "https://cdn-icons-png.flaticon.com/512/869/869.png", "options": ["Khangchendzonga", "Mount Everest", "Nanda Devi", "K2"], "answer": "Khangchendzonga"},
    {"q": "⚽ 4. Where will FIFA World Cup 2026 be held?", "cartoon": "https://cdn-icons-png.flaticon.com/512/33/33308.png", "options": ["USA, Canada, Mexico", "India", "Brazil", "Germany"], "answer": "USA, Canada, Mexico"},
    {"q": "🏆 5. How many teams will play in World Cup 2026?", "cartoon": "https://cdn-icons-png.flaticon.com/512/5968/5968705.png", "options": ["32", "48", "24", "64"], "answer": "48"},
    {"q": "📅 6. In which year was the first FIFA World Cup?", "cartoon": "https://cdn-icons-png.flaticon.com/512/747/747310.png", "options": ["1930", "1950", "1920", "1942"], "answer": "1930"},
    {"q": "🌟 7. Who has scored the most World Cup goals?", "cartoon": "https://cdn-icons-png.flaticon.com/512/1042/1042395.png", "options": ["Lionel Messi", "Cristiano Ronaldo", "Miroslav Klose", "Kylian Mbappe"], "answer": "Miroslav Klose"},
    {"q": "🇦🇷 8. Who won FIFA World Cup 2022?", "cartoon": "https://cdn-icons-png.flaticon.com/512/5968/5968705.png", "options": ["France", "Brazil", "Argentina", "Croatia"], "answer": "Argentina"},
    {"q": "🏟️ 9. Where will World Cup 2026 Final be played?", "cartoon": "https://cdn-icons-png.flaticon.com/512/2165/2165061.png", "options": ["MetLife Stadium", "Wembley", "Maracana", "Azteca"], "answer": "MetLife Stadium"},
    {"q": "⚡ 10. What is the theme for World Cup 2026?", "cartoon": "https://cdn-icons-png.flaticon.com/512/869/869636.png", "options": ["Unity", "Diversity", "Passion", "Victory"], "answer": "Unity"},
]

# HELLO THERE SCREEN
if not st.session_state.quiz_started:
    st.markdown("<h1 class='sparkle'>💗 Hello there! 💗</h1>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/616/616408.png", width=200)
    st.image("https://cdn-icons-png.flaticon.com/512/5968/5968705.png", width=180)
    st.markdown("<h3 class='sparkle'>✨ Are you ready for the Cute Cartoon Quiz? ✨</h3>", unsafe_allow_html=True)
    st.markdown("#### 🏔️ 3 Questions about Sikkim")
    st.markdown("#### ⚽ 7 Questions about World Cup 2026")
    st.markdown("### Let's learn and have fun! 🥰")
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("🚀 Let's Start", use_container_width=True):
            st.session_state.quiz_started = True
            st.rerun()
    st.stop()

# QUIZ QUESTIONS
if st.session_state.current_question < len(questions):
    q = questions[st.session_state.current_question]
    st.progress((st.session_state.current_question + 1) / len(questions))
    st.markdown(f"<h2 class='sparkle'>Question {st.session_state.current_question + 1} / 10 🥰</h2>", unsafe_allow_html=True)
    
    # BIG CUTE CARTOON - STATIC IMAGE
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image(q["cartoon"], width=200)
    
    st.subheader(q["q"])
    st.write(f"**⭐ Your Score: {st.session_state.score} / 10 ⭐**")
    choice = st.radio("Choose your answer:", q["options"], key=st.session_state.current_question)
    
    if st.button("Submit Answer ✅"):
        if choice == q["answer"]:
            st.success(f"🎉 YAY! That's RIGHT! Well done! 👏")
            st.markdown("### ✨ Correct! ✨")
            st.session_state.score = st.session_state.score + 1  # FIXED SCORE
        else:
            st.error(f"❌ Oops! That's WRONG!")
            st.info(f"💡 Don't worry! Correct Answer: **{q['answer']}**")
        time.sleep(2)
        st.session_state.current_question = st.session_state.current_question + 1
        st.rerun()

# FINAL SCORE SCREEN WITH COMMENTS
else:
    st.markdown("<h1 class='sparkle'>🎊 Quiz Finished! 🎊</h1>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/5968/5968705.png", width=200)
    st.markdown(f"<h2 class='sparkle'>⭐ Your Final Score: {st.session_state.score} / 10 ⭐</h2>", unsafe_allow_html=True)
    
    # SMART COMMENTS BASED ON SCORE
    if st.session_state.score == 10:
        st.success("🏆 PERFECT!!! 10/10 🏆")
        st.markdown("### 🌟 WOW! You are a GENIUS! 🌟")
        st.markdown("You know EVERYTHING about Sikkim and World Cup! I'm so proud of you! 💗")
    elif 8 <= st.session_state.score <= 9:
        st.success(f"🎉 AMAZING! {st.session_state.score}/10 🎉")
        st.markdown("### 😄 EXCELLENT JOB!")
        st.markdown("You did SO WELL! Just 1 or 2 small mistakes. You're super smart! 💗")
    elif 6 <= st.session_state.score <= 7:
        st.success(f"👏 GOOD JOB! {st.session_state.score}/10 👏")
        st.markdown("### 😊 NICE WORK!")
        st.markdown("You know a lot! Keep practicing and you'll get 10/10 next time! 💪")
    elif 4 <= st.session_state.score <= 5:
        st.warning(f"💗 NOT BAD! {st.session_state.score}/10 💗")
        st.markdown("### 🙂 YOU TRIED!")
        st.markdown("That's okay! Learning is fun. Let's play again and do better! ✨")
    else:
        st.info(f"🌟 KEEP TRYING! {st.session_state.score}/10 🌟")
        st.markdown("### 💪 DON'T GIVE UP!")
        st.markdown("Every expert was once a beginner! You can do it! Let's try again! 💗")
    
    st.markdown("<h3 class='sparkle'>💗 Thank you for playing! 💗</h3>", unsafe_allow_html=True)
    st.markdown("### You can play again! ✨")
    
    if st.button("🔄 Play Again"):
        st.session_state.quiz_started = False
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.rerun()
