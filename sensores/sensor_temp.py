import paho.mqtt.client as mqtt
import random
import time
from config import BROKER, PORT, TOPIC_TEMP

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(BROKER, PORT)

while True:
    temperatura = random.uniform(15, 35) # Gera temperatura aleatória
    client.publish(TOPIC_TEMP, f"{temperatura:.2f}") # Envia para MQTT
    print(f"Sensor Temp -> {temperatura:.2f}°C")
    time.sleep(5)