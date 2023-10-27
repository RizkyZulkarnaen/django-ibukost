from django.core.management.base import BaseCommand
from django.utils import timezone
import paho.mqtt.client as mqtt
import os
from dotenv import load_dotenv, dotenv_values
import logging as log

load_dotenv()

class Command(BaseCommand):
    help = 'Displays current time'
    def handle(self, *args, **kwargs):
        
        mqtt_broker = os.getenv('MQTT_BROKER_URL')
        mqtt_port = os.getenv('MQTT_BROKER_PORT')
        mqtt_keepalive = os.getenv('MQTT_KEEPALIVE')
        
        client = mqtt.Client()
        client.connect(mqtt_broker, int(mqtt_port), int(mqtt_keepalive))