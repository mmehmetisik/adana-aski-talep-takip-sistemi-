# 🛠️ Teknoloji Stack'i

## Programlama Dili ve Framework'ler

### Python 3.x
Ana programlama dili olarak Python seçilmesinin nedenleri:

**Neden Python?**
Python, bu proje için ideal bir seçimdi çünkü:
- Hızlı prototipleme ve geliştirme imkanı sunar
- Zengin kütüphane ekosistemi vardır
- Okunabilir ve bakımı kolay kod yazmayı teşvik eder
- Hem masaüstü hem de backend geliştirme için uygundur
- Google API'leri için mükemmel destek sağlar

**Kullanılan Python Özellikleri**
- Type hints ile daha güvenli kod
- Context managers ile kaynak yönetimi
- Decorators ile kod tekrarını azaltma
- Threading ile asenkron işlemler
- JSON modülü ile veri serileştirme

### Tkinter - GUI Framework
Python'un standart GUI kütüphanesi olan Tkinter, ana sistem arayüzü için kullanılmıştır.

**Avantajları:**
- Python ile birlikte gelir, ekstra kurulum gerektirmez
- Cross-platform desteği (Windows, Linux, Mac)
- Hafif ve hızlı
- Geniş widget seti

**Kullanılan Tkinter Bileşenleri:**
- Frame ve LabelFrame (layout yönetimi)
- Entry ve Text widgets (veri girişi)
- Button ve Checkbutton (interaktif elemanlar)
- Treeview (tablo görünümü)
- Canvas (animasyonlar için)

### CustomTkinter - Modern UI
Viewer uygulaması için CustomTkinter kullanılarak daha modern bir görünüm elde edilmiştir.

**Sağladığı Özellikler:**
- Yuvarlak köşeli modern butonlar
- Smooth animasyonlar
- Dark/Light tema desteği
- Responsive tasarım elemanları

## Veritabanı Teknolojileri

### SQLite
Yerel veritabanı çözümü olarak SQLite tercih edilmiştir.

**Neden SQLite?**
- Serverless mimari - kurulum gerektirmez
- Tek dosya veritabanı - kolay yedekleme
- ACID uyumlu - veri bütünlüğü garantisi
- Küçük ve orta ölçekli projeler için ideal
- Python ile mükemmel entegrasyon

**Veritabanı Şeması:**
```sql
-- Ana talepler tablosu
CREATE TABLE talepler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    talep_no TEXT UNIQUE NOT NULL,
    is_adi TEXT NOT NULL,
    talep_tarihi TEXT NOT NULL,
    mevcut_durum TEXT NOT NULL,
    firma TEXT,
    son_guncelleme TEXT NOT NULL,
    olusturan TEXT NOT NULL,
    alim_turu TEXT,
    alim_turu_detay TEXT,
    olusturma_zamani TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Güncelleme geçmişi tablosu
CREATE TABLE guncellemeler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    talep_no TEXT NOT NULL,
    kontrol_tarihi TEXT NOT NULL,
    yil TEXT NOT NULL,
    durum TEXT NOT NULL,
    firma TEXT,
    aciklama TEXT,
    guncelleyen TEXT NOT NULL,
    guncelleme_zamani TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (talep_no) REFERENCES talepler (talep_no)
);
```
## Bulut Teknolojileri

### Google Drive API
Viewer uygulaması için veri senkronizasyonu Google Drive üzerinden sağlanır.

**Kullanılan API Özellikleri:**
- Files.list() - Dosya listesi alma
- Files.get() - Dosya metadata okuma
- Files.get_media() - Dosya içeriği indirme
- OAuth 2.0 kimlik doğrulama

**Entegrasyon Detayları:**
```python
# API istemcisi oluşturma
service = build('drive', 'v3', credentials=creds)

# Dosya arama
results = service.files().list(
    q=f"name='{DRIVE_FILE_NAME}'",
    fields="files(id, name, modifiedTime)"
).execute()
```
## OAuth 2.0
Google kimlik doğrulama için endüstri standardı OAuth 2.0 protokolü kullanılır.

**Güvenlik Akışı:**
1. Kullanıcı Google hesabı ile giriş yapar
2. Uygulama için izinleri onaylar
3. Access token alınır
4. Token güvenli şekilde saklanır
5. API çağrılarında token kullanılır

## Email Teknolojileri

### SMTP Protocol

Email gönderimi için Python'un built-in SMTP kütüphanesi kullanılır.

**Özellikler:**

- TLS/SSL şifreleme desteği
- HTML email gönderimi
- Çoklu alıcı desteği
- Ek dosya gönderimi (opsiyonel)

