#!/bin/bash
# Displays the size in bytes of the body of the response from the URL
curl -s "$1" | wc -c
