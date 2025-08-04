# elevate_labs_task01

Python Data Cleaning and Preprocessing Script
This repository contains a Python script for cleaning and preprocessing a raw dataset using the Pandas library. The script demonstrates a standard workflow for preparing data for analysis or machine learning tasks.

📝 Description
The primary goal of this project is to take a raw CSV file, perform essential cleaning operations, and save the processed data into a new, clean CSV file. The script is configured to work with the Mall Customer Segmentation Data from Kaggle but can be easily adapted for other datasets.

✨ Features
The script performs the following data cleaning tasks:

Standardize Column Headers: Renames columns to be lowercase and use underscores for better accessibility (e.g., Annual Income (k$) becomes annual_income_k).

Handle Missing Values: Checks the entire dataset for any null or missing values.

Remove Duplicates: Scans for and reports any duplicate rows in the dataset.

Verify Data Types: Ensures that each column has an appropriate data type (e.g., age as an integer).

Standardize Categorical Data: Checks for unique values in categorical columns to ensure consistency.

🔧 Requirements
To run this script, you will need:

Python 3.x

Pandas library

You can install the required library using pip:

pip install pandas

🚀 Usage
Clone the repository:

git clone https://github.com/pranavvv0016/elevate_labs_task01.git
cd elevate_labs_task01

Download the dataset:

Download the Mall_Customers.csv file from Kaggle.

Place the Mall_Customers.csv file in the root directory of the project.

Run the script:
Execute the Python script from your terminal.

python your_script_name.py
📊 Output
After running the script, the following will happen:

Console Output: The script will print a step-by-step log of its operations, including the initial data summary, the changes made, and final data verification.

Cleaned CSV File: A new file named cleaned_mall_customers.csv will be created in the project directory. This file contains the cleaned data, ready for further analysis.
