from django.core.management.base import BaseCommand
from django.utils import timezone
import paho.mqtt.client as mqtt
import os, time
from dotenv import load_dotenv, dotenv_values
import logging as log
from dashboard.models import kost_member, user_member

load_dotenv()

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        mqtt_broker_url = os.getenv('MQTT_BROKER_URL')
        mqtt_port = 1883
        mqtt_keepalive = os.getenv('MQTT_KEEPALIVE')

        while True:
            # mqtt connect
            client = mqtt.Client()
            client.connect(mqtt_broker_url, int(mqtt_port), int(mqtt_keepalive))

            data_kost_member = kost_member.objects.all()
            data_user_member = user_member.objects.all()

            # Inisialisasi dictionary untuk menyimpan hasil gabungan
            joined = {}

            # Gabungkan data berdasarkan field unique_id
            for item_kost_member in data_kost_member:
                items_user_member = data_user_member.filter(unique_id=item_kost_member.unique_id)
                for item_user_member in items_user_member:
                    # Kunci unik berdasarkan kombinasi nama_kost dan username
                    key = f'{item_kost_member.nama_kost}_{item_user_member.username}'

                    # Jika data ditemukan, gabungkan dan tambahkan ke joined
                    if key not in joined:
                        joined[key] = {
                            'nama_kost': item_kost_member.nama_kost,
                            'unique_id': item_kost_member.unique_id,
                            'nomor_kost': item_kost_member.nomor_kost,
                            'status': item_kost_member.status,
                            'username': item_user_member.username,
                            'tag_id': item_user_member.tag_id,
                            'telepon': item_user_member.telepon,
                            'alamat': item_user_member.alamat,
                        }

            # Tampilkan hasil atau lakukan operasi lain sesuai kebutuhan
            topic_mqtt = 'ibukost/door/'
            sub = client.subscribe(topic_mqtt+'900')
            print(sub)
            
            id = 8890
            rfid = 227177105168
            mqtt_sub = {
                'uniqe_id': id,
                'rfid' : rfid,
            }

            for key, data in joined.items():
                mqtt_pub = {
                    'uniqe_id': data['unique_id'],
                    'rfid' : data['tag_id'],
                    'status' : data['status'],
                }
                if data['unique_id'] == mqtt_sub['uniqe_id'] and data['tag_id'] == mqtt_sub['rfid'] and data['status'] == 'open':
                    self.stdout.write(self.style.SUCCESS(f"{data['username']} {data['status']}"))
                    client.publish(topic_mqtt + str(data['unique_id']), payload=str(mqtt_pub))

                    # Tunggu beberapa saat sebelum memulai iterasi berikutnya
                    # Atau sesuaikan dengan kebutuhan
                    client.loop_stop()
                    client.disconnect()
                    break

            time.sleep(1)
