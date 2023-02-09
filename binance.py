import websocket
import rel
import json


symbol = "xrpusdt"
url = f"wss://stream.binance.com:9443/ws/{symbol}@ticker_1h"


def check_drop(msg):
    hi_price = float(msg.get("h"))
    last_price = float(msg.get("c"))
    diff = (hi_price - last_price) * 100 / last_price
    # print(f"Hi price: {hi_price}, last price: {last_price}, diff: {diff:.2f}")
    if diff > 1:
        print(f"Attention! Last price fell {diff:.2f}% in the last hour.")
        print(f" Hi price: {hi_price}, last_price: {last_price}")


def on_message(ws, message):
    message_json = json.loads(message)
    check_drop(message_json)


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


def on_open(ws):
    print("Opened connection")


if __name__ == "__main__":
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp(
        url,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
    )
    ws.run_forever(
        dispatcher=rel, reconnect=5
    )  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()
