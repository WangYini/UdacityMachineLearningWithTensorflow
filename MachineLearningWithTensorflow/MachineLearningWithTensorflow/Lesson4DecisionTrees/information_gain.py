import math
import pandas as pd
import os

def calculate_entropy(m, n):
    tol = m + n
    a = m/tol
    b = n/tol
    entropy = -a * math.log(a, 2) - b * math.log(b, 2)
    return entropy

def run():
    current_path = os.path.dirname(os.path.realpath(__file__))
    data = pd.read_csv(current_path + "//ml-bugs.csv")

    #parent entropy
    mobug_condition = data["Species"] == "Mobug"
    lobug_condition = data["Species"] == "Lobug"
    parent_mobugs = data[mobug_condition]
    parent_lobugs = data[lobug_condition]
    mobug_num = len(parent_mobugs)
    lobug_num = len(parent_lobugs)

    entropy_parent = calculate_entropy(mobug_num, lobug_num)

    print("when color is brown")
    condi_gain(data["Color"] =="Brown", data, mobug_condition, lobug_condition, entropy_parent)
    print("when color is green")
    condi_gain(data["Color"] =="Green", data, mobug_condition, lobug_condition, entropy_parent)
    print("when color is blue")
    condi_gain(data["Color"] =="Blue", data, mobug_condition, lobug_condition, entropy_parent)
    print("when length less than 17mm")
    condi_gain(data["Length"] < 17.00, data, mobug_condition, lobug_condition, entropy_parent)
    print("when length less than 20mm")
    condi_gain(data["Length"] < 20.00, data, mobug_condition, lobug_condition, entropy_parent)


def condi_gain(condition, data, mobug_condition, lobug_condition, entropy_parent):
    one_bucket = data[condition]
    other_bucket = data[~condition]
    entropy_one_bucket = calculate_entropy(len(one_bucket[mobug_condition]),
                                             len(one_bucket[lobug_condition]))
    tol_one_bucket = len(one_bucket)
    tol_other_bucket = len(other_bucket)
    tol = tol_one_bucket + tol_other_bucket
    entropy_other_bucket = calculate_entropy(len(other_bucket[mobug_condition]),
                                             len(other_bucket[lobug_condition]))

    information_gain = entropy_parent -  (tol_one_bucket/tol)* entropy_one_bucket - (tol_other_bucket/tol) * entropy_other_bucket
    print(information_gain)


