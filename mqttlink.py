# python 3.6

import time
import random
import json
import yaml

from paho.mqtt import client as mqtt_client


# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'

def connect_mqtt(config):
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    broker = config['broker']
    print(broker)
    port = config['port']
    client.connect(broker, port)
    return client


def publish(client, config):
    msg_count = 0
    while True:
        time.sleep(1)
        x = len(config['sensors'])
        print("Sensors to declare :" + str(x))

        for i in range(x):
            device_class = config['sensors'][i]['device_class']
            friendly_name = config['sensors'][i]['friendly_name']
            unit_of_measurement = config['sensors'][i]['unit_of_measurement']
            topic = config['topic']
            name = friendly_name + "_" + unit_of_measurement
            state_topic = "Qdata/last/" + name + "/" + str(i) + "/value/1"
            unique_id = name + "_" + str(i)
            fulltopic = topic + "/sensor/" + name + "/1/config"
            mqttmessage = {
                "value_template":"{{ value_json.value }}",
                "device_class":device_class,
                "unit_of_measurement":unit_of_measurement,
                "state_topic":state_topic,
                "json_attributes_topic":state_topic,
                "device": {
                    "identifiers":[
                    friendly_name
                    ],
                    "manufacturer":"TITA",
                    "model":"L150",
                    "name":friendly_name,
                    "sw_version":"1.0"
                },
                "name":name,
                "unique_id":unique_id
                }
            msg =  json.dumps(mqttmessage)
            result = client.publish(fulltopic, msg, retain=True)
            status = result[0]
            if status == 0:
                print(f"Send ok to topic `{fulltopic}`")
            else:
                print(f"Failed to send message to topic {fulltopic}")
            msg_count += 1
        exit()

def read_config():
    with open('config.yaml') as f:   
    
        config = yaml.load(f, Loader=yaml.FullLoader)
    print(f"config readed")
    return config



def run():
    config = read_config()
    client = connect_mqtt(config)
    client.loop_start()
    publish(client, config)


if __name__ == '__main__':
    run()
