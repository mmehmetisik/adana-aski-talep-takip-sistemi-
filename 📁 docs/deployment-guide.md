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

### Konfigürasyon Ayarları

Sistem konfigürasyonu, uygulamanın davranışını belirleyen kritik ayarları içerir. Bu ayarların doğru yapılması, sistemin sorunsuz çalışması için şarttır.

**Email Konfigürasyonu:**

Email sistemi ilk çalıştırmada otomatik olarak bir konfigürasyon dosyası oluşturacaktır. Bu dosyayı düzenlemeniz gerekecek:

```
{
  "smtp_sunucu": {
    "sunucu": "smtp.gmail.com",
    "port": 587,
    "guvenlik": "TLS",
    "kullanici_adi": "sizin_email@gmail.com",
    "sifre": "uygulama_sifresi",
    "gonderici_adi": "ADANA ASKİ Talep Sistemi"
  },
  "alici_gruplari": {
    "yoneticiler": ["yonetici1@adana-aski.gov.tr"],
    "muhendisler": ["muhendis1@adana-aski.gov.tr"],
    "diğer": ["diger@adana-aski.gov.tr"]
  }
}
```

**Gmail İçin Özel Ayarlar:**

Gmail kullanıyorsanız, güvenlik nedeniyle normal şifrenizi kullanamayacaksınız. Bunun yerine "Uygulama Şifresi" oluşturmanız gerekir:

1. Google hesabınızda 2 faktörlü doğrulamayı aktifleştirin
2. Hesap ayarlarından "Güvenlik" bölümüne gidin
3. "Uygulama şifreleri" seçeneğini bulun
4. Yeni bir uygulama şifresi oluşturun
5. Bu şifreyi email_config.json dosyasına yapıştırın

### İlk Çalıştırma

Tüm hazırlıklar tamamlandıktan sonra sistemi ilk kez çalıştırabilirsiniz. İlk çalıştırmada sistem otomatik olarak gerekli dosya ve klasörleri oluşturacaktır.

```
python main.py
```

**İlk Çalıştırma Kontrol Listesi:**

- Varsayılan kullanıcı dosyası oluşturuldu mu?
- Log klasörü oluşturuldu mu?
- Email template'leri oluşturuldu mu?
- Giriş ekranı düzgün açıldı mı?

## Viewer Uygulaması Kurulumu

Viewer uygulaması, ana sistemden bağımsız olarak kurulur ve Google Drive üzerinden veri senkronizasyonu yapar.

### Google Cloud Console Ayarları

Google Drive API'sini kullanabilmek için öncelikle Google Cloud Console'da bir proje oluşturmanız gerekmektedir.

**Proje Oluşturma Adımları:**

1. Google Cloud Console'a gidin (console.cloud.google.com)
2. Yeni bir proje oluşturun (Proje adı: "Talep Takip Viewer")
3. Oluşturulan projeyi seçin

**Drive API'yi Aktifleştirme:**

API'nin aktifleştirilmesi, uygulamanın Google Drive'a erişebilmesi için gereklidir.

1. Sol menüden "API'ler ve Hizmetler" > "Kitaplık" seçeneğine gidin
2. "Google Drive API" araması yapın
3. API'yi bulun ve "ETKİNLEŞTİR" butonuna tıklayın

**OAuth 2.0 Kimlik Bilgileri Oluşturma:**

Güvenli erişim için OAuth 2.0 kimlik bilgileri gereklidir. Bu bilgiler, uygulamanın kullanıcı adına Drive'a erişmesini sağlar.

1. "API'ler ve Hizmetler" > "Kimlik Bilgileri" bölümüne gidin
2. "Kimlik Bilgileri Oluştur" > "OAuth istemci kimliği" seçin
3. Uygulama türü olarak "Masaüstü uygulaması" seçin
4. İsim verin ve oluşturun
5. JSON dosyasını indirin ve "credentials.json" olarak kaydedin

### CustomTkinter Kurulumu

Viewer uygulaması, modern arayüz için CustomTkinter kütüphanesini kullanır.

```
pip install customtkinter==5.2.0
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

### Viewer Uygulaması Dosya Yapısı

```
talep_takip_viewer/
├── credentials.json        # Google OAuth kimlik bilgileri
├── token.json             # Yetkilendirme token'ı (otomatik oluşur)
├── main.py                # Ana program
├── ui_manager.py          # Arayüz yönetimi
├── drive_manager.py       # Drive işlemleri
├── database_manager.py    # Veritabanı okuma
└── config.py             # Konfigürasyon
```

### İlk Yetkilendirme


```
python main.py
```

**Yetkilendirme Süreci:**

1. Uygulama otomatik olarak web tarayıcınızı açacak
2. Google hesabınızla giriş yapın
3. Uygulama izinlerini inceleyin ve onaylayın
4. Yetkilendirme tamamlandığında tarayıcı sekmesini kapatabilirsiniz
5. token.json dosyası otomatik oluşturulacak

## Executable (EXE) Oluşturma

Kullanıcıların Python kurulumu yapmadan uygulamayı çalıştırabilmesi için executable dosya oluşturabilirsiniz.

### PyInstaller Kurulumu

PyInstaller, Python uygulamalarını tek bir çalıştırılabilir dosyaya dönüştürür.

```
pip install pyinstaller
```

### Spec Dosyası Oluşturma
Spec dosyası, PyInstaller'ın nasıl build alacağını belirler. Her iki uygulama için ayrı spec dosyaları gereklidir.

```
**Ana Sistem için spec dosyası (TalepTakipSistemi.spec):**

# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('app.ico', '.')],  # İkon dosyası
    hiddenimports=['openpyxl.cell._writer'],  # Gizli importlar
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='TalepTakipSistemi',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    runtime_tmpdir=None,
    console=False,  # Konsol penceresi gösterme
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['app.ico'],  # Uygulama ikonu
)
```

### Build Alma

Spec dosyası hazır olduğunda build işlemini başlatabilirsiniz:

```
pyinstaller TalepTakipSistemi.spec
```

Build işlemi tamamlandığında, "dist" klasöründe executable dosyanız hazır olacaktır.

### Deployment (Dağıtım) Stratejileri

#### Yerel Ağ Dağıtımı

Kurum içi kullanım için en yaygın dağıtım yöntemidir.

**Paylaşımlı Klasör Yöntemi:**

1. Ağda erişilebilir bir paylaşımlı klasör oluşturun
2. Executable dosyaları bu klasöre kopyalayın
3. Gerekli konfigürasyon dosyalarını ekleyin
4. Kullanıcılara klasör yolunu ve erişim bilgilerini iletin

**Avantajları:**

- Merkezi güncelleme imkanı
- Kolay erişim
- Minimum kurulum

### Kullanıcı Bilgisayarlarına Kurulum

Her kullanıcının bilgisayarına ayrı ayrı kurulum yapılması gereken durumlarda:

**Kurulum Paketi Hazırlama:**

1. Tüm gerekli dosyaları bir klasörde toplayın
2. Basit bir kurulum scripti hazırlayın
3. ZIP dosyası olarak paketleyin

**Kurulum Scripti Örneği (install.bat):**

```
@echo off
echo ADANA ASKİ Talep Takip Sistemi Kurulumu
echo ========================================

:: Program Files klasörüne kopyala
xcopy /s /i "TalepTakipSistemi" "%ProgramFiles%\TalepTakipSistemi"

:: Masaüstüne kısayol oluştur
powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('%userprofile%\Desktop\Talep Takip.lnk');$s.TargetPath='%ProgramFiles%\TalepTakipSistemi\TalepTakipSistemi.exe';$s.Save()"

echo.
echo Kurulum tamamlandı!
pause
```

## Güncelleme Prosedürleri

Sistemin güncel tutulması, güvenlik ve performans açısından kritiktir.

### Versiyon Kontrolü

Her güncelleme öncesi mevcut versiyonu not edin ve yedek alın.

**Versiyon Numaralandırma:**

- Major.Minor.Patch formatı kullanın (örn: 1.2.3)
- Major: Büyük değişiklikler
- Minor: Yeni özellikler
- Patch: Hata düzeltmeleri

### Güncelleme Adımları
**Test Ortamında Deneme:**

1. Güncellemeleri önce test ortamında deneyin
2. Tüm fonksiyonları test edin
3. Veri uyumluluğunu kontrol edin

**Production Güncellemesi:**

1. Kullanıcıları bilgilendirin
2. Veritabanı yedeği alın
3. Eski executable'ı yedekleyin
4. Yeni versiyonu dağıtın
5. Kullanıcı geri bildirimlerini takip edin

### Sorun Giderme
#### Yaygın Sorunlar ve Çözümleri
**"Python bulunamadı" hatası:**

- Python'un PATH'e eklendiğinden emin olun
- Komut satırını yeniden başlatın
- Python kurulumunu kontrol edin

**"ModuleNotFoundError" hatası:**

- Eksik modülü pip ile kurun
- Sanal ortamın aktif olduğundan emin olun
- requirements.txt dosyasını kontrol edin

**Executable çalışmıyor:**

- Antivirüs yazılımını kontrol edin
- Windows Defender'a istisna ekleyin
- Visual C++ Redistributable kurulu mu kontrol edin

**Google Drive bağlantı hatası:**

- İnternet bağlantısını kontrol edin
- credentials.json dosyasının doğru yerde olduğundan emin olun
- token.json dosyasını silip yeniden yetkilendirme yapın

### Log Dosyalarını İnceleme
Sorun giderme için log dosyaları kritik bilgiler içerir.

**Log Konumu:**

```
data/logs/talep_takip.log
```

**Log Seviyeleri:**

- DEBUG: Detaylı bilgi
- INFO: Genel bilgi
- WARNING: Uyarılar
- ERROR: Hatalar
- CRITICAL: Kritik hatalar

### Destek Alma
**Sorunlarınızı çözemezseniz:**

1. Log dosyalarını toplayın
2. Hata ekran görüntüsü alın
3. Sistem bilgilerinizi not edin
4. IT departmanı ile iletişime geçin

### Güvenlik Önerileri
#### Deployment Güvenliği
**Dosya İzinleri:**

- Konfigürasyon dosyalarına sadece yetkili kullanıcılar erişebilmeli
- Log klasörü yazma izinlerine dikkat edilmeli
- Executable dosyalar değiştirilememeli

**Ağ Güvenliği:**

- Email trafiği için güvenli portlar kullanın
- Firewall ayarlarını kontrol edin
- VPN kullanımını değerlendirin

**Veri Güvenliği:**

- Düzenli yedekleme yapın
- Hassas bilgileri şifreleyin
- Kullanıcı erişimlerini logla
