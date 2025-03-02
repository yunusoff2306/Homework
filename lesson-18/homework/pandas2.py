import pandas as pd
import datetime as dt

# Load the data
df = pd.read_csv('task/stackoverflow_qa.csv')

# 1. Find all questions that were created before 2014
# First, convert creationdate to datetime
df['creationdate'] = pd.to_datetime(df['creationdate'])
before_2014 = df[df['creationdate'] < '2014-01-01']
print(f"Questions created before 2014: {len(before_2014)}")

# 2. Find all questions with a score more than 50
high_score = df[df['score'] > 50]
print(f"Questions with score > 50: {len(high_score)}")

# 3. Find all questions with a score between 50 and 100
mid_score = df[(df['score'] > 50) & (df['score'] <= 100)]
print(f"Questions with score between 50 and 100: {len(mid_score)}")

# 4. Find all questions answered by Scott Boston
scott_questions = df[df['ans_name'] == 'Scott Boston']
print(f"Questions answered by Scott Boston: {len(scott_questions)}")

# 5. Find all questions answered by the following 5 users
# Note: The prompt doesn't list the 5 users, so I'm assuming they'd be specified
# For example purposes, let's use some names from the sample data
selected_users = ['Mike Pennington', 'doug', 'Demitri', 'Scott Boston', 'Unutbu']
user_questions = df[df['ans_name'].isin(selected_users)]
print(f"Questions answered by selected users: {len(user_questions)}")

# 6. Find questions created between March 2014 and October 2014, answered by Unutbu with score < 5
specific_questions = df[(df['creationdate'] >= '2014-03-01') & 
                        (df['creationdate'] <= '2014-10-31') & 
                        (df['ans_name'] == 'Unutbu') & 
                        (df['score'] < 5)]
print(f"Questions matching complex criteria: {len(specific_questions)}")

# 7. Find questions with score between 5-10 or view count > 10,000
combined_criteria = df[((df['score'] >= 5) & (df['score'] <= 10)) | (df['viewcount'] > 10000)]
print(f"Questions with score 5-10 or views > 10000: {len(combined_criteria)}")

# 8. Find questions not answered by Scott Boston
# Filter out nulls first to avoid comparing NaN values
not_scott = df[(df['ans_name'].notna()) & (df['ans_name'] != 'Scott Boston')]
print(f"Questions not answered by Scott Boston: {len(not_scott)}")

#puzzle 2
import pandas as pd

# Load the data
titanic_df = pd.read_csv("task/titanic.csv")

# 1. Select Female Passengers in Class 1 with Ages between 20 and 30
q1 = titanic_df[(titanic_df['Sex'] == 'female') & 
                (titanic_df['Pclass'] == 1) & 
                (titanic_df['Age'] >= 20) & 
                (titanic_df['Age'] <= 30)]
print(f"1. Female passengers in Class 1 with ages 20-30: {len(q1)}")

# 2. Filter Passengers Who Paid More than $100
q2 = titanic_df[titanic_df['Fare'] > 100]
print(f"2. Passengers who paid more than $100: {len(q2)}")

# 3. Select Passengers Who Survived and Were Alone
q3 = titanic_df[(titanic_df['Survived'] == 1) & 
                (titanic_df['SibSp'] == 0) & 
                (titanic_df['Parch'] == 0)]
print(f"3. Passengers who survived and were alone: {len(q3)}")

# 4. Filter Passengers Embarked from 'C' and Paid More Than $50
q4 = titanic_df[(titanic_df['Embarked'] == 'C') & 
                (titanic_df['Fare'] > 50)]
print(f"4. Passengers embarked from 'C' who paid > $50: {len(q4)}")

# 5. Select Passengers with Siblings/Spouses and Parents/Children
q5 = titanic_df[(titanic_df['SibSp'] > 0) & 
                (titanic_df['Parch'] > 0)]
print(f"5. Passengers with SibSp > 0 and Parch > 0: {len(q5)}")

# 6. Filter Passengers Aged 15 or Younger Who Didn't Survive
q6 = titanic_df[(titanic_df['Age'] <= 15) & 
                (titanic_df['Survived'] == 0)]
print(f"6. Passengers aged ≤15 who didn't survive: {len(q6)}")

# 7. Select Passengers with Cabins and Fare Greater Than $200
q7 = titanic_df[(titanic_df['Cabin'].notna()) & 
                (titanic_df['Fare'] > 200)]
print(f"7. Passengers with cabins and fare > $200: {len(q7)}")

# 8. Filter Passengers with Odd-Numbered Passenger IDs
q8 = titanic_df[titanic_df['PassengerId'] % 2 == 1]
print(f"8. Passengers with odd-numbered IDs: {len(q8)}")

# 9. Select Passengers with Unique Ticket Numbers
# First count occurrences of each ticket number
ticket_counts = titanic_df['Ticket'].value_counts()
# Then filter for tickets that appear exactly once
unique_tickets = ticket_counts[ticket_counts == 1].index
q9 = titanic_df[titanic_df['Ticket'].isin(unique_tickets)]
print(f"9. Passengers with unique ticket numbers: {len(q9)}")

# 10. Filter Passengers with 'Miss' in Their Name and Were in Class 1
q10 = titanic_df[(titanic_df['Name'].str.contains('Miss')) & 
                 (titanic_df['Pclass'] == 1)]
print(f"10. Passengers with 'Miss' in name and in Class 1: {len(q10)}")
