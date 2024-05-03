import json

# JSON verisini oku
with open('guncellenmis.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

# Türkçe karşılıklar için sözlük oluştur
turkce_karsiliklar = {
        "Kendi isinde çalisiyor mu":"Kendi isinde calisiyor mu",
        "Aliskanliklarini Değistirme":"Aliskanliklarini Degistirme",
    "Başa cikma Guclugu":"Basa cikma Guclugu",
    "Zaman":"Zaman",
    "Cinsiyet":"Cinsiyet" ,
    "Ulke":"Ulke",
    "Meslek":"Meslek" ,
    "Aile Gecmisi":"Aile Gecmisi",
    "Tedavi Gordu mu":"Tedavi Gordu mu" ,
    "evde gecirdigi sure":"evde gecirdigi sure" ,
    "Artan Stres mucadele":"Artan Stres mucadele",
    "mental_saglik":"mental_saglik",
    "Ruhsal Dalgalanma":"Ruhsal Dalgalanma" ,
    "is ilgisi":"is ilgisi",
    "Sosyal Zayiflik":"Sosyal Zayiflik",
}


# Türkçe karşılıkları uygula
for record in json_data:
    for key, value in turkce_karsiliklar.items():
        if key in record:
            record[value] = record.pop(key)

# Güncellenmiş JSON verisini dosyaya yaz
with open('guncellenmis.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=4, ensure_ascii=False)