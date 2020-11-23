import streamlit as st
from modeler.modeler import Modeler


m = Modeler()

st.title('First streamlit app')

x = st.slider('Select input value')

st.write('Output', m.predict(x))