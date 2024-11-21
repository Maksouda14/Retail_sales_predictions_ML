import streamlit as st
import pickle
import numpy as np

st.title("Sales Application")

x1=st.text_input("Sale1",value =0)
x2=st.text_input("Sale2",value =0)
x3=st.text_input("Sale3",value =0)


feature=[int(x2),int(x2),int(x3)]
feature=np.array(feature).reshape(1,-1)

model=pickle.load(open("SALES.pickle","rb"))
forecast=model.predict(feature)

if st.button("Forecast"):
    st.success(forecast)
    