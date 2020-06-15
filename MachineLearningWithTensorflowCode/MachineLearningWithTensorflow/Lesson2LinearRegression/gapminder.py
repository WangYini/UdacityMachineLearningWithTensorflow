# TODO: Add import statements
import pandas as pd
from sklearn.linear_model import LinearRegression
import os
import numpy as np

def run():
    # Assign the dataframe to this variable.
    # TODO: Load the data
    current_path = os.path.dirname(os.path.realpath(__file__))
    bmi_life_data = pd.read_csv(current_path + "//bmi_and_life_expectancy.csv")

    # Make and fit the linear regression model
    #TODO: Fit the model and Assign it to bmi_life_model
    bmi_life_model = LinearRegression()
    #my solution
    #x_values = np.reshape(np.array(bmi_life_data["BMI"]), [-1, 1])
    #y_values = np.array(bmi_life_data["Life expectancy"])
    #bmi_life_model.fit(x_values, y_values)
    #standard solution
    bmi_life_model.fit(bmi_life_data[['BMI']], bmi_life_data[["Life expectancy"]])

    # Make a prediction using the model
    # TODO: Predict life expectancy for a BMI value of 21.07931
    laos_life_exp = bmi_life_model.predict([[21.07931]])
    print(laos_life_exp)