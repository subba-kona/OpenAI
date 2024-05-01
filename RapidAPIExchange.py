import requests
import streamlit as st

url = "https://currency-exchange.p.rapidapi.com/exchange"

querystring = {"from":"USD","to":"INR","q":"15.0"}

headers = {
	"X-RapidAPI-Key": "48f6df45cemshcdaa8c0d3584c98p108ba6jsn4f7d253e5b24",
	"X-RapidAPI-Host": "currency-exchange.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

string1=f'''The Doller (USD) currently trading at, {response.json()}, with Indian Rupee (INR)'''

st.title("Exchange Analysis")
st.subheader(string1)