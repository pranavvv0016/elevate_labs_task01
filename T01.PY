import pandas as pd

try:
    df = pd.read_csv('Mall_Customers.csv')
    print("✅ Dataset loaded successfully.")
    print("\n--- Original Data Head & Info ---")
    print(df.head())
    df.info()
except FileNotFoundError:
    print("❌ Error: 'Mall_Customers.csv' not found. Please download it and place it in the correct directory.")
    exit()

print("\n--- 2. Standardizing Column Headers ---")
new_columns = {
    'CustomerID': 'customer_id',
    'Gender': 'gender',
    'Age': 'age',
    'Annual Income (k$)': 'annual_income_k',
    'Spending Score (1-100)': 'spending_score'
}
df.rename(columns=new_columns, inplace=True)
print("Columns renamed.")
print(df.columns.tolist())

print("\n--- 3. Checking for Missing Values and Duplicates ---")
missing_values = df.isnull().sum().sum()
print(f"Total missing values found: {missing_values}")

duplicate_rows = df.duplicated().sum()
print(f"Total duplicate rows found: {duplicate_rows}")

if duplicate_rows > 0:
    df.drop_duplicates(inplace=True)
    print(f"Removed {duplicate_rows} duplicate rows.")

print("\n--- 4. Standardizing Categorical Data ---")
print(f"Unique values in 'gender' column: {df['gender'].unique()}")

print("\n--- 5. Verifying Final Data Types ---")
df.info()

print("\n--- 6. Saving Cleaned Data ---")
output_filename = 'cleaned_mall_customers.csv'
df.to_csv(output_filename, index=False)
print(f"✅ Successfully cleaned the data and saved it to '{output_filename}'")