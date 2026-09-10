import streamlit as st
from GYMviews import Dbconnect
from GYMviews import GymMemberManager


connection_instance = Dbconnect()
member_instance = GymMemberManager()
tab1 ,tab2 = st.tabs(["ADD","VIEWS"])

with tab1:
    st.title("ADD MEMBER")
    name = st.text_input("Enter Member name")
    place = st.text_input("Enter Member place")
    plan = st.text_input("Enter Member plan package")
    fee = st.text_input("Enter Member fee package")
    joined_date = st.text_input("Enter Member Joined date")
    if st.button("ADDED NEW MEMBER"):
        member_instance.post(name=name,place=place,plan=plan,fee=fee,joined_date=joined_date)
        st.success("NEW MEMBER ADDED SUCCESSFULLY")
with tab2:
    st.title("VIEW MEMBER")
