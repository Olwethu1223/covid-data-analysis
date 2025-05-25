# covid-data-analysis
# 🦠 COVID-19 Global Data Tracker

## 📘 Project Overview

This project provides a global overview of the COVID-19 pandemic using data from **Our World In Data**. It focuses on analyzing and visualizing key metrics such as total cases, deaths, new infections, and vaccination progress across various countries over time.

This data analysis project was developed as part of a data analysis assignment using Python and Jupyter Notebook. It uses tools like `pandas`, `matplotlib`, `seaborn`, and `plotly` for data wrangling and visualization.

---

## 📁 Dataset Used

- Source: [Our World in Data – COVID-19 Dataset](https://github.com/owid/covid-19-data/tree/master/public/data)
- File: `owid-covid-data.csv`

---

## 🛠 How to Run This Project

### Requirements:
Make sure you have the following installed:
- Python 3.x
- Jupyter Notebook or JupyterLab
- Required libraries:
  ```bash
  pip install pandas matplotlib seaborn plotly
  ```

### Steps:
1. Download the dataset `owid-covid-data.csv` and place it in the same folder as your notebook.
2. Open the notebook `covid19_data_tracker.ipynb` in Jupyter.
3. Run the cells step by step.
4. Explore the charts and summary insights.
5. Optionally, export the notebook as a PDF for submission or presentation.

---

## 📊 Key Features & Analysis Steps

### ✅ Step 1: Data Collection
- Downloaded the cleaned COVID-19 global dataset from **Our World in Data**.

### ✅ Step 2: Data Loading & Exploration
- Loaded the dataset using `pandas`.
- Explored the dataset’s structure and missing values.

### ✅ Step 3: Data Cleaning
- Filtered and selected countries of interest.
- Converted date fields and handled missing data.

### ✅ Step 4: Exploratory Data Analysis (EDA)
- Tracked and compared total cases, deaths, and new daily cases.
- Calculated death rates.
- Created visual comparisons between countries.

### ✅ Step 5: Visualizing Vaccination Progress
- Analyzed the number of people vaccinated and fully vaccinated.
- Visualized vaccine rollouts across countries.

### ✅ Step 6: Choropleth Map
- Used Plotly to create an interactive world map of total COVID-19 cases.
- Visualized the global spread with color-coded intensity.

### ✅ Step 7: Insights & Reporting
#### Key Insights:
1. **USA and India** had the highest total reported cases.
2. **Kenya** and **South Africa** had lower death rates compared to some Western countries.
3. **Vaccination rates** were highest in wealthier nations, while many developing countries lagged behind.
4. **Vaccination rollouts** accelerated significantly in 2021.
5. **Daily new cases** showed waves of infection at different times across regions.

---

## 📌 Tools & Libraries

- `pandas`: Data manipulation
- `matplotlib` & `seaborn`: Data visualization
- `plotly.express`: Interactive world map
- `Jupyter Notebook`: Development environment

---

## 📥 Output

The final notebook contains:
- Cleaned data
- Graphs and maps
- Written summaries and insights in Markdown
- Option to export as PDF

---

## 👤 Author

Amahle Mathebula – *Data Analysis / Python Learner*  




