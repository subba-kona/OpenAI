import requests

url = "<replace with your openAI secret>"

querystring = {"from":"USD","to":"INR","q":"15.0"}

headers = {
	"X-RapidAPI-Key": "48f6df45cemshcdaa8c0d3584c98p108ba6jsn4f7d253e5b24",
	"X-RapidAPI-Host": "currency-exchange.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print("The Doller (USD) currently trading at", response.json(), "with Indian Rupee (INR)")