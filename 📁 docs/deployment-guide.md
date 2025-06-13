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

python --version

Bu komut, kurulu Python versiyonunu göstermelidir.

**Linux İçin Python Kurulumu:**

Çoğu Linux dağıtımında Python önceden kurulu gelir. Ancak versiyonu kontrol etmek ve gerekirse güncellemek önemlidir.

```bash
# Python versiyonunu kontrol et
python3 --version

# Eğer kurulu değilse veya eski versiyonsa
sudo apt update
sudo apt install python3.9 python3-pip python3-venv
```

## Gerekli Kütüphanelerin Kurulumu

Python kütüphaneleri, sistemin işlevselliğini sağlayan modüllerdir. Her kütüphanenin belirli bir görevi vardır ve eksik olması durumunda sistem çalışmayacaktır.

**Sanal Ortam Oluşturma (Önerilen):**

Sanal ortam kullanmak, projenin bağımlılıklarını sistem genelindeki Python kurulumundan izole eder. Bu yaklaşım, farklı projeler arasında versiyon çakışmalarını önler.

```
# Sanal ortam oluştur
python -m venv talep_takip_env

# Windows'ta aktifleştir
talep_takip_env\Scripts\activate

# Linux/Mac'te aktifleştir
source talep_takip_env/bin/activate
```

**Kütüphanelerin Kurulumu:**

Gerekli tüm kütüphaneleri tek komutla kurabilirsiniz. Her kütüphanenin işlevi şöyledir:

- tkinter: Ana arayüz framework'ü (Python ile birlikte gelir)
- openpyxl: Excel dosyası işlemleri için
- hashlib: Şifre güvenliği için (Python ile birlikte gelir)
- smtplib: Email gönderimi için (Python ile birlikte gelir)

```
pip install openpyxl==3.1.2

```

## Klasör Yapısının Oluşturulması

Uygulamanın düzgün çalışması için belirli bir klasör yapısına ihtiyaç vardır. Bu yapı, verilerin organize edilmesini ve yönetilmesini kolaylaştırır.

```
talep_takip_sistemi/
├── data/                    # Veri dosyaları
│   ├── logs/               # Log dosyaları
│   ├── backup/             # Yedekleme dosyaları
│   └── email_templates/    # Email şablonları
├── main.py                 # Ana program dosyası
├── config.py               # Konfigürasyon dosyası
├── database_manager.py     # Veritabanı yönetimi
├── email_manager.py        # Email yönetimi
├── excel_manager.py        # Excel işlemleri
├── log.py                  # Loglama sistemi
├── main_window.py          # Ana pencere
└── password_screen.py      # Giriş ekranı
```


































