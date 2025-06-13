# 📚 Kullanım Kılavuzu

Bu kılavuz, ADANA ASKİ Talep Takip Sistemi'nin hem ana yönetim sistemi hem de viewer uygulaması için detaylı kullanım talimatlarını içermektedir. Her iki uygulama da farklı kullanıcı grupları için tasarlanmış olup, farklı yetki ve özelliklere sahiptir.

## Ana Yönetim Sistemi Kullanımı

### Sisteme Giriş

Uygulama açıldığında karşınıza modern tasarımlı giriş ekranı gelecektir. Bu ekranda sistem güvenliği için çeşitli kontroller yapılmaktadır.

**Giriş Adımları:**

1. **Kullanıcı Adı Girişi**: Sistem yöneticiniz tarafından size verilen kullanıcı adınızı girin. Kullanıcı adları genellikle kısa ve kolay hatırlanabilir formattadır (örnek: admin, mali).

2. **Şifre Girişi**: Şifrenizi güvenli bir şekilde girin. Şifre girerken karakterler güvenlik amacıyla nokta (•) şeklinde görünecektir.

3. **Giriş Butonu**: Bilgilerinizi girdikten sonra "Giriş Yap" butonuna tıklayın veya Enter tuşuna basın.

**Güvenlik Uyarıları:**
- 5 başarısız giriş denemesinden sonra IP adresiniz 15 dakika boyunca engellenecektir
- Şifrenizi kimseyle paylaşmayın
- Oturumunuzu bitirdiğinizde mutlaka çıkış yapın

### Ana Menü ve Navigasyon

Başarılı giriş sonrasında ana menü ekranı açılacaktır. Üst kısımda kurum bilgileri ve kullanıcı adınız görünecektir.

**Ana Menü Seçenekleri:**

- **➕ Yeni Talep**: Yeni bir talep oluşturmak için kullanılır
- **🔄 Talep Güncelle**: Mevcut talepleri güncellemek için kullanılır
- **📋 Talep Listesi**: Tüm talepleri liste halinde görüntüler
- **📊 Excel Export**: Verileri Excel dosyası olarak dışa aktarır

### Yeni Talep Oluşturma

Yeni talep oluşturmak, sistemin en temel işlevidir. Bu işlem için aşağıdaki adımları takip edin:

**1. Form Alanlarının Doldurulması:**

**Talep No**: Sistem otomatik olarak bir talep numarası önerir (örnek: 2025/001). Bu numarayı değiştirebilirsiniz ancak benzersiz olmalıdır.

**İşin Adı**: Talebin ne ile ilgili olduğunu açık ve net bir şekilde yazın. Örnek: "B Blok Pompa Motoru Bakımı" veya "Klor Dozaj Pompası Alımı".

**İşi Alan Firma**: Eğer firma belirlenmişse firma adını girin. Henüz belirlenmemişse boş bırakabilirsiniz.

**Talep Tarihi**: Varsayılan olarak bugünün tarihi gelir. Farklı bir tarih girmek isterseniz değiştirebilirsiniz.

**Talep Durumu**: Açılır listeden uygun durumu seçin. Yeni talepler genellikle "Ceyhandan Gönderildi" durumu ile başlar.

**2. Alım Türü Seçimi:**

Bu bölüm, talebin hangi kategoride değerlendirileceğini belirler. Üç ana kategori vardır:

**Mal Alımı**: Herhangi bir malzeme, ekipman veya ürün alımı için kullanılır.
- Tüketim: Sarf malzemeleri, kimyasallar, yedek parçalar
- Demirbaş: Kalıcı ekipmanlar, makineler, mobilyalar

**Yapım İşleri**: İnşaat, tadilat veya yapım işleri için kullanılır. Alt kategorisi yoktur.

**Hizmet Alımı**: Hizmet satın alımları için kullanılır.
- Bakım Onarım: Periyodik bakımlar, arıza onarımları
- Diğer: Danışmanlık, eğitim, temizlik gibi diğer hizmetler

**3. Açıklama Girişi:**

Açıklama alanına taleple ilgili detaylı bilgileri girin. Bu alan için öneriler:
- Talebin gerekçesini açıklayın
- Teknik detayları belirtin
- Aciliyet durumunu belirtin
- Varsa referans numaraları ekleyin

**4. Talebi Kaydetme:**

Tüm alanları doldurduktan sonra "💾 Talebi Kaydet" butonuna tıklayın. Sistem otomatik olarak:
- Talebi veritabanına kaydeder
- İlgili kişilere email bildirimi gönderir
- Başarı mesajı gösterir

### Talep Güncelleme

Mevcut talepleri güncellemek için bu menüyü kullanın. Güncelleme yapmak talep sürecinin takibi açısından kritiktir.

**Güncelleme Adımları:**

1. **Talep Seçimi**: Açılır listeden güncellemek istediğiniz talebi seçin. Liste "Talep No - İş Adı (Mevcut Durum)" formatında gösterilir.

