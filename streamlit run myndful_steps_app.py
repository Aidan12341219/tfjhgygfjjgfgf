import streamlit as st
import pandas as pd
import datetime

# Set the page title and layout
st.set_page_config(page_title="Myndful Steps", layout="wide")

# Title of the app
st.title("Myndful Steps")

# Initialize session state variables to avoid AttributeError
if 'confidence' not in st.session_state:
    st.session_state.confidence = 5
if 'stage' not in st.session_state:
    st.session_state.stage = "Precontemplation"
if 'exercise_frequency' not in st.session_state:
    st.session_state.exercise_frequency = 3
if 'exercise_duration' not in st.session_state:
    st.session_state.exercise_duration = 30

# Sidebar navigation
st.sidebar.header("Navigation")
app_mode = st.sidebar.radio("Select Mode", ["Home", "Self-Efficacy", "Stages of Change", "Physical Activity", "Results"])

# Home Page
if app_mode == "Home":
    st.header("Welcome to Myndful Steps")
    st.write("""
    This app helps you track your health behavior changes, measure your exercise levels, and get personalized recommendations to support your wellness journey.
    """)

# Self-Efficacy Assessment
elif app_mode == "Self-Efficacy":
    st.header("Self-Efficacy Assessment")
    
    st.write("""
    Self-efficacy refers to an individual's belief in their ability to succeed in specific situations or accomplish a task.
    This assessment will help measure your confidence in making health behavior changes.
    """)

    # Self-Efficacy scale (1-10)
    st.session_state.confidence = st.slider("On a scale from 1 to 10, how confident are you in your ability to make a lasting change in your health behaviors?", 1, 10, st.session_state.confidence)
    
    st.success(f"Your self-efficacy score is: {st.session_state.confidence}. Higher scores indicate greater confidence in making health changes.")

# Stages of Change Assessment
elif app_mode == "Stages of Change":
    st.header("Stages of Change Assessment")

    st.write("""
    Behavior change occurs in stages. This assessment will help identify your current stage of change for health behaviors.
    """)

    # Stages of Change options
    st.session_state.stage = st.radio("Which of the following best describes your current stage of behavior change?", 
                                      ("Precontemplation", "Contemplation", "Preparation", "Action", "Maintenance"))

    st.success(f"Your current stage of change is: {st.session_state.stage}.")

# Physical Activity Assessment
elif app_mode == "Physical Activity":
    st.header("Physical Activity Assessment")

    st.write("""
    The Physical Activity Assessment helps evaluate the frequency and duration of your weekly exercise routine.
    """)

    # Frequency of Exercise (How often per week)
    st.session_state.exercise_frequency = st.slider("How many days per week do you engage in moderate or strenuous exercise?", 0, 7, st.session_state.exercise_frequency)

    # Duration of Exercise (How many minutes per session)
    st.session_state.exercise_duration = st.slider("On average, how many minutes per session do you engage in moderate or strenuous exercise?", 0, 120, st.session_state.exercise_duration)

    st.success(f"You engage in exercise {st.session_state.exercise_frequency} days per week for an average of {st.session_state.exercise_duration} minutes per session.")

# Results Page
elif app_mode == "Results":
    st.header("Myndful Steps Results")

    st.write(f"**Self-Efficacy Score**: {st.session_state.confidence}")
    st.write(f"**Stage of Change**: {st.session_state.stage}")
    st.write(f"**Physical Activity**: {st.session_state.exercise_frequency} days per week, {st.session_state.exercise_duration} minutes per session.")

    # Provide recommendations based on user input
    st.write("\n### Recommendations:")
    
    if st.session_state.confidence < 5:
        st.write("- **Build Confidence**: Consider focusing on small, consistent actions to boost confidence in your ability to make changes.")
    
    if st.session_state.stage == "Precontemplation":
        st.write("- **Precontemplation**: Reflect on why a health change is important for you.")
    elif st.session_state.stage == "Contemplation":
        st.write("- **Contemplation**: Set small, achievable goals to start moving forward.")
    elif st.session_state.stage == "Preparation":
        st.write("- **Preparation**: Create a clear action plan and set a start date.")
    elif st.session_state.stage == "Action":
        st.write("- **Action**: Track your progress and celebrate small wins.")
    elif st.session_state.stage == "Maintenance":
        st.write("- **Maintenance**: Keep up the good work and consider ways to prevent relapse.")

    # Exercise recommendations
    if st.session_state.exercise_frequency < 3:
        st.write("- **Physical Activity**: Aim to increase exercise frequency to 3-5 days per week for optimal health benefits.")
    if st.session_state.exercise_duration < 30:
        st.write("- **Physical Activity**: Try to meet the recommendation of 150 minutes of moderate exercise weekly by increasing your session duration.")

    st.write("\nRemember, Bentley University’s Counseling Center is available for support:")
    st.write("""
    - **Phone**: 781-891-2274
    - **Location**: Callahan Building, 2nd Floor
    - **Hours**: 
        - Administrative Concerns: Mon-Fri, 8:30am-4:30pm
        - Clinical Care: Mon-Fri, 9am-12pm & 1pm-4pm
        - Closed for lunch from 12-1pm, weekends, and Bentley holidays
    """)

    st.write("Keep up the great work, and continue striving for positive health behavior change with Myndful Steps!")
