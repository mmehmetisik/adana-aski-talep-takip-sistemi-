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
