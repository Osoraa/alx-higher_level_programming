#!/bin/bash
# Displays the size of the body of a response from a given URL

# Curl the link, silent, only headers, grep Content-legth
# cut and return the actual number, remove white space
curl -sI "$1" | grep Content-Length | cut -d : -f 2 | tr -d "[:space:]"

# Carriage return
echo
