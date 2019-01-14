#!/bin/bash

# write out current crontab
crontab -l > mycron
#echo new cron into cron file
echo '20 06 * * * /home/pi/alarm_triggers_youtube/alarm_triggers_youtube.py' >> mycron
#install new cron file
crontab mycron
rm mycron
