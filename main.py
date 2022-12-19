import streamlit as st
import requests, json

##### SIDEBAR #####
myList = ['Assets', 'Events', 'Rarity']

with st.sidebar:
    st.success("Select an Option.")

endpoint = st.sidebar.selectbox("Endpoints",myList)

with st.sidebar:
    if endpoint != myList[0]:
        st.success(f"You selected {endpoint}!")

st.sidebar.subheader("Filters")  
collection = st.sidebar.text_input("Collection")
owner = st.sidebar.text_input("Owner Adress")

##### MAINPAGE #####
st.header(f"Opensea Listing API Explore - {endpoint}")

st.write(myList[0])

if endpoint=='Assets':
    params = {}
    if collection:
        params['collection'] = collection
    if owner:
        params['owner'] = owner
        
    

    url = "https://testnets-api.opensea.io/api/v1/assets?order_direction=desc&offset=0&limit=20&include_orders=false"
    response = requests.get(url, params)
    st.write(response.json())

