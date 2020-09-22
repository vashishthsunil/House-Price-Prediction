# title = house price prediction ##

##import libraries
import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from datetime import datetime as dt



##load dataset from local machine
#set working directory
os.chdir("C:/Users/vashi/OneDrive/python programs")

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

##exploring test and train dataset
train.info()
train.describe()

## train dataset has total 1460 observations and 81 columns including target variable
## out of 81 variable 3 is floating, 35 is integer and 43 is object type.

#first of all drop 'id' column
train.drop(columns="Id",inplace=True)
test.drop(columns="Id",inplace=True)

##data cleaning and preprocessing

##missing value analysis in train dataset
missing_train= pd.DataFrame(train.isnull().sum()).reset_index()
missing_train = missing_train.rename(columns={"index":"variable_name",0:"missing_percentage"})
missing_train["missing_percentage"] = (missing_train["missing_percentage"]/len(train))*100

## we drop all columns that have missing percentage more than 70%
## drop columns PoolQC, MiscFeature, Alley, Fence
train.drop(columns={"PoolQC","MiscFeature","Alley","Fence"},inplace=True)

