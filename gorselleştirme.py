import pandas as pd
import matplotlib.pyplot as plt
import json

# JSON dosyasını okuma ve DataFrame'e yükleme
with open('eski_veriler.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Tüm dağılımları alt grafikler olarak gösterme
fig, axs = plt.subplots(3, 3, figsize=(15, 12))  # 3x3 alt grafik düzeni, genişlik ve yükseklik belirtiliyor

# Cinsiyet dağılımı
gender_counts = df['Gender'].value_counts()
gender_counts.plot(kind='pie', ax=axs[0, 0], color='skyblue')
axs[0, 0].set_title('Gender Distribution')

# Treatment dağılımı
treatment_counts = df['treatment'].value_counts()
treatment_counts.plot(kind='bar', ax=axs[0, 1], color='lightgreen')
axs[0, 1].set_title('Treatment Distribution')

# Meslek dağılımı
occupation_counts = df['Occupation'].value_counts()
occupation_counts.plot(kind='bar', ax=axs[0, 2], color='salmon')
axs[0, 2].set_title('Occupation Distribution')


# Growing Stress dağılımı
stress_counts = df['Growing_Stress'].value_counts()
stress_counts.plot(kind='bar', ax=axs[1, 1], color='lightblue')
axs[1, 1].set_title('Growing Stress Distribution')

# Changes Habits dağılımı
habits_counts = df['Changes_Habits'].value_counts()
habits_counts.plot(kind='bar', ax=axs[1, 2], color='pink')
axs[1, 2].set_title('Changes Habits Distribution')

# Mood Swings dağılımı
mood_counts = df['Mood_Swings'].value_counts()
mood_counts.plot(kind='bar', ax=axs[2, 0], color='purple')
axs[2, 0].set_title('Mood Swings Distribution')


# Social Weakness dağılımı
social_counts = df['Social_Weakness'].value_counts()
social_counts.plot(kind='bar', ax=axs[2, 2], color='green')
axs[2, 2].set_title('Social Weakness Distribution')

plt.tight_layout()  # Grafiklerin daha iyi düzenlenmesini sağlar
plt.show()