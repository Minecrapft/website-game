import streamlit as st 
import random
from PIL import Image




st.set_page_config(page_title="Dead or Alive", page_icon="☠️", layout="centered")

option = ["## ALIVE!"] * 3 + ["## DEAD!"]


if "score" not in st.session_state:
    st.session_state.score = 0
    

if "dead_or_alive" not in st.session_state:  
    st.session_state.dead_or_alive = random.choice(option)
    
if "high_score" not in st.session_state:
    st.session_state.high_score = 0

if "attempts" not in st.session_state:
    st.session_state.attempts = 0    

number_of_Scores = st.session_state.score + 1

Odds_of_surviving = (0.75 ** number_of_Scores ) * 100
High_score_probality = (0.75 ** st.session_state.high_score) * 100


st.title("Dead or Alive")

st.write("---")

st.write("### Click the button to see if you survive!")
st.write("""You have a 3-to-1 chance of surviving, which means, 
         at the start, you have a 75% chance of surviving. Each time you score, 
         the odds of your survival become less likely. 
         I will give you 50 pesos if you score 50, which has a probability of 0.00173%""")

st.write("---")

st.write("# High score", st.session_state.high_score)
st.write(f"Your high score has a probability of {High_score_probality}%") 

st.write("---")



is_pressed = st.button("Press here")

st.write(f"Your chances of surviving {Odds_of_surviving}%")


if is_pressed:
    st.write(st.session_state.dead_or_alive)    
    
    if st.session_state.dead_or_alive == "## ALIVE!":
        st.write("You are alive, click the button again ")
        st.session_state.dead_or_alive = random.choice(option)
        st.session_state.score += 1
        st.write("## Current Score: ", st.session_state.score)
        if st.session_state.score > st.session_state.high_score:
            st.session_state.high_score = st.session_state.score
                                      
    elif st.session_state.dead_or_alive == "## DEAD!":
        st.session_state.dead_or_alive = random.choice(option)
        st.write("You are dead")
        st.session_state.score = 0
        st.write("## Current Score: ", st.session_state.score)


if is_pressed:
    st.session_state.attempts += 1          
    st.write("### total button pressed: ", st.session_state.attempts)