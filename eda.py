# eda.py

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import os

# Set up output directory
output_dir = 'analysis_outputs/plots'
os.makedirs(output_dir, exist_ok=True)

# Define columns of interest
columns_of_interest = [
    'date', 'location', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths',
    'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated', 'population'
]

# Load the dataset
data_path = 'data/owid-covid-data.csv'
covid_df = pd.read_csv(data_path)

# Filter the dataset
covid_df = covid_df[columns_of_interest]

# Convert 'date' column to datetime
covid_df['date'] = pd.to_datetime(covid_df['date'])

# Filter for specific countries
countries_of_interest = ['Kenya', 'United States', 'India']
covid_df = covid_df[covid_df['location'].isin(countries_of_interest)]

# Fill missing values for numeric columns
numeric_columns = ['total_cases', 'new_cases', 'total_deaths', 'new_deaths',
                   'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated']
covid_df[numeric_columns] = covid_df[numeric_columns].fillna(0)

# Forward fill cumulative columns
cumulative_columns = ['total_cases', 'total_deaths', 'total_vaccinations', 
                      'people_vaccinated', 'people_fully_vaccinated']
covid_df[cumulative_columns] = covid_df[cumulative_columns].ffill()

# Verify the cleaning process
print("Data Overview:\n", covid_df.head())
print("\nMissing Values:\n", covid_df.isnull().sum())

# Exploratory Data Analysis: Plot total cases and deaths over time for each country
for country in countries_of_interest:
    country_data = covid_df[covid_df['location'] == country]
    
    plt.figure(figsize=(12, 6))
    plt.plot(country_data['date'], country_data['total_cases'], label='Total Cases', color='blue')
    plt.plot(country_data['date'], country_data['total_deaths'], label='Total Deaths', color='red')
    plt.title(f'COVID-19 Cases and Deaths in {country}')
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.legend()
    plt.grid(alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot
    plot_path = os.path.join(output_dir, f'{country}_cases_deaths.png')
    plt.savefig(plot_path)
    print(f"Plot saved: {plot_path}")
    plt.close()

print("\nEDA complete. Plots are saved in the 'analysis_outputs/plots' folder.")
