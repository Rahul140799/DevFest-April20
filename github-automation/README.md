# Github Automation Scripts

This repository has code for three tasks:
1. Viewing a repository on the browser
2. Creating a local and online repository via terminal
3. Automatically generate basic README.md for specified repository

## Requirements:

``` pip install -r requirements.txt```

Also, you will need to download the chrome webdriver for your version of the browser and place it in the drivers directory (replace existing)
You can download it [here](https://chromedriver.chromium.org/downloads)

### Setup
1. Enter username and password in credentials.txt in line 1 and line 2 respectively.
2. Add downloaded chromedriver to the drivers folder
3. Move ```github-automation``` repo to root directory
4. Run ```echo -e "source ~/github-automation/my_commands.sh" >> ~/.bashrc``` in terminal
5. Restart terminal to see it in effect.


### To Run
1. ```gcreate REPO_NAME```
2. ```gshow USER_NAME REPO_NAME``` (for third party repos)
3. ```gopen REPO_NAME``` (for personal repos)
4. ```greadme REPO_NAME```

