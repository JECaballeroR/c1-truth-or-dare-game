import streamlit as st
import random

# Configuración de página
st.set_page_config(page_title="Truth or Dare", layout="wide")

# Títulos de cabecera
st.title("🎉 C1's Marketing Team Truth or Dare")
st.markdown("""
*Just in case someone can't think of something to ask, we also have this nice app to give us some!  
They are SFW and Zoom-friendly!*  
---
""")

# Banco original
truths = [
    "What’s your most unusual remote work habit?",
    "Have you ever stayed in pajamas all day while working?",
    "What’s the most embarrassing thing that happened to you on a video call?",
    "What's your secret to pretending you're not distracted?",
    "What’s the strangest item on your desk right now?",
    "What’s one task you always procrastinate on?",
    "Who in the team would you swap jobs with for a day and why?",
    "If you could eliminate one work task forever, what would it be?",
    "Have you ever accidentally sent a message to the wrong work chat?",
    "What's one non-work tab open on your browser right now?",
    "What’s a guilty pleasure you indulge in during breaks?",
    "What’s one thing your coworkers would be surprised to learn about you?",
    "What’s the weirdest snack you’ve had while working?",
    "Who’s the funniest person on the team (besides you)?",
    "What’s a skill you secretly wish you had for this job?",
    "Have you ever been on a call and muted just to laugh?",
    "What's the last non-work thing you Googled?",
    "What’s the weirdest background you’ve seen on a Zoom call?",
    "What’s the longest you’ve gone without speaking to anyone in a day?",
    "What's one thing you'd add to our remote work routine?",
    "Have you ever pretended to freeze on a Zoom call?",
    "What's a pet peeve you have about virtual meetings?",
    "If your home workspace had a theme song, what would it be?",
    "What’s the most creative excuse you’ve made for being late?",
    "What emoji do you overuse in work chats?",
    "Who on the team would you want as your survival partner?",
    "What’s your go-to work distraction?",
    "What’s a professional skill you learned recently?",
    "What was your first job ever?",
    "What do you love most about working remotely?"
]

dares = [
    "Give a 1-minute tour of your workspace.",
    "Show the weirdest thing within arm’s reach.",
    "Do your best impression of your favorite boss or colleague (nicely!).",
    "Change your Zoom background to something ridiculous for the next 10 mins.",
    "Talk about your favorite snack as if you're on a cooking show.",
    "Do 10 jumping jacks or dance moves on camera.",
    "Balance something on your head for 30 seconds.",
    "Let someone else choose your Zoom background.",
    "Speak in an accent of your choice for the next question you answer.",
    "Share a picture of your pet or your favorite mug.",
    "Draw a self-portrait and show it on camera.",
    "Take a sip of your drink with exaggerated dramatic flair.",
    "Type your next sentence with your nose.",
    "Hum a popular song and let others guess it.",
    "Give a fake product pitch using only items in your reach.",
    "Wear a funny hat or object on your head for the next round.",
    "Do a slow clap while maintaining eye contact with the camera.",
    "Pretend your chair is a rollercoaster and react accordingly.",
    "Pick an object near you and sell it QVC-style.",
    "Pretend to be a news anchor delivering breaking news about your morning.",
    "Put on your best “Zoom face” and hold it for 15 seconds.",
    "Rename yourself on Zoom to something silly for the next 5 minutes.",
    "Make a 10-second commercial for your favorite snack or beverage.",
    "Share a clean joke that made you laugh recently.",
    "Mime an activity (e.g., making coffee) for others to guess.",
    "Show us the wallpaper or lock screen of your phone.",
    "Speak only in rhymes for your next turn.",
    "Pretend your webcam is frozen for 15 seconds.",
    "Show a hidden talent (e.g., tongue roll, pen spin, etc.).",
    "Reenact your morning routine using props."
]

# Inicializar estado de sesión
if "remaining_truths" not in st.session_state:
    st.session_state.remaining_truths = truths.copy()
if "remaining_dares" not in st.session_state:
    st.session_state.remaining_dares = dares.copy()
if "last_item" not in st.session_state:
    st.session_state.last_item = ""

# Funciones
def get_random_item(category):
    if category == "truth":
        if len(st.session_state.remaining_truths) == 0:
            st.session_state.last_item = "⚠️ No more TRUTHs left! Click '🔄 Re-start question bank' to refresh."
            return
        item = random.choice(st.session_state.remaining_truths)
        st.session_state.remaining_truths.remove(item)
    else:
        if len(st.session_state.remaining_dares) == 0:
            st.session_state.last_item = "⚠️ No more DAREs left! Click '🔄 Re-start question bank' to refresh."
            return
        item = random.choice(st.session_state.remaining_dares)
        st.session_state.remaining_dares.remove(item)
    st.session_state.last_item = item

def restart_banks():
    st.session_state.remaining_truths = truths.copy()
    st.session_state.remaining_dares = dares.copy()
    st.session_state.last_item = ""

# Layout de botones grandes
col1, col2 = st.columns(2)
with col1:
  
    if st.button("🎯 TRUTH", use_container_width=True):
        get_random_item("truth")
with col2:
    if st.button("🔥 DARE", use_container_width=True):
        get_random_item("dare")

# Resultado actual
st.markdown("### 👇 Prompt generado:")
if st.session_state.last_item:
    st.info(st.session_state.last_item, icon="💬")
else:
    st.info("Click on TRUTH or DARE to begin!", icon="💬")

# Botón para reiniciar
st.markdown("---")
if st.button("🔄 Re-start question bank"):
    restart_banks()
    st.success("Done!")
