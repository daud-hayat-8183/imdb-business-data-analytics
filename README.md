# 🎬 IMDb Movie Success Predictor: My Final Semester Business Data Analytics Project

Welcome to my repository! If you're reading this, you are looking at the culmination of my final semester in Business Data Analytics. Countless late nights, endless cups of coffee, and moments of wrestling with massive datasets have all poured into this one comprehensive project. 

I set out to answer a question that has fascinated the film industry for decades: **Can we predict whether a movie will be a hit or a flop based solely on its core attributes?** This project isn't just about crunching numbers; it's a complete end-to-end data journey. From taking raw, messy, real-world data directly from IMDb, cleaning it, exploring its hidden stories, to building machine learning models and wrapping it all up in an interactive web application. I am incredibly proud of this work, and I'm thrilled to share it with you.

---

## 🚀 The Project Overview

In this project, I processed over hundreds of thousands of records from the official IMDb database. The workflow includes:
1. **Data Ingestion & Cleaning:** Handling missing values, filtering out extreme outliers (like 10-hour movies!), and dealing with IMDb's quirky data formatting.
2. **Exploratory Data Analysis (EDA):** Generating statistical insights and beautiful visualizations to understand runtime trends, top genres, and historical rating averages.
3. **Machine Learning Pipeline:** - **Regression:** Predicting the exact IMDb rating using a Linear Regression model.
   - **Classification:** Predicting if a movie is a "Hit" (Rating ≥ 7.0) using a powerful Logistic Regression pipeline with One-Hot Encoding for categorical features.
4. **Interactive Deployment:** A fully functional Streamlit frontend application where users can input custom movie metrics to see if their hypothetical movie would survive the harsh critics of IMDb.

---

## 🛠️ Tech Stack & Libraries Used
- **Python 3** (The backbone of it all)
- **Pandas & NumPy** (For heavy lifting and data manipulation)
- **Matplotlib & Seaborn** (For bringing the data to life visually)
- **Scikit-Learn** (For the machine learning pipelines and models)
- **Streamlit** (For building the interactive user interface)
- **Joblib** (For saving and loading the trained models)

---

## 🗄️ How to Get the Data (Important!)

Because the raw IMDb datasets are absolutely massive (well over GitHub's 100MB file limit), I have not included them in this repository. To run my notebook successfully, you will need to download the data yourself. 

Don't worry, it's free and easy! Here is how to get the exact files I used:

1. Go to the official IMDb dataset page: [IMDb Datasets (Non-Commercial)](https://datasets.imdbws.com/)
2. Download these two specific files:
   - `title.basics.tsv.gz`
   - `title.ratings.tsv.gz`
3. Extract the `.gz` files on your computer. You will get two `.tsv` files.
4. Rename them to `title.basics.tsv_2` and `title.ratings.tsv_2` (or just update the file paths in the first cell of my notebook).
5. Put them in the same folder as the notebook, or upload them to your Google Colab environment.

---

## 🏃‍♂️ How to Run This Project

**1. To view my analysis and models:**
Simply open the `.ipynb` notebook file in Google Colab or Jupyter Notebook. Ensure the two data files (mentioned above) are loaded into your environment. You can click "Run All" and watch the magic happen step-by-step.

**2. To run the Interactive Web App locally:**
I have included the trained model (`imdb_classification_pipeline.pkl`), the saved genres (`top_genres.pkl`), and the app script (`app.py`) right here in the repository! 
To play with the app:
- Clone this repository to your local machine.
- Open your terminal or command prompt in the folder.
- Run the following command:
  ```bash
  streamlit run app.py
