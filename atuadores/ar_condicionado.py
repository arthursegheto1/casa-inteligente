import paho.mqtt.client as mqtt
from config import BROKER, PORT, TOPIC_AR

def on_message(client, userdata, msg):
    print(f"Ar-condicionado: {msg.payload.decode()}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message

client.connect(BROKER, PORT)
client.subscribe(TOPIC_AR)

print("Atuador Ar-condicionado pronto!")
client.loop_forever()