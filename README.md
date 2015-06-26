# gitOverseer
For a given git repository it calculates the contribution percentage by file and directory

Run tests with:
cd gitOverseer
python -m unittest discover -s src -p '*_test.py'

Run like:
python src/main/main.py ~/dev/repos/dev/adt-common/src/main/java/com/ezrez/adtcommon/coreapi/services


Known Issues:
------------
Some of the entries show somehting like  
79 Not Committed Yet
because of this:
http://stackoverflow.com/questions/4638500/git-blame-showing-no-history
SOLVED by adding HEAD to git blame
----------