**SMTP Konfigürasyonu:**
```
smtp_ayarlari = {
    "sunucu": "smtp.gmail.com",
    "port": 587,
    "guvenlik": "TLS",
    "kullanici_adi": "email@gmail.com",
    "sifre": "app_password"
}
```

## HTML/CSS Email Templates

Modern ve responsive email şablonları için HTML5 ve CSS3 kullanılır.

**Email Template Teknikleri:**
- Inline CSS (email client uyumluluğu için)
- Table-based layout (eski client desteği)
- Media queries (mobil optimizasyon)
- Web-safe fontlar

**Örnek Email Template Yapısı:**
```
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; }
        .container { max-width: 600px; margin: 0 auto; }
        .header { background: linear-gradient(135deg, #1e3a8a, #3b82f6); }
    </style>
</head>
<body>
    <div class="container">
        <!-- Email içeriği -->
    </div>
</body>
</html>
```
## Güvenlik Teknolojileri

### Hashlib - SHA-256

Şifre güvenliği için SHA-256 hash algoritması kullanılır.

```
def sifre_hashle(self, sifre):
    salt = "aski_2025_secure_"
    sifre_salt = salt + sifre + salt
    return hashlib.sha256(sifre_salt.encode('utf-8')).hexdigest()
```

### SSL/TLS

Email iletişimi ve API bağlantıları için SSL/TLS şifreleme kullanılır.

**Güvenlik Katmanları:**

- SMTP üzerinde STARTTLS
- HTTPS üzerinde API iletişimi
- Sertifika doğrulama

### Geliştirme Araçları

#### openpyxl

Excel dosyası işlemleri için kullanılır.

**Özellikler:**
- .xlsx dosya okuma/yazma
- Hücre formatlama
- Grafik oluşturma
- Formula desteği

**Kullanım Örneği:**
```
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment

# Workbook oluşturma
wb = openpyxl.Workbook()
ws = wb.active

# Hücre formatlama
cell = ws['A1']
cell.font = Font(bold=True, color="FFFFFF")
cell.fill = PatternFill(start_color="1E3A8A", fill_type="solid")
```

#### JSON

Konfigürasyon ve veri alışverişi için JSON formatı kullanılır.

**Kullanım Alanları:**
- Kullanıcı verileri (users.json)
- Email konfigürasyonu (email_config.json)
- API response işleme

#### Threading

Asenkron işlemler için Python threading modülü kullanılır.

**Kullanım Alanları:**

- Email gönderimi (UI'ı dondurmadan)
- Log yazma işlemleri
- Periyodik güncelleme kontrolleri

**Thread-Safe Log Örneği:**

```
import threading

_logger_lock = threading.Lock()

def log_yaz(mesaj):
    with _logger_lock:
        # Thread-safe log yazma
        logger.info(mesaj)
```

### PyInstaller

Executable dosya oluşturmak için PyInstaller kullanılır.

**Build Konfigürasyonu:**

```
# .spec dosyası özellikleri
a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('credentials.json', '.'), ('token.json', '.'), ('app.ico', '.')],
    hiddenimports=['openpyxl.cell._writer'],
    ...
)

exe = EXE(
    ...
    name='TalepTakipSistemi',
    console=False,  # Konsol penceresi gösterme
    icon=['app.ico']  # Özel uygulama ikonu
)
```

## Sistem Gereksinimleri

### Minimum Gereksinimler

- İşletim Sistemi: Windows 7/Linux/macOS 10.12 veya üzeri
- Python: 3.7 veya üzeri
- RAM: 2 GB
- Disk Alanı: 100 MB
- Ekran Çözünürlüğü: 1366x768

### Önerilen Gereksinimler

- İşletim Sistemi: Windows 10/11
- Python: 3.9 veya üzeri
- RAM: 4 GB
- Disk Alanı: 500 MB
- Ekran Çözünürlüğü: 1920x1080
- İnternet Bağlantısı: Email ve Drive sync için gerekli

### Bağımlılıklar (Dependencies)

```
# requirements.txt
tkinter (built-in)
customtkinter==5.2.0
openpyxl==3.1.2
google-api-python-client==2.100.0
google-auth-httplib2==0.1.1
google-auth-oauthlib==1.1.0
pillow==10.0.0
```

## Performans Optimizasyonları

### Veritabanı Optimizasyonları

-İndeksleme stratejisi
- Prepared statements kullanımı
- Connection pooling
- Query optimization

### Bellek Yönetimi

- Lazy loading implementasyonu
- Garbage collection optimizasyonu
- Large dataset pagination
- Resource cleanup

### UI Performansı

- Virtual scrolling
- Debouncing for search
- Progressive rendering
- Animation frame limiting


















