from middleware.middleware import Middleware
from config import TOPIC_AR, TOPIC_UMIDIFICADOR

middleware = Middleware()

while True:
    print("Digite (1) para ligar/desligar o ar-condicionado, (2) para o umidificador:")
    comando = input()

    if comando == "1":
        middleware.send_command(TOPIC_AR, "LIGADO")
    elif comando == "2":
        middleware.send_command(TOPIC_UMIDIFICADOR, "LIGADO")
    else:
        print("Opção inválida! Digite 1 ou 2.")