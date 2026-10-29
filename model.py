import pandas as pd
import sys , os , json
import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.ticker import parcentFormatter 


# from sklearn.model_selection import train_test_split, StratifiedGroupKFold,cross_val_predict
# from sklearn.compose import ColumnTransformer
# from sklearn.linear_model import LogisticRegression
# from sklearn.preprocessing import OneHotEncoder,StandardScaler


SRC = sys.argv[1]
OUT = "out"
os.makedirs(OUT,exist_ok=True)

SEED = 42
df = pd.read_csv(SRC,dtype=str)



