import paho.mqtt.client as mqtt
from config import BROKER, PORT, TOPIC_TEMP, TOPIC_UMIDADE, TOPIC_AR, TOPIC_UMIDIFICADOR

def on_message(client, userdata, msg):
    valor = float(msg.payload.decode())

    if msg.topic == TOPIC_TEMP:
        if valor > 28:
            client.publish(TOPIC_AR, "LIGADO")
        else:
            client.publish(TOPIC_AR, "DESLIGADO")

    if msg.topic == TOPIC_UMIDADE:
        if valor < 40:
            client.publish(TOPIC_UMIDIFICADOR, "LIGADO")
        else:
            client.publish(TOPIC_UMIDIFICADOR, "DESLIGADO")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message

client.connect(BROKER, PORT)
client.subscribe([(TOPIC_TEMP, 0), (TOPIC_UMIDADE, 0)])

print("Controlador Réplica iniciado!")
client.loop_forever()