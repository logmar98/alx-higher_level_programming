#!/bin/bash
# show allowed http methed
curl -sI $1 | grep Allow: | awk -F ': ' '{print $2}'