#!/bin/bash
#-Sends a JSONPOST request to a URL,displays the body of the response.
curl -s -H "Content-Type: application/json" -d @"$2"" "$1"
