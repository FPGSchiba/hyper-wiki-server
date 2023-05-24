from ariadne import QueryType, graphql_sync, make_executable_schema, load_schema_from_path, ObjectType, MutationType
from ariadne.explorer import ExplorerGraphiQL
from flask import Flask, jsonify, request
from ..util.config import Config

CONF = Config()
type_defs = load_schema_from_path(CONF.graph_schema)

query = QueryType()


@query.field("page")
def resolve_page(*_, id=None, location=None):
    if id is not None and location is None:
        return {"id": id, "location": "somersetting", "versions": [{"id": "id1", "name": "name1", "version": 0},
                                                                   {"id": "id2", "name": "name2", "version": 1}]}
    if location is not None and id is None:
        return {"id": "testing", "location": location, "versions": [{"id": "id1", "name": "name1", "version": 0},
                                                                    {"id": "id2", "name": "name2", "version": 1}]}
    if id is not None and location is not None:
        return {"id": id, "location": location, "versions": [{"id": "id1", "name": "name1", "version": 0},
                                                             {"id": "id2", "name": "name2", "version": 1}]}
    return {"id": "testing", "location": "somersetting",
            "versions": [{"id": "id1", "name": "name1", "version": 0}, {"id": "id2", "name": "name2", "version": 1}]}


@query.field("pages")
def resolve_pages(*_, id=None, location=None):
    return [{"id": "testing", "location": "somersetting",
             "versions": [{"id": "id1", "name": "name1", "version": 0}, {"id": "id2", "name": "name2", "version": 1}]},
            {"id": "testing2", "location": "somersetting",
             "versions": [{"id": "id1", "name": "name1", "version": 0}, {"id": "id2", "name": "name2", "version": 1}]}]


mutation = MutationType()

schema = make_executable_schema(type_defs, query, mutation)

app = Flask(__name__)

# Retrieve HTML for the GraphiQL.
# If explorer implements logic dependant on current request,
# change the html(None) call to the html(request)
# and move this line to the graphql_explorer function.
explorer_html = ExplorerGraphiQL().html(None)


@app.route("/", methods=["GET"])
def graphql_explorer():
    # On GET request serve the GraphQL explorer.
    # You don't have to provide the explorer if you don't want to
    # but keep on mind this will not prohibit clients from
    # exploring your API using desktop GraphQL explorer app.
    return explorer_html, 200


@app.route("/", methods=["POST"])
def graphql_server():
    # GraphQL queries are always sent as POST
    data = request.get_json()

    # Note: Passing the request to the context is optional.
    # In Flask, the current request is always accessible as flask.request
    success, result = graphql_sync(
        schema,
        data,
        context_value={"request": request},
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code
