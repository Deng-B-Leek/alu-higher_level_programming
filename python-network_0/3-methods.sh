#!/bin/bash
curl -s -i -X OPTIONS "$1" | grep -i "^Allow:" | cut -d " " -f2- | tr -d '\r'
