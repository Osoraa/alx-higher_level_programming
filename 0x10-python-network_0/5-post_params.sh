#!/bin/bash
# Sends a POST request to a url and displays the body
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1"
