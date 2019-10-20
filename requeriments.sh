# configure scheduled task #
(crontab -l ; echo "@reboot sleep 60; python /home/assistant.task/src/assistant-alive.py &") | crontab -

# install python dependencies
sudo sh ./src/dependencies.sh