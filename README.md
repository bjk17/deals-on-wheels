# deals-on-wheels
"Deals on Wheels" POC for SPMM class at RU in November 2018

## Development

```bash
$ virtualenv venv
$ source venv/bin/activate
$ (venv) pip install -r requirements.txt

$ (venv) ./manage.py makemigrations dow
$ (venv) ./manage.py migrate
$ (venv) ./manage.py shell < init_db_with_mock_data.py
$ (venv) ./manage.py runserver
```

then head to <http://localhost:8000> for main site or <http://localhost:8000/admin> for admin interface.

### API endpoints

The following endpoints have been set up which may be of help in order to develop a nice from page:

* <http://localhost:8000/get/all/manufacturers>
* <http://localhost:8000/get/all/cars>
* <http://localhost:8000/get/all/advertisements>
