1. Create a virtual environment
```
mkvirtualenv hopeline

```
2. Install required python libraries
```
pip install -r requirements.txt
```
3. Test decision logic
```
python test.py
```

for anaconda users:
1. Create a virtual environment
```
conda create -n hopeline_env python=3 python

```
2. Install required python libraries
```
conda install pip
pip install -r requirements.txt
```
3. Test decision logic
```
python test.py
```
4. Exit test.py
```
ctrl-z
```
### Notes about deployment
Followed example from https://github.com/zachwill/flask_heroku
