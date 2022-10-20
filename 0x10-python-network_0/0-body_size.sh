#!/bin/bash
# Displays the size of the body of a response from a given URL
curl -sI "$1" | grep Content-Length | cut -d : -f 2 | tr -d "[:space:]"; echo
