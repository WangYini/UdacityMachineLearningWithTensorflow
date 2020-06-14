# TODO: Add import statements
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso
import os

def run():
    # Assign the data to predictor and outcome variables
    # TODO: Load the data
    current_path = os.path.dirname(os.path.realpath(__file__))
    train_data = np.genfromtxt(current_path + '//regularization.csv', delimiter=',')
    X = train_data[:, :-1]
    y = train_data[:, -1]

    # TODO: Create the standardization scaling object.
    scaler = StandardScaler()

    # TODO: Fit the standardization parameters and scale the data.
    X_scaled = scaler.fit_transform(X)

    # TODO: Create the linear regression model with lasso regularization.
    lasso_reg = Lasso()

    # TODO: Fit the model.
    lasso_reg.fit(X_scaled, y)

    # TODO: Retrieve and print out the coefficients from the regression model.
    reg_coef = lasso_reg.coef_
    print(reg_coef)