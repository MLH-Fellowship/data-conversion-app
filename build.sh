#!/bin/bash

# Hermes build script. Battle tested on Ubuntu 18, Ubuntu 20, and Arch Linux
# 2021. Written by Gideon Tong. Run on Linux. Needs zip and other standard
# utilities in PATH.

STAGING_NAME='build-staging'

echo "Removing old build folder $STAGING_NAME"
rm -rf $STAGING_NAME
DATE=`date +"%Y-%m%d-%H%M%S"`
echo "Beginning new build with ID of $DATE"
mkdir $STAGING_NAME

echo 'Copying Python module'
mkdir "$STAGING_NAME/app"
find app/* -type d -exec mkdir "$STAGING_NAME/{}" \;
find app/*.py app/*/*.py -type f -exec cp '{}' "$STAGING_NAME/{}" \;

echo 'Copying data and entrypoint'
mkdir "$STAGING_NAME/data"
find data/*.* -exec cp '{}' "$STAGING_NAME/{}" \;
cp app.py "$STAGING_NAME"

echo 'Creating build zip'
cd "$STAGING_NAME"
zip -r -D "../build-$DATE.zip" *
cd ..

echo "Created build zip at build-$DATE.zip"
rm -rf $STAGING_NAME
