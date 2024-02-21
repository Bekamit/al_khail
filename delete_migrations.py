import os
# from apps.users.models import *
from django.core.management import call_command


apps = ['admin_app', 'analytics', 'city', 'company', 'estate', 'project', 'staticdata']

sql_file = './db.sqlite3'

for app in apps:
    migration_path = f'./apps/{app}/migrations/'

    for filename in os.listdir(migration_path):
        if filename.endswith('.py') and filename != '__init__.py':
            migration_file = os.path.join(migration_path, filename)
            os.remove(migration_file)
            if os.path.isdir(sql_file):
                os.remove(sql_file)
