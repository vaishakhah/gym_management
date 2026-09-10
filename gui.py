import streamlit as st
from GYMviews import Dbconnect
from GYMviews import GymMemberManager


connection_instance = Dbconnect()
member_instance = GymMemberManager()
tab1 ,tab2 = st.tabs(["ADD","VIEWS"])

with tab1:
    st.title("ADD GYM MEMBER")
    name = st.text_input("Enter Member name")
    place = st.text_input("Enter Member place")
    mobile = st.text_input("Enter Member Mobile ")
    plan = st.selectbox("Please Select your Plan",["1 month","2 month","3 month"])
    fee = st.text_input("Enter Member fee package")
    joined_date = st.date_input("Enter Joined date")
    if st.button("ADDED NEW MEMBER"):
        member_instance.post(name=name,place=place,mobile =mobile,plan=plan,fee=fee,joined_date=joined_date)
        st.success("NEW MEMBER ADDED SUCCESSFULLY")
with tab2:
    st.title("VIEW GYM MEMBER DETAILS")
    records = member_instance.get()
    if records:
        st.table(records)
    else:
        st.warning("RECORD NOT FOUND")
