## POE.TRADE Scraper

This script allows you to connect to http://poe.trade via websocket search for items that match a specific search pattern. When that occurs, the most recent item gets copied to your clipboard

### Dependencies
* BeautifulSoup 
* pygame
* pyperclip
* requests
* websocket-client

### Installation

```
pip install -r requirements.txt
```

### Usage

```python
python main.py
```

A user input is required in order to enter the desired search pattern, you just need to copy paste a PoE.Trade URL (e.g. http://poe.trade/search/ugonaranikimot or http://poe.trade/search/ugonaranikimot/live)

## Notes
This is a fairly rudimentary script that requires improvement, I've just made it to help out a friend that loves Path of Exile and I've decided to share it should someone else find it useful

## Todo
This works decently for specific filters, if your filter is too broad you will receive several items per iteration and you will only have the most recent one on your clipboard
