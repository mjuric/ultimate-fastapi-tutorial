#!/bin/bash

rm result.*
for i in $(seq 1 20); do 
	curl --silent -X 'POST' \
	  'http://34.127.39.101/precovery/singleorbit' \
	  -H 'accept: application/json' \
	  -H 'Content-Type: application/json' \
	  -d '{
	  "orbit_type": "car",
	  "x": 3.1814935923872047,
	  "y": -1.7818842866371896,
	  "z": 0.5413047375097928,
	  "vx": 0.003965128676498027,
	  "vy": 0.006179760229698789,
	  "vz": 0.003739659079259056,
	  "mjd_tdb": 56534.00089159205
	  }' > result.$i &
done
wait
