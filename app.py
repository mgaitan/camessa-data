from a2wsgi import ASGIMiddleware
from datasette.app import Datasette

ds = Datasette(["oferta_grupos.sqlite"], metadata="metadata.yaml")
application = ASGIMiddleware(ds.app())
