import streamlit as st

st.title('Semantic Similarity')
sentences1 = st.text_input('Insert sentences1:')
sentences2 = st.text_input('Insert sentences2:')

if st.button('Submit'):
    st.write('Sentences1 is:', sentences1)
    st.write('Sentences2 is:', sentences2)

    


# Installing & Importing Data
#u stands for upgrade #q stands for quiet/not so much output 
!pip install xgboost -U -q 
!pip install sklearn -U -q
!pip install shap -U -q
#importing libraries
import pandas as pd
import numpy as np
import altair as alt
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
import itertools
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import shap
import pickle

