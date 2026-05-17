import pandas as pd
import yfinance as yf


def load_csv_data(filepath):

    df = pd.read_csv(filepath)

    return df


def load_live_option_chain(
    symbol,
    expiry
):

    stock = yf.Ticker(symbol)

    option_chain = stock.option_chain(expiry)

    calls = option_chain.calls

    puts = option_chain.puts

    return calls, puts


def get_available_expiries(symbol):

    stock = yf.Ticker(symbol)

    return stock.options
