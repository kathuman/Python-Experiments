import websocket
import json

def on_message(ws, message):
    values = json.loads(message)['values']
    x = values[0]
    y = values[1]
    z = values[2]
    print('x =',x,'y = ',y,'z = ',z)

def on_error(ws, error):
    print("error occurred")
    print(error)

def on_close(ws, close_code, reason):
    print("connection close")
    print("close code : ", close_code)
    print("reason : ", reason  )

def on_open(ws):
    print("connection open")
    

if __name__ == "__main__":
    ws = websocket.WebSocketApp("ws://192.168.86.176:8081/sensor/connect?type=android.sensor.linear_acceleration",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

    ws.run_forever()
 
 # To analyse multiple sensor data simultaneously, you can add as many websocket connections for different sensors as you want. 
