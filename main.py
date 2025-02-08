import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSV dosyasını yükleme
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Veri setini tanıma
def explore_data(df):
    print("\n📌 İlk 5 Satır:\n", df.head())
    print("\n📌 Veri Kümesi Bilgisi:")
    print(df.info())
    print("\n📌 Eksik Değerler:\n", df.isnull().sum())
    print("\n📌 Benzersiz Değer Sayıları:\n", df.nunique())
    print("\n📌 İstatistiksel Özet:\n", df.describe())

# Tüm görselleri tek ekranda gösterme
def visualize_all(df):
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # Eksik verileri göster
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis', ax=axes[0, 0])
    axes[0, 0].set_title("Eksik Veriler")
    
    # Veri tiplerini göster
    df.dtypes.value_counts().plot(kind='bar', color='skyblue', ax=axes[0, 1])
    axes[0, 1].set_xlabel("Veri Tipleri")
    axes[0, 1].set_ylabel("Sütun Sayısı")
    axes[0, 1].set_title("Veri Tiplerinin Dağılımı")
    
    # Playlist genre dağılımı
    sns.countplot(y=df['playlist_genre'], order=df['playlist_genre'].value_counts().index, palette="coolwarm", ax=axes[1, 0])
    axes[1, 0].set_title("Playlist Türlerinin Dağılımı")
    axes[1, 0].set_xlabel("Şarkı Sayısı")
    axes[1, 0].set_ylabel("Playlist Türü")
    
    # Track popularity dağılımı
    sns.histplot(df['track_popularity'], bins=30, kde=True, color='purple', ax=axes[1, 1])
    axes[1, 1].set_title("Şarkı Popülerliği Dağılımı")
    axes[1, 1].set_xlabel("Popülerlik")
    axes[1, 1].set_ylabel("Frekans")
    
    plt.tight_layout()
    plt.show()

# Ana çalışma fonksiyonu
def main():
    file_path = "spotify_songs.csv"  # Dosya yolunu buraya ekleyin
    df = load_data(file_path)
    explore_data(df)
    visualize_all(df)

if __name__ == "__main__":
    main()
