import datetime
import os
from pprint import pprint

import anthropic
import panel as pn
import yfinance as yf
from dotenv import load_dotenv

load_dotenv()


client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])


MODEL = "claude-3-5-sonnet-20240620"
MAX_TOKENS = 1000


def get_stock_price(ticker: str, start="2024-01-01", end="2024-04-30"):
    stock = yf.download(ticker, start=start, end=end)
    return stock


def get_stock_ticker(description: str):
    response = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        tools=[
            {
                "name": "get_stock_ticker",
                "description": "Provide the stock ticker for the most probable company which is described in the input text. If in doubt which company to choose, use the company with the highest market capitalization.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "ticker": {
                            "type": "string",
                            "description": "Ticker symbol of the company, e.g. TSLA",
                        }
                    },
                    "required": ["ticker"],
                },
            }
        ],
        messages=[{"role": "user", "content": description}],
    )
    pprint(response.to_dict())
    return response.content[-1].input["ticker"]


def get_stock_performance(question, user, interface):
    current_day = str(datetime.date.today())
    ticker = get_stock_ticker(question)
    df = get_stock_price(ticker, start="2024-01-01", end=current_day)
    price_at_beginning_of_year = df["Close"].iloc[0]
    price_recent = df["Close"].iloc[-1]
    performance_since_beginning_of_year = (
        price_recent / price_at_beginning_of_year - 1
    ) * 100
    response = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        messages=[
            {
                "role": "user",
                "content": f"You act as stock analyst. Describe the company and the performance for the stock {ticker}, which is {performance_since_beginning_of_year:.2f}% since the beginning of the year. They started the year with ${price_at_beginning_of_year:.2f} and the price on {current_day} was ${price_recent:.2f}. Present your findings as a markdown table, with no other text at the start or end.",
            }
        ],
    )
    return response.content[0].text


chat_interface = pn.chat.ChatInterface(
    callback=get_stock_performance, callback_user="LLM"
)


chat_interface.send(
    "Describe the company you want to know the stock performance for.",
    user="LLM",
    respond=False,
)


chat_interface.show()
