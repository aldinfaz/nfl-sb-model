import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('nfl_2022_data.csv')
print(df.head)

def createPtsPlot():
    plt.figure(figsize=(10, 5))
    sns.histplot(df['PtsW'], color='blue', label='Winner Points', kde=True)
    sns.histplot(df['PtsL'], color='red', label='Loser Points', kde=True)
    plt.legend()
    plt.title('Distribution of Points: Winners vs Losers')
    plt.xlabel('Points')
    plt.ylabel('Frequency')
    plt.show()

def createYdsPlot():
    plt.figure(figsize=(10, 5))
    sns.histplot(df['YdsW'], color='blue', label='Winner Yards', kde=True)
    sns.histplot(df['YdsL'], color='red', label='Loser Yards', kde=True)
    plt.legend()
    plt.title('Distribution of Yards: Winners vs Losers')
    plt.xlabel('Yards')
    plt.ylabel('Frequency')
    plt.show()

df['Winner'] = (df['PtsW'] > df['PtsL']).astype(int)
features = ['YdsW', 'TOW', 'YdsL', 'TOL']

"""
#model selection and training
df['Winner'] = (df['PtsW'] > df['PtsL']).astype(int)
features = ['YdsW', 'TOW', 'YdsL', 'TOL']  # Add more features as needed
X = df[features]
y = df['Winner']

from sklearn.model_selection import train_test_split

# Split the data into training (80%) and test (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Initialize the model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
print('Confusion Matrix:')
print(confusion_matrix(y_test, y_pred))
print('Classification Report:')
print(classification_report(y_test, y_pred))
"""