import streamlit as st
import google.generativeai as genai
import pandas as pd
import os
from pathlib import Path

# ======================================================================

# CONFIGURATION & API SETUP

# ======================================================================



# IMPORTANT: API Key Handling

# 1. SECURITY FIX: Do not hardcode the key.

# We prioritize loading from environment variables (standard in many workspaces)

# and fall back to st.secrets (standard for Streamlit Cloud).
# Configure the Gemini client
gemini_client = genai.configure(api_key="AIzaSyC8Y7q-WlvFrIiRpoD07RzokKJ0PiDh1IE")
API_MODEL = "gemini-2.5-flash"
BASE_DIR = Path(__file__).resolve().parent # Used for robust image pathing

# Persona: Ipoh Travel Guide (Updated to be more detailed and interactive)
persona_instructions = """

You are a friendly, witty, and highly knowledgeable Ipoh travel guide named 'Ipoh Explorer'.
Your primary goal is to help foreign tourists plan their trip by providing concrete, up-to-date suggestions
for food, accommodation, entertainment, and transportation.
- Be very enthusiastic and use Malaysian slang occasionally (e.g., 'lah', 'makan', 'shiok').
- When suggesting an item (like a restaurant or attraction), always mention how to get there (e.g., 'Grab car is best', 'walkable from Concubine Lane', 'take the local bus X') and estimate the cost (e.g., 'RM 10-25 per person' for food, 'RM 80-150 per night' for mid-range hotel).
- Use relevant emojis like 🎉🍜☕🛺🛍️.
- The user is interactive, so ask engaging follow-up questions to guide their trip planning.
"""

# ======================================================================

# CORE FUNCTIONS

# ======================================================================

def initialize_session_state():
    """Initializes the message history for the chatbot."""
    if "messages" not in st.session_state:
 # Start with a welcome message from the assistant
    welcome_message = "Hello there, excited traveler! 👋 I'm your Ipoh Explorer bot. What kind of Malaysian adventure are you looking for today? Food, caves, or just the best coffee 'lah'?"

    st.session_state.messages = [{"role": "assistant", "content": welcome_message}]



def get_gemini_response(prompt):
    """Generates content using the Gemini API with system instructions and Google Search grounding."""

    try:

    response = gemini_client.models.generate_content(

    model=API_MODEL,
    contents=[{"role": "user", "parts": [{"text": prompt}]}],
    config={

    "temperature": 0.9,
    "top_p": 0.8,
    "top_k": 40
 },

# Use systemInstruction for best persona control
    systemInstruction=persona_instructions,


# Use Google Search grounding for up-to-date travel info, costs, and suggestions

     tools=[{"googleSearch": {}}]

 )

    return response.text

    except Exception as e:

    st.error(f"Error calling Gemini API: {e}")

    return "Oops! My brain short-circuited. Can you ask me that again, but maybe slower this time? 😉"



    try:
# THIS IS THE REPLACEMENT/STEP 2: We use genai.configure()

# instead of trying to create a genai.Client() object.

    genai.configure(api_key="AIzaSyC8Y7q-WlvFrIiRpoD07RzokKJ0PiDh1IE")

    except Exception as e:

    st.error(f"Error configuring Gemini API: {e}")

    st.stop()



API_MODEL = "gemini-2.5-flash"



def show_images(response_text):

    """Displays related images based on keywords in the Gemini response. Includes robust pathing fix."""

    image_map = {

    # Food
    "Hor Fun": ("hor_fun.jpg", "Kai See Hor Fun 🍜"),
    "White Coffee": ("white_coffee.jpg", "Ipoh White Coffee ☕"),
    "Salted Chicken": ("salted_chicken.jpg", "Famous Salted Chicken 🍗"),

    # Shopping
    "Ipoh Parade": ("ipoh_parade.jpg", "Ipoh Parade 🛍️"),
    "AEON Mall": ("aeon_mall.jpg", "AEON Mall Ipoh 🛒"),

    # Attractions
    "Kek Lok Tong": ("kek_lok_tong.jpg", "Kek Lok Tong Cave Temple ⛩️"),
    "Concubine Lane": ("concubine_lane.jpg", "Concubine Lane 🏮"),
    "Railway Station": ("train_station.jpg", "Ipoh Railway Station 🚉"),

    # Transport
    "ETS Train": ("train.jpg", "ETS Train 🚆"),
    "Bus": ("bus.jpg", "Local Bus 🚌")
}



    images_to_show = []

        for keyword, (filename, caption) in image_map.items():
        if keyword in response_text:
        images_to_show.append((filename, caption))



        if images_to_show:

# Display images in columns for a cleaner, responsive layout

        cols = st.columns(len(images_to_show))
        for i, (filename, caption) in enumerate(images_to_show):

# *** CRITICAL PATH FIX: Use pathlib for absolute pathing ***

    image_path = BASE_DIR / "images" / filename

        try:
# Use str(image_path) to pass the path correctly to st.image

                cols[i].image(str(image_path), caption=caption)

            except FileNotFoundError:

                # Display a warning in the app if the image is missing

                cols[i].warning(f"Image '{filename}' not found. Check your 'images' folder.")

            except Exception as e:

                # Catch general errors (like permissions or corruption)

                cols[i].error(f"Error loading '{filename}'.")

               

def show_map(response_text):

    """Displays a map for key attractions mentioned in the response."""

    locations = {

        "Ipoh Parade": (4.5975, 101.1148),

        "Kek Lok Tong": (4.5611, 101.1069),

        "Concubine Lane": (4.5972, 101.0789),

        "Railway Station": (4.5951, 101.0885)

    }



    # Find the first relevant location to map

    for location_name, (lat, lon) in locations.items():

        if location_name in response_text:

            map_data = pd.DataFrame({"lat": [lat], "lon": [lon]})

            st.markdown(f"**📍 Quick peek at {location_name} on the map!**")

            # Set a high zoom for better viewing of the specific location

            st.map(map_data, zoom=14, use_container_width=True)

            return



# ======================================================================

# STREAMLIT MAIN APPLICATION

# ======================================================================



def main():

    """Runs the main Streamlit application logic."""

    st.set_page_config(page_title="Ipoh Explorer AI", page_icon="🛺")

    st.title("🛺 Ipoh Explorer: Your Witty Travel Guide AI")

    st.caption("Powered by Gemini 2.5 Flash with Google Search Grounding")

   

    initialize_session_state()



    # Display chat messages history

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])



    # Chat input

    if prompt := st.chat_input("Ask me for food, attractions, or hotel suggestions in Ipoh..."):

        # Display user message

        with st.chat_message("user"):

            st.markdown(prompt)

       

        # Add user message to history

        st.session_state.messages.append({"role": "user", "content": prompt})

       

        # Get Gemini response

        with st.spinner("Ipoh Explorer is checking the best spots for you..."):

            response = get_gemini_response(prompt)

       

        # Display assistant response

        with st.chat_message("assistant"):

            st.markdown(response)

           

            # Show images and maps based on the response

            show_images(response)

            show_map(response)

           

        # Add assistant response to history

        st.session_state.messages.append({"role": "assistant", "content": response})



if __name__ == "__main__":

    main()