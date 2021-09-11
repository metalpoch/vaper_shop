# Vaper Shop

*An online vape store built on Django 3.2 and Python 3.8*
Register and buy your favorite vape in this virtual store simulator
![image](https://github.com/metalpoch/vaper_shop/blob/main/static/img/vaper_shop.gif?raw=true)

## Installation

##### Clone this repository [GitHub](https://github.com/metalpoch/Traffic-Access-Dashboard#)
```bash
git clone https://github.com/metalpoch/vaper_shop.git
cd vaper_shop/
```
##### Create a virtual environment
```Bash
virtualenv venv
source venv/bin/activate
```
or
```Bash
python -m venv venv
source venv/bin/activate
```

##### Use [pip](https://pip.pypa.io/en/stable/) to install the modules in the file requirements.txt 
```bash
pip install -r requirements.txt
```

## Use

##### Run server with sample database
```bash
python manage.py runserver
```

##### Run the server with a clean database
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser  # create a superuser
```

Articles need to be added manually from the Django admin site
![image](https://github.com/metalpoch/vaper_shop/blob/main/static/img/addProduct.png?raw=true)

## Licence
[MIT](https://choosealicense.com/licenses/mit/)
