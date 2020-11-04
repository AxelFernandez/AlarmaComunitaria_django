release: python manage.py migrate --run-syncdb --settings=alarma_comunitaria_site.settings.production
web: gunicorn alarma_comunitaria_site.wsgi --log-file -