# configure scheduled task #
(crontab -l ; echo "@reboot python ./src/assistant-alive.py &") | crontab -

# install python dependencies
sudo sh ./src/dependencies.sh