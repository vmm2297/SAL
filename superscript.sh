#!/bin/sh
sudo /var/www/html/PiBits/ServoBlaster/user/servod --cycle-time=2550 --min=0 --max=255
echo 1=100% > /dev/servoblaster
echo 3=100% > /dev/servoblaster
echo 4=100% > /dev/servoblaster
python /home/mnv/assistant-sdk-python/google-assistant-sdk/googlesamples/assistant/library/hotword.py --device_model_id smart-ambilamp-v1
sudo python /var/www/html/sensors/readSensors.py &
