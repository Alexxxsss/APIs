# importing the required module
import matplotlib.pyplot as plt
import requests
import os
clear = lambda: os.system('cls')
clear()
x = []
y = []

def date(que):
    print(que)
    y = input("Year (xxxx): ")
    m = input("Mounth (xx): ")
    d = input("Day (xx): ")
    clear()
    return y+"-"+m+"-"+d

start = date("Start Year: ")
end = date("End Year: ")
cur = input("Curency\nusd = United States dollar\ncad = Canadian Dollar\nsek = Swedish crowns\neur = Euro\n")
response = requests.get(f"https://api.coindesk.com/v1/bpi/historical/close.json?start={start}&end={end}&currency={cur}")
data = response.json()
data = data["bpi"]
#print(x)
for i, b in data.items():
    print(i, b)
    x.append(i)
    y.append(b)
    
    
plt.plot(x, y)

#Labels
plt.xlabel('Tid')
plt.ylabel('Para')
  
plt.title('Bitcoin!')

plt.show()