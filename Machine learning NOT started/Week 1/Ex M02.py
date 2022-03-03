import pandas as pd

adult_census = pd.read_csv("../datasets/adult-census-numeric.csv")
target_name = "class"
target = adult_census[target_name]
data = adult_census.drop(columns=[target_name, ])

# to display nice model diagram
from sklearn import set_config
set_config(display='diagram')
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier()
model.fit(data, target)

target_predicted = model.predict(data)

adult_census_test = pd.read_csv('../datasets/adult-census-numeric-test.csv')
target_test = adult_census_test[target_name]
data_test = adult_census_test.drop(columns=[target_name, ])
accuracy = model.score(data_test, target_test)
model_name = model.__class__.__name__
