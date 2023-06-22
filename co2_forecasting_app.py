
# importing necessary libraries
import pickle
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import warnings
warnings.filterwarnings("ignore")



#load the model
model = pickle.load(open('/Users/geet/Documents/Projects_Git/EcoTrendPredictor/CO2_forecast_Model.pkl','rb'))

#load dataset to plot alongside predictions
df = pd.read_csv("/Users/geet/Documents/Projects_Git/EcoTrendPredictor/Data/CO2.csv")
df['Year'] = pd.to_datetime(df['Year'], format='%Y')
df.set_index(['Year'], inplace=True)


#page configuration
st.set_page_config(layout='centered') #configures the page layout to be centered
image = Image.open('/Users/geet/Downloads/co2.jpg')
st.image(image) # displays the image on the Streamlit application

year = st.slider("Select number of Years",1,30,step = 1) #creates a slider widget where the user can select a 
                                                        #number of years between 1 and 30.
    
    
pred = model.forecast(year) #predict future values based on the selected number of years.
pred = pd.DataFrame(pred, columns=['CO2'])  # predicted values are stored in pred.
   
if st.button("Predict"):

        col1, col2 = st.columns([2,3])
        with col1:
             st.dataframe(pred)
        with col2:
            fig, ax = plt.subplots(figsize=(10, 12))
            df['CO2'].plot(style='--', color='gray', legend=True, label='known')
            pred['CO2'].plot(color='b', legend=True, label='prediction')
            
            # Increase font size
            plt.xlabel('X-axis label', fontsize=12)
            plt.ylabel('Y-axis label', fontsize=12)
            plt.xticks(fontsize=12)
            plt.yticks(fontsize=12)
            plt.legend(fontsize=12)
            st.pyplot(fig)