2. **Güncelleme Formunun Doldurulması**:
   - **Kontrol Tarihi**: Güncelleme yapılan tarih
   - **Yıl**: Otomatik olarak mevcut yıl gelir
   - **Yeni Durum**: Talebin yeni durumunu seçin
   - **İşi Alan Firma**: Firma bilgisi güncellenmişse girin
   - **Açıklama**: Güncelleme ile ilgili detayları yazın

3. **Güncellemeyi Kaydetme**: Form doldurulduktan sonra "🔄 Güncellemeyi Kaydet" butonuna tıklayın.

### Talep Listesi Görüntüleme

Sistemdeki tüm talepleri tablo formatında görüntülemek için kullanılır.

**Liste Özellikleri:**
- Talep No, İş Adı, Tarih, Durum, Firma ve Alım Türü bilgileri gösterilir
- Listede arama yapabilirsiniz
- Herhangi bir satıra tıklayarak detayları görebilirsiniz
- Seçili talebi silebilirsiniz (dikkatli kullanın!)

**Talep Silme:**
1. Listeden silmek istediğiniz talebi seçin
2. "🗑️ Seçili Talebi Sil" butonuna tıklayın
3. Onay mesajında "Evet" seçeneğini tıklayın

### Excel Export İşlemi

Tüm talep verilerini Excel dosyası olarak dışa aktarmak için kullanılır.

**Export Özellikleri:**
- Tüm talepler ana sayfada listelenir
- Her talep için ayrı detay sayfası oluşturulur
- Profesyonel formatlama uygulanır
- Dosya otomatik olarak data klasörüne kaydedilir

## Viewer Uygulaması Kullanımı

Viewer uygulaması, sadece görüntüleme yetkisine sahip kullanıcılar için tasarlanmıştır.

### İlk Çalıştırma ve Google Yetkilendirme

Uygulama ilk açıldığında Google hesabınızla giriş yapmanız gerekecektir.

**Yetkilendirme Adımları:**
1. Uygulama otomatik olarak web tarayıcınızı açacaktır
2. Google hesabınızla giriş yapın
3. Uygulama izinlerini onaylayın (sadece Drive okuma izni)
4. Yetkilendirme tamamlandığında uygulama otomatik olarak açılacaktır

### Ana Ekran Kullanımı

Viewer uygulamasının ana ekranı, talepleri liste halinde gösterir.

**Ekran Bölümleri:**
- **Üst Başlık**: Kurum bilgileri ve son güncelleme zamanı
- **Arama Alanı**: Talep no veya iş adına göre arama yapabilirsiniz
- **Talep Listesi**: Tüm talepler kart formatında listelenir
- **Güncelle Butonu**: Manuel olarak Drive'dan veri çekmek için

### Arama ve Filtreleme

Arama kutusuna yazdığınız metne göre sonuçlar anında filtrelenir.

**Arama İpuçları:**
- Talep numarasının bir kısmını yazmanız yeterlidir
- İş adında geçen kelimeleri arayabilirsiniz
- Büyük/küçük harf duyarlılığı yoktur

### Talep Detaylarını Görüntüleme

Listeden herhangi bir talebe tıkladığınızda detay penceresi açılır.

**Detay Penceresi İçeriği:**
- Talep numarası ve iş adı
- Tüm talep bilgileri
- Son durum ve firma bilgisi
- Detaylı açıklama
- Güncelleme geçmişi (varsa)

### Otomatik Güncelleme

Uygulama varsayılan olarak her 5 dakikada bir Google Drive'ı kontrol eder ve yeni verileri indirir.

**Güncelleme Göstergeleri:**
- Ana ekranda "Son Güncelleme" zamanı gösterilir
- Güncelleme sırasında durum çubuğunda bilgi gösterilir
- Başarılı güncelleme sonrası liste otomatik yenilenir

## Genel İpuçları ve Öneriler

### Performans İpuçları

1. **Düzenli Güncelleme**: Talep durumlarını düzenli olarak güncelleyin
2. **Açıklayıcı Notlar**: Açıklama alanlarını detaylı doldurun
3. **Doğru Kategori**: Alım türünü doğru seçin

### Güvenlik Önerileri

1. **Şifre Güvenliği**: Şifrenizi düzenli olarak değiştirin
2. **Oturum Kapatma**: İşiniz bittiğinde mutlaka çıkış yapın
3. **Yetkisiz Erişim**: Hesabınızı başkalarıyla paylaşmayın

### Sorun Giderme

**Giriş Yapamıyorum:**
- Kullanıcı adı ve şifrenizi kontrol edin
- Caps Lock tuşunun kapalı olduğundan emin olun
- 5 deneme hakkınızı doldurduysanız 15 dakika bekleyin

**Email Bildirimi Almıyorum:**
- Spam/gereksiz klasörünü kontrol edin
- IT departmanı ile email adresinizin doğruluğunu teyit edin

**Viewer Uygulaması Güncelleme Yapmıyor:**
- İnternet bağlantınızı kontrol edin
- Google hesap yetkilendirmesini yenileyin
- Manuel güncelleme butonunu kullanın

### İletişim ve Destek

Teknik sorunlar veya öneriler için:
- Sistem Yöneticisi: IT Departmanı
- Geliştirici: Mehmet Işık
- Birim: Ceyhan Atıksu Arıtma Tesisi
