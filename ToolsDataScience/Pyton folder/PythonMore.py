# Python More 
# Achraf Cohen - acohen@uwf.edu
# *****************************************************
# use python3 -m pip install --user statsmodels

import statsmodels.api as stat # allow access easily to most of the functions
import statsmodels.formula.api as statf # allow to use formula style to fit the models
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = stat.datasets.get_rdataset("mtcars", "datasets").data # load data "mtcars" from the R package 'datasets'
print(df.info())

fit_olsregression = statf.ols("mpg ~ wt + cyl",data=df).fit()
print(fit_olsregression.summary())

pred_ols = fit_olsregression.get_prediction()
pred_ols.summary_frame().head()


df["cyl"] = df["cyl"].astype("category") # make cyl categorical variable
fit_olsregression = statf.ols("mpg ~ wt + cyl",data=df).fit() # refit with a categorical variable 
print(fit_olsregression.summary())




from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error

df = stat.datasets.get_rdataset("mtcars", "datasets").data # load data "mtcars" from the R package 'datasets'

# split data
training_data, testing_data = train_test_split(df, test_size=0.2, random_state=28)

# Create X and Y from training
Y = training_data["mpg"] # response variable / outcome
X = training_data.drop(columns=["mpg"]) #predictors / features
reg =  linear_model.LinearRegression().fit(X,Y)

# Create X and Y from testing
Y_test = testing_data["mpg"] # response variable / outcome
X_test = testing_data.drop(columns=["mpg"]) #predictors / features
mpg_y_pred = reg.predict(X_test) # predictions

print(reg.coef_)

mean_absolute_percentage_error(y_true=Y_test,y_pred=mpg_y_pred)


import matplotlib.pyplot as plt
import numpy as np
import matplotlib
#matplotlib.use('Agg') # To plot with Markdown

x = np.linspace(0, 10, 100)
plt.figure();
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.show()
plt.close()

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris 
import matplotlib
#matplotlib.use('Agg') # To plot with Markdown

iris = load_iris()
df_iris = pd.DataFrame(iris.data)
df_iris.columns = iris.feature_names

# Boxplot
plt.figure();
plt.boxplot(df_iris)
plt.xticks([1, 2, 3, 4], iris.feature_names)
plt.grid()
plt.show()
plt.close()

#  histogram
plt.figure();
plt.hist(df_iris.iloc[:,0])
plt.show()
plt.close()

