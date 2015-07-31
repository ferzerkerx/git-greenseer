git-greenseer
------------------
Generates html report for a given git repository. Report shows:
- Contribution percentage by category. (shows a bar chart)
- Contribution per developer for each category. (shows a pie chart)

Dependencies:
-------------------
- Jinja2 framework
- Bootstrap.js
- Charts.js

How to use it:
-------------------
- Modify setup.py and change settings
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
----------