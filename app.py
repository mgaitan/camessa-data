# app.py
from datasette.app import Datasette
from asgiref.wsgi import ASGItoWSGI

ds = Datasette(["oferta_grupos.sqlite"], metadata="metadata.yaml")

# Adaptar ASGI -> WSGI para PythonAnywhere
application = ASGItoWSGI(ds.app())
