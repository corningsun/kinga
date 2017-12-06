#!/bin/sh

# stop mac
ps -A | grep 'src/__main__.py' | awk '{print $1}'| sed -n '1p'| xargs -I {} kill -9 {}