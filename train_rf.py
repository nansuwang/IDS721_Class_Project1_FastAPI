import pickle

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# load the data
df = pd.read_csv("IT Salary Survey EU 2018.csv")
print(df.head())

df.rename(
    columns={
        "Years of experience": "exp",
        "Salary one year ago": "Salary_one_year_ago",
        "Salary two years ago": "Salary_two_years_ago",
        "Current Salary": "Current_Salary",
    },
    inplace=True,
)

# extract the predictors and the response variable
data = df.iloc[:, [1, 5, 8, 9, 7]]
print(data.head())
print("The shape of data is: ", data.shape)

# drop NA
data = data.dropna()
print("The shape of data is: ", data.shape)


X = data.iloc[:, [0, 1, 2, 3]]
y = data.iloc[:, -1]

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

# build the model
rf = RandomForestRegressor(n_estimators=1000)
rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)

# mse = mean_squared_error(y_test, y_pred)
# print("mse: ", mse)

# test case
testcase = rf.predict([[35, 8, 50000, 55000]])
print(testcase)

# export the model as a pickle file
pickle_out = open("regression_model.pkl", "wb")
pickle.dump(rf, pickle_out)
pickle_out.close()
