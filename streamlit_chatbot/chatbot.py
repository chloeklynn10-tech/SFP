import streamlit as st
import google.generativeai as genai

# -------------------- API Setup --------------------
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]  # safer way!
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

# -------------------- Helpers --------------------
def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def get_gemini_response(prompt, persona_instructions=""):
    full_prompt = f"{persona_instructions}\n\nUser: {prompt}\nAssistant:"
    response = model.generate_content(full_prompt)
    return response.text

# -------------------- Persona --------------------
persona_instructions = """
You are a friendly Ipoh travel guide for foreigners.  
- Recommend **meals, accommodation, entertainment, and transportation**.  
- Use light humor, emojis, and be welcoming.  
- Keep answers clear and practical.
"""

# -------------------- Main App --------------------
def main():
    st.title("🌏 Welcome to Ipoh Travel Guide (Powered by Gemini AI)")

    # Sidebar
    with st.sidebar:
        st.header("Explore Ipoh")
        category = st.radio("Choose a category", 
                            ["Meals", "Accommodation", "Entertainment", "Transportation"])
        
        if category == "Meals":
            choice = st.selectbox("Cuisine", 
                                  ["Western", "Chinese", "Japanese", "Malay", "Indian", "Thai", "Italian", "Others"])
            st.write(f"You’re curious about {choice} food 🍽️")
        elif category == "Accommodation":
            price = st.slider("Approximate price per night (RM)", 50, 700, 200)
            st.write(f"Looking for stays around RM {price}/night 🏨")
        elif category == "Entertainment":
            activity = st.selectbox("Pick one", 
                                    ["Shopping", "Theme Park & Nature", "Culture & History"])
            st.write(f"Great! You like {activity} 🎉")
        else:
            transport = st.selectbox("Transport", ["Train", "Bus", "Grab/Taxi"])
            st.write(f"You prefer {transport} 🚖")

    # Chatbot
    st.subheader("💬 Chat with Ipoh AI Guide")
    initialize_session_state()

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input("Ask me anything about Ipoh..."):
        st.chat_message("user").write(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = get_gemini_response(prompt, persona_instructions)
        st.chat_message("assistant").write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# -------------------- Run --------------------
if __name__ == "__main__":
    main()
