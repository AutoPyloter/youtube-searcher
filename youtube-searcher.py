from ddgs import DDGS
import re

class YouTubeSearcher:
    def __init__(self, query, max_results=10):
        """
        YouTube arama sınıfı
        :param query: Aranacak metin
        :param max_results: Maksimum sonuç sayısı (varsayılan: 10)
        """
        self.query = query
        self.max_results = max_results
        self.results = []
        self.search_performed = False
    
    def search(self, max_results=None):
        """
        YouTube'da arama yapar ve sonuçları kaydeder
        :param max_results: Bu arama için maksimum sonuç sayısı (None ise sınıf değerini kullanır)
        :return: Bulunan video sayısı
        """
        # Parametre verilmediyse sınıfın varsayılan değerini kullan
        if max_results is None:
            max_results = self.max_results
        
        try:
            with DDGS() as ddgs:
                full_query = f"{self.query} site:youtube.com"
                raw_results = ddgs.text(
                    full_query,
                    max_results=max_results
                )
                
                self.results = []
                for result in raw_results:
                    video_id = self._extract_video_id(result['href'])
                    if video_id:
                        self.results.append({
                            'title': result['title'],
                            'url': f"https://www.youtube.com/watch?v={video_id}",
                            'video_id': video_id,
                            'snippet': result['body'][:100] + '...'
                        })
                
                self.search_performed = True
                return len(self.results)
                
        except Exception as e:
            print(f"Arama sırasında hata oluştu: {str(e)}")
            return 0
    
    def list_videos(self):
        """Bulunan videoları liste halinde gösterir"""
        if not self.search_performed:
            print("Önce arama yapmanız gerekiyor. search() metodunu çağırın.")
            return
        
        if not self.results:
            print("Hiç video bulunamadı.")
            return
        
        print(f"\n🔍 '{self.query}' için {len(self.results)} YouTube videosu bulundu:")
        print("=" * 80)
        
        for i, video in enumerate(self.results, 1):
            print(f"{i}. {video['title']}")
            print(f"   🔗 {video['url']}")
            print(f"   📝 {video['snippet']}")
            print("-" * 80)
    
    def get_video(self, index):
        """
        Belirtilen indexteki videoyu döndürür
        :param index: Video indeksi (1'den başlar)
        :return: Video bilgileri veya None
        """
        if not self.search_performed:
            print("Önce arama yapmanız gerekiyor. search() metodunu çağırın.")
            return None
        
        if index < 1 or index > len(self.results):
            print(f"Geçersiz indeks. 1-{len(self.results)} arası bir değer girin.")
            return None
        
        return self.results[index - 1]
    
    def print_video(self, index):
        """
        Belirtilen indexteki videoyu detaylı şekilde yazdırır
        :param index: Video indeksi (1'den başlar)
        """
        video = self.get_video(index)
        if not video:
            return
        
        print(f"\n🎬 Video #{index}")
        print("=" * 50)
        print(f"Başlık: {video['title']}")
        print(f"URL: {video['url']}")
        print(f"Video ID: {video['video_id']}")
        print(f"Açıklama: {video['snippet']}")
        print("=" * 50)
    
    def _extract_video_id(self, url):
        """YouTube URL'sinden video ID'sini çıkarır"""
        patterns = [
            r'(?:v=|\/)([0-9A-Za-z_-]{11}).*',  # Standart URL
            r'(?:embed\/)([0-9A-Za-z_-]{11})',  # Embed URL
            r'(?:youtu\.be\/)([0-9A-Za-z_-]{11})'  # Kısa URL
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        return None


# Örnek Kullanım
if __name__ == "__main__":
    # 1. Arama sınıfını oluştur
    searcher = YouTubeSearcher("python machine learning")
    
    # 2. Farklı sayılarla arama yap
    print("=== İlk Arama (3 sonuç) ===")
    result_count = searcher.search(max_results=3)
    print(f"{result_count} video bulundu")
    searcher.list_videos()
    
    print("\n=== İkinci Arama (5 sonuç) ===")
    result_count = searcher.search(max_results=5)
    print(f"{result_count} video bulundu")
    searcher.list_videos()
    
    print("\n=== Üçüncü Arama (varsayılan değer) ===")
    result_count = searcher.search()  # max_results verilmedi, sınıfın varsayılan değerini kullanır
    print(f"{result_count} video bulundu")
    searcher.list_videos()
    
    # 4. Belirli bir videoyu yazdır
    if result_count > 0:
        print("\n=== Detaylı Video Bilgisi ===")
        searcher.print_video(1)