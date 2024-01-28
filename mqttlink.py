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
    if config['user'] and config['password']:
        print("MQTT user and password set")
        client.username_pw_set(config['user'], config['password'])
    else:
        print("No MQTT user") 
 
    client.on_connect = on_connect
    broker = config['broker']
    print(broker)
    port = config['port']
    client.connect(broker, port)
    return client

def sensors(config, i):
    topic = config['discoverytopic']
    friendly_name = config['sensors'][i]['friendly_name']
    sensorname = config['sensors'][i]['name']
    identifiers = sensorname + "_" + config['sensors'][i]['model']
    if 'device_class' in config['sensors'][i] and config['sensors'][i]['device_class']:
        name = friendly_name + "_" + config['sensors'][i]['device_class']
    else:
        name = friendly_name

    fulltopic = topic + "/sensor/" + name + "/1/config"

    if 'state_topic' in config['sensors'][i]:
        state_topic = config['sensors'][i]['state_topic']
        print("state_config detected for sensor" + str(i))
    else:
        state_topic = "Qdata/last/" + name + "/" + str(i) + "/value/1"
            
            
    if 'manufacturer' in config['sensors'][i]:
        manufacturer = config['sensors'][i]['manufacturer']
        print("manufacturer detected for sensor" + str(i))
    else:
        manufacturer = "unknown"
            
    if 'model' in config['sensors'][i]:
        model = config['sensors'][i]['model']
        print("model detected for sensor" + str(i))
    else:
        model = "unknow"

    if 'sw_version' in config['sensors'][i]:
        sw_version = config['sensors'][i]['sw_version']
        print("sw_version detected for sensor" + str(i))
    else:
        sw_version = "unknown"
            
    unique_id = name + "_" + str(i)

    mqttmessage = {
        "state_topic":state_topic,
        #"json_attributes_topic":state_topic,
        "device": {
            "identifiers":[
            identifiers
            ],
            "manufacturer":manufacturer,
            "model":model,
            "name":sensorname,
            "sw_version":sw_version
        },
        "name":name,
        "unique_id":unique_id
        }
    if 'value_template' in config['sensors'][i] and config['sensors'][i]['value_template']:
        print("value_template detected")
        mqttmessage["value_template"] = config['sensors'][i]['value_template']
    else:
        print("there is no value_template")

    if 'unit_of_measurement' in config['sensors'][i] and config['sensors'][i]['unit_of_measurement']:
        print("unit_of_measurement detected")
        mqttmessage["unit_of_measurement"] = config['sensors'][i]['unit_of_measurement']
    else:
        print("there is no unit_of_measurement")

    if 'device_class' in config['sensors'][i] and config['sensors'][i]['device_class']:
        print("device_class detected")
        mqttmessage["device_class"] = config['sensors'][i]['device_class']    
    else:
        print("there is no device_class")

    if 'state_class' in config['sensors'][i] and config['sensors'][i]['state_class']:
        print("state_class detected")
        mqttmessage["state_class"] = config['sensors'][i]['state_class']   
    else:
        print("there is no state_class")

    return mqttmessage, fulltopic

def binary_sensors(config, i):
    topic = config['discoverytopic']
    friendly_name = config['binary_sensors'][i]['friendly_name']
    name = friendly_name + "_binary"
    sensorname = config['binary_sensors'][i]['name']
    identifiers = sensorname + "_" + config['binary_sensors'][i]['model']
    fulltopic = topic + "/binary_sensor/" + name + "/1/config"
    payload_on = config['binary_sensors'][i]['payload_on']
    payload_off = config['binary_sensors'][i]['payload_off']            

    if 'state_topic' in config['binary_sensors'][i]:
        state_topic = config['binary_sensors'][i]['state_topic']
        print("state_config detected for binary_sensor" + str(i))
    else:
        state_topic = "Qdata/last/" + name + "/" + str(i) + "/value/1"
            
            
    if 'manufacturer' in config['binary_sensors'][i]:
        manufacturer = config['binary_sensors'][i]['manufacturer']
        print("manufacturer detected for binary_sensor" + str(i))
    else:
        manufacturer = "unknown"
            
    if 'model' in config['binary_sensors'][i]:
        model = config['binary_sensors'][i]['model']
        print("model detected for binary_sensor" + str(i))
    else:
        model = "unknow"

    if 'sw_version' in config['binary_sensors'][i]:
        sw_version = config['binary_sensors'][i]['sw_version']
        print("sw_version detected for binary_sensor" + str(i))
    else:
        sw_version = "unknown"
            
    unique_id = name + "_" + str(i)

    mqttmessage = {
        "payload_on": payload_on,
        "payload_off": payload_off,
        "state_topic":state_topic,
        # "json_attributes_topic":state_topic,
        "device": {
            "identifiers":[
            identifiers
            ],
            "manufacturer":manufacturer,
            "model":model,
            "name":sensorname,
            "sw_version":sw_version
        },
        "name":name,
        "unique_id":unique_id
        }

    if 'value_template' in config['binary_sensors'][i] and config['binary_sensors'][i]['value_template']:
        print("value_template detected")
        mqttmessage["value_template"] = config['binary_sensors'][i]['value_template']
        
    else:
        print("there is no value_template")

    return mqttmessage, fulltopic

