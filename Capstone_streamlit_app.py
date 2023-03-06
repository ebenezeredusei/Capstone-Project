# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 00:23:54 2023

@author: Ebenezer Edusei
"""


import numpy as np
import pickle
import streamlit as st

# load the saved model
loaded_model = pickle.load(open("C:/Users/Ebenezer Edusei/anaconda3/envs/PythonEnv/Edusei_Demo/Capstone Project/trained_model.sav", 'rb'))


#Creating a function for prediction
def churn_prediction(input_data):
     
     
    #change the input data into a numpy array
    input_data_nparray = np.asarray(input_data)

    #reshape the array given we are predicting for one instance
    input_data_reshape = input_data_nparray.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshape)
    print(prediction)

    if (prediction[0]==0):
        return('customer will not churn')
    else:
        return('customer will churn')
    
    
    
    
def main():
    
    #Titling our web app
    st.title("Customer Churn Web App")
    
    
    #Getting user input data
    montant = st.slider("select customer top-up amount", min_value=0, max_value=5000, value=0, step=1)
    freq_Rech = st.slider("select frequency of recharge", min_value=0, max_value=1000, value=0, step=1)
    on_net = st.number_input("enter the number of times customer places on_net calls", min_value=0, max_value=1000, value=0, step=1)
    orange = st.number_input("select the number of times customer placed calls on orange amount", min_value=0, max_value=1000, value=0, step=1)
    Regularity = st.number_input("how many times has the customer been active", min_value=0, max_value=1000, value=0, step=1)
    freq_top_pack   = st.number_input("indicate the number of times the customer has activated  top package", min_value=0, max_value=1000, value=0, step=1)
    region_Dakar  = st.selectbox("Indicate if customer is from dakar (Yes=1,No=0)", [1,0])
    duration_longterm  = st.selectbox("Indicate if customer prefers a long-term(minimum 21 months) subscriotion (Yes=1,No=0)", [1,0])
    duration_shortterm  = st.selectbox("Indicate if customer prefers a short-term(maximum 1 year) subscription (Yes=1,No=0)", [1,0])
    package_data  = st.selectbox("Indicate if customer prefers the data package or not(Yes=1,No=0)", [1,0])
    
    
    #Montant, Orange, Regularity, Region_Dakar, Region_Kaffrine, Region_Kedougou,Region_Kolda, Region_saint, Region_Sedhtiou, Tenure_D, Tenure_G, Tenure_H, Tenure_I, Tenure_J, Tenure_K, MRG
    #montant, freq_Rech, on_net, orange, Regularity, freq_top_pack, region_Dakar, duration_longterm, duration_shortterm, package_data    
    
    # code for prediction
    customer_churn = " "
    
    #Creating a button for predition
    
    if st.button("Predict"):
        customer_churn = churn_prediction([[montant, freq_Rech, on_net, orange, Regularity, freq_top_pack, region_Dakar, duration_longterm, duration_shortterm, package_data]])
    
        st.success(customer_churn)
    
    
    
    
if __name__=='__main__':
    main()
    
    
    
    
