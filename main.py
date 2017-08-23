import websocket
import thread
import time
import sys
import requests
from bs4 import BeautifulSoup
import pygame
import pyperclip

new_id = -1
poe_trade_url = None

def on_message(ws, message):
    global new_id
    global poe_trade_url

    payload = {'id': new_id}
    r = requests.post("http://poe.trade/search/"+poe_trade_url+"/live", data=payload, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    new_id = r.json()['newid']
    if r.json().has_key('data'):
        html_doc = r.json()['data']
        soup = BeautifulSoup(html_doc, 'html.parser')
        items = soup.find_all("tbody", { "class" : "item" })

        if sys.argv[1] == 'True':
            pygame.mixer.init()
            pygame.mixer.music.load("beep.wav")
            pygame.mixer.music.play()
        for item in items:
            #por placeholders neste caos lul
            pyperclip.copy(item.get('data-name'))
            print('Hey ' +item.get('data-ign') + 'I want your ' + item.get('data-name') + ' listed for ' + item.get('data-buyout') + ' on ' + item.get('data-league')+' located on your stash tab ' + item.get('data-tab')+ ' located left ' + item.get('data-x')+ ' top ' +item.get('data-y') )
    else:
        print("nothing found")
 
def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        #for i in range(3):
        #    time.sleep(1)
        #    ws.send("Hello %d" % i)
        time.sleep(99999999)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    poe_trade_url_ini = raw_input("Please enter your poe.trade URL: ")
    poe_trade_url_split = poe_trade_url_ini.split("search/", 1)[1]
    
    poe_trade_url = poe_trade_url_split.split("/live",1)[0]
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp("ws://live.poe.trade/" + poe_trade_url,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()