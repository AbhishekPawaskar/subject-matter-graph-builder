import os
from neo4j import GraphDatabase

graphdb_connection_string = os.environ.get('GRAPH_DB_CONN_STRING')
graphdb_username = os.environ.get('GRAPH_DB_USERNAME')
graphdb_password = os.environ.get('GRAPH_DB_PASSWORD')

class GraphDBConnection:

    _instance = None

    def __init__(self):
        if GraphDBConnection._instance is None:
            GraphDBConnection._instance = GraphDatabase.driver(graphdb_connection_string, auth=("",""))
        

    @staticmethod
    def get_driver():
        if GraphDBConnection._instance is None: 
            GraphDBConnection()
        return GraphDBConnection._instance