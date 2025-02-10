import paho.mqtt.client as mqtt
from config import BROKER, PORT, TOPIC_UMIDIFICADOR

def on_message(client, userdata, msg):
    print(f"Umidificador: {msg.payload.decode()}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message

client.connect(BROKER, PORT)
client.subscribe(TOPIC_UMIDIFICADOR)

print("Atuador Umidificador pronto!")
client.loop_forever()