#!/bin/bash

function gshow() {
    cd 
    python3 github-automation/automate.py $1 $2
}

function gcreate() {
    cd
    python3 github-automation/create.py $1
    mkdir /home/{}/{}/$1   #   - Specify the path where you want to create the project folders
    cd /home/{}/{}/$1     #   - Specify the path where you want to create the project folders
    touch README.md
    git init
    git remote add origin https://github.com/{GIT_USERNAME}/$1.git  # Edit {Username to your username}
    git add -A
    git commit -m "Initial Commit"
    git push origin master
    code .
}

function greadme() {
    cp /home/{}/github-automation/readme.py /home/{}/{}/$1 # Add [github-automation repo path] followed by [project directory]
    cd /home/{}/{}/$1 # Add project directory
    python3 readme.py
    git add README.md
    git commit -m "Add auto-generated README.md"
    git push origin master
    rm readme.py
}