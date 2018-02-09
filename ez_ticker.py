from bs4 import BeautifulSoup
import requests

text_file = open("ticker_list.dat", "r")
ticker_list = text_file.read().split('\n')
text_file.close()
index = 0
tick_results = []
ticker_results = open("ticker_results.dat", "w")

for x in ticker_list:
    url = ("https://coinmarketcap.com/currencies/" + ticker_list[index] + "/")
    ez_req  = requests.get(url)
    ez_data = ez_req.text
    ez_soup = BeautifulSoup(ez_data, "html.parser")
    ez_bs4 = str(ez_soup.find(id="quote_price"))
    ez_tick = ez_bs4.replace('<span data-currency-price="" data-usd="', '')
    ez_tick = ez_tick.replace('" id="quote_price">', '')
    tick_results.extend(ez_tick.split('\n', 1)[0] + "\n")
    index += 1
tick_results = tick_results[:-1]
ticker_results.writelines(tick_results)
ticker_results.close()