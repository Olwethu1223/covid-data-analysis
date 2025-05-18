# covid-data-analysis
# COVID-19 Global Data Tracker

This project analyzes COVID-19 global data to explore trends in cases, deaths, and vaccinations across selected countries over time. The analysis is conducted using Python and various data analysis libraries, with visualizations to effectively communicate findings.

## 📁 Project Structure

- **owid-covid-data.csv**: COVID-19 dataset sourced from [Our World in Data](https://ourworldindata.org/coronavirus-source-data).
- **eda.py**: Script for data loading, cleaning, and exploratory data analysis (EDA).
- **analysis_outputs/plots**: Directory where all generated visualizations are saved.
- **covid_analysis.ipynb**: Jupyter Notebook with data exploration, visualizations, and key insights.

## ✅ Project Objectives

- Import and clean COVID-19 data
- Analyze time trends for cases, deaths, and vaccinations
- Compare metrics across selected countries (Kenya, USA, India)
- Visualize trends with charts
- Summarize findings in a Jupyter Notebook

## 📦 Dependencies

- Python 3.x
- pandas
- matplotlib
- os

Install the required libraries using:

```bash
pip install pandas matplotlib
```

## 🚀 How to Run the Project

1. Clone the repository or download the files.
2. Ensure that the `owid-covid-data.csv` file is in the same directory as `eda.py`.
3. Open a terminal and navigate to the project directory.

Run the analysis script:

```bash
python eda.py
```

4. View the generated plots in the `analysis_outputs/plots` directory.

## 📊 Data Analysis and Visualizations

- Total cases and deaths over time for each country
- New daily cases comparison
- Vaccination progress over time

All visualizations are saved in the `analysis_outputs/plots` folder.

## ✨ Insights

- Key observations and insights are documented in the Jupyter Notebook (`covid_analysis.ipynb`).
- Markdown cells in the notebook provide detailed explanations of the analysis steps and findings.

## 🛠️ Future Enhancements

- Integrate interactive visualizations using Plotly or Seaborn.
- Expand the dataset to include additional countries.
- Implement a map visualization to track global case density.
