pip install -r requirements.txt
cp local_settings.py-dist local_settings.py
pyhton manage.py synchdb --migrate
python manage.py run_gunicorn -c gunicorn.conf.py


