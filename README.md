# Casa Inteligente - Sistema Distribuído com MQTT

Este projeto simula uma casa inteligente (Smart Home) utilizando o protocolo MQTT para comunicação entre sensores, atuadores, controladores e um middleware. O sistema é composto por sensores de temperatura e umidade, atuadores (ar-condicionado e umidificador), controladores e um cliente que permite interagir com o sistema.

---

## **Requisitos**

- Python 3.x instalado.
- Biblioteca `paho-mqtt` instalada. Para instalar, execute:
  ```bash
  pip install paho-mqtt


Como Rodar o Projeto:

1. Clone o repositório ou baixe os arquivos do projeto.

2. Navegue até a pasta do projeto.

Execute os componentes:

3. Abra terminais separados para cada componente e execute os comandos abaixo.

- Sensor de Temperatura
  
   python -m sensores.sensor_temp

- Sensor de Umidade

   python -m sensores.sensor_umid

- Atuador Ar-Condicionado

   python -m atuadores.ar_condicionado

- Atuador Umidificador

   python -m atuadores.umidificador

- Controlador Principal

   python -m controladores.controlador_principal

- Controlador Réplica (Opcional)

   python -m controladores.controlador_replica

- Middleware

   python -m middleware.middleware

- Cliente

   python -m cliente.cliente

4. Interaja com o sistema:

   Use o cliente para enviar comandos e visualizar o status dos atuadores.

Como o Projeto Funciona: 

Componentes

1. Sensores:

   - Sensor de Temperatura: Publica valores aleatórios de temperatura (entre 15°C e 35°C) no tópico casa/sensor/temperatura.

   - Sensor de Umidade: Publica valores aleatórios de umidade (entre 30% e 90%) no tópico casa/sensor/umidade.

2. Atuadores:

   - Ar-Condicionado: Assina o tópico casa/atuador/arcondicionado e exibe o status (LIGADO ou DESLIGADO).

   - Umidificador: Assina o tópico casa/atuador/umidificador e exibe o status (LIGADO ou DESLIGADO).

3. Controladores:

   - Controlador Principal: Processa os dados dos sensores e publica comandos para os atuadores.

   - Controlador Réplica: Funciona como backup e pode assumir o controle caso o principal falhe.

4. Middleware:

   - Faz a intermediação entre o cliente e o sistema.

   - Verifica a consistência dos dados recebidos dos sensores.

   - Encaminha as informações para os controladores.

5. Cliente:

   - Permite que o usuário envie comandos para ligar/desligar o ar-condicionado e o umidificador.

Exemplo de Funcionamento

1. Sensores Publicam Dados:

   - O sensor de temperatura publica: Sensor Temp -> 25.34°C.

   - O sensor de umidade publica: Sensor Umidade -> 60.45%.

2. Controlador Toma Decisões:

   - Se a temperatura for maior que 28°C, o controlador publica LIGADO no tópico do ar-condicionado.

   - Se a umidade for menor que 40%, o controlador publica LIGADO no tópico do umidificador.

3. Atuadores Respondem:

   - O ar-condicionado exibe: Ar-condicionado: LIGADO.

   - O umidificador exibe: Umidificador: LIGADO.

4. Cliente Envia Comandos:

   - O usuário pode digitar 1 para ligar/desligar o ar-condicionado ou 2 para o umidificador.
   - 
   Link para documentação:

https://hackmd.io/@9hRrKkrcTwuWoSV-mbHrDQ/S10CNiPF1x
