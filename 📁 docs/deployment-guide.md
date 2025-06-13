# 🚀 Kurulum ve Dağıtım Kılavuzu

Bu kılavuz, ADANA ASKİ Talep Takip Sistemi'nin her iki bileşeninin (Ana Yönetim Sistemi ve Viewer Uygulaması) kurulum ve dağıtım süreçlerini detaylı olarak açıklamaktadır. Her adım, neden gerekli olduğu açıklamasıyla birlikte sunulmuştur.

## Genel Bakış ve Hazırlık

Sistem kurulumuna başlamadan önce, ortamınızın hazır olduğundan emin olmanız gerekmektedir. Bu hazırlık süreci, ileride karşılaşabileceğiniz sorunları minimize edecek ve kurulumun sorunsuz geçmesini sağlayacaktır.

### Sistem Gereksinimleri

Sistemin sağlıklı çalışabilmesi için minimum gereksinimlerin karşılanması kritiktir. Bu gereksinimler, yoğun kullanım senaryoları ve gelecekteki güncellemeler düşünülerek belirlenmiştir.

**Donanım Gereksinimleri:**

Minimum gereksinimler, sistemin temel işlevlerini yerine getirebilmesi için gerekli olan en düşük donanım özelliklerini ifade eder. Ancak daha iyi performans ve kullanıcı deneyimi için önerilen gereksinimleri karşılamanız tavsiye edilir.

- İşlemci: Dual Core 2.0 GHz veya üzeri (Önerilen: Quad Core 2.5 GHz)
- RAM: 2 GB (Önerilen: 4 GB veya üzeri)
- Disk Alanı: 500 MB boş alan (Veritabanı büyüklüğüne göre artabilir)
- Ekran Çözünürlüğü: 1366x768 (Önerilen: 1920x1080)

**Yazılım Gereksinimleri:**

İşletim sistemi ve yazılım bağımlılıkları, sistemin düzgün çalışması için kritik öneme sahiptir. Özellikle Python versiyonu, kullanılan kütüphanelerin uyumluluğu açısından önemlidir.

- İşletim Sistemi: Windows 7/10/11, Ubuntu 18.04+, macOS 10.12+
- Python: 3.7 veya üzeri (Önerilen: 3.9+)
- İnternet Bağlantısı: Email ve Google Drive senkronizasyonu için gerekli

## Ana Yönetim Sistemi Kurulumu

Ana yönetim sisteminin kurulumu, birkaç temel adımdan oluşmaktadır. Her adımı dikkatlice takip etmeniz, sorunsuz bir kurulum deneyimi yaşamanızı sağlayacaktır.

### Python Kurulumu

Python, sistemimizin temel yapı taşıdır. Doğru versiyonun kurulu olması ve PATH ayarlarının yapılmış olması kritiktir.

**Windows İçin Python Kurulumu:**

1. Python'un resmi web sitesinden (python.org) Windows için Python 3.9 veya üzeri versiyonu indirin. İndirme sırasında sisteminizin 32-bit mi yoksa 64-bit mi olduğuna dikkat edin.

2. İndirilen kurulum dosyasını çalıştırın. Kurulum ekranında mutlaka "Add Python to PATH" seçeneğini işaretleyin. Bu seçenek, Python'u komut satırından çalıştırabilmenizi sağlar.

3. Kurulum tamamlandıktan sonra, komut istemcisini açın ve aşağıdaki komutu çalıştırarak kurulumu doğrulayın:
