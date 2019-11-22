# configure scheduled task #
(crontab -l ; echo "@reboot sleep 60; cd /home/pi/assistant.task/src/ ; python /home/pi/assistant.task/src/assistant-alive.py & > home/pi/assistant.task/src/cache/logfile.txt") | crontab -

# install python dependencies
sudo sh ./src/dependencies.sh
