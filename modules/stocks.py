import requests


def get_stock(stock_name):
    headers = {
            'User-Agent': 'https://github.com/rkpkr/tellMe'
    }
    url = 'https://api.iextrading.com/1.0/stock/' + stock_name + '/stats/'
    r = requests.get(url, headers=headers)
    j = r.json()
    return j



if __name__ == '__main__':
    stock = input('Enter stock ticker: ')
    b = get_stock(stock)
    print(b['companyName'], b['week52high'])
