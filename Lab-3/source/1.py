import csv
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

def get_data(filename):
    with open(filename,'r') as csvdocument:
        csvFileContent = csv.reader(csvdocument)
        next(csvFileContent)  # skipping column names
        for row in csvFileContent:
            x.append(int(row[0]))
            y.append(int(row[1]))
    return

get_data('datasets/pizzafranchise.csv')

model = linear_model.LinearRegression()
x = np.reshape(x,(len(x),1))
y = np.reshape(y,(len(y),1))
model.fit(x, y)

#predictions
predicted_cost = model.predict(900)
coeff = model.coef_[0][0]
const = model.intercept_[0]

#plotting
plt.scatter(x,y,color="yellow",label="Data Points")
plt.plot(x,model.predict(x),color="blue",label="Regression Line")
plt.scatter(900,model.predict(900),color="red",marker = "x",s=150,label="Predicted Value")
plt.xlabel('annual franchise fee ($1000)')
plt.ylabel('start up cost ($1000)')
plt.legend()
plt.show()

print("The start up cost with franchise fee 900 is: $", str(predicted_cost[0][0]))
print("The regression coefficient is ", str(coeff), ", and the constant is ", str(const))
print("the relationship equation between Franchise_Fee and Startup_Cost is: Startup_Cost = ", str(coeff), "* Franchise_Fee + ", str(const))