import streamlit as st

st.set_page_config(
    page_title="ETIZAN | Workplace Wellbeing",
    page_icon="🌿",
    layout="centered"
)

st.title("🌿 ETIZAN")
st.subheader("Workplace Wellbeing")
st.write("A small step toward a healthier workday.")

st.divider()

st.header("How are you feeling today?")
mood = st.select_slider(
    "Choose your current mood",
    options=["Very low", "Low", "Okay", "Good", "Great"]
)

st.header("What's causing you stress?")
stressor = st.selectbox(
    "Select an option",
    [
        "Workload",
        "Time pressure",
        "Work relationships",
        "Work-life balance",
        "Other",
        "Nothing specific"
    ]
)

st.header("Take a mindful break")
st.write("Relax your shoulders. Breathe in slowly, then breathe out gently.")
if st.button("I've taken a short break"):
    st.success("Well done! Taking a moment for yourself matters.")

if st.button("Save today's check-in"):
    st.success("Your check-in is saved for this session.")
    st.write("Mood:", mood)
    st.write("Main stressor:", stressor)

st.caption(
    "ETIZAN supports personal wellbeing. It does not diagnose or treat health conditions."
)
