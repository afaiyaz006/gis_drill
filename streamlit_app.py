import streamlit as st
import gis_process
st.title("GIS TESTING APP")

with st.form(key="amar_form"):
    text_input=st.text_input(label='Enter Coordinates')
    submit_button=st.form_submit_button(label='Submit')

if submit_button:
    lat,longi=text_input.split(',')
    st.write(f"Submitted this: {text_input}")
    st.write(f"longitude is {float(longi)}")
    st.write(f"lattitude is {float(lat)}")
    output=gis_process.process(float(lat),float(longi))
    st.write(output)
    