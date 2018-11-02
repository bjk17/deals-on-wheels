# deals-on-wheels
"Deals on Wheels" POC for SPMM class at RU in November 2018

## Development

```bash
$ virtualenv venv
$ source venv/bin/activate
$ (venv) pip install -r requirements.txt

$ (venv) ./manage.py migrate
$ (venv) ./manage.py runserver
```

then head to <http://localhost:8000> for main site or <http://localhost:8000/admin> for admin interface.
