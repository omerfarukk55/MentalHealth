import json
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# JSON dosyasını yükleme
with open('guncellenmis.json', 'r') as file:
    data = json.load(file)

# DataFrame'e dönüştürme
df = pd.DataFrame(data)

# Özelliklere karşılık gelen sayısal değerlerin belirlendiği sözlük
encoding_map = {
    "Meslek": {"Student": 0, "Business": 1, "Housewife": 2, "Occupation": 3, "Corporate": 4, "Others": 5},
    "Kendi isinde calisiyor mu": {"Yes": 0, "No": 1, "Maybe": 2,"": 3},
    "Aile Gecmisi": {"Yes": 0, "No": 1, "Maybe": 2},
    "Tedavi Gordu mu": {"Yes": 0, "No": 1, "Maybe": 2},
    "evde gecirdigi sure": {"1-14 days": 0, "31-60 days": 1, "More than 2 months": 2, "15-30 days": 3,"Go out Every day":4},
    "Artan Stres mucadele": {"Yes": 0, "No": 1, "Maybe": 2},
    "Aliskanliklarini Degistirme": {"Yes": 0, "No": 1, "Maybe": 2},
    "mental_saglik": {"Yes": 0, "No": 1, "Maybe": 2},
    "Ruhsal Dalgalanma": {"High": 0, "Medium": 1, "Low": 2, "Maybe": 3},
    "Basa cikma Guclugu": {"Yes": 0, "No": 1, "Maybe": 2},
    "is ilgisi": {"Yes": 0, "No": 1, "Maybe": 2},
    "Sosyal Zayiflik": {"Yes": 0, "No": 1, "Maybe": 2}
}

# Kategorik sütunları sayısal değerlere dönüştürme
for col, encoding in encoding_map.items():
    df[col] = df[col].map(encoding)

# Eksik verileri işleme
df.fillna(value={"Kendi işinde çalışıyor mu": 2}, inplace=True)  # "Maybe" için 2

# Bağımsız ve bağımlı değişkenleri ayırma
X = df.drop("mental_saglik", axis=1)
y = df["mental_saglik"]

if df.empty:
    print("DataFrame boş!")
else:
    print("DataFrame dolu!")
    # Yeni JSON dosyasına normalleştirilmiş verileri yazma
    with open('normalized_veriler2.json', 'w') as file:
        df.to_json(file, orient='records', indent=4)
        print("JSON dosyasına yazma işlemi başarılı!")