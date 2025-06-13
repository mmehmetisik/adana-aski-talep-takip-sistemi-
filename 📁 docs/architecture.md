# 🏗️ Sistem Mimarisi

## Genel Bakış

ADANA ASKİ Talep Takip Sistemi, iki ana bileşenden oluşan modern bir mimari yapıya sahiptir. Sistem, kullanıcı rollerine göre farklı erişim seviyeleri sunarak güvenli ve verimli bir talep yönetimi sağlar.

## Sistem Bileşenleri

### 1. Ana Yönetim Sistemi (Main Management System)

Ana sistem, tam yetkili kullanıcıların talep oluşturma, güncelleme ve yönetim işlemlerini gerçekleştirdiği merkezi uygulamadır.

#### Temel Katmanlar:

**Sunum Katmanı (Presentation Layer)**
- Tkinter tabanlı masaüstü arayüzü
- Modern ve responsive tasarım
- Gradient efektler ve animasyonlar

**İş Mantığı Katmanı (Business Logic Layer)**
- Talep yönetimi modülü
- Kullanıcı kimlik doğrulama
- Email bildirim sistemi
- Raporlama ve export işlemleri

**Veri Katmanı (Data Layer)**
- SQLite veritabanı
- JSON tabanlı konfigürasyon dosyaları
- Yerel dosya sistemi yönetimi

### 2. Viewer Uygulaması (Read-Only Viewer)

Sadece görüntüleme yetkisine sahip kullanıcılar için tasarlanmış, Google Drive üzerinden veri senkronizasyonu yapan hafif bir istemci uygulaması.

#### Temel Özellikleri:

**Google Drive Entegrasyonu**
- OAuth 2.0 kimlik doğrulama
- Otomatik veri senkronizasyonu
- Offline çalışma desteği

**Veri Senkronizasyonu**
- Periyodik güncelleme kontrolü
- Değişiklik algılama
- Yerel cache yönetimi

## Veri Akışı

[Kullanıcı Girişi] → [Ana Sistem] → [SQLite DB] → [Google Drive] → [Viewer App]
↓
[Email Sistemi]

### İşlem Akışı:

1. **Talep Oluşturma**
   - Kullanıcı ana sistemde yeni talep oluşturur
   - Veri SQLite veritabanına kaydedilir
   - Email bildirimi ilgili kişilere gönderilir
   - Veri Google Drive'a yüklenir

2. **Veri Senkronizasyonu**
   - Viewer uygulaması periyodik olarak Drive'ı kontrol eder
   - Güncel veritabanı dosyası indirilir
   - Yerel cache güncellenir
   - Kullanıcı arayüzü yenilenir

## Güvenlik Mimarisi

### Kimlik Doğrulama
- SHA-256 şifre hashleme
- IP bazlı giriş deneme limiti
- Oturum timeout mekanizması

### Veri Güvenliği
- Hassas bilgilerin şifrelenmesi
- Google OAuth 2.0 güvenli bağlantı
- SSL/TLS email iletişimi

### Yetkilendirme
- Rol tabanlı erişim kontrolü
- İşlem bazlı yetki kontrolü
- Audit log sistemi

## Teknoloji Stack'i

### Backend
- **Python 3.x**: Ana programlama dili
- **SQLite**: Yerel veritabanı
- **Google Drive API**: Bulut depolama
- **SMTP**: Email gönderimi

### Frontend
- **Tkinter**: Ana sistem UI
- **CustomTkinter**: Modern UI bileşenleri
- **HTML/CSS**: Email şablonları

### Güvenlik
- **OAuth 2.0**: Google kimlik doğrulama
- **SHA-256**: Kriptografik hash
- **SSL/TLS**: Güvenli iletişim

## Ölçeklenebilirlik

Sistem, modüler yapısı sayesinde kolayca genişletilebilir:

- Yeni talep türleri eklenebilir
- Farklı departmanlar için özelleştirilebilir
- API katmanı eklenebilir
- Web tabanlı arayüze geçiş yapılabilir

## Performans Optimizasyonları

- Veritabanı indeksleme
- Lazy loading mekanizması
- Cache yönetimi
- Asenkron email gönderimi
- Thread-safe log sistemi
