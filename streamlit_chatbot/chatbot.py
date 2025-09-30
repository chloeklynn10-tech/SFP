import streamlit as st
import pandas as pd


def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def main():
    with st.sidebar:
        st.title("Sidebar") 
    #anything added inside this indented section will pop up in the sidebar#
        st.radio("Radio-button select", ["Meals", "Accomodation", "Entertainment", "Transportation"], index=0)
        if st.radio == "Meals":
                st.selectbox("Dropdown select",  ["Western Cuisine", "Chinese Cuisine", "Japanese Cuisine", "Malay Cuisine", "Indian Cuisine", "Thai Cuisine","Italian Cuisine","Others"], default=["  "])
        elif st.radio == "Accomodation":
                print("Approximate price per night:")
                st.slider("Slider", min_value=1, max_value=700, value=1)
        elif st.radio == "Entertainment":
                print("Take a peek...")
                st.selectbox("Dropdown select",  ["Shopping Centre","Theme Park and Nature","Culture and History"])
        else:
                print("Modes of Transport:")
                st.selectbox("Dropdown select",  ["Train","Buses","Grab and Taxis"])
    

    st.title("Welcome to Ipoh")
    print("What do you want to know?")
    initialize_session_state()

    user_emoji = "😁" # Change this to any emojis you like
    robot_img = "pikachu.jpg" # Find a picture online(jpg/png), download it and drag to
												# your files under the Chatbot folder

    # Display chat messages
    for message in st.session_state.messages:
        if message["role"] == "assistant":
            with st.chat_message("assistant", avatar=robot_img):
                st.write(f"{messages['content']}")
    else:
        with st.chat_message("user", avatar=user_emoji):
            st.write(f"{messages['content']}")

    # Chat input
    if prompt := st.chat_input("What's on your mind?"):
        # Display user message
        with st.chat_message("user"):
            st.write(prompt)
        
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Add simple bot response
        response = f"You said: {prompt}"
        with st.chat_message("assistant"):
            st.write(response)
        
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__": 
    main()

use_emoji = "😁" # Change this to any emojis you like
robot_img = "robot.jpg" # Find a picture online(jpg/png), download it and drag to
												# your files under the Chatbot folder






import streamlit as st
import google.generativeai as genai



# Configure Gemini API
GOOGLE_API_KEY = "AIzaSyC8Y7q-WlvFrIiRpoD07RzokKJ0PiDh1IE"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def get_gemini_response(prompt):
    response = model.generate_content(prompt)
    return response.text

def main():
    st.title("Gemini AI Chatbot")
    
    initialize_session_state()

    # Display chat messages
    for message in st.session_state.messages:
        if message["role"] == "assistant":
            with st.chat_message("assistant", avatar=robot_img):
                st.write(f"{message['content']}")
    else:
        with st.chat_message("user", avatar=user_emoji):
            st.write(f"{message['content']}")

    # Chat input
    if prompt := st.chat_input("Chat with Gemini"):
        # Display user message
        with st.chat_message("user"):
            st.write(prompt)
        
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Get Gemini response
        def get_gemini_response(prompt, persona_instructions):
            full_prompt = f"{persona_instructions}\n\nUser: {prompt}\nAssistant:"
            response = model.generate_content(full_prompt)
            return response.text
        
        # Display assistant response
        with st.chat_message("assistant"):
            st.write(response)
        
        # Add assistant response to history
        st.session_state.messages.append({"role": "assistant", "content": response})



persona_instructions = """
You are a hilarious roast bot.
Be playful and witty.
Your roasts should be light-hearted, never offensive.
Use funny emojis and sarcasm in your replies.
"""

if prompt := st.chat_input("Chat with Gemini"):
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)

    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get Gemini response with persona
    response = get_gemini_response(prompt, persona_instructions)

    # Display assistant response
    with st.chat_message("assistant"):
        st.write(response)

    st.session_state.messages.append({"role": "assistant", "content": response})



if __name__ == "__main__":
    main()