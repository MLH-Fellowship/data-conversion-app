#!/bin/bash

DEFAULT_DIRS=(
    "data/ceesim/schema/pattern"
    "data/ceesim/schema/simulation"
)

process_file () {
    echo "Now processing: $1"
    pyxbgen -u $1 -m $1
}

process_files_in_directory () {
    DIR_LISTING_SEARCH="$1/*"
    DIR_LISTING=$(ls -d $DIR_LISTING_SEARCH)
    while IFS=" " read -ra FILENAMES; do
        for file in "${FILENAMES[@]}"
        do
            process_file $file
        done
    done <<< $DIR_LISTING
}

if [ "$#" -ge 1 ]; then
    for folder in "$@";
    do
        process_files_in_directory $folder
    done
else
    for folder in ${DEFAULT_DIRS[@]};
    do
        process_files_in_directory $folder
    done
fi