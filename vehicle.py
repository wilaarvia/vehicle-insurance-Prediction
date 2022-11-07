# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 13:58:59 2022

@author: rifqi arman
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu




# loading the saved model
insurance_model = pickle.load(open('insurance_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('vehicle insurance Prediction System',
                          
                          ['vehicle insurance Prediction',
                           'About the project',
                           'About the author'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'vehicle insurance Prediction'):
    
    # page title
    st.title('vehicle insurance Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        Gender = st.text_input('gender of the customer ')
        
    with col2:
        Age = st.text_input('age of the customer')
    
    with col3:
        Driving_License = st.text_input('do the customer have Driving License?')
    
    with col4:
        Region_Code = st.text_input('region code of the customer')
    
    with col1:
        Previously_Insured = st.text_input('do the customer have vehicle insurance yet?')
    
    with col2:
        Vehicle_Age = st.text_input('vehicle age of the customer')
    
    with col3:
        Vehicle_Damage = st.text_input('Has the customer ever been in a vehicle accident?')
    
    with col4:
        Annual_Premium = st.text_input('how much the annual premium in a year')
        
    with col1:
        Policy_Sales_Channel = st.text_input('policy sales channel of the customer')
    
    with col2:
        Vintage	 = st.text_input('number of day the customer has been in the company')
        
    
    # code for Prediction
    prediction = ''
    
    # creating a button for Prediction
    
    if st.button('vehicle insurance Test Result'):
        insurance_prediction = insurance_model.predict([[Gender, Age, Driving_License, Region_Code, Previously_Insured, Vehicle_Age, Vehicle_Damage, Annual_Premium, Policy_Sales_Channel, Vintage]])
        
        if (insurance_prediction[0] == 0):
          prediction = 'The coustumer is not interested'
        else:
          prediction = 'The coustumer is interested'
        
    st.success(prediction)
    
# Heart Disease Prediction Page
if (selected == 'About the project'):
    
    # page title
    st.title('vehicle insurance Prediction using ML')
    
    
    
# Heart Disease Prediction Page
if (selected == 'About the author'):
    
    # page title
    st.title('about the author')
    st.text('hi, my name is wila. nice to meet you')
        
        
