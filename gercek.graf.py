from py2neo import Graph, Node, Relationship
import json

# JSON verisini oku
with open('guncellenmis.json', 'r') as f:
    json_data = json.load(f)

# Neo4j bağlantısı oluştur
graph = Graph("neo4j+s://36a5aa75.databases.neo4j.io", auth=("neo4j", "6xYJUrgdXITl5gNMuAj9BcXaO0xXqNIf9qygl5iwaXs"))

# Her özellik için düğümleri oluştur
properties = ["Meslek", "Kendi işinde çalışıyor mu", "Aile Geçmişi", "Tedavi Gördü mü", "evde geçirdiği süre","Artan Stres mücadele", "Alışkanlıklarını Değiştirme", "Mental Sağlık Geçmişi", "Ruhsal Dalgalanma", "Başa Çıkma Güçlüğü", "İş İlgisi", "Sosyal Zayıflık"]
        
for prop in properties:
    prop_node = Node(prop)
    graph.create(prop_node)

# Her bir kayıt için insan düğümünü ve ilgili özellik düğümlerini ilişkilendirme
for record in json_data:
    insan_node = Node("insan",zaman=record["Zaman"],cinsiyet=record["Cinsiyet"],yaşadığı_şehir=record["Ülke"])
    graph.create(insan_node)
    
    # Her özelliği kontrol et ve ilgili özellik düğümüne ilişkilendir
    for prop in properties:
        prop_value = record[prop]
        prop_node = graph.nodes.match(prop).first()
        if prop_value == "Yes":
            relation = Relationship(insan_node, "sahip", prop_node)
            graph.create(relation)
        elif prop_value == "No":
            relation = Relationship(insan_node, "sahip değil", prop_node)
            graph.create(relation)
        elif prop_value == "Maybe":
            relation = Relationship(insan_node, "kararsız", prop_node)
            graph.create(relation)

print("İnsanlar ve özellikler arasında ilişkiler oluşturuldu.")
