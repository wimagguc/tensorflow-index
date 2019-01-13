from requests import get

"""
Run this script to download historical price data from Yahoo Finance:
* For between 19/Feb/2015 and 19/Feb/2018
* For each ticker in our hard-coded list
* Save them as a list of CSVs in the current folder

(This hardcoded list of tickers are the ones found in multiple ETFs.)
"""

def download(url, file_name):
    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)


list = ['AAPL', 'MSFT', 'FB', 'AMZN', 'JNJ', 'JPM', 'XOM', 'GOOG', 'GOOGL',
        'WFC', 'BAC', 'PG', 'T', 'BRK-A', 'GE', 'CVX', 'PFE', 'VZ',
        'CMCSA', 'V', 'HSBC', 'UNH', 'C', 'KO', 'NVS', 'HD', 'PM',
        'MRK', 'INTC', 'PEP', 'DIS', 'CSCO', 'ORCL', 'TM', 'BTI', 'BA', 'MCD',
        'INTC', 'AMGN', 'MA', 'MO', 'RDS-B', 'MMM', 'WMT', 'TSS', 'ABBV',
        'SNY', 'BP', 'MDT', 'RY', 'GILD', 'RDS-B',
        'SAP', 'HON', 'BMY', 'AVGO', 'UL',
        'GSK', 'TD', 'UTX', 'BUD', 'NVDA', 'BASFY', 'PCLN',
        'UNP', 'CHTR', 'NVO', 'DEO', 'WBK',
        'TXN', 'ACN', 'LLY', 'GS', 'SBUX', 'UPS', 'DWDP',
        'TWX', 'CVS', 'QCOM', 'ADBE', 'NFLX', 'VOD', 'AGN', 'WBA', 'BNS',
        'AZN', 'TMO', 'MTU', 'PYPL', 'CAT',
        'BHP', 'ING', 'COST', 'CB', 'AXP', 'BIIB', 'ENB',
        'MS', 'MDLZ', 'CRM', 'RB.L', 'DUK', 'PNC',
        'PUK', 'CL', 'AIG', 'RIO', 'LYG',
        'BBVA', 'ASML', 'GLEN.L', 'AET', 'BK', 'FDX', 'COP', 'RTN',
        'GD', 'SU', 'MON', 'DHR', 'F', 'SPG', 'BLK', 'KHC', 'SNE',
        'DM', 'EOCC', 'AMAT', 'GM', 'EOG', 'SO', 'DM', 'ADP', 'SCHW',
        'TJX', 'SYK', 'CSX', 'ATVI', 'CGG', 'BMO', 'CI',
        'ABB', 'TSLA', 'OXY', 'NOC', 'BDX', 'PRU', 'MET',
        'SHPG', 'F', 'ABB', 'AGN', 'AIR', 'ALV', 'BAC',
        'BAYN', 'BNS', 'CBA', 'COP', 'CS', 'CSL',
        'DAI', 'DG', 'DTE', 'HON', 'JPM',
        'MC', 'NAB', 'ROG', 'SCL', 'SIE', 'SU', 'TEF',
        'TRP', 'CCI', 'CME', 'ITW', 'GLE', 'CTSH', 'ADS', 'DPW', 'MMC',
        'ENI', 'BIL', 'SPGI', 'ITB', 'VNX', 'ISRG',
        'COF', 'REGN', 'HUM',

        # Indexes
        'DAX', 'AIEQ', 'DJI', 'INX',

        ]

for l in list:
    url = 'http://finance.google.com/finance/historical?q=' + l \
        + '&startdate=Feb+19%2C+2015&enddate=Feb+19%2C+2018' \
        + '&output=csv'
    file_name = l + '.csv'
    download(url, file_name)
