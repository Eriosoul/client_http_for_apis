from requests_html import HTMLSession
from templates.lib.data import Item


class Client():
    def __init__(self):
        self.base_url = f'https://www.fxpedalplanet.co.uk/product/tonetuga-fx-songbird-spectrum-overdrive-effects-pedal'
        self.session = HTMLSession()
        
    def get_data(self):
        rep = self.session.get(self.base_url)
        return rep

    def parse_data(self, response):
        product = Item(
            name= response.html.find('h1')[0].text,
            price= response.html.find('p.prod-price')[0].text,
            sku= response.html.find('h2.prod-title')[0].text,
            attributes= [item.text for item in response.html.find('div.medium-6.cell li')]
        )
        return product



