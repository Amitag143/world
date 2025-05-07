import streamlit as st  
import pandas as pd
# # import openpyxl 
# dataset = pd.read_excel("D:\BIMINING REPORTS\AMIT  BI-MINING REPORTS\life summary\MAJAOR BREAKDOWN\ACCIDENTIAL TRUCK RECORD @ BINA SITE.xlsx")
# st.dataframe(dataset)

# create a form
name = st.text_input("Enter your name")
email = st.text_input("Enter your email")
fname = st.text_input("Enter your father name")

# create a long paragrah then used st.text_input to get the input from user
adress = st.text_input("Enter your address : ")    

# CREATE A SELETBOX BY USING BELOW CODE
classdata = st.selectbox("enter your class : ", (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# create a bottom button to submit the form
button = st.button("Submit")
if button:
    st.markdown(f"""
                name : {name}
                email : {email}
                father name : {fname}
                address : {adress}  
                class : {classdata}
                """)
    


