import pandas as pd 
import numpy as np 
# Create Uncleaned Dummy Data 
data = { 
'Name': ['Atharva', 'Amit', 'Atharva', 'Sneha', np.nan], 
'Age': [20, 200, 20, 22, 21], # 200 is an outlier 
'City': ['Mumbai', 'Pune', 'Mumbai', None, 'Delhi'] 
} 
df = pd.DataFrame(data) 
# Simple Cleaning Techniques 
df = df.drop_duplicates()                       
df['City'] = df['City'].fillna('Unknown')       
# Remove duplicate rows 
# Fill missing strings 
df['Age'] = df['Age'].fillna(df['Age'].median()) # Fill missing numbers with median 
df = df[df['Age'] < 100]                        
# Remove outliers (Age > 100) 
print("Cleaned Data:") 
print(df) 