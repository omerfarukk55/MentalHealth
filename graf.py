import neo4j
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

uri = "neo4j://localhost:7687"
username = "neo4j"
password = "omerfaruk"

# Excel dosyası yolu
excel_file_path = "data.csv"
# Excel dosyasını okuma ve veritabanına yazma
# Veritabanına yazma işlemini başlatma
# Veritabanına yazma işlemini başlatma
def import_excel_to_neo4j(tx, data):
  """
  Excel dosyasındaki verileri Neo4j veritabanına aktarır.

  Parametreler:
    tx: Neo4j işleme nesnesi
    data: Pandas DataFrame nesnesi
  """

  for index, row in data.iterrows():
    # Node1 ve Node2 için MERGE sorguları
    tx.run("MERGE (node1:Node {name: $name1})", name1=row['Node1'])
    tx.run("MERGE (node2:Node {name: $name2})", name2=row['Node2'])

    # Node1 ve Node2 arasında RELATION ilişkisi oluşturma
    tx.run("MERGE (node1)-[:RELATION]->(node2)", name1=row['Node1'], name2=row['Node2'])

def read_excel_and_write_to_neo4j():
  """
  Excel dosyasını okur ve verileri Neo4j'e aktarır.
  """

  data = pd.read_excel(excel_file_path, engine='csv')
  driver = neo4j.GraphDatabase.driver(uri, auth=(username, password))

  with driver.session() as session:
    session.write_transaction(import_excel_to_neo4j, data)

def create_and_show_graph():
  """
  Neo4j'den veri alır ve grafı oluşturup gösterir.
  """

  driver = neo4j.GraphDatabase.driver(uri, auth=(username, password))

  with driver.session() as session:
    # Tüm ilişkileri içeren sorgu
    result = session.run("MATCH (n)-[r]->(m) RETURN n.name, r, m.name")

    graph_data = [(record["n.name"], record["m.name"], record["r"].type) for record in result]

  # Graf oluşturma
  graph = nx.DiGraph()
  for data in graph_data:
    graph.add_node(data[0])
    graph.add_node(data[1])
    graph.add_edge(data[0], data[1], label=data[2])

  # Pos ve labels değişkenlerini oluşturma
  pos = nx.spring_layout(graph)
  labels = nx.get_edge_attributes(graph, "label")

  # Grafı gösterme
  nx.draw(graph, pos, with_labels=True, node_size=1500, node_color="skyblue", font_size=10)
  nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
  plt.show()

# Verileri Neo4j'e aktar
read_excel_and_write_to_neo4j()

# Grafı oluştur ve göster
create_and_show_graph()
