git-greenseer
[![Build Status](https://travis-ci.org/ferzerkerx/git-greenseer.svg?branch=master)](https://travis-ci.org/ferzerkerx/git-greenseer)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=git-greenseer&metric=alert_status)](https://sonarcloud.io/dashboard/index/git-greenseer)

This repo is archived: use https://github.com/ferzerkerx/repo-stats as a replacement
------------------
Generates html report for a given git repository. Report shows:
- Contribution percentage by category. (shows a bar chart)
![alt tag](https://raw.githubusercontent.com/ferzerkerx/git-greenseer/master/screenshots/category_view.png)

- Contribution per developer for each category. (shows a pie chart)
![alt tag](https://raw.githubusercontent.com/ferzerkerx/git-greenseer/master/screenshots/dev_vew.png)

Dependencies:
-------------------
- Jinja2 framework
- Bootstrap.js
- Charts.js

How to use it:
-------------------
- Modify setup.py and change settings
- pip install -r requirements.txt
- python src/main/main.py /my/git/repo/path

How to run tests:
-------------------
- cd git-greenseer
- python -m unittest discover -s src -p '*_test.py'

How does it work:
----------------------
1. Obtains the list of files that are part of the git repository using: 
"git ls-files master ."
2. For each listed file it counts the lines for each contributor using this command:
"git blame HEAD --line-porcelain " + file_name + " | sed -n 's/^author //p' | sort | uniq -c | sort -rn"
3.Each file is assigned a category based on the path it has:
/category1/category2/category3/ when we run it to identify category1 it will generate statistics for that category

Known Issues:
------------
Some of the entries show something like  
79 Not Committed Yet
because of this:
http://stackoverflow.com/questions/4638500/git-blame-showing-no-history
SOLVED by adding HEAD to git blame

Backlog:
---------------
- Write more tests
- Add last date of commit per contributor per category
- Generate report per file (see old text report https://github.com/ferzerkerx/git-greenseer/commit/7452cfc4faf7482451f6a3fe8340d394a3dd5c59  print_stats_for_files_in_dir)
- Add cache
- Add a way to compare between branches
