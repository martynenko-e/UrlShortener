#!/usr/bin/env bash

if [ "$1" == "-b" ]; then
    docker build -t django11 .
fi

SRC_VOLUME="/Users/yevhenmartynenko/_projects/shrt_mrtn/src"

docker run -d -p 9000:8000 --name urlshort -v $SRC_VOLUME:/src django11
#docker exec -it blog_site main-admin startproject main