def select(config, i):
    topic = config['discoverytopic']
    friendly_name = config['select'][i]['friendly_name']
    name = friendly_name + "_select"
    sensorname = config['select'][i]['name']
    identifiers = sensorname + "_" + config['select'][i]['model']
    fulltopic = topic + "/select/" + name + "/1/config"
    command_topic = config['select'][i]['command_topic']
    
    options = config['select'][i]['options']
            
            
    if 'manufacturer' in config['select'][i]:
        manufacturer = config['select'][i]['manufacturer']
        print("manufacturer detected for select" + str(i))
    else:
        manufacturer = "unknown"
            
    if 'model' in config['select'][i]:
        model = config['select'][i]['model']
        print("model detected for select" + str(i))
    else:
        model = "unknow"

    if 'sw_version' in config['select'][i]:
        sw_version = config['select'][i]['sw_version']
        print("sw_version detected for select" + str(i))
    else:
        sw_version = "unknown"
            
    unique_id = name + "_" + str(i)

    
    mqttmessage = {
        "command_topic":command_topic,
        #"json_attributes_topic":command_topic,
        "device": {
            "identifiers":[
            identifiers
            ],
            "manufacturer":manufacturer,
            "model":model,
            "name":sensorname,
            "sw_version":sw_version
        },
        "options":options,
        "name":name,
        "unique_id":unique_id
        }
    if 'state_topic' in config['select'][i] and config['select'][i]['state_topic']:
        print("state_topic detected")
        mqttmessage["state_topic"] = config['select'][i]['state_topic']
        
    else:
        print("there is no state_topic")
    
    return mqttmessage, fulltopic

def climate(config, i):
    topic = config['discoverytopic']
    friendly_name = config['climate'][i]['friendly_name']
    name = friendly_name + "_climate"
    sensorname = config['climate'][i]['name']
    identifiers = sensorname + "_" + config['climate'][i]['model']
    fulltopic = topic + "/climate/" + name + "/1/config"
    temperature_command_topic = config['climate'][i]['temperature_command_topic']
    temperature_state_topic = config['climate'][i]['temperature_state_topic']
    current_temperature_topic = config['climate'][i]['current_temperature_topic']
    max_temp = config['climate'][i]['max_temp']
    min_temp = config['climate'][i]['min_temp']
    mode_command_topic = config['climate'][i]['mode_command_topic']
    mode_state_topic = config['climate'][i]['mode_state_topic']  
    modes = config['climate'][i]['modes']
    if 'manufacturer' in config['climate'][i]:
        manufacturer = config['climate'][i]['manufacturer']
        print("manufacturer detected for climate" + str(i))
    else:
        manufacturer = "unknown"
            
    if 'model' in config['climate'][i]:
        model = config['climate'][i]['model']
        print("model detected for climate" + str(i))
    else:
        model = "unknow"

    if 'sw_version' in config['climate'][i]:
        sw_version = config['climate'][i]['sw_version']
        print("sw_version detected for climate" + str(i))
    else:
        sw_version = "unknown"
            
    unique_id = name + "_" + str(i)
    
    mqttmessage = {
        "temperature_command_topic":temperature_command_topic,  
        "temperature_state_topic":temperature_state_topic,
        "current_temperature_topic":current_temperature_topic,
        #"mode_command_topic": mode_command_topic,
        #"mode_state_topic": mode_state_topic,
        #"modes": modes,
        #"json_attributes_topic":temperature_command_topic,
        "min_temp": min_temp,
        "max_temp": max_temp,
        "device": {
            "identifiers":[
            identifiers
            ],
            "manufacturer":manufacturer,
            "model":model,
            "name":sensorname,
            "sw_version":sw_version
        },
        "name":name,
        "unique_id":unique_id
        }
    
    if 'temperature_command_template' in config['climate'][i] and config['climate'][i]['temperature_command_template']:
        print("temperature_command_template")
        mqttmessage["temperature_command_template"] = config['climate'][i]['temperature_command_template']
    else:
        print("there is no temperature_command_template")

    if 'temp_step' in config['climate'][i] and config['climate'][i]['temp_step']:
        print("temp_step")
        mqttmessage["temp_step"] = config['climate'][i]['temp_step']
    else:
        print("there is no temp_step")

    return mqttmessage, fulltopic

