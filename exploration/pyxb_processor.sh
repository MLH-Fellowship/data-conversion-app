#!/bin/bash

DEFAULT_DIRS=(
    'data/ceesim/schema/pattern'
    'data/ceesim/schema/simulation'
)

process_files_in_directory () {
    echo $0
}

if [ "$#" -ne 1 ]; then
    for folder in "$@"
    do
        process_files_in_directory folder
    done
else
    for folder in DEFAULT_DIRS
    do
        process_files_in_directory folder
    done
fi