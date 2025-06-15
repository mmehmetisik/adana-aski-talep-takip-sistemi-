# 🏢 ADANA ASKİ Talep Takip Sistemi



![Giriş Ekranı](https://github.com/user-attachments/assets/07d8f13d-ddc6-4180-becd-82c7591381ab)


## 📋 Proje Hakkında

ADANA ASKİ Ceyhan Atıksu Arıtma Tesisi için geliştirilmiş, modern ve kullanıcı dostu bir talep takip sistemidir. Sistem, mal alımı, yapım işleri ve hizmet alımı taleplerinin dijital ortamda yönetilmesini sağlar.

## 📖 Projenin Hikayesi
Ceyhan Atıksu Arıtma Tesisi olarak, günlük operasyonlarımızda yüzlerce satın alma talebi oluşturuyoruz. Mekanik arızalar için yedek parçalar, elektrik sistemleri için malzemeler, laboratuvar analizleri için kimyasallar, proje çalışmaları için ekipmanlar... Her birim kendi ihtiyaçları doğrultusunda sürekli talep oluşturuyor.

🔴 Sorun: Kağıt Üzerinde Kaos
Geleneksel sistemde, her talep evrak olarak hazırlanıp taşınır kayıt görevlisine teslim ediliyordu. Ancak bu yöntem ciddi sorunlar yaratmaya başladı:

- Takip Zorluğu: "Bu talep hangi aşamada?", "Kim ne zaman talep yapmış?", "Nerede bekliyor?" sorularına cevap bulmak neredeyse imkansızdı
- Kayıp Talepler: Yoğunluktan bazı talepler kayboluyordu
- Geciken Bilgilendirmeler: Excel listelerinin güncellenmesi çok geç oluyordu
- İletişim Kopukluğu: Talep sahipleri, taleplerinin durumunu öğrenmek için sürekli telefon açmak zorunda kalıyordu

💡 Çözüm: Dijital Dönüşüm
Bu karmaşayı sonlandırmak için iki aşamalı bir dijital çözüm geliştirdim:

1️⃣ Ana Talep Takip Sistemi
Taşınır kayıt görevlisinin kullanacağı merkezi sistem. Tüm talepleri dijital ortamda kaydediyor, durumlarını güncelliyor ve her işlemde otomatik email bildirimleri gönderiyor. Artık hiçbir talep kaybolmuyor, her şey kayıt altında.

2️⃣ Viewer Uygulaması
Talep sahipleri ve yöneticiler için tasarlanmış görüntüleme arayüzü. Herkes kendi taleplerinin durumunu anlık olarak görebiliyor. Telefon trafiği %90 azaldı, herkes bir tıkla bilgiye ulaşabiliyor.

✅ Sonuç: Verimlilik Patlaması
Bu sistem sayesinde:

Talep takip süresi %75 azaldı
Kayıp talep sayısı sıfıra indi
Telefon trafiği %90 düştü
Tüm süreç şeffaf ve izlenebilir hale geldi

Bugün Ceyhan Atıksu Arıtma Tesisi'nde bu sistem aktif olarak kullanılıyor ve günde ortalama 50+ talebin sorunsuz yönetilmesini sağlıyor. Kağıt karmaşasından dijital düzene geçiş, sadece bir yazılım projesi değil, aynı zamanda kurumsal bir başarı hikayesi oldu.

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

![Ekran görüntüsü 2025-06-15 145008](https://github.com/user-attachments/assets/ef200781-af53-4e09-97c8-3d62f10abea0)

![Ekran görüntüsü 2025-06-15 145021](https://github.com/user-attachments/assets/de67c05a-84df-4c98-a14b-d0db36fa7cc2)

![Ekran görüntüsü 2025-06-15 145040](https://github.com/user-attachments/assets/c6df1881-a15b-4520-a50d-c79f8aac28c9)


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

## ❓ Sıkça Sorulan Sorular

**S: Viewer uygulaması internet olmadan çalışır mı?**

**C: Evet, son senkronize edilen verilerle offline çalışabilir.**

**S: Kaç kullanıcı aynı anda sistemi kullanabilir?**

**C: Ana sistemde sınırsız, viewer uygulaması salt okunur olduğu için performans sorunu yaşanmaz.**

**S: Email bildirimleri zorunlu mu?**

**C: Hayır, konfigürasyondan devre dışı bırakılabilir.**

## 👥 Geliştirici

**Mehmet IŞIK**  
ADANA ASKİ - Yazılım Geliştirici

## 📄 Lisans

Bu proje Mehmet IŞIK'a aittir. Tüm hakları saklıdır.

---

<p align="center">
  <i>🏢 ADANA ASKİ - Ceyhan Atıksu Arıtma Tesisi için geliştirilmiştir</i>
</p>
