import openai

openai.api_key = "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"

def basicgeneration(prompt) :
     completion = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages= [ {"role": "user", "content": prompt }])

     return completion.choices[0].message.content

prompt= "please provide the details about Kakinada Parliament Constituency"

print(basicgeneration(prompt))



    