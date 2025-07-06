from fastapi import FastAPI
from ariadne import load_schema_from_path, make_executable_schema, QueryType
from ariadne.asgi import GraphQL
from .resolvers import mutation

query = QueryType()
query.set_field("_empty", lambda *_: "ok")

type_defs = load_schema_from_path("app/schema.graphql")
schema = make_executable_schema(type_defs, [query, mutation])

app = FastAPI()
graphql_app = GraphQL(schema, context_value=lambda request: {"request": request})
app.mount("/", graphql_app)
