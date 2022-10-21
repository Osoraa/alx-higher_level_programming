#!/bin/bash
# Get the methods available on a url
curl -sIX OPTIONS "$1" | grep Allow | tail -c +8
