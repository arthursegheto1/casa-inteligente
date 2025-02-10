import paho.mqtt.client as mqtt
from config import BROKER, PORT, TOPIC_TEMP, TOPIC_UMIDADE, TOPIC_AR, TOPIC_UMIDIFICADOR

class Middleware:
    def __init__(self):
        print("Middleware iniciado! Aguardando mensagens...")  
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.client.on_message = self.on_message
        self.client.connect(BROKER, PORT)
        self.client.subscribe([(TOPIC_TEMP, 0), (TOPIC_UMIDADE, 0)])
        self.client.loop_start()

    def on_message(self, client, userdata, msg):
        valor = float(msg.payload.decode())

        # Verificação de consistência
        if msg.topic == TOPIC_TEMP and (valor < 15 or valor > 35):
            print(f"Valor inconsistente recebido: {valor}°C")
            return

        if msg.topic == TOPIC_UMIDADE and (valor < 30 or valor > 90):
            print(f"Valor inconsistente recebido: {valor}%")
            return

        # Encaminha os dados para o controlador ativo
        if msg.topic == TOPIC_TEMP:
            if valor > 28:
                self.client.publish(TOPIC_AR, "LIGADO")
                print(f"Temperatura alta detectada: {valor}°C. Ar-condicionado LIGADO.")
            else:
                self.client.publish(TOPIC_AR, "DESLIGADO")
                print(f"Temperatura normal: {valor}°C. Ar-condicionado DESLIGADO.")

        if msg.topic == TOPIC_UMIDADE:
            if valor < 40:
                self.client.publish(TOPIC_UMIDIFICADOR, "LIGADO")
                print(f"Umidade baixa detectada: {valor}%. Umidificador LIGADO.")
            else:
                self.client.publish(TOPIC_UMIDIFICADOR, "DESLIGADO")
                print(f"Umidade normal: {valor}%. Umidificador DESLIGADO.")

    def send_command(self, topic, command):
        self.client.publish(topic, command)

middleware = Middleware()