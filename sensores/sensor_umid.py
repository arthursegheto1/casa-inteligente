import paho.mqtt.client as mqtt
import random
import time
from config import BROKER, PORT, TOPIC_UMIDADE

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)  
client.connect(BROKER, PORT)

while True:
    umidade = random.uniform(30, 90)  # Gera umidade aleatória
    client.publish(TOPIC_UMIDADE, f"{umidade:.2f}")  # Envia para MQTT
    print(f"Sensor Umidade -> {umidade:.2f}%")
    time.sleep(5)