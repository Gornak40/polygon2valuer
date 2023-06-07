# polygon2valuer
Simple tool for converting polygon tests to valuer.cfg (ejudge format). 

It works only when groups are ordered and each test belongs to only one group.

It supports EACH_TEST and COMPLETE_GROUP score policies, dependencies and ignores feedback policy.

### Install
1. Run ```python -m venv venv```.
2. Run ```source venv/bin/activate```.
3. Run ```pip install -r requirements.txt```.

### Usage

1. Click tests in your Polygon problem.
2. Press ```Ctrl+Shift+I```.
3. Copy ```<body>``` section or any other which contains ```#testGroupsTable```.
4. Run tool and paste copied html to stdin.
5. Press ```Ctrl+D```.
6. Congratulations!

## Autoscoring

1. Run ```python pol2val.py -s```.
2. You will get ```scoring.tex``` with template for problem scoring.
