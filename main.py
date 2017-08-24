import websocket
import thread
import time
import requests
from bs4 import BeautifulSoup
import pygame
import pyperclip

import settings

new_id = -1
poe_trade_url = None

def on_message(ws, message):
    global new_id
    global poe_trade_url

    payload = {'id': new_id}
    r = requests.post(settings.SEARCH_URL + poe_trade_url + "/live", data=payload, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    new_id = r.json()['newid']
    if r.json().has_key('data'):
        html_doc = r.json()['data']
        soup = BeautifulSoup(html_doc, 'html.parser')
        items = soup.find_all("tbody", { "class" : "item" })

        pygame.mixer.init()
        pygame.mixer.music.load("beep.wav")
        pygame.mixer.music.play()
        
        for item in items:
            pyperclip.copy('@'+item.get('data-ign') + ' Hi, I would like to buy your ' + item.get('data-name') + ' listed for ' + item.get('data-buyout') + ' in ' + item.get('data-league')+' (stash tab \"' + item.get('data-tab')+ '\"; position: left ' + item.get('data-x')+ ', top ' +item.get('data-y') +')')
            #should put some placeholders instead
            print('@'+item.get('data-ign') + ' Hi, I would like to buy your ' + item.get('data-name') + ' listed for ' + item.get('data-buyout') + ' in ' + item.get('data-league')+' (stash tab \"' + item.get('data-tab')+ '\"; position: left ' + item.get('data-x')+ ', top ' +item.get('data-y') +')')

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

if __name__ == "__main__":
    poe_trade_url_ini = raw_input("Please enter your poe.trade URL: ")
    poe_trade_url_split = poe_trade_url_ini.split("search/", 1)[1]
    poe_trade_url = poe_trade_url_split.split("/live",1)[0]

    websocket.enableTrace(False)
    ws = websocket.WebSocketApp(settings.WS_URL + poe_trade_url,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.run_forever()