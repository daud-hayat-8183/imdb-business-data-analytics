import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load resources
@st.cache_resource
def load_assets():
    model = joblib.load("imdb_classification_pipeline.pkl")
    genres = joblib.load("top_genres.pkl")
    return model, genres

model, top_genres = load_assets()

st.title("🎬 IMDb Hit Predictor App")
st.write("Enter the details of a movie/title to predict if it will be a Hit (Rating ≥ 7.0).")

# Layout
col1, col2 = st.columns(2)

with col1:
    start_year = st.number_input("Release Year", min_value=1900, max_value=2030, value=2023)
    runtime = st.number_input("Runtime (Minutes)", min_value=10, max_value=300, value=120)
    title_type = st.selectbox("Title Type", ["movie", "tvSeries", "short", "documentary", "tvEpisode"])

with col2:
    votes = st.number_input("Number of Votes", min_value=100, value=5000)
    selected_genres = st.multiselect("Select Genres", top_genres)

if st.button("Predict Outcome"):
    # Build a dictionary matching the pipeline expectations
    input_data = {
        'startYear': [start_year],
        'runtimeMinutes': [runtime],
        'numVotes': [votes],
        'titleType': [title_type]
    }
    
    # Set binary flags for all top genres
    for g in top_genres:
        input_data[f'genre_{g}'] = [1 if g in selected_genres else 0]
        
    # Create DataFrame
    input_df = pd.DataFrame(input_data)
    
    # Predict
    prediction = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1] # Probability of being class 1 (Hit)
    
    st.divider()
    if prediction == 1:
        st.success(f"🌟 **Prediction: HIT** (Probability: {prob:.2%})")
    else:
        st.error(f"📉 **Prediction: FLOP** (Probability: {prob:.2%})")
