web: python manage.py makemigrations && python manage.py migrate && (python manage.py createsuperuser --noinput) || echo "Cannot create admin user" && gunicorn WelbeX_test.wsgi --log-file -
