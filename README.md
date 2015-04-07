## APT Final project - SDU Disqus Backend

### Installation

```
virtualenv disqus
. disqus/bin/activate
mkdir -p disqus/src
cd disqus/src
git clone <project repo> disqus_be
pip install -r requirements-base.txt
pip install -r requirements-devel.txt
./manage.py syncdb
```

### Running tests

```
coverage run ./manage.py test -- -vvv -F && coverage report
```
