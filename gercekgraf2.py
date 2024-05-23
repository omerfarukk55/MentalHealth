from py2neo import Graph, Node, Relationship
import pandas as pd

# CSV dosyasından veriyi oku
df = pd.read_csv('mentalsaglik.csv')

# Neo4j bağlantısı oluştur
graph = Graph("neo4j+s://36a5aa75.databases.neo4j.io", auth=("neo4j", "6xYJUrgdXITl5gNMuAj9BcXaO0xXqNIf9qygl5iwaXs"))

# Özellikler ve bu özelliklerin farklı değerleri için düğümleri oluştur
properties = {
    "Meslek":  ["Student", "Business", "Housewife", "Occupation","Corporate","Others"],
    "kendi_isi_mi": ["Yes", "No", "Maybe"],
    "ailesinin_mental_sagligi": ["Yes", "No", "Maybe"],
    "tedavi_oldu_mu": ["Yes", "No", "Maybe"],
    "evde_kaldigi_gun": ["1-14 days", "31-60 days", "More than 2 months", "15-30 days"],
    "strese_dayanikliligi": ["Yes", "No", "Maybe"],
    "Aliskanlik_degistirirmi": ["Yes", "No", "Maybe"],
    "mental_saglik_gecmisi": ["Yes", "No", "Maybe"],
    "Ruh_hali_Degisimleri": ["High", "Medium", "Low", "Maybe"],
    "sorunla_basa_cikma": ["Yes", "No", "Maybe"],
    "is_ilgisi":  ["High", "Medium", "Low", "Maybe"],
    "sosyal_zayiflik": ["High", "Medium", "Low", "Maybe"],
    "mulakatda_ruh_sagligini_soyler_misin": ["Yes", "No", "Maybe"],
    "tedavi_seceneklerin_var_mi": ["Yes", "No", "Maybe"]
}
# Her bir özellik için düğümleri oluştur
for prop, values in properties.items():
    for value in values:
        prop_node = Node(prop, deger=value)
        graph.create(prop_node)

# Her bir kayıt için insan düğümünü ve ilgili özellik düğümlerini ilişkilendirme
for _, record in df.iterrows():
    insan_node = Node("İnsan", zaman=record["zaman"], cinsiyet=record["cinsiyet"], yaşadığı_şehir=record["ulke"])
    graph.create(insan_node)

    # Her özelliği kontrol et ve ilgili özellik düğümüne ilişkilendir
    for prop, values in properties.items():
        prop_value = record[prop]
        prop_node = graph.nodes.match(prop, deger=prop_value).first()
        if prop_node is not None:
            relation = Relationship(insan_node, "sahip", prop_node)
            graph.create(relation)
        else:
            print(f"{prop} için {prop_value} değerine sahip bir düğüm bulunamadı.")

print("İnsanlar ve özellikler arasında ilişkiler oluşturuldu.")
