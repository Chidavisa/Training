import streamlit as st
from PIL import Image

with st.form(key='my_form'):
    username = st.text_input('Username')
    password = st.text_input('Password')
    st.form_submit_button('Login')
    
img = Image.open('pix.jpeg')
st.image(img.resize((400,400)))

st.checkbox('agree')

st.title('my first webapp')
st.subheader('Train with us')


st.selectbox('Gender',['Male','Female','other'])

w = st.sidebar.number_input('how much do you weigh')
h = st.sidebar.number_input('how tall are you')

def bmi_calc(w,h):
    bmi = round(w/(h**2),1)
    return bmi

a1,a2 = st.columns(2)
with a1:
    st.checkbox('Accept')
    st.number_input('how old are you?', step=1)
    st.text_input('what is your name')
with a2:
    st.checkbox('reject')
    st.text_area('address')
    st.date_input('date of last visit')

if st.button('calculate'):
    st.balloons()
    st.write(bmi_calc(w,h))