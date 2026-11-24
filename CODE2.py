# Step 1: Import Libraries
import pandas as pd
import numpy as np

# Step 2: Create Dataset
data = {
    'Name': ['Aditya', 'Rahul', 'Aman', 'Priya', 'Rahul'],
    'Age': [20, 21, np.nan, 22, 21],
    'Gender': ['Male', 'Male', 'Male', 'Female', 'Male'],
    'Salary': [25000, 30000, 28000, np.nan, 30000],
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Pune', 'Mumbai']
}

df = pd.DataFrame(data)

print("ORIGINAL DATASET")
print(df)


# Step 3: Inspect Dataset Structure
print("\nDATASET INFORMATION")
print(df.info())

print("\nFIRST FIVE RECORDS")
print(df.head())

print("\nDATASET SHAPE")
print(df.shape)

print("\nSTATISTICAL SUMMARY")
print(df.describe())


# Step 4: Identify Missing Values
print("\nMISSING VALUES")
print(df.isnull().sum())


# Step 5: Identify Duplicate Records
print("\nDUPLICATE RECORDS")
print(df.duplicated().sum())


# Step 6: Handle Missing Values
df['Age'] = df['Age'].fillna(df['Age'].mean())

df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

print("\nAFTER HANDLING MISSING VALUES")
print(df)


# Step 7: Remove Duplicate Records
df = df.drop_duplicates()

print("\nAFTER REMOVING DUPLICATES")
print(df)


# Step 8: Correct Data Types
df['Age'] = df['Age'].astype(int)

df['Salary'] = df['Salary'].astype(int)

print("\nCORRECTED DATA TYPES")
print(df.dtypes)


# Step 9: Correct Inconsistent Data Entries
df['Name'] = df['Name'].str.strip().str.title()

df['Gender'] = df['Gender'].str.strip().str.title()

df['City'] = df['City'].str.strip().str.title()

print("\nAFTER CORRECTING INCONSISTENT DATA")
print(df)


# Step 10: Final Dataset Verification
print("\nFINAL CLEANED DATASET")
print(df)

print("\nMISSING VALUES AFTER CLEANING")
print(df.isnull().sum())

print("\nDUPLICATES AFTER CLEANING")
print(df.duplicated().sum())


# Step 11: Save Cleaned Dataset
df.to_csv('cleaned_dataset.csv', index=False)

print("\nCleaned dataset saved successfully as cleaned_dataset.csv")


# Step 12: Read Saved CSV File
cleaned_data = pd.read_csv('cleaned_dataset.csv')

print("\nSAVED CLEANED CSV DATASET")
print(cleaned_data)
