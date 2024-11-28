#!/usr/bin/bash

while true; do
  res=$(curl -s "https://hack.arrrg.de/chal/orakel" -H "cookie: htw_language_preference=en")
  
  if [[ "$res" != *"Try again later."* ]]; then
    echo "$res" >> "output"
    echo "response recorded at $(date)" >> "output"
    break
  fi

  sleep 840
done
