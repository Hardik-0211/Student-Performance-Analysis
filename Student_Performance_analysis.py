import pandas as pd
import numpy as np

df = pd.read_csv("data/student_grades.csv")

print("--- Dataset Overview ---")
print(df.head())
print("\nSummary Statistics:\n",df.describe())

# Calculating Average
df['Average'] = df[['Math','Science','English']].mean(axis=1).round(2)

#Top 20% 
top_percentile = df['Average'].quantile(0.80)
top20 = df[df['Average'] >= top_percentile]
print("\n--- Top Performance ---")
print(top20[['Student_ID', 'Average']])
 
#Co-relation 
cor = df['Study_Hours'].corr(df['Average'])
print(f"\nCorrelation betn Study Hours & Average Score : {cor:.2f}")

def rankk(a):
    if a >= 80:
        return 'A'
    elif a >= 60:
        return 'B'
    elif a >= 50:
        return 'C'
    elif a >= 35:
        return 'D'
    else:
        return 'F'   

df['Grade'] = df['Average'].apply(rankk)

df.to_csv("data/student_performance_result.csv",index=False)
print("\nResult saved to 'student_performance_result.csv'.")