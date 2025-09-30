import streamlit as st
import random

st.title("🎲 Number Guessing Game")

st.write("I am thinking of a number between 1 and 20. Can you guess it?")

import streamlit as st
import random

st.title("🎲 Number Guessing Game")

# Generate a random number once and store it in session state
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 20)

# User input
guess = st.number_input("Enter your guess (1-20):", min_value=1, max_value=20, step=1)

# Button to check guess
if st.button("Check my guess"):
    if guess == st.session_state.number:
        st.success("🎉 Correct! You guessed the number!")
        st.session_state.number = random.randint(1, 20)  # reset game
    elif guess < st.session_state.number:
        st.info("Too low! Try again.")
    else:
        st.info("Too high! Try again.")
