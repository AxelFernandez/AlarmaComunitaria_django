release: python manage.py migrate --run-syncdb --settings=alarma_comunitaria.settings.production
web: gunicorn alarma_comunitaria_site.wsgi --log-file -