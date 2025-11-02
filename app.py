from datasette.app import Datasette
import asyncio

# Initialize Datasette with your DB and metadata
ds = Datasette(["oferta_grupos.sqlite"], metadata="metadata.yaml")

# Expose WSGI application
application = asyncio.get_event_loop().run_until_complete(ds.app())
