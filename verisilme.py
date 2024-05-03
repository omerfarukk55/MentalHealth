import json

# JSON dosyasını yükle
with open('guncellenmis.json', 'r') as file:
    data = json.load(file)

# Tüm verilerdeki "Cinsiyet" anahtarına sahip değerleri sil
for veri in data:
    if "Cinsiyet" in veri:
        del veri["Cinsiyet"]

# Güncellenmiş verileri başka bir dosyaya yaz
with open('guncellenmis.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Cinsiyet bilgileri başarıyla silindi.")