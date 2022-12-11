import requests
from gtts import gTTS
import os

response = requests.get("http://api.sr.se/api/v2/traffic/messages?format=json")

x = response.json()
ttsText = ""

for i in range(len(x["messages"])):
    index = i-1
    print(f'{x["messages"][index]["title"]}: {x["messages"][index]["description"]}')
    ttsText += x["messages"][index]["title"] + ":" + " " + x["messages"][index]["description"]+". . . \n\n"

myobj = gTTS(text=ttsText, lang="sv", slow=False)


myobj.save("trafik.mp3") # File controll
os.system("trafik.mp3") # File controll