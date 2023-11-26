from django.core.management.base import BaseCommand
from django.utils import timezone
import paho.mqtt.client as mqtt
import os, time, json
from dotenv import load_dotenv, dotenv_values
import logging as log
from dashboard.models import kost_member, user_member

load_dotenv()

class Command(BaseCommand):
    help = 'Displays current time'

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.mqtt_message = None
        
    def on_message(self, client, userdata, msg):
        print(f"Terima pesan: {msg.payload} pada topik {msg.topic}")
        try:
            # Mendekode nilai JSON dari payload pesan
            payload_dict = json.loads(msg.payload.decode('utf-8').replace("'", "\""))

            # Simpan nilai JSON ke dalam atribut kelas
            self.mqtt_message = payload_dict
        except (UnicodeDecodeError, json.JSONDecodeError) as e:
            print(f"Error decoding/parsing message: {e}")

    def handle(self, *args, **kwargs):
        mqtt_broker_url = os.getenv('MQTT_BROKER_URL')
        mqtt_port = 1883
        mqtt_keepalive = os.getenv('MQTT_KEEPALIVE')

        # mqtt connect
        client = mqtt.Client()
        client.on_message = self.on_message
        client.connect(mqtt_broker_url, int(mqtt_port), int(mqtt_keepalive))

        # Inisialisasi dictionary untuk menyimpan hasil gabungan
        joined = {}

        while True:
            
            data_kost_member = kost_member.objects.all()
            data_user_member = user_member.objects.all()

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
            topic_mqtt_pub = 'ibukost/door/'
            topic_mqtt_sub = 'ibukost/server/house'
            client.subscribe(topic_mqtt_sub)
            
            mqtt_sub = self.mqtt_message
            
            if mqtt_sub is not None:
                found_data = None
                for key, data in joined.items():
                    if (
                        data['unique_id'] == mqtt_sub.get('unique_id') and
                        str(data['tag_id']) == str(mqtt_sub.get('rfid')) and
                        data['status'] == 'open'
                    ):
                        found_data = data
                        break

                if found_data:
                    self.stdout.write(self.style.SUCCESS(f"- username : {found_data['username']}\n- rfid : {found_data['tag_id']}"))
                    client.publish(topic_mqtt_pub + str(found_data['unique_id']), "0")
                    self.mqtt_message = None
                else:
                    self.stdout.write(self.style.ERROR_OUTPUT(f"{mqtt_sub.get('rfid')} Data not found"))
                    self.mqtt_message = None
            else:
                # self.stdout.write(self.style.HTTP_BAD_REQUEST("decoding/parsing message"))
                pass
            
            client.loop_start()
            time.sleep(1)
            client.loop_stop()
