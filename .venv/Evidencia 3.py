from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor
from counterfit_shims_grove.grove_led import GroveLed
import paho.mqtt.client as mqtt
import json
import time

CounterFitConnection.init("localhost",5000)

sensor_de_luz = GroveLightSensor(0)
print(f"El Nivel de luz es:{sensor_de_luz.light}")
faro_led = GroveLed(1)

#MQTT
id = "25883d4a-f67e-4ec5-af3e-d2b9257cc3be"
nombre_cliente = id + "LuzAutomatica"
mqtt_cliente = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1,nombre_cliente)
mqtt_cliente.connect("test.mosquitto.org")
mqtt_cliente.loop_start()
if mqtt_cliente.is_connected:
    print("Conectado al servidor")
else:
    print("Hubo un problema al conectarse")

cliente_telemetria_topico = id + "/telemetry"
#Para que se ejecute siempre
while True:
    lumenes_sensor1 = sensor_de_luz.light
    telemetria = json.dumps({"Luz" : lumenes_sensor1})
    print(f"Enviando valor del sensor de luz 1: {telemetria}")
    mqtt_cliente.publish(cliente_telemetria_topico,telemetria)    
    time.sleep(5)