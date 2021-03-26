#!/bin/bash
# to mount a directory from the local machine to the Docker container
# syntax:
# docker run -v /path/on/host:/path/on/container

# the file to run in the python environment
file=$1
docker run -v /home/christian/Documents/dock:/mnt/src \
    --rm \
    python \
    python /mnt/src/$file

    # capture the execution output somehow....
    # python3 /mnt/src/$file &> out.txt
