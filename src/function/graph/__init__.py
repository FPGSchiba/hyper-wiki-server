from ariadne import QueryType, graphql_sync, make_executable_schema, load_schema_from_path, ObjectType, MutationType
from ariadne.explorer import ExplorerGraphiQL
from flask import Flask, jsonify, request
from ..util.config import Config
from .query import *
from .mutation_delete import *
from .mutation_create import *
from .mutation_update import *

CONF = Config()
type_defs = load_schema_from_path(CONF.graph_schema)

# Query definition
query = QueryType()

# page resolvers
query.set_field('page', resolve_page)
query.set_field('pages', resolve_pages)

# page version resolvers
query.set_field('pageVersion', resolve_page_version)
query.set_field('pageVersions', resolve_page_versions)

# folder resolvers
query.set_field('folder', resolve_folder)
query.set_field('folders', resolve_folders)

# notebook resolvers
query.set_field('notebook', resolve_notebook)
query.set_field('notebooks', resolve_notebooks)

# graph resolver
query.set_field('graph', resolve_graph)

# node resolvers
query.set_field('node', resolve_node)
query.set_field('nodes', resolve_nodes)

# edge resolvers
query.set_field('edge', resolve_edge)
query.set_field('edges', resolve_edges)

# Mutation definition
mutation = MutationType()

# Delete Mutations
mutation.set_field('deletePage', delete_page)
mutation.set_field('deleteFolder', delete_folder)
mutation.set_field('deleteNotebook', delete_notebook)
mutation.set_field('deletePageVersion', delete_page_version)

# Create Mutations
mutation.set_field('createPage', create_page)
mutation.set_field('createFolder', create_folder)
mutation.set_field('createNotebook', create_notebook)
mutation.set_field('createPageVersion', create_page_version)

# Update Mutations
mutation.set_field('updatePage', update_page)
mutation.set_field('updateFolder', update_folder)
mutation.set_field('updateNotebook', update_notebook)
mutation.set_field('updatePageVersion', update_page_version)

# Schema & App definition
schema = make_executable_schema(type_defs, query, mutation)

app = Flask('HYPER-WIKI-GRAPHQL')
app.debug = True

# Explorer definition
explorer_html = ExplorerGraphiQL().html(None)


@app.route("/", methods=["GET"])
def graphql_explorer():
    return explorer_html, 200


@app.route("/", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value={"request": request},
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code
