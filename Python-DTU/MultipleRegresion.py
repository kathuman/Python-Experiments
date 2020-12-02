# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 09:41:15 2020

@author: Gokul
"""



# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset=pd.read_excel('Data_Gokul.xlsx', sheet_name='Data Sheet')

X=dataset.iloc[1:,1:4].values

y = dataset.iloc[1:,4 ].values
z = dataset.iloc[1:, 4].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)



#fitting_multiple Regression model 
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#predict_test set
y_pred=regressor.predict(X_test)

# Visualising the Multiple regression results

plt.plot(y_test, regressor.predict(X_test), color = 'blue')
plt.title('Actual v Prediction')
plt.xlabel('Actual')
plt.ylabel('Prediction')
plt.show()

# Visualising the SVR results (for higher resolution and smoother curve)
"""X_grid = np.arange(min(X), max(X), 0.01) # choice of 0.01 instead of 0.1 step because the data is feature scaled
X_grid = X_grid.reshape((len(X_grid), 1))"""
plt.scatter(y_test, regressor.predict(X_test), color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Actual v Prediction')
plt.xlabel('Actual')
plt.ylabel('Prediction')
plt.show()

#measure of accuracy and scatter plot
Reg_confidence = regressor.score(y_test,regressor.predict(X_test))
print('regression confidence :', Reg_confidence)
"""from sklearn.utils.validation import check_array
def mean_absolute_percentage_error(y_true, y_pred): 
    y_true, y_pred = check_array(y_true, y_pred)
    return """

    ## Note: does not handle mix 1d representation
    #if _is_1d(y_true): 
    #    y_true, y_pred = _check_1d_array(y_true, y_pred)


MAPE= np.mean(np.abs((y_test - y_pred) / y_test)) * 100
print("MAPE :",MAPE)