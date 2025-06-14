# 🏗️ Sistem Mimarisi Diyagramı

Bu diyagram, ADANA ASKİ Talep Takip Sistemi'nin genel mimarisini ve bileşenler arası ilişkileri göstermektedir.

## Diyagram Açıklaması

┌─────────────────────────────────────────────────────────────────────────────┐
│                          ADANA ASKİ TALEP TAKİP SİSTEMİ                     │
│                              Sistem Mimarisi Genel Görünüm                   │
└─────────────────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────┐     ┌─────────────────────────────────┐
│         KULLANICI KATMANI           │     │        KULLANICI KATMANI        │
│  ┌─────────────────────────────┐   │     │  ┌─────────────────────────┐   │
│  │    Ana Yönetim Sistemi      │   │     │  │    Viewer Uygulaması    │   │
│  │                             │   │     │  │                         │   │
│  │  • Tkinter GUI              │   │     │  │  • CustomTkinter GUI    │   │
│  │  • Tam Yetki                │   │     │  │  • Sadece Okuma         │   │
│  │  • Windows/Linux/Mac        │   │     │  │  • Windows/Linux/Mac    │   │
│  └─────────────┬───────────────┘   │     │  └───────────┬─────────────┘   │
│                │                    │     │              │                  │
└────────────────┼────────────────────┘     └──────────────┼──────────────────┘
│                                          │
▼                                          ▼
┌─────────────────────────────────────┐     ┌─────────────────────────────────┐
│         İŞ MANTIĞI KATMANI          │     │      SENKRON KATMANI            │
│  ┌─────────────────────────────┐   │     │  ┌─────────────────────────┐   │
│  │   Talep Yönetimi Modülü     │   │     │  │   Google Drive Manager  │   │
│  │   • CRUD İşlemleri          │   │     │  │   • OAuth 2.0 Auth      │   │
│  │   • İş Kuralları            │   │     │  │   • File Download       │   │
│  │   • Validasyon              │   │     │  │   • Auto Sync           │   │
│  └─────────────┬───────────────┘   │     │  └───────────┬─────────────┘   │
│                │                    │     │              │                  │
│  ┌─────────────▼───────────────┐   │     │              │                  │
│  │   Email Bildirim Sistemi    │   │     │              │                  │
│  │   • SMTP Client             │   │     │              ▼                  │
│  │   • HTML Templates          │   │     │     ┌──────────────┐           │
│  │   • Grup Yönetimi           │   │◄────┼─────│ Google Drive │           │
│  └─────────────┬───────────────┘   │     │     │   Storage    │           │
│                │                    │     │     └──────────────┘           │
│  ┌─────────────▼───────────────┐   │     │                                 │
│  │   Kullanıcı Yönetimi        │   │     └─────────────────────────────────┘
│  │   • Authentication          │   │
│  │   • Authorization           │   │
│  │   • Session Management      │   │
│  └─────────────┬───────────────┘   │
│                │                    │
└────────────────┼────────────────────┘
│
▼
┌─────────────────────────────────────┐
│          VERİ KATMANI               │
│  ┌─────────────────────────────┐   │
│  │      SQLite Database         │   │     ┌─────────────────────────────┐
│  │   • Talepler Tablosu         │   │     │    YARDIMCI SERVİSLER       │
│  │   • Güncellemeler Tablosu    │   │     │  ┌─────────────────────┐   │
│  │   • İndeksler                │   │     │  │   Log Sistemi       │   │
│  └─────────────┬───────────────┘   │     │  │   • Dosya Bazlı     │   │
│                │                    │     │  │   • Rotating Logs   │   │
│  ┌─────────────▼───────────────┐   │     │  │   • Seviye Bazlı    │   │
│  │      JSON Dosyaları          │   │     │  └─────────────────────┘   │
│  │   • users.json               │   │     │                             │
│  │   • email_config.json        │   │     │  ┌─────────────────────┐   │
│  │   • token.json (Viewer)      │   │     │  │   Excel Manager     │   │
│  └─────────────────────────────┘   │     │  │   • Import/Export   │   │
│                                     │     │  │   • Formatlama      │   │
└─────────────────────────────────────┘     │  └─────────────────────┘   │
└─────────────────────────────┘


## Mimari Bileşenler Detayı

### 1. Kullanıcı Katmanı (Presentation Layer)

#### Ana Yönetim Sistemi
- **Teknoloji**: Tkinter (Python standart GUI kütüphanesi)
- **Özellikler**: 
  - Modern ve responsive tasarım
  - Gradient efektler ve animasyonlar
  - Form validasyonları
  - Gerçek zamanlı geri bildirimler

#### Viewer Uygulaması
- **Teknoloji**: CustomTkinter (Modern UI kütüphanesi)
- **Özellikler**:
  - Yuvarlak köşeli modern elemanlar
  - Smooth scroll ve animasyonlar
  - Dark/Light tema desteği (potansiyel)
  - Minimalist tasarım

### 2. İş Mantığı Katmanı (Business Logic Layer)

#### Talep Yönetimi Modülü
- Yeni talep oluşturma
- Talep güncelleme
- Talep silme
- Durum yönetimi
- Alım türü kategorizasyonu

#### Email Bildirim Sistemi
- Otomatik bildirim tetikleme
- HTML email şablonları
- Grup bazlı alıcı yönetimi
- Hata yönetimi ve retry mekanizması

#### Kullanıcı Yönetimi
- SHA-256 şifre hashleme
- IP bazlı güvenlik kontrolleri
- Oturum yönetimi
- Rol bazlı yetkilendirme

### 3. Veri Katmanı (Data Layer)

#### SQLite Database
**Talepler Tablosu**:
- Birincil anahtar: `id`
- Benzersiz alan: `talep_no`
- İndekslenmiş alanlar: `talep_no`, `mevcut_durum`

**Güncellemeler Tablosu**:
- Foreign key: `talep_no` → `talepler.talep_no`
- Otomatik timestamp: `guncelleme_zamani`

#### JSON Dosyaları
- **users.json**: Kullanıcı bilgileri ve hash'lenmiş şifreler
- **email_config.json**: SMTP ayarları ve alıcı grupları
- **token.json**: Google OAuth token (sadece Viewer)

### 4. Entegrasyon Katmanı

#### Google Drive Entegrasyonu
- OAuth 2.0 güvenli kimlik doğrulama
- Periyodik senkronizasyon (5 dakika)
- Offline cache mekanizması
- Hata toleransı

### 5. Yardımcı Servisler

#### Log Sistemi
- Thread-safe implementasyon
- Rotating file handler
- Seviye bazlı loglama (DEBUG, INFO, WARNING, ERROR, CRITICAL)

#### Excel Manager
- Database → Excel export
- Profesyonel formatlama
- Multi-sheet desteği

## Veri Akışı

1. Kullanıcı İsteği
↓
2. GUI Katmanı (Validasyon)
↓
3. İş Mantığı (İşleme)
↓
4. Veri Katmanı (Kayıt)
↓
5. Bildirim Sistemi (Email)
↓
6. Google Drive (Sync - sadece Viewer için)
