#!/bin/bash

function gshow() {
    cd 
    python ~/github-automation/automate.py $1 $2
}

function gcreate() {
    username=$(head -n 1 ~/github-automation/credentials.txt)
    directory=$(pwd)
    cd
    python github-automation/create.py $1
    mkdir $directory/$1
    cd $directory/$1
    touch README.md
    git init
    git remote add origin https://github.com/$username/$1.git  # Edit {Username to your username}
    git add -A
    git commit -m "Initial Commit"
    git push origin master
    code .
}

function greadme() {
    directory=$(pwd)
    cp ~/github-automation/readme.py $directory
    python readme.py
    git add README.md
    git commit -m "Add auto-generated README.md"
    git push origin master
    rm readme.py
}