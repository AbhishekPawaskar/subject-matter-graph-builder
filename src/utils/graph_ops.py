from src.connector.graph_db_connector import GraphDBConnection


def transform_text(text:str):
    return text.replace(" ",'_').upper()

class GraphOps:
    def __init__(self):
        self.driver_connection = GraphDBConnection

    def upload_nodes(self, name:str):
        with self.driver_connection as session:
            session.verify_connectivity()
            records, summary, keys = session.execute_query("CREATE (n:Node {name: $name}) RETURN n;",
                                                           name=name,
                                                           database_="memgraph",)
        return True
    
    def upload_edges(self, fromEntity:str, toEntity:str, relation:str):
        statement = "MATCH (f:Node {name:'"+fromEntity+"'}), (t:Node {name:'"+toEntity+"'}) CREATE (f)-[r:"+relation+"]->(t) RETURN f,r,t;"
        with self.driver_connection as session:
            session.verify_connectivity()
            records, summary, keys = session.execute_query(statement,
                                                           database_="memgraph",)
        return True
    
    def nodes_exists(self, name:str):
        with self.driver_connection as session:
            session.verify_connectivity()
            records, summary, keys = session.execute_query("MATCH (n:Node {name: $name}) RETURN n;",
                                                           name=name,
                                                           database_="memgraph",)
            if len(records)==0:
                return False
            else:
                return True
    
    def full_upload(self, graph_data_dict:dict):
        edge_list = graph_data_dict['relation']
        for edge in edge_list:
            fromEntity = transform_text(edge['fromEntity'])
            toEntity = transform_text(edge['toEntity'])
            relation = transform_text(edge['relationship'])
            from_ack = self.nodes_exists(name=fromEntity)
            to_ack = self.nodes_exists(name=toEntity)
            if from_ack==False:
                from_ack=self.upload_nodes(fromEntity)
            if to_ack==False:
                to_ack=self.upload_nodes(toEntity)
            if from_ack & to_ack:
                edge_ack = self.upload_edges(fromEntity=fromEntity,toEntity=toEntity,relation=relation)
        return True

        

