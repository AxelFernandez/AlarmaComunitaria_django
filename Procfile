release: python manage.py migrate --run-syncdb --settings=alarma_comunitaria.settings.production
web: gunicorn deliveryLavalle_site.wsgi --log-file -