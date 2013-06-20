pip install -r requirements.txt
cp local_settings.py-dist local_settings.py
python manage.py syncdb --migrate --noinput
python manage.py run_gunicorn -c gunicorn.conf.py
