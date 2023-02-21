import streamlit as st
st.title('Campusx')

col1,col2=st.columns(2)

with col1:
    st.image('sdn.jpg')
with col2:
    st.write("""
    this is website created for the youngesters of india to build a carrrer in the field of data science.
    Hi, my name is Nitish. I am an educational content creator on YouTube with 50K+ Subscribers in the domain of Data Science. I have been in the tech industry for the past 10 years and taught more than 50,000 students offline. I am passionate about data and take pride in creating content that simplifies complex topics.
    """)
st.header("course offered")
st.subheader('data science and machine learning')
st.subheader('data engineer')
st.subheader('deep learning')
st.subheader('sql')
st.subheader('python')

st.sidebar.title('welocome to ml model')
st.sidebar.markdown("""
- home
- office
- school
""")


