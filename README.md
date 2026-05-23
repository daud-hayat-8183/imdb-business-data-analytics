# 🎬 Predicting Movie Success: My BDA Final Project

Hi there! I'm Muhhammad Dawood Hayat, and welcome to my final semester Business Data Analytics project for COMSATS University Islamabad. 

If you are reading this, you are looking at the exact moment a whole semester of learning actually clicked into place. I honestly can't believe this project is finally finished. Between the late-night coding sessions, wrestling with massive datasets that kept crashing my Colab environment, and figuring out how to deploy a web app—this has been an absolute rollercoaster. But it works, and I am so incredibly proud of it.

I wanted to answer a question that has always fascinated me: **Can we actually predict if a movie will be a hit or a massive flop based just on its core data?** Let me walk you through what I built.

---

## 🧠 What I Actually Did (The Journey)

This wasn't just about throwing numbers into a machine. It was a complete start-to-finish data journey.
* **Taming the Data:** I started with hundreds of thousands of raw records straight from IMDb. The data was a beast. I had to clean out missing values, drop extreme outliers (nobody is watching a 10-hour movie!), and format everything so my models could actually read it.
* **Finding the Story (EDA):** This was the fun part. I created visualizations to find out what really makes a movie tick. Turns out, documentaries score surprisingly high, and there is definitely a "sweet spot" for how long a movie should be if you want a good rating.
* **Training the Machine:** I built two distinct machine learning pipelines. First, a Linear Regression model to predict the exact IMDb rating. Second, a Logistic Regression model to classify whether a movie is officially a "Hit" (a rating of 7.0 or higher).
* **Bringing it to Life:** I didn't want my models just sitting in a Jupyter notebook where nobody could use them. So, I built a fully interactive web app using Streamlit. You can literally type in your own imaginary movie details and see if my model thinks it will survive the box office.

---

## ⚠️ How to Grade or Run My Code (Please Read!)

Here is the catch: The raw IMDb data files are huge. They completely break GitHub's strict file size limits, so I couldn't upload them here. 

**If you want to run my `.ipynb` notebook, here is exactly what you need to do:**
1. Go to the official [IMDb Datasets page](https://datasets.imdbws.com/).
2. Download these two specific compressed files: `title.basics.tsv.gz` and `title.ratings.tsv.gz`.
3. Extract them on your computer.
4. Rename them to `title.basics.tsv_2` and `title.ratings.tsv_2` (or just change the file names in the very first block of my code).
5. Put them in the same folder as my notebook, or upload them to your Google Colab workspace.
6. Open my notebook, hit **Run All**, and watch the magic happen!

---

## 🕹️ Try the Web App Yourself!

I've included everything you need right here in this repository to run the app on your own computer (`app.py`, the `top_genres.pkl` list, and the `imdb_classification_pipeline.pkl` model).

To play with it:
1. Clone this repository to your laptop.
2. Open your terminal or command prompt inside the folder.
3. Type this exact command and hit enter: `streamlit run app.py`
4. A browser window will pop up. Have fun testing it out!

---

## 📊 A Quick Peek at the Insights

![IMDb Data Visualizations](eda_visualizations.png)

*If you just want to see some of the trends I found without running the code, check out the graphs above!*

---

## ❤️ Final Thoughts

Finishing this capstone feels like closing a massive chapter. Data analytics isn't just about math or code anymore; I've learned it's really about finding the human stories hidden inside millions of rows of text. 

Thank you so much for taking the time to visit my repository and look at my work. If you have any feedback or just want to chat about the project, I'd love to hear from you.
