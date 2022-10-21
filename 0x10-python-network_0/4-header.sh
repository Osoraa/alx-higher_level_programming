#!/bin/bash
# Get the methods available on a url
curl -sH "X-School-User-Id: 98" "$1" #| grep Allow | tail -c +8
