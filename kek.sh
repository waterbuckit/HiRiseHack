#/bin/bash

IMAGEFILE=$1

python extractirb.py $IMAGEFILE

mkdir tmp/blended
rm tmp/blended/*.jpg

./gifblender.sh -o tmp/blended -s 5 tmp/*.jpg

echo $(basename "$IMAGEFILE")
convert tmp/blended/*.jpg gif:- | gifsicle -d 1 -l > results/$(basename "$IMAGEFILE").gif
