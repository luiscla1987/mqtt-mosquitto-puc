import paho.mqtt.client as mqtt
from datetime import datetime
import time

mqttBroker = '192.168.0.10'
port = 1884
topic = "\\Aula02\\Luis-Claudio\\"
username = 'luis'
password = '123456'

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))
 

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(username, password)
client.on_publish = on_publish
client.on_connect = on_connect
client.connect(mqttBroker, port)

while True:
    topic_now = topic + str(datetime.now().hour)
    print("TOPIC: ",topic_now)
    (rc, mid) = client.publish(topic_now, "Testando: " + str(datetime.now().second), qos=1)
    time.sleep(30)

