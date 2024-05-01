import openai
import requests
import json

openai.api_key = "<replace with your openAI secret>"

def basicgeneration(prompt) :
     completion = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages= [ {"role": "user", "content": prompt }])

     return completion.choices[0].message.content


def RapidAPIExchange() :
     
    url = "https://currency-exchange.p.rapidapi.com/exchange"

    querystring = {"from":"USD","to":"INR","q":"15.0"}

    headers = {
	    "X-RapidAPI-Key": "48f6df45cemshcdaa8c0d3584c98p108ba6jsn4f7d253e5b24",
	    "X-RapidAPI-Host": "currency-exchange.p.rapidapi.com"
    }

    return requests.get(url, headers=headers, params=querystring)
    
response=RapidAPIExchange()    
Exchange =  response.json()


prompt = f"""You are a an expert in international currently exchange trade with more than 10 years of experiance.
            I will provide you with the US dollar to Indian Rupee exchange rate as of today.
            Please provide with the technical analysis of Dollar to INR exchange rates trending.
            here is what I want : 
            Exhange overview,
            Hightest exchange rate in last 6 months with the date,
            Lowest exchange rate in last 6 months with the date,
            average exchage rate in last 6 months,  
            Shall I buy or Sell the USD? 
            here is the today's exchange rate {Exchange}"""

            
print(prompt)            
print(basicgeneration(prompt))

