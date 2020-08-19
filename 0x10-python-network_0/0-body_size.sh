#!/usr/bin/env bash
# cURL body size
curl -so /dev/null "$1" -w '%{size_download}\n'