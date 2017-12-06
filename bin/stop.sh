#!/bin/sh

# stop linux
ps -ef | grep 'src/__main__.py' | awk '{print $2}'| sed -n '1p'| xargs -I {} kill -9 {}