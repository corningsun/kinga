#!/bin/sh

nohup stdbuf -oL python3 ../src/__main__.py >out.log 2>&1 &