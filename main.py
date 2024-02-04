import pandas as pd

# Load the raw flight data set dataset
data = pd.read_csv("raw-flight-data.csv")


#check shape of the data 

print(data.shape)


# #Getting a statistical decription of our data 
print(data.describe())
# # Check for missing values
# # 0 indicates no missing data
# # number indicates number of missing values
print(data.isnull().sum())


# Handle missing values (fill with mean for demonstration)
data['DepDelay'].fillna(data['DepDelay'].mean(), inplace=True)
data['ArrDelay'].fillna(data['ArrDelay'].mean(), inplace=True)

# Save the cleaned dataset to a new CSV file
data.to_csv("cleaned-data.csv", index=False)

# Display information about the cleaned dataset
print(data.info())
