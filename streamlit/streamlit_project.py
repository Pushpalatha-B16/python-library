import streamlit as st
import PyPDF2 as pdf
st.title("Course Registraction Form")
st.image("course.jpg")
st.text_input("Enter name")
st.text_input("Enter qualification")
st.text_input("Enter Email id")
st.date_input("choose date")
st.radio("Gender",("male","Female"))
st.subheader("Choose courses")
c1=st.checkbox("Python")
c2=st.checkbox("java")
c3=st.checkbox("Front End")
c4=st.checkbox("Backend")
st.write("Selected courses")

if c1:
    st.write("Python")
if c2:
    st.write("java")
if c3:
    st.write("Front End")
if c4:
    st.write("Backend")
f=st.file_uploader("your proof",type="pdf")
d=pdf.PdfReader(f)
st.button("submit")
