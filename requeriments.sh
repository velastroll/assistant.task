# configure scheduled task #
echo "@reboot sudo python ./src/assistant-live.py &" >> mycron
crontab mycron
rm mycron

# install python dependencies
sh ./src/dependencies.sh