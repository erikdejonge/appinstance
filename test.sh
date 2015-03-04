#!/usr/bin/env bash
python app1.py &
sleep 0.1
# app 2 should start, has different parameters
python app2.py & 
sleep 0.1
# not allowed to start, already running
python app1.py &
sleep 0.1
python app2.py &

wait