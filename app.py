import pandas as pd
import streamlit as st
import pickle
import numpy as np
import pandas as pd

st.title('🐱‍🚀 Agriculture Yield Predictor')

st.info("This is a Machine Learning App.")

df = pickle.load(open('df.pkl','rb'))
model = pickle.load(open('LR.pkl','rb'))


st.markdown("Select Below Parameters 😄")

Region = st.selectbox('Region', df['Region'].unique())
Soil_Type = st.selectbox('Soil_Type', df['Soil_Type'].unique())
Crop = st.selectbox('Crop', df['Crop'].unique())
Rainfall_mm = st.number_input("Rainfall_mm")
Temperature_Celsius = st.number_input("Temperature_Celsius")
Fertilizer_Used = st.selectbox('Fertilizer_Used', df['Fertilizer_Used'].unique())
Irrigation_Used = st.selectbox('Irrigation_Used',df['Irrigation_Used'].unique())
Weather_Condition = st.selectbox('Weather_Condition',df['Weather_Condition'].unique())
Days_to_Harvest = st.number_input('Days_to_Harvest')


if st.button('Predict Yield'):

    if Region == "West":
        Region = 3
    elif Region == "South":
        Region = 2
    elif Region == "North":
        Region = 1
    else:
        Region = 0

    if Soil_Type == "Clay":
        Soil_Type = 1
    elif Soil_Type == "Chalky":
        Soil_Type = 0
    elif Soil_Type == "Loan":
        Soil_Type = 2
    elif Soil_Type == "Peaty":
        Soil_Type = 3
    elif Soil_Type == "Sandy":
        Soil_Type = 4
    else:
        Soil_Type = 5

    if Crop == "Barley":
        Crop = 0
    elif Crop == "Cotton":
        Crop = 1
    elif Crop == "Maize":
        Crop = 2
    elif Crop == "Rice":
        Crop = 3
    elif Crop == "Soybean":
        Crop = 4
    else:
        Crop = 5

    if Fertilizer_Used == "True":
        Fertilizer_Used = 1
    else:
        Fertilizer_Used = 0
   
    if Irrigation_Used == "True":
        Irrigation_Used = 1
    else:
        Irrigation_Used = 0

    if Weather_Condition == "Cloudy":
        Weather_Condition = 0
    elif Weather_Condition == "Rainy":
        Weather_Condition = 1
    else:
        Weather_Condition = 2
    
    query = np.array([Region,Soil_Type,Crop,Rainfall_mm,Temperature_Celsius,Fertilizer_Used,Irrigation_Used,Weather_Condition,Days_to_Harvest])
    query = query.reshape(1,9)

    
    st.title("The predicted yield for the selected parameters is "+str(np.round(float(model.predict(query)),3)) +" Tons")

st.write('Made with ❤️ by [Anurag Vishwakarma](https://www.linkedin.com/in/anurag2407/)')

