#!/bin/bash
cd ./.system/server/ && node server.js & xdg-open "http://127.0.0.1:8888/index" 
notify-send "Wiki at 127.0.0.1:8888"
