#!/bin/bash

MY_IP_SCRIPT="myip.py"

echo "Init rpi0 - $(date)"

echo "Start notificator-api:"
pm2 resurrect
pm2 start notificator-api
sleep 5

echo "Send my ip:"
python $MY_IP_SCRIPT

exit