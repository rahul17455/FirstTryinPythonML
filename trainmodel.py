#import pandas
#from sklearn import model_selection
#from sklearn.linear_model import LogisticRegression
#import pickle
#
#
#from pandas import read_excel
#df=read_excel('obs_data_w.xlsx',sheet_name='Sheet1')
#
#
#Y=df.iloc[:,0].values
#
#X=df.iloc[:,[1,3]].values


#url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
#names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
#dataframe = pandas.read_csv(url, names=names)
#array = dataframe.values
#X = array[:,0:8]
#Y = array[:,8]

#test_size = 0.33
#seed = 7
#X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)
#
#
#model = LogisticRegression()
#model.fit(X_train, Y_train)

#save the model to disk
#filename = 'finalized_model.sav'
#pickle.dump(model, open(filename, 'wb'))



from sklearn import linear_model
from sklearn import svm
from sklearn import model_selection

classifiers = [
    svm.SVR(),
    linear_model.SGDRegressor(),
    linear_model.BayesianRidge(),
    linear_model.LassoLars(),
    linear_model.ARDRegression(),
    linear_model.PassiveAggressiveRegressor(),
    linear_model.TheilSenRegressor(),
    linear_model.LinearRegression()]

from pandas import read_excel
df=read_excel('obs_data_w.xlsx',sheet_name='Sheet1')

Y=df.iloc[:,0].values

X=df.iloc[:,[1,3]].values

test_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)

trainingData    = X_train
trainingScores  = Y_train
predictionData  = X_test

#trainingData    = np.array([ [2.3, 4.3, 2.5],  [1.3, 5.2, 5.2],  [3.3, 2.9, 0.8],  [3.1, 4.3, 4.0]  ])
#trainingScores  = np.array( [3.4, 7.5, 4.5, 1.6] )
#predictionData  = np.array([ [2.5, 2.4, 2.7],  [2.7, 3.2, 1.2] ])

for item in classifiers:
    print(item)
    clf = item
    clf.fit(trainingData, trainingScores)
    print(clf.predict(predictionData),'\n')