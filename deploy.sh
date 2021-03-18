#!/usr/bin/env sh

set -e
cd website
yarn run build
cd dist
git init
git add -A
git commit -m "Deploy"
git push -f https://github.com/sorenmulli/adpocalypse.git master:gh-pages
cd ..
cd ..

