# 🎬 IMDb Movie Success Predictor: My Final Capstone Project

Welcome to my repository! If you are reading this, you are looking at the culmination of my final semester in Business Data Analytics. Countless late nights, a dangerous amount of caffeine, and moments of wrestling with massive, messy datasets have all poured into this one project. 

I set out to answer a question that has fascinated the film industry for decades: **Can we predict whether a movie will be a hit or a flop based solely on its core attributes?** This project isn't just about crunching numbers or passing a class; it is a complete, end-to-end data journey. I took raw, real-world data directly from IMDb, cleaned it up, explored the hidden stories inside it, built machine learning models, and finally brought it to life in an interactive web app. 

I am incredibly proud of this work. Thank you for taking the time to check it out!

---

## 🧭 What's Inside? (The Workflow)

I processed hundreds of thousands of records from the official IMDb database. Here is the journey this project takes:
* **Data Ingestion & Cleaning:** Dealing with missing values, filtering out extreme outliers (like 10-hour movies!), and untangling IMDb's quirky data formatting so the machine learning models could actually understand it.
* **Exploratory Data Analysis (EDA):** Generating statistical insights and visual charts to find the "sweet spot" for movie runtimes, rank top genres, and map out historical rating trends.
* **Machine Learning Pipelines:** * **Regression:** Predicting the exact IMDb rating of a title using Linear Regression.
  * **Classification:** Predicting if a movie is a "Hit" (Rating ≥ 7.0) using a powerful Logistic Regression pipeline, complete with One-Hot Encoding for categorical features.
* **The Web App:** A fully functional Streamlit frontend. You can plug in custom movie metrics and see if your hypothetical movie would survive the harsh critics of the internet.

---

## 🛠️ The Tech Stack
* **Python 3:** The backbone of the entire project.
* **Pandas & NumPy:** For the heavy lifting and data manipulation.
* **Matplotlib & Seaborn:** For bringing the data to life visually.
* **Scikit-Learn:** For the machine learning pipelines, baseline benchmarks, and evaluations.
* **Streamlit:** For building the interactive user interface.
* **Joblib:** For saving and loading the trained models.

---

## ⚠️ Important Note About the Data (How to Run This)

Because the raw IMDb datasets are absolutely massive (well over GitHub's strict 100MB file limit), I could not upload the raw `.tsv` files directly to this repository. 

**To grade or run my notebook successfully, please follow these quick steps:**

1. Go to the official [IMDb Datasets page](https://datasets.imdbws.com/).
2. Download these two specific compressed files:
   * `title.basics.tsv.gz`
   * `title.ratings.tsv.gz`
3. Extract them on your computer.
4. Rename them to `title.basics.tsv_2` and `title.ratings.tsv_2` (or simply update the file paths in the very first cell of my Jupyter Notebook).
5. Place them in the same folder as the `.ipynb` file, or upload them to your Google Colab environment.
6. Open the notebook and click **Run All**!

---

## 🕹️ Try the Interactive Web App!

I didn't just want to leave the models sitting in a notebook—I wanted them to be usable. I have included the trained model (`imdb_classification_pipeline.pkl`), the saved genres (`top_genres.pkl`), and the app script (`app.py`) right here in the repository.

To play with the app locally:
1. Clone this repository to your machine.
2. Open your terminal or command prompt in the project folder.
3. Run the following command:
   `streamlit run app.py`
4. Your browser will open the app, and you can start predicting movie hits immediately!

---

## ❤️ Final Thoughts

Closing this notebook marks the end of an incredible academic chapter for me. Data analytics isn't just about math; it is about finding the story that the numbers are trying to hide. I learned a massive amount about memory management, model pipelines, and deployment through this dataset.

If you have any questions, feedback, or just want to chat about the data, please feel free to reach out. Thank you for visiting!
