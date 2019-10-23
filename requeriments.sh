# configure scheduled task #
(crontab -l ; echo "@reboot sleep 60; cd /home/pi/assistant.task/src/ ; /usr/bin/python /home/pi/assistant.task/src/assistant-alive.py & > logfile.txt") | crontab -

# install python dependencies
sudo sh ./src/dependencies.sh