Asif Imran's Personal Website
* Author: Asif Imran
* License: BSD 3-clause

####How to publish to github user page from scratch
```
(master) git init
(master) git checkout -b source
(source) git add .
(source) git commit -m “initial commit of the source tree”
(source) git remote add origin git@github.com:aimran/aimran.github.io.git
(source) git push origin source
(source) git checkout —orphan master
(master) git rm -rf .
(master) git merge -s ours --no-commit origin/source
(master) git read-tree -m -u source:output
(master) git commit -m "Merge output folder from branch source"
(master) git push --all
```

####To do regular update using the output tree
```
(source) pelican content -o output -s pelicanconf.py
(source) git checkout master
(master) git pull --no-edit -s subtree origin source
```

