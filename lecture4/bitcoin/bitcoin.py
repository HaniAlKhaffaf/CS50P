import sys, requests

def main():
    if len(sys.argv) < 2:
        print("missing command-line argument")
    elif len(sys.argv) > 2:
        print("Too many argumnts")
    else:
        try:
            user_input = float(sys.argv[1])
            bitcoin_price = fetch_bitcoin()
            final_price = bitcoin_price * user_input
            formatted_price = f"{final_price:,.4f}"
            print(formatted_price)
        except:
            sys.exit("Command-line argument is not a number")

def fetch_bitcoin():
    try:
        respone = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = respone.json()
        bitcoin_in_float = o["bpi"]["USD"]["rate_float"]
        return bitcoin_in_float 
    except requests.RequestException:
        print("Couldn't fetch data")





if __name__ == "__main__":
    main()

 