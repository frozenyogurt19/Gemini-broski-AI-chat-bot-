# flask == web server , (in htttp web server you made server from kinda scratch, handlers port ip etc, here flask is all that)
from flask import Flask, request, jsonify , render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from chatBotV1 import geminiii

# code below replaces LiveServer with flask server, so flask sever is used to connect (1) html and gemini and now also (2) open webpage
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/history')
def history():
    return render_template('history.html')




# decorator, always needed, connects flask with the link 
@app.route("/messages", methods=["POST"])
def flaskServerFunc():
    #(1) getting POST request from link ( i send "hi" in the chat)
    my_message = request.json["messages"] # "hi" exists  in json.  in request  obj provided by flask server(cuz server have httprequesthandler )
    #(2) sending this to gemini aip ( code made in chatBoyv1.py)
    # + (3) return  the gemini api's reply
    gemini_reply = geminiii(my_message)
    
    # NOTE: the chat bubbles are updated by javascript code inside html


    return jsonify({"reply": gemini_reply})



app.run(host='0.0.0.0') # running the server 


# pc link :  http://127.0.0.1:5000

#phone link :  http://192.168.1.43:5000


# to test if flash and gemini are connected, run in terminal :  Invoke-WebRequest -Uri http://127.0.0.1:5000/messages -Method POST -ContentType "application/json" -Body '{"messages": "hi"}'
# (it sends a quick POST request like "hi" to flask )