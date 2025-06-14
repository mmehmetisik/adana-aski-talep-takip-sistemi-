# 🏢 ADANA ASKİ Talep Takip Sistemi

<p align="center">
  <img src="screenshots/main-system/01-login-screen.png" width="400" alt="Giriş Ekranı"/>
</p>

## 📋 Proje Hakkında

ADANA ASKİ Ceyhan Atıksu Arıtma Tesisi için geliştirilmiş, modern ve kullanıcı dostu bir talep takip sistemidir. Sistem, mal alımı, yapım işleri ve hizmet alımı taleplerinin dijital ortamda yönetilmesini sağlar.

### 🎯 Temel Özellikler

- ✅ **Modern Kullanıcı Arayüzü**: Gradient efektler ve animasyonlar ile zenginleştirilmiş tasarım
- ✅ **Çift Uygulama Mimarisi**: Yönetici ve görüntüleyici kullanıcılar için ayrı uygulamalar
- ✅ **Otomatik Email Bildirimleri**: HTML şablonları ile profesyonel bildirimler
- ✅ **Google Drive Entegrasyonu**: Bulut tabanlı veri senkronizasyonu
- ✅ **Güvenli Kimlik Doğrulama**: Şifrelenmiş kullanıcı yönetimi
- ✅ **Detaylı Loglama**: Tüm sistem aktivitelerinin kaydı

## 🏗️ Sistem Mimarisi

<p align="center">
  <img src="diagrams/system-architecture.png" width="600" alt="Sistem Mimarisi"/>
</p>

### 📱 İki Uygulama Yaklaşımı

#### 1. Ana Yönetim Sistemi
- Talep oluşturma ve güncelleme
- Kullanıcı yönetimi
- Email bildirim sistemi
- Raporlama ve Excel export

#### 2. Viewer Uygulaması
- Sadece görüntüleme yetkisi
- Google Drive üzerinden veri senkronizasyonu
- Arama ve filtreleme özellikleri
- Offline çalışma desteği

## 🛠️ Teknoloji Stack'i

### Backend & Core
- **Python 3.x** - Ana programlama dili
- **SQLite** - Yerel veritabanı yönetimi
- **Google Drive API** - Bulut senkronizasyonu
- **SMTP/Email** - Bildirim sistemi

### Frontend & UI
- **Tkinter** - Ana sistem arayüzü
- **CustomTkinter** - Modern UI bileşenleri
- **HTML/CSS** - Email şablonları

### Güvenlik & Auth
- **OAuth 2.0** - Google kimlik doğrulama
- **SHA-256** - Şifre hashleme
- **SSL/TLS** - Güvenli email iletimi

## 📸 Ekran Görüntüleri

### Ana Yönetim Sistemi

<table>
  <tr>
    <td><img src="screenshots/main-system/02-main-dashboard.png" width="300" alt="Yeni Talep"/></td>
    <td><img src="screenshots/main-system/03-new-request-form.png" width="300" alt="Talep Güncelle"/></td>
    <td><img src="screenshots/main-system/05-request-list.png" width="300" alt="Talep Listesi"/></td>
  </tr>
  <tr>
    <td align="center">Ana Panel</td>
    <td align="center">Yeni Talep Formu</td>
    <td align="center">Talep Listesi</td>
  </tr>
</table>

### Viewer Uygulaması

<table>
  <tr>
    <td><img src="screenshots/viewer-app/02-main-view.png" width="300" alt="Ana Görünüm"/></td>
    <td><img src="screenshots/viewer-app/03-search-filter.png" width="300" alt="Arama"/></td>
    <td><img src="screenshots/viewer-app/04-request-details.png" width="300" alt="Detay"/></td>
  </tr>
  <tr>
    <td align="center">Ana Görünüm</td>
    <td align="center">Arama & Filtreleme</td>
    <td align="center">Talep Detayları</td>
  </tr>
</table>

## 🎥 Demo
![proje](https://github.com/user-attachments/assets/ba34c781-a3a8-4bab-a12f-6fa106d4504b)


<p align="center">
  <img src="demos/workflow-demo.gif" width="600" alt="İş Akışı Demosu"/>
</p>

## 📧 Email Bildirimleri

Sistem, her talep oluşturulduğunda ve güncellendiğinde otomatik olarak ilgili kişilere profesyonel HTML email bildirimleri gönderir.

<p align="center">
  <img src="screenshots/main-system/06-email-notification.png" width="400" alt="Email Bildirimi"/>
</p>

## 🚀 Öne Çıkan Özellikler

### 🔐 Güvenlik
- Şifrelenmiş kullanıcı bilgileri
- IP bazlı giriş deneme limiti
- Oturum yönetimi ve zaman aşımı

### 📊 Raporlama
- Excel export özelliği
- Detaylı talep geçmişi
- İstatistiksel analizler

### 🔄 Senkronizasyon
- Google Drive üzerinden otomatik senkronizasyon
- Offline çalışma ve yerel cache
- Çakışma yönetimi

### 🎨 Modern Tasarım
- Responsive arayüz
- Gradient efektler ve animasyonlar
- Kullanıcı dostu form elemanları

## 👥 Geliştirici

**Mehmet IŞIK**  
ADANA ASKİ - Yazılım Geliştirici

## 📄 Lisans

Bu proje ADANA ASKİ'ye aittir. Tüm hakları saklıdır.

---

<p align="center">
  <i>🏢 ADANA ASKİ - Ceyhan Atıksu Arıtma Tesisi için geliştirilmiştir</i>
</p>
