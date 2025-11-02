# app.py
from datasette.app import Datasette
from asgiref.wsgi import AsgiToWsgi

# Inicializá Datasette con tu DB y metadata
ds = Datasette(["oferta_grupos.sqlite"], metadata="metadata.yaml")

# ds.app() devuelve una app ASGI -> adaptamos a WSGI para PythonAnywhere
application = AsgiToWsgi(ds.app())
