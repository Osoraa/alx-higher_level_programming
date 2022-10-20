#!/bin/bash
# Displays body of response to query
res=$(curl -sw "%{response_code}" -o lmao "$1")

if (("$res" == 200)); then
    cat lmao
fi

rm lmao
