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

```
┌─────────────────────────────────┐     ┌─────────────────────────────────┐
│      ANA YÖNETİM SİSTEMİ        │     │      VIEWER UYGULAMASI          │
│                                 │     │                                 │
│  • Talep Oluşturma/Güncelleme  │     │  • Sadece Görüntüleme          │
│  • Kullanıcı Yönetimi          │     │  • Google Drive Sync           │
│  • Email Bildirimleri          │     │  • Arama ve Filtreleme         │
│  • Excel Export                │     │  • Offline Çalışma             │
└────────────┬───────────────────┘     └──────────────┬──────────────────┘
             │                                         │
             ▼                                         ▼
        ┌─────────────────────┐                 ┌──────────────┐
        │   SQLite Database   │      ◄──────►   │ Google Drive │
        │                     │                 │   Storage    │
        │  • Talepler         │                 └──────────────┘
        │  • Güncellemeler    │
        └─────────────────────┘
                    │
                    ▼
            ┌──────────────┐
            │ Email Server │
            │    (SMTP)    │
            └──────────────┘
```

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

#### Yeni Talep Ekranı

![Ekran görüntüsü 2025-06-13 104151](https://github.com/user-attachments/assets/6792e21b-60e3-4f78-8a93-a9e669727818)

![Ekran görüntüsü 2025-06-13 131857](https://github.com/user-attachments/assets/1dd0ecd8-1027-4f9d-aaa8-3a3ac948082f)

#### Talep güncelleme Ekranı

![Ekran görüntüsü 2025-06-13 132021](https://github.com/user-attachments/assets/e2653ad9-f9ab-474c-8d31-2723128f4a26)

#### Talep Listesi ekranı

![Ekran görüntüsü 2025-06-13 132037](https://github.com/user-attachments/assets/f06074cb-2421-4134-9c67-d4f7e143ae74)

![Ekran görüntüsü 2025-06-13 132050](https://github.com/user-attachments/assets/59618b7b-a949-4873-abbe-873ad7ef9252)

#### Excel Export

![Ekran görüntüsü 2025-06-13 132109](https://github.com/user-attachments/assets/9411b1ab-7fd3-4581-901e-e7c388832ef8)

![Ekran görüntüsü 2025-06-13 132125](https://github.com/user-attachments/assets/60e64cce-92dc-4a05-8987-1cc514e39b29)


### Viewer Uygulaması



## 🎥 Demo
![proje](https://github.com/user-attachments/assets/ba34c781-a3a8-4bab-a12f-6fa106d4504b)


<p align="center">
  <img src="demos/workflow-demo.gif" width="600" alt="İş Akışı Demosu"/>
</p>

## 📧 Email Bildirimleri

Sistem, her talep oluşturulduğunda ve güncellendiğinde otomatik olarak ilgili kişilere profesyonel HTML email bildirimleri gönderir.

![Ekran görüntüsü 2025-06-13 131651](https://github.com/user-attachments/assets/d31f5bb8-68c1-4b73-9a94-81b34b580b75)

![Ekran görüntüsü 2025-06-13 131727](https://github.com/user-attachments/assets/dca1de37-885f-4a45-b81c-02b4f67651c3)



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

🛠️ Kullanılan Teknolojiler

Python 3.x - Ana programlama dili
Tkinter & CustomTkinter - Kullanıcı arayüzü
SQLite - Veritabanı
Google Drive API - Bulut entegrasyonu
SMTP - Email gönderimi

## 👥 Geliştirici

**Mehmet IŞIK**  
ADANA ASKİ - Yazılım Geliştirici

## 📄 Lisans

Bu proje Mehmet IŞIK'a aittir. Tüm hakları saklıdır.

---

<p align="center">
  <i>🏢 ADANA ASKİ - Ceyhan Atıksu Arıtma Tesisi için geliştirilmiştir</i>
</p>
