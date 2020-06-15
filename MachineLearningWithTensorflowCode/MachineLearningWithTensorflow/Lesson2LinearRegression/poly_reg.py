# TODO: Add import statements
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import os
import numpy as np

def run():
    # Assign the data to predictor and outcome variables
    # TODO: Load the data
    current_path = os.path.dirname(os.path.realpath(__file__))
    train_data = pd.read_csv(current_path + "//data3.csv")

    #mysolution
    #X = np.array(train_data[["Var_X"]])
    #y = np.array(train_data[["Var_Y"]])

    #standardsolution
    X = train_data['Var_X'].values.reshape(-1, 1)
    y = train_data['Var_Y'].values

    # Create polynomial features
    # TODO: Create a PolynomialFeatures object, then fit and transform the
    # predictor feature
    poly_feat = PolynomialFeatures(degree = 4)

    X_poly = poly_feat.fit_transform(X)

    # Make and fit the polynomial regression model
    # TODO: Create a LinearRegression object and fit it to the polynomial predictor
    # features
    poly_model = LinearRegression()
    poly_model.fit(X_poly, y)

    # Once you've completed all of the steps, select Test Run to see your model
    # predictions against the data, or select Submit Answer to check if the degree
    # of the polynomial features is the same as ours!