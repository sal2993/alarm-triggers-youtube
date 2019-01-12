#!/bin/bash

# write out current crontab
crontab -l > mycron
#echo new cron into cron file
echo "30 12 * * * pi /home/pi/alarm_triggers_youtube/test_crontab.py" >> mycron
#install new cron file
crontab mycron
rm mycron
