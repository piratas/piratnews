import os

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

bind = "127.0.0.1:%(gunicorn_port)s"
workers = (os.sysconf("SC_NPROCESSORS_ONLN") * 2) + 1
loglevel = "error"
proc_name = "%(project_name)s"
