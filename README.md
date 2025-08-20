# YouTubeSearcher

DuckDuckGo kullanarak YouTube videolarını arayan, listeleyen ve detaylı bilgiler sunan Python modülü.

## Özellikler
- DuckDuckGo üzerinden YouTube araması yapar
- Video ID'sini farklı URL formatlarından otomatik çıkarır
- Arama sonuçlarını numaralandırılmış liste halinde gösterir
- Belirtilen indexteki videoyu detaylı şekilde yazdırır
- Esnek sonuç sayısı kontrolü (her arama için farklı sayıda sonuç)
- Kolay kullanımlı sınıf tabanlı arayüz

## Kurulum
1. Bu depoyu klonlayın:
   ```bash
   git clone https://github.com/AutoPyloter/youtube-searcher.git
   cd youtube-searcher
   ```
2. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

## Kullanım
### Modül Olarak Kullanım
```python
from youtube_searcher import YouTubeSearcher

# Arama sınıfını oluştur
searcher = YouTubeSearcher("python machine learning", max_results=10)

# Arama yap
result_count = searcher.search(max_results=5)
print(f"{result_count} video bulundu")

# Tüm videoları listele
searcher.list_videos()

# Belirli bir videoyu detaylı yazdır
if result_count > 0:
    searcher.print_video(1)  # İlk video
```

### Farklı Sonuç Sayılarıyla Arama
```python
searcher = YouTubeSearcher("data science")

# İlk arama: 3 sonuç
searcher.search(max_results=3)
searcher.list_videos()

# İkinci arama: 8 sonuç
searcher.search(max_results=8)
searcher.list_videos()

# Üçüncü arama: varsayılan değer (10)
searcher.search()  # max_results verilmedi
searcher.list_videos()
```

## Metotlar
### `__init__(query, max_results=10)`
- **Açıklama**: YouTube arama sınıfını başlatır
- **Parametreler**:
  - `query` (str): Aranacak metin
  - `max_results` (int): Maksimum sonuç sayısı (varsayılan: 10)

### `search(max_results=None)`
- **Açıklama**: YouTube'da arama yapar ve sonuçları kaydeder
- **Parametre**: `max_results` (int, optional): Bu arama için maksimum sonuç sayısı
- **Dönüş**: `int` - Bulunan video sayısı

### `list_videos()`
- **Açıklama**: Bulunan videoları liste halinde gösterir
- **Dönüş**: Yok (ekrana çıktı verir)

### `get_video(index)`
- **Açıklama**: Belirtilen indexteki videoyu döndürür
- **Parametre**: `index` (int) - Video indeksi (1'den başlar)
- **Dönüş**: `dict` - Video bilgileri veya None (hata durumunda)
- **Örnek Çıktı**:
  ```python
  {
      'title': 'Video Başlığı',
      'url': 'https://www.youtube.com/watch?v=VIDEO_ID',
      'video_id': 'VIDEO_ID',
      'snippet': 'Video açıklamasının ilk 100 karakteri...'
  }
  ```

### `print_video(index)`
- **Açıklama**: Belirtilen indexteki videoyu detaylı şekilde yazdırır
- **Parametre**: `index` (int) - Video indeksi (1'den başlar)
- **Dönüş**: Yok (ekrana çıktı verir)

## Örnek Çıktı
```
=== İlk Arama (3 sonuç) ===
3 video bulundu

🔍 'python machine learning' için 3 YouTube videosu bulundu:
================================================================================
1. Machine Learning with Python - Full Course for Beginners
   🔗 https://www.youtube.com/watch?v=abc123
   📝 In this comprehensive Machine Learning course, you will learn everything you need to know...
--------------------------------------------------------------------------------
2. Python Machine Learning Tutorial (Part 1)
   🔗 https://www.youtube.com/watch?v=def456
   📝 Learn the basics of machine learning with Python in this tutorial series. We'll cover...
--------------------------------------------------------------------------------
3. Machine Learning Tutorial Python - 1: What is Machine Learning?
   🔗 https://www.youtube.com/watch?v=ghi789
   📝 In this video, we'll understand what machine learning is and how it works. We'll also...
--------------------------------------------------------------------------------

=== Detaylı Video Bilgisi ===

🎬 Video #1
==================================================
Başlık: Machine Learning with Python - Full Course for Beginners
URL: https://www.youtube.com/watch?v=abc123
Video ID: abc123
Açıklama: In this comprehensive Machine Learning course, you will learn everything you need to know...
==================================================
```

## Gereksinimler
- Python 3.8+
- duckduckgo-search>=5.0.0

## Lisans
Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.

## Katkıda Bulunma
Katkılarınızı memnuniyetle karşılıyoruz! Lütfen değişiklik yapmadan önce aşağıdaki adımları izleyin:
1. Depoyu fork edin
2. Yeni bir dal oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Değişikliklerinizi yapın ve commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Dalı pushlayın (`git push origin feature/yeni-ozellik`)
5. Bir Pull Request oluşturun

## Yazar
- [AutoPyloter](https://github.com/AutoPyloter)

## Destek
Sorularınız veya önerileriniz için lütfen [Issues](https://github.com/AutoPyloter/youtube-searcher/issues) bölümünü kullanın.