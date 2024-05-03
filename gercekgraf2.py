from py2neo import Graph, Node, Relationship
import json

# JSON verisini oku
with open('guncellenmis.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

# Neo4j bağlantısı oluştur
graph = Graph("neo4j+s://36a5aa75.databases.neo4j.io", auth=("neo4j", "6xYJUrgdXITl5gNMuAj9BcXaO0xXqNIf9qygl5iwaXs"))

# Özellikler ve bu özelliklerin farklı değerleri için düğümleri oluştur






properties = {
    "Meslek": ["Student", "Business", "Housewife", "Occupation","Corporate","Others"],
    "Kendi işinde çalışıyor mu": ["Yes", "No", "Maybe"],
    "Aile Geçmişi": ["Yes", "No", "Maybe"],
    "Tedavi Gördü mü": ["Yes", "No", "Maybe"],
    "evde geçirdiği süre": ["1-14 days", "31-60 days", "More than 2 months", "15-30 days"],
    "Artan Stres mücadele": ["Yes", "No", "Maybe"],
    "Alışkanlıklarını Değiştirme": ["Yes", "No", "Maybe"],
    "Mental Sağlık Geçmişi": ["Yes", "No", "Maybe"],
    "Ruhsal Dalgalanma": ["High", "Medium", "Low", "Maybe"],
    "Başa Çıkma Güçlüğü": ["Yes", "No", "Maybe"],
    "İş İlgisi": ["High", "Medium", "Low", "Maybe"],
    "Sosyal Zayıflık": ["High", "Medium", "Low", "Maybe"]
}

# Her bir özellik için düğümleri oluştur
for prop, values in properties.items():
    for value in values:
        prop_node = Node(prop, deger=value)
        graph.create(prop_node)

# Her bir kayıt için insan düğümünü ve ilgili özellik düğümlerini ilişkilendirme
for record in json_data:
    insan_node = Node("İnsan", zaman=record["Zaman"], cinsiyet=record["Cinsiyet"], yaşadığı_şehir=record["Ülke"])
    graph.create(insan_node)

    # Her özelliği kontrol et ve ilgili özellik düğümüne ilişkilendir
from py2neo import Graph, Node, Relationship
import json

# JSON verisini oku
with open('guncellenmis.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

# Neo4j bağlantısı oluştur
graph = Graph("neo4j+s://36a5aa75.databases.neo4j.io", auth=("neo4j", "6xYJUrgdXITl5gNMuAj9BcXaO0xXqNIf9qygl5iwaXs"))

# Özellikler ve bu özelliklerin farklı değerleri için düğümleri oluştur






properties = {
    "Meslek": ["Student", "Business", "Housewife", "Occupation","Corporate","Others"],
    "Kendi işinde çalışıyor mu": ["Yes", "No", "Maybe"],
    "Aile Geçmişi": ["Yes", "No", "Maybe"],
    "Tedavi Gördü mü": ["Yes", "No", "Maybe"],
    "evde geçirdiği süre": ["1-14 days", "31-60 days", "More than 2 months", "15-30 days"],
    "Artan Stres mücadele": ["Yes", "No", "Maybe"],
    "Alışkanlıklarını Değiştirme": ["Yes", "No", "Maybe"],
    "Mental Sağlık Geçmişi": ["Yes", "No", "Maybe"],
    "Ruhsal Dalgalanma": ["High", "Medium", "Low", "Maybe"],
    "Başa Çıkma Güçlüğü": ["Yes", "No", "Maybe"],
    "İş İlgisi": ["High", "Medium", "Low", "Maybe"],
    "Sosyal Zayıflık": ["High", "Medium", "Low", "Maybe"]
}

# Her bir özellik için düğümleri oluştur
for prop, values in properties.items():
    for value in values:
        prop_node = Node(prop, deger=value)
        graph.create(prop_node)

# Her bir kayıt için insan düğümünü ve ilgili özellik düğümlerini ilişkilendirme
for record in json_data:
    insan_node = Node("İnsan", zaman=record["Zaman"], cinsiyet=record["Cinsiyet"], yaşadığı_şehir=record["Ülke"])
    graph.create(insan_node)

    # Her özelliği kontrol et ve ilgili özellik düğümüne ilişkilendir
    for prop, values in properties.items():
        prop_value = record[prop]
        prop_node = graph.nodes.match(prop, deger=prop_value).first()
        if prop_node is not None:
            if prop_value == "yes":
                relation = Relationship(insan_node, "sahip", prop_node)
            graph.create(relation)
        else:
            print(f"{prop} için {prop_value} değerine sahip bir düğüm bulunamadı.")
            

print("İnsanlar ve özellikler arasında ilişkiler oluşturuldu.")

print("İnsanlar ve özellikler arasında ilişkiler oluşturuldu.")