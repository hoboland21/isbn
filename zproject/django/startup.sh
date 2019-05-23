
if [ ! -d "isbn" ] ;then
/usr/local/bin/python /usr/local/bin/django-admin  startproject isbn 
fi
cd isbn
./manage.py makemigrations --noinput
./manage.py  migrate
gunicorn --workers=2 --bind=0:8000  isbn.wsgi
