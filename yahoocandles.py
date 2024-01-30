import pandas as pd
from datetime import datetime, timedelta, time
import requests

def unix_to_human(unix_timestamp):
    return datetime.utcfromtimestamp(unix_timestamp).strftime('%Y-%m-%d %H:%M:%S')

def get_data(symbol: str, interval: str, exchange: str) -> None:
    if exchange=="NSE":
        symbol=symbol+".NS"
    elif exchange=="BSE":
        symbol=symbol+".BO"
    
    current_datetime = datetime.now()

    if interval == "1m":
        start_datetime = current_datetime - timedelta(7)
    elif interval == "1d":
        start_datetime = current_datetime - timedelta(180)
    elif interval=="2m" or interval=="5m" or interval=="15m":
        start_datetime = current_datetime - timedelta(50)
    else:
        start_datetime = current_datetime - timedelta(30)

    print("Current Date Time: ", current_datetime)
    print("Start Date Time: ", start_datetime)

    current_unix_timestamp = int(current_datetime.timestamp())
    start_unix_timestamp = int(start_datetime.timestamp())
    try:
        url = "https://query1.finance.yahoo.com/v8/finance/chart/" + symbol
        payload = {
            'symbol': symbol,
            'period1': start_unix_timestamp,
            'period2': current_unix_timestamp,
            'useYfid': True,
            'interval': interval,
            'includePrePost': False,
            'events': 'div|split|earn',
            'lang': 'en-US',
            'region': 'US',
            'crumb': 'sOg8bcPRuSJ',
            'corsDomain': 'finance.yahoo.com'
        }
        headers = {
            'method': 'GET',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Origin': 'https://finance.yahoo.com',
            'Referer': 'https://finance.yahoo.com/quote/TATAPOWER.NS/chart?p=TATAPOWER.NS',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
        }
    
        response = requests.request("GET", url, headers=headers, params=payload)
    
        json_response = response.json()
    
        timestamp = json_response['chart']['result'][0]['timestamp']
        last_timestamp = timestamp[-1]
        open_price = json_response['chart']['result'][0]['indicators']['quote'][0]["open"]
        high_price = json_response['chart']['result'][0]['indicators']['quote'][0]["high"]
        low_price = json_response['chart']['result'][0]['indicators']['quote'][0]["low"]
        close_price = json_response['chart']['result'][0]['indicators']['quote'][0]["close"]
    
        time_df = pd.DataFrame(timestamp, columns=['Date'])
        time_df['Date'] = time_df['Date'].apply(unix_to_human)
        open_df = pd.DataFrame(open_price, columns=['Open'])
        high_df = pd.DataFrame(high_price, columns=['High'])
        low_df = pd.DataFrame(low_price, columns=['Low'])
        close_df = pd.DataFrame(close_price, columns=['Close'])
        final_df = pd.concat([time_df, open_df, high_df, low_df, close_df], axis=1)
    
        if interval == "1d":
            final_df.insert(0, 'Symbol', symbol)
            last_timestamp = datetime.utcfromtimestamp(last_timestamp)
            if last_timestamp.time() != time(3, 45, 0):
                last_date = final_df.iloc[-1, 1]
                last_date = datetime.strptime(last_date, "%Y-%m-%d %H:%M:%S")
                time_offset = timedelta(hours=5, minutes=30)
                time_offset = last_date + time_offset
                time_offset = time_offset.strftime("%Y-%m-%d %H:%M:%S")
                final_df.at[final_df.index[-1], 'Date'] = time_offset
        else:
            final_df['Date'] = final_df['Date'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))
            time_offset = timedelta(hours=5, minutes=30)
            final_df['Date'] = final_df['Date'] + time_offset
            final_df['Date'] = final_df['Date'].apply(lambda x: x.strftime("%Y-%m-%d %H:%M:%S"))
            final_df.insert(0, 'Symbol', symbol)
    
        return final_df
    except:
        print("Error Occured Try Again")

if __name__ == "__main__":
    symbol = str(input("Enter the Stock Symbol as per Yahoo Finance: "))
    interval = str(input("Enter Interval (1m, 2m, 5m, 15m, 1d): "))
    exchange=str(input("Enter Exchange (NSE/BSE)"))
    stock_data = get_data(symbol, interval,exchange)
    print(stock_data)
