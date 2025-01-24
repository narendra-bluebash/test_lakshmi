#!/bin/bash

# unset http proxy which maybe set by docker daemon
export http_proxy=""; export https_proxy=""; export no_proxy=""; export HTTP_PROXY=""; export HTTPS_PROXY=""; export NO_PROXY=""

/usr/sbin/nginx

export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/

PY=python3

while [ 1 -eq 1 ];do
    $PY uvicorn app:app --host 0.0.0.0 --port 8000
done

wait;