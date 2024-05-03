import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# JSON dosyasını yükleme
with open('normalized_veriler2.json', 'r') as file:
    data = json.load(file)

# DataFrame'e dönüştürme
df = pd.DataFrame(data)

# Özelliklere karşılık gelen sayısal değerlerin belirlendiği sözlük
encoding_map = {
    "Meslek": {"Student": 0, "Business": 1, "Housewife": 2, "Occupation": 3, "Corporate": 4, "Others": 5},
    "Kendi isinde calisiyor mu": {"Yes": 0, "No": 1, "Maybe": 2, "":2},
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
df.dropna(inplace=True)

# Bağımsız ve bağımlı değişkenleri ayırma
X = df.drop("mental_saglik", axis=1)
y = df["mental_saglik"]

# Eğitim ve test setlerini ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)


# Model oluşturma
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Modeli derleme
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Modeli eğitme
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Modeli değerlendirme
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"Test loss: {test_loss}")
print(f"Test accuracy: {test_accuracy}")

# Sınıflandırma raporunu görüntüleme
y_pred_prob = model.predict(X_test)
y_pred = (y_pred_prob > 0.5).astype(int)
print(classification_report(y_test, y_pred))