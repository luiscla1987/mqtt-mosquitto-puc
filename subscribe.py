import paho.mqtt.client as mqtt
from datetime import datetime

mqttBroker = '192.168.0.10'
port = 1884
topic = "/Aula02/Luis-Claudio/"
username = 'luis'
password = '123456'

def coletar_hora():
    return datetime.now().hour

def callback(client, userdata, message):
    print("Topico: ", str(message.topic))
    print("Msg: ", str(message.payload.decode("utf-8")))


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(username, password)
client.connect(mqttBroker, port)

topic_now = topic + str(datetime.now().hour)
print("TOPIC: ",topic_now)


client.message_callback_add(topic_now, callback)
client.subscribe(topic_now)

client.loop_forever()