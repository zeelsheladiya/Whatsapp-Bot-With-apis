from keep_alive import keep_alive
from flask import Flask, request
from threading import Thread
from twilio.twiml.messaging_response import MessagingResponse
from covid_api import covid_inf
from google_news_api import GNews
from bbc_news_api import NewsFromBBC
from advice_slip_api import advice_slip
from quote_api import get_quote

app = Flask('')

#=========  messageRecieveServer flask app

@app.route('/')
def home():
    return "Zeelubha's Whatsapp Bot"

def runRecieveServer():
  app.run(host='0.0.0.0',port=4)

@app.route("/sms",methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    message = request.form.get('Body')
    msg = str(message)

    print(msg)
    if msg == '$covid' :
      covid_info = covid_inf()
      resp = MessagingResponse()
      resp.message(covid_info)

    elif msg == '$gnews' :
      resp = MessagingResponse()
      gnews = GNews()
      resp.message(gnews)

    elif msg == '$bbcnews':
      resp = MessagingResponse()
      resp.message(NewsFromBBC())

    elif msg == '$advice':
      resp = MessagingResponse()
      resp.message(advice_slip())

    elif msg == '$quote':
      resp = MessagingResponse()
      resp.message(get_quote())

    elif msg == "who are you?":
      resp = MessagingResponse()
      resp.message("I am a whatsapp bot which created by zeel sheladiya")

    elif msg == "hii":
      resp = MessagingResponse()
      resp.message("Hello")

    elif msg == "who is your owner?":
      resp = MessagingResponse()
      resp.message("I am not person. i am a program! if you want to advancement in me go and check out my live server and make me advance!")

    elif msg == "What is your purpose?":
      resp = MessagingResponse()
      resp.message("My purpose is to make whatsapp programmable! that's why zeel created me!")

    elif msg == "thank you":
      resp = MessagingResponse()
      resp.message("arigato gozimasu!")

    else:
      # Create reply
      resp = MessagingResponse()
      resp.message("You said: {}".format(message))

    return str(resp)

def runResponceFromServer():
    t = Thread(target=runRecieveServer)
    t.start()



if __name__ == '__main__':

  # keep alive this script by revieving the responce from the server
  keep_alive()

  #main app running
  runResponceFromServer()
    

