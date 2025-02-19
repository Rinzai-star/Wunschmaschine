import streamlit as st

# Wunschmaschine-Titel
st.title("✨ Wunschmaschine ✨")
st.subheader("Formuliere deinen Wunsch und folge den Schritten!")

# Eingabe des Wunsches
wish = st.text_input("📌 Dein Wunsch:")

# Falls der Nutzer einen Wunsch eingibt, startet der Prozess
if wish:
    st.write("🔍 Dein Wunsch:", wish)
    
    # Erster Reflexionsschritt
    st.subheader("1️⃣ Reflexion: Warum willst du das?")
    reason = st.text_area("Was steckt hinter diesem Wunsch? Warum möchtest du ihn wirklich?")
    
    # Zweiter Reflexionsschritt
    st.subheader("2️⃣ Annahme & Blockaden erkennen")
    st.write("Gibt es innere Widerstände oder Muster, die diesem Wunsch entgegenstehen?")
    acceptance = st.text_area("Was darfst du erst annehmen, bevor dieser Wunsch Realität wird?")
    
    # Dritter Reflexionsschritt
    st.subheader("3️⃣ Handlung oder Anpassung?")
    action = st.radio("Ist jetzt der richtige Zeitpunkt?", ("Ja, ich kann aktiv werden!", "Nein, es braucht noch Zeit."))
    
    if action == "Ja, ich kann aktiv werden!":
        steps = st.text_area("Welche konkreten Schritte kannst du jetzt unternehmen?")
    else:
        st.write("Vielleicht ist es gerade wichtiger, Geduld zu üben oder etwas anderes zuerst zu erledigen.")
    
    # Abschluss
    st.subheader("4️⃣ Letzte Überprüfung")
    confirm = st.checkbox("Ich vertraue dem Prozess und lasse den Wunsch los.")
    
    if confirm:
        st.success("🌟 Dein Wunsch wurde bewusst bearbeitet. Jetzt kannst du ihn loslassen und vertrauen! 🌟")
