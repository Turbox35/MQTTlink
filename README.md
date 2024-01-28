# MQTTlink
 Automatic device creation for Domoticz / Home Assistant with autodiscovery
 
 It can be used to make a link between domoticz and homeassitant using MQTT.
 Or to generates sensors for BSB_LAN

Now it integrates all sensors (temperature, power, ...), binary_sensors, select, climate and switch.

It's easy to use, just fill the config.yaml file by your sensors and run the python file.

For Domoticz bridge to Home Assistant, here a tutorial link:
https://blogmotion.fr/diy/connecter-domoticz-homeassistant-mqtt-20653

For BSB-LAN example, my config file is:
<blockquote>broker: '192.168.1.52'
port: 1883
user: 
password:
discoverytopic: homeassistant
sensors:
    - state_topic: BSB-LAN/8000
      friendly_name: Etat_circuit_chauffage
      manufacturer: Atlantic
      model: "Alfea AI"
      name: "BSB LAN"
      sw_version: "3.3.2"
    - state_topic: BSB-LAN/8006
      friendly_name: Etat_pompe_a_chaleur
      manufacturer: Atlantic
      model: "Alfea AI"
      name: "BSB LAN"
      sw_version: "3.3.2"
    - state_topic: BSB-LAN/8410
      state_class: measurement
      unit_of_measurement: "°C"
      device_class: temperature
      friendly_name: Temp_PAC_eau_retour
      manufacturer: Atlantic
      model: "Alfea AI"
      name: "BSB LAN"
      sw_version: "3.3.2"
    - state_topic: BSB-LAN/8411
      state_class: measurement
      unit_of_measurement: "°C"
      device_class: temperature
      friendly_name: Temp_PAC_eau_consigne
      manufacturer: Atlantic
      model: "Alfea AI"
      name: "BSB LAN"
      sw_version: "3.3.2"
    - state_topic: BSB-LAN/8412
      state_class: measurement
      unit_of_measurement: "°C"
      device_class: temperature
      friendly_name: Temp_PAC_eau_depart
      manufacturer: Atlantic
      model: "Alfea AI"
      name: "BSB LAN"
      sw_version: "3.3.2"
    - state_topic: BSB-LAN/8413
      state_class: measurement
      unit_of_measurement: "%"
      friendly_name: Modulation_compresseur
      manufacturer: Atlantic
      model: "Alfea AI"
      name: "BSB LAN"
      sw_version: "3.3.2"
    - state_topic: BSB-LAN/8425
      state_class: measurement
      unit_of_measurement: "°C"
      device_class: temperature
      friendly_name: Temp_condenseur
      manufacturer: Atlantic
      model: "Alfea AI"
      name: "BSB LAN"
      sw_version: "3.3.2"
    - state_topic: BSB-LAN/8450
      state_class: measurement
      unit_of_measurement: "h"
      device_class: duration
      friendly_name: Duree_fonctionnement_compresseur
      manufacturer: Atlantic
      model: "Alfea AI"
      name: "BSB LAN"
      sw_version: "3.3.2"
    - state_topic: BSB-LAN/8700
      state_class: measurement
      unit_of_measurement: "°C"
      device_class: temperature
      friendly_name: Temp_ext
      manufacturer: Atlantic
      model: "Alfea AI"
      name: "BSB LAN"
      sw_version: "3.3.2"
    - state_topic: BSB-LAN/8740
      state_class: measurement
      unit_of_measurement: "°C"
      device_class: temperature
      friendly_name: Temp_int
      manufacturer: Atlantic
      model: "Alfea AI"
      name: "BSB LAN"
      sw_version: "3.3.2"
    - state_topic: BSB-LAN/8741
      state_class: measurement
      unit_of_measurement: "°C"
      device_class: temperature
      friendly_name: Temp_consigne
      manufacturer: Atlantic
      model: "Alfea AI"
      name: "BSB LAN"
      sw_version: "3.3.2"
    - state_topic: BSB-LAN/6700
      friendly_name: Erreur_PAC
      manufacturer: Atlantic
      model: "Alfea AI"
      name: "BSB LAN"
      sw_version: "3.3.2"
    - state_topic: BSB-LAN/3113
      state_class: measurement
      unit_of_measurement: "kWh"
      device_class: energy
      friendly_name: Energie_totale_PAC
      manufacturer: Atlantic
      model: "Alfea AI"
      name: "BSB LAN"
      sw_version: "3.3.2"
    - state_topic: BSB-LAN/8451
      device_class: enum
      friendly_name: Compteur_demarrage_compresseur
      manufacturer: Atlantic
      model: "Alfea AI"
      name: "BSB LAN"
      sw_version: "3.3.2"
binary_sensors:
    - state_topic: BSB-LAN/8400
      payload_on: 255 - Marche
      payload_off: 0 - Arrêt
      friendly_name: Etat_PAC
      manufacturer: Atlantic
      model: "Alfea AI"
      name: "BSB LAN"
      sw_version: "3.3.2"
    - state_topic: BSB-LAN/8406
      payload_on: 255 - Marche
      payload_off: 0 - Arrêt
      friendly_name: Etat_condenseur
      manufacturer: Atlantic
      model: "Alfea AI"
      name: "BSB LAN"
      sw_version: "3.3.2"
select:
    - command_topic: BSB-LAN700
      state_topic: BSB-LAN/700
      friendly_name: Mode_fonctionnement
      options:
        - "0 - Mode protection"
        - "1 - Automatique"
        - "2 - Réduit"
        - "3 - confort"
      manufacturer: Atlantic
      model: "Alfea AI"
      name: "BSB LAN"
      sw_version: "3.3.2"
climate:
    - temperature_command_topic: BSB-LAN710
      temperature_state_topic: BSB-LAN/710
      mode_command_topic: BSB-LAN700
      mode_state_topic: BSB-LAN/700
      mode_state_template: "{{ 'heat' if value|string == 1 else 'off' }}"
      modes:
        - "0 - Mode protection"
        - "1 - Automatique"
        - "2 - Réduit"
        - "3 - confort"
      current_temperature_topic: BSB-LAN/8740
      friendly_name: Consigne_confort
      manufacturer: Atlantic
      model: "Alfea AI"
      name: "BSB LAN"
      sw_version: "3.3.2"
      max_temp: 25
      min_temp: 17
      temp_step: 0.5
switch:
    - command_topic: BSB-LAN5710
      state_topic: BSB-LAN/5710
      device_class: switch
      payload_on: 255 - Marche
      payload_off: 0 - Arrêt
      state_on: 255 - Marche
      state_off: 0 - Arrêt
      friendly_name: Circuit_chauffage
      manufacturer: Atlantic
      model: "Alfea AI"
      name: "BSB LAN"
      sw_version: "3.3.2"</blockquote>
Next:
- test other kind of devices
- docker
