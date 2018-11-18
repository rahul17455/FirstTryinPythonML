import numpy as np
import pandas as pd

from pandas import read_excel
df=read_excel('obs_data_w.xlsx',sheet_name='Sheet1')


y=df.iloc[:,0].values

X=df.iloc[:,[1,3]].values

from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(X_train,y_train)

y_pred = regressor.predict(X_test)
from sklearn.metrics import r2_score
r2_error_lin_model = r2_score(y_test, y_pred) 
print(r2_error_lin_model)