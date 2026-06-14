with open("apikey.txt", "r") as f:
    my_api_key = f.read().strip()



from google import genai

client = genai.Client(api_key=my_api_key)

response = client.models.generate_content(
    model="gemini-3-flash-preview" ,
    contents="start the convo, like good morning or welcome"
)


chat_history = []
#first_chat = False

# gemini start convo with (response.text)
#print(response.text)

# adding to chat history ( google genai accepts "text" key inside "parts")
chat_history.append( {"role": "model", "parts": [{ "text": response.text}] })


def geminiii(my_reply): # also first_chat

    chat_history.append( {"role": "user", "parts": [{ "text": str(my_reply)}] })

   
    # gemini continues convo, now with a history 
    response = client.models.generate_content(
    model="gemini-3-flash-preview" ,
    contents= chat_history
    )
    # adding to chat history 
    chat_history.append( {"role": "model", "parts": [{ "text": response.text}] })

    #print("gemini: "+  response.text)

    
    return response.text
        