def switch(config, i):
    topic = config['discoverytopic']
    friendly_name = config['switch'][i]['friendly_name']
    name = friendly_name + "_switch"
    sensorname = config['switch'][i]['name']
    identifiers = sensorname + "_" + config['switch'][i]['model']
    fulltopic = topic + "/switch/" + name + "/1/config"
    command_topic = config['switch'][i]['command_topic']
    device_class = config['switch'][i]['device_class']
    state_topic = config['switch'][i]['state_topic']
            
    if 'manufacturer' in config['switch'][i]:
        manufacturer = config['switch'][i]['manufacturer']
        print("manufacturer detected for switch" + str(i))
    else:
        manufacturer = "unknown"
            
    if 'model' in config['switch'][i]:
        model = config['switch'][i]['model']
        print("model detected for switch" + str(i))
    else:
        model = "unknow"

    if 'sw_version' in config['switch'][i]:
        sw_version = config['switch'][i]['sw_version']
        print("sw_version detected for switch" + str(i))
    else:
        sw_version = "unknown"
            
    unique_id = name + "_" + str(i)
    
    mqttmessage = {
        "command_topic":command_topic,  
        "device_class":device_class,
        "state_topic":state_topic,
        "device": {
            "identifiers":[
            identifiers
            ],
            "manufacturer":manufacturer,
            "model":model,
            "name":sensorname,
            "sw_version":sw_version
        },
        "name":name,
        "unique_id":unique_id
        }
    
    if 'payload_on' in config['switch'][i] and config['switch'][i]['payload_on']:
        print("payload_on")
        mqttmessage["payload_on"] = config['switch'][i]['payload_on']
    else:
        print("there is no payload_on")

    if 'payload_off' in config['switch'][i] and config['switch'][i]['payload_off']:
        print("payload_off")
        mqttmessage["payload_off"] = config['switch'][i]['payload_off']
    else:
        print("there is no payload_off")
    
    if 'state_on' in config['switch'][i] and config['switch'][i]['state_on']:
        print("state_on")
        mqttmessage["state_on"] = config['switch'][i]['state_on']  
    else:
        print("there is no state_on")

    if 'state_off' in config['switch'][i] and config['switch'][i]['state_off']:
        print("state_off")
        mqttmessage["state_off"] = config['switch'][i]['state_off']  
    else:
        print("there is no state_off")
    return mqttmessage, fulltopic


def publish(client, config):
    msg_count = 0
    while True:
        time.sleep(1)
        x = len(config['sensors'])
        print("Sensors to declare :" + str(x))

        for i in range(x):           
            mqttmessage, fulltopic = sensors(config, i)
            msg =  json.dumps(mqttmessage)
            result = client.publish(fulltopic, msg, retain=True)
            status = result[0]
            if status == 0:
                print(f"Sent to topic `{fulltopic}`")
            else:
                print(f"Failed to send message to topic {fulltopic}")
            msg_count += 1
        
        y = len(config['binary_sensors'])
        print("binary_ensors to declare :" + str(y))
        for i in range(y):           
            mqttmessage, fulltopic = binary_sensors(config, i)
            msg =  json.dumps(mqttmessage)
            result = client.publish(fulltopic, msg, retain=True)
            status = result[0]
            if status == 0:
                print(f"Sent to topic `{fulltopic}`")
            else:
                print(f"Failed to send message to topic {fulltopic}")
            msg_count += 1
        
        z = len(config['select'])
        print("Select to declare :" + str(z))

        for i in range(z):           
            mqttmessage, fulltopic = select(config, i)
            msg =  json.dumps(mqttmessage)
            result = client.publish(fulltopic, msg, retain=True)
            status = result[0]
            if status == 0:
                print(f"Sent to topic `{fulltopic}`")
            else:
                print(f"Failed to send message to topic {fulltopic}")
            msg_count += 1
        
        w = len(config['climate'])
        print("Climate to declare :" + str(w))

        for i in range(w):           
            mqttmessage, fulltopic = climate(config, i)
            msg =  json.dumps(mqttmessage)
            result = client.publish(fulltopic, msg, retain=True)
            status = result[0]
            if status == 0:
                print(f"Sent to topic `{fulltopic}`")
            else:
                print(f"Failed to send message to topic {fulltopic}")
            msg_count += 1
        
        w = len(config['switch'])
        print("switch to declare :" + str(w))

        for i in range(w):           
            mqttmessage, fulltopic = switch(config, i)
            msg =  json.dumps(mqttmessage)
            result = client.publish(fulltopic, msg, retain=True)
            status = result[0]
            if status == 0:
                print(f"Sent to topic `{fulltopic}`")
            else:
                print(f"Failed to send message to topic {fulltopic}")
            msg_count += 1
        exit()

def read_config():
    with open('config.yaml', encoding='utf-8') as f:   
    
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
