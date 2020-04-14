# Github Automation Scripts

This repository has code for three tasks:
1. Viewing a repository on the browser
2. Creating a local and online repository via terminal
3. Automatically generate basic README.md for specified repository

## Requirements:

``` pip install selenium pygithub ```

Also, you will need to download the chrome webdriver for your version of the browser and place it in the drivers directory (replace existing)
You can download it from, https://chromedriver.chromium.org/downloads

### Setup
1. Enter username and password in automate.py and create.py
2. Add absolute path for webdriver in automate.py
3. Add absolute path wherever specified in my_commands.sh
4. Add github username in my_commands.sh wherever specified.
5. Move ```github-automation``` repo to root directory
6. Copy my_commands.sh into root directory from ```github-automation```
7. Run ```echo -e "source ~/my_commands.sh" >> ~/.bashrc``` in terminal
8. Restart terminal to see it in effect.


### To Run
1. ```gcreate REPO_NAME```
2. ```gshow USER_NAME REPO_NAME```
3. ```greadme REPO_NAME```

