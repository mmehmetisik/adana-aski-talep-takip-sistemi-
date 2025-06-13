# 🚀 Özellikler

## Ana Yönetim Sistemi Özellikleri

### 🔐 Kullanıcı Yönetimi ve Güvenlik

**Gelişmiş Kimlik Doğrulama Sistemi**
Sistem, kullanıcı güvenliğini en üst düzeyde tutmak için çok katmanlı bir güvenlik yapısı kullanır. Kullanıcı şifreleri SHA-256 algoritması ile hash'lenerek saklanır. Bu sayede veritabanına erişim sağlansa bile şifreler okunamaz durumda kalır.

**IP Bazlı Güvenlik Önlemleri**
Her giriş denemesi IP adresi ile birlikte loglanır. Belirli sayıda başarısız giriş denemesinden sonra (varsayılan 5), ilgili IP adresi geçici olarak engellenir. Bu süre varsayılan olarak 15 dakikadır ve konfigürasyon dosyasından değiştirilebilir.

**Oturum Yönetimi**
Kullanıcı oturumları güvenli bir şekilde yönetilir. Her başarılı girişte son giriş zamanı kaydedilir ve uzun süre işlem yapılmayan oturumlar otomatik olarak sonlandırılır.

### 📝 Talep Yönetimi

**Kapsamlı Talep Oluşturma Formu**
Yeni talep oluşturma ekranı, kullanıcının ihtiyaç duyabileceği tüm alanları içerir:
- Otomatik talep numarası üretimi (2025/001 formatında)
- Detaylı iş tanımı alanı
- Dinamik tarih seçimi
- Firma bilgisi girişi
- Kapsamlı açıklama alanı

**Alım Türü Kategorilendirmesi**
Sistem, üç ana alım türünü destekler ve her birinin alt kategorileri vardır:
- **Mal Alımı**: Tüketim, Demirbaş
- **Yapım İşleri**: Tek seçenek
- **Hizmet Alımı**: Bakım Onarım, Diğer

**Durum Takip Sistemi**
Her talep, yaşam döngüsü boyunca takip edilebilir durumlardan geçer:
- Ceyhandan Gönderildi
- Burakda Bekliyor
- Şube Müdüründe İmzada
- Daire Başkanında İmzada
- Genel Müdür Yardımcısında İmzada
- Destek Biriminde
- Fiyat Araştırmasında
- Firmada
- İade Edildi

### 📧 Otomatik Email Bildirimleri

**HTML Tabanlı Profesyonel Email Şablonları**
Sistem, modern ve responsive HTML email şablonları kullanır. Her email:
- Kurum logosu ve kurumsal kimlik öğelerini içerir
- Gradient arka planlar ve modern tasarım elementleri kullanır
- Mobil cihazlarda da düzgün görüntülenir
- Talep detaylarını açık ve anlaşılır şekilde sunar

**Akıllı Bildirim Sistemi**
Email bildirimleri şu durumlarda otomatik olarak gönderilir:
- Yeni talep oluşturulduğunda
- Talep durumu güncellendiğinde
- Kritik durum değişikliklerinde

**Grup Bazlı Email Yönetimi**
Farklı kullanıcı gruplarına (yöneticiler, mühendisler, diğer) ayrı ayrı veya toplu email gönderilebilir.

### 📊 Raporlama ve Analiz

**Excel Export Özelliği**
Tüm talep verileri, detaylı Excel raporları olarak dışa aktarılabilir. Export edilen dosya:
- Ana özet sayfası (dashboard)
- Her talep için ayrı detay sayfaları
- Profesyonel formatlama ve renklendirme
- Otomatik sütun genişliği ayarları

**İstatistiksel Analizler**
Sistem, talep verilerini analiz ederek şu istatistikleri sunar:
- Toplam talep sayısı
- Durum bazlı dağılım
- Zaman bazlı trendler
- Firma bazlı analizler

### 🎨 Modern Kullanıcı Arayüzü

**Responsive ve Estetik Tasarım**
- Gradient efektler ve yumuşak geçişler
- Hover animasyonları
- Modern renk paleti
- Kullanıcı dostu form elemanları

**Akıllı Form Validasyonu**
Tüm form alanları, veri girişi sırasında otomatik olarak kontrol edilir ve kullanıcıya anında geri bildirim verilir.

## Viewer Uygulaması Özellikleri

### 🔄 Google Drive Senkronizasyonu

**Otomatik Veri Güncelleme**
Viewer uygulaması, belirlenen aralıklarla (varsayılan 5 dakika) Google Drive'ı kontrol eder ve güncel veritabanını indirir.

**Offline Çalışma Desteği**
İnternet bağlantısı olmadığında, son indirilen veritabanı kullanılarak çalışmaya devam edilir.

### 🔍 Gelişmiş Arama ve Filtreleme

**Çoklu Arama Kriterleri**
- Talep numarasına göre arama
- İş adına göre arama
- Durum bazlı filtreleme
- Tarih aralığı filtreleme

**Anlık Sonuç Güncelleme**
Arama kutusuna yazılan her karakterde sonuçlar anında filtrelenir.

### 📱 Modern ve Responsive Arayüz

**CustomTkinter Tabanlı Tasarım**
- Yuvarlak köşeli modern butonlar
- Smooth scroll efektleri
- Dinamik renk geçişleri
- Responsive layout yapısı

### 🔒 Güvenlik Özellikleri

**OAuth 2.0 Kimlik Doğrulama**
Google hesabı üzerinden güvenli giriş yapılır. Kullanıcı kimlik bilgileri yerel olarak saklanmaz.

**Sadece Okuma Yetkisi**
Viewer uygulaması, veritabanında hiçbir değişiklik yapamaz. Sadece görüntüleme yetkisine sahiptir.

## 🔧 Teknik Özellikler

### Performans Optimizasyonları

**Veritabanı İndeksleme**
Sık kullanılan sorgular için veritabanı indeksleri oluşturulur, bu sayede arama işlemleri çok hızlı gerçekleşir.

**Thread-Safe İşlemler**
Log yazma ve veritabanı işlemleri thread-safe olarak tasarlanmıştır. Birden fazla işlem aynı anda güvenli bir şekilde çalışabilir.

**Bellek Yönetimi**
Büyük veri setleri ile çalışırken bellek kullanımı optimize edilmiştir. Lazy loading teknikleri kullanılır.

### Hata Yönetimi

**Kapsamlı Hata Yakalama**
Tüm kritik işlemler try-catch blokları ile korunur. Hatalar detaylı olarak loglanır.

**Kullanıcı Dostu Hata Mesajları**
Teknik hata detayları kullanıcıdan gizlenir, yerine anlaşılır hata mesajları gösterilir.

**Otomatik Kurtarma Mekanizmaları**
Bazı hata durumlarında sistem otomatik olarak kendini toparlayabilir (örneğin, bağlantı kopması durumunda yeniden deneme).
