import openai

openai.api_key = "<replace with your openAI secret>"

def basicgeneration(prompt) :
     completion = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages= [ {"role": "user", "content": prompt }])

     return completion.choices[0].message.content

prompt= "please provide the details about Kakinada Anchorage Port"

print(basicgeneration(prompt))



    