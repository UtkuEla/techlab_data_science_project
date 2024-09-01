import pandas as pd

# Load the dataset
file_path = 'gym_membership_prediction_with_professional_status.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the dataset to understand its structure
print("First 5 rows of the dataset:\n", df.head())

# Display basic information about the dataset, including data types and missing values
print("\nBasic information about the dataset:\n", df.info())

# Display summary statistics to understand the distribution of numerical features
print("\nSummary statistics:\n", df.describe())

# Check for missing values across the dataset
missing_values = df.isnull().sum()
print("\nMissing values in each column:\n", missing_values)

# Data Wrangling

# 1. Handling Missing Values
# Since there are no missing values in the dataset, we can skip this step.
# If there were missing values, we could drop columns/rows or fill them using various strategies.

# 2. Removing Duplicate Rows
# Checking if there are any duplicate rows in the dataset
duplicates = df.duplicated().sum()
print("\nNumber of duplicate rows in the dataset:", duplicates)

# Removing duplicate rows if any exist
if duplicates > 0:
    df = df.drop_duplicates()
    print("Duplicate rows removed.")

# 3. Converting Columns to Appropriate Data Types
# Converting 'Preferred Time' and 'Membership Prediction' to categorical types
df['Preferred Time'] = df['Preferred Time'].astype('category')
df['Membership Prediction'] = df['Membership Prediction'].astype('category')

# 4. Renaming Columns
# Renaming columns for consistency and ease of use
df.rename(columns=lambda x: x.strip().lower().replace(' ', '_'), inplace=True)
print("\nColumns after renaming:\n", df.columns)

# 5. Feature Engineering
# Creating new features if necessary; for now, we retain the existing features.

# 6. Analyzing Categorical Variables
# Displaying unique values in categorical columns to understand the categories better
categorical_columns = df.select_dtypes(include=['object', 'category']).columns
for col in categorical_columns:
    print(f"\nUnique values in '{col}':\n", df[col].unique())

# 7. Analyzing the Distribution of Numerical Variables
# Displaying the distribution of numerical variables using summary statistics
numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
for col in numerical_columns:
    print(f"\nDistribution of '{col}':\n", df[col].describe())
