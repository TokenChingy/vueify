#!/bin/bash

if [ "$1" == "" ]; then
  echo "Usage: $0 -source"
  exit 1
fi

if [ -d "./dist" ]; then
  rm -rf ./dist
  mkdir ./dist
else
  mkdir ./dist
fi

python -m nuitka --show-progress --standalone --recurse-all --experimental=use_pefile --experimental=use_pefile_recurse --experimental=use_pefile_fullrecurse --include-package=bs4 --output-dir=./dist $1

d="$(sed 's/\(\.py\)//g' <<< $1)"

mv ./dist/$d.dist/* ./dist

rm -rf ./dist/$d.build
rm -rf ./dist/$d.dist