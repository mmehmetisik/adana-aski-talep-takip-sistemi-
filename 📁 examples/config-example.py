"""
ADANA ASKİ Talep Takip Sistemi - Örnek Konfigürasyon Dosyası

Bu dosya, gerçek config.py dosyasının hassas bilgiler içermeyen örnek versiyonudur.
Sistemi kurarken bu dosyayı referans alarak kendi konfigürasyonunuzu oluşturabilirsiniz.

NOT: Bu dosyadaki değerler örnek amaçlıdır. Gerçek kullanımda kendi değerlerinizi girmeniz gerekir.
"""

import os
from datetime import datetime

# ==================== TEMEL AYARLAR ====================

# Proje Bilgileri
PROJE_ADI = "ADANA ASKİ Talep Takip Sistemi"
PROJE_VERSIYONU = "1.0.0"
KURUM_ADI = "ADANA ASKİ GENEL MÜDÜRLÜĞÜ"
BIRIM_ADI = "Ceyhan Atıksu Arıtma Tesisi"

# Dosya ve Klasör Yolları
# NOT: Bu yollar otomatik olarak oluşturulacaktır
VERI_KLASORU = "data"
LOG_KLASORU = os.path.join(VERI_KLASORU, "logs")
EXCEL_DOSYASI = os.path.join(VERI_KLASORU, "talep_takip.xlsx")
KULLANICI_DOSYASI = os.path.join(VERI_KLASORU, "users.json")
EMAIL_CONFIG_DOSYASI = os.path.join(VERI_KLASORU, "email_config.json")

# ==================== GÖRSEL AYARLAR ====================

# Modern Renk Paleti
# Bu renkler, uygulamanın görsel tutarlılığını sağlar
RENKLER = {
    # Ana renkler - Gradient efektler için
    "ana_mavi": "#2563eb",      # Canlı mavi - Ana tema rengi
    "ana_mavi_koyu": "#1e40af",  # Koyu mavi - Gradient ve hover efektleri için
    "ikincil_mavi": "#3b82f6",   # Orta ton mavi - İkincil elemanlar için
    "acik_mavi": "#dbeafe",      # Açık mavi - Arka planlar için
    
    # Nötr renkler - Genel kullanım için
    "beyaz": "#ffffff",
    "acik_gri": "#f8fafc",       # Ana arkaplan rengi
    "gri_100": "#f1f5f9",        # Kart arka planları için
    "orta_gri": "#64748b",       # İkincil metin rengi
    "koyu_gri": "#1e293b",       # Ana metin rengi
    
    # Durum renkleri - Talep durumları için
    "basarili": "#10b981",       # Yeşil - Başarılı işlemler
    "basarili_acik": "#d1fae5",  # Açık yeşil - Başarı arka planı
    "uyari": "#f59e0b",          # Turuncu - Uyarılar
    "uyari_acik": "#fef3c7",     # Açık turuncu - Uyarı arka planı
    "hata": "#ef4444",           # Kırmızı - Hatalar
    "hata_acik": "#fee2e2",      # Açık kırmızı - Hata arka planı
    "bilgi": "#06b6d4",          # Cyan - Bilgi mesajları
    "bilgi_acik": "#cffafe",     # Açık cyan - Bilgi arka planı
    "mor": "#8b5cf6",            # Mor - Özel durumlar
    "mor_acik": "#ede9fe",       # Açık mor - Özel durum arka planı
}

# Font Ayarları
FONTLAR = {
    "ana_font": ("Segoe UI", 10),
    "baslik_font": ("Segoe UI Semibold", 12),
    "buyuk_baslik_font": ("Segoe UI", 16, "bold"),
    "kucuk_font": ("Segoe UI", 9),
    "buton_font": ("Segoe UI", 10, "bold"),
    "ikon_font": ("Segoe UI Emoji", 14)
}

# Pencere Boyutları
PENCERE_BOYUTLARI = {
    "giris_penceresi": "450x650",
    "ana_pencere": "900x700",
    "minimum_boyut": (800, 500),
    "giris_minimum": (450, 650)
}

# ==================== İŞ KURALLARI ====================

# Talep Durumları
# Bu durumlar, talebin yaşam döngüsündeki aşamaları temsil eder
TALEP_DURUMLARI = [
    "Ceyhandan Gönderildi",        # İlk durum - Talep oluşturuldu
    "Burakda Bekliyor",            # İlk kontrol aşaması
    "Şube Müdüründe İmzada",       # Birinci onay seviyesi
    "Daire Başkanında İmzada",     # İkinci onay seviyesi
    "Genel Müdür Yardımcısında İmzada",  # Üçüncü onay seviyesi
    "Destek Biriminde",            # Teknik değerlendirme
    "Fiyat Araştırmasında",        # Piyasa araştırması
    "Firmada",                     # İş firmaya verildi
    "İade Edildi"                  # Talep iptal edildi
]

# Email Bildirim Kuralları
EMAIL_BILDIRIM_KURALLARI = {
    "yeni_talep": True,          # Yeni talep oluştuğunda email gönder
    "durum_degisikli": True,     # Durum değiştiğinde email gönder
    "tamamlanan_isler": True,    # İş tamamlandığında email gönder
    "iptal_durumu": False        # İptal durumunda email gönderme
}

# ==================== GÜVENLİK AYARLARI ====================

# Şifre Kuralları
SIFRE_KURALLARI = {
    "min_uzunluk": 6,            # Minimum şifre uzunluğu
    "max_uzunluk": 50,           # Maksimum şifre uzunluğu
    "ozel_karakter_gerekli": False,  # Özel karakter zorunluluğu
    "sayi_gerekli": False        # Sayı zorunluluğu
}

# Oturum Ayarları
OTURUM_AYARLARI = {
    "max_basarisiz_deneme": 5,    # Maximum başarısız giriş denemesi
    "engelleme_suresi_dakika": 15, # IP engelleme süresi
    "oturum_timeout_saat": 8      # Oturum zaman aşımı
}

# ==================== SİSTEM AYARLARI ====================

# Log Ayarları
LOG_AYARLARI = {
    "max_dosya_boyutu_mb": 5,     # Log dosyası maksimum boyutu
    "max_yedek_sayisi": 10,       # Maksimum yedek log dosyası sayısı
    "log_seviyesi": "INFO",       # DEBUG, INFO, WARNING, ERROR, CRITICAL
    "konsol_ciktisi": True        # Konsola da log yaz
}

# Excel Ayarları
EXCEL_AYARLARI = {
    "sheet_isimleri": {
        "dashboard": "Genel Durum",     # Ana özet sayfası
        "talep_prefix": "Talep_"        # Talep detay sayfası öneki
    },
    "max_sheet_sayisi": 100,      # Maksimum sheet sayısı
    "otomatik_kayit": True        # Her işlemde otomatik kaydet
}

# Email Ayarları
EMAIL_AYARLARI = {
    "max_gonderim_denemesi": 3,   # Email gönderim deneme sayısı
    "timeout_saniye": 30,         # SMTP timeout süresi
    "batch_boyutu": 10,           # Aynı anda gönderilecek maksimum email
    "debug_mode": False           # Debug modunda gerçek email gönderme
}

# ==================== VIEWER UYGULAMASI AYARLARI ====================

# Google Drive Ayarları
# NOT: Bu dosya adı, Drive'da aranacak veritabanı dosyasının adıdır
DRIVE_FILE_NAME = "talep_takip.db"

# Google API Scopes
# Sadece okuma yetkisi istiyoruz
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

# Credential Dosyaları
# NOT: Bu dosyalar Google Cloud Console'dan indirilmelidir
CREDENTIALS_FILE = "credentials.json"
TOKEN_FILE = "token.json"

# Yerel Dosya Ayarları
LOCAL_DB_PATH = os.path.join(os.path.expanduser("~"), ".talep_takip_viewer", "talep_takip.db")
LOCAL_DIR = os.path.dirname(LOCAL_DB_PATH)

# Otomatik Güncelleme Ayarları
AUTO_UPDATE_INTERVAL = 300000  # 5 dakika (milisaniye cinsinden)

# ==================== YARDIMCI FONKSİYONLAR ====================

def klasor_olustur(klasor_yolu):
    """
    Belirtilen klasörü oluşturur (eğer yoksa).
    
    Args:
        klasor_yolu (str): Oluşturulacak klasör yolu
        
    Returns:
        bool: İşlem başarılı mı?
    """
    try:
        if not os.path.exists(klasor_yolu):
            os.makedirs(klasor_yolu)
            return True
        return True
    except Exception:
        return False

def sistem_klasorlerini_hazirla():
    """
    Sistemin ihtiyaç duyduğu tüm klasörleri oluşturur.
    
    Returns:
        dict: Her klasör için başarı durumu
    """
    gerekli_klasorler = [VERI_KLASORU, LOG_KLASORU]
    sonuclar = {}
    
    for klasor in gerekli_klasorler:
        sonuclar[klasor] = klasor_olustur(klasor)
    
    return sonuclar

def tarih_formatla(tarih_objesi=None, format_tipi="tam"):
    """
    Tarih objesini istenen formatta string'e dönüştürür.
    
    Args:
        tarih_objesi: datetime objesi (None ise şu anki zaman)
        format_tipi: "tam", "tarih", "saat", "dosya_adi"
        
    Returns:
        str: Formatlanmış tarih string'i
    """
    if tarih_objesi is None:
        tarih_objesi = datetime.now()
    
    formatlar = {
        "tam": "%d.%m.%Y %H:%M:%S",
        "tarih": "%d.%m.%Y",
        "saat": "%H:%M:%S",
        "dosya_adi": "%Y%m%d_%H%M%S"
    }
    
    return tarih_objesi.strftime(formatlar.get(format_tipi, formatlar["tam"]))

def email_gecerli_mi(email):
    """
    Basit email validasyonu yapar.
    
    Args:
        email (str): Kontrol edilecek email
        
    Returns:
        bool: Email geçerli mi?
    """
    if not email or not isinstance(email, str):
        return False
    
    # Basit kontroller
    if "@" not in email or "." not in email:
        return False
    
    # @ işareti tek olmalı ve başta/sonda olmamalı
    if email.count("@") != 1:
        return False
    
    username, domain = email.split("@")
    if not username or not domain:
        return False
    
    return True

def varsayilan_kullanici_verileri():
    """
    Sistem ilk kurulumunda oluşturulacak varsayılan kullanıcıları döndürür.
    
    NOT: Bu şifreler sadece örnek amaçlıdır. Gerçek kullanımda
    mutlaka değiştirilmelidir!
    
    Returns:
        dict: Varsayılan kullanıcı verileri
    """
    return {
        "admin": {
            "ad_soyad": "Sistem Yöneticisi",
            "email": "admin@kurumadi.gov.tr",  # Kendi email adresinizi girin
            "rol": "yonetici",
            "sifre": "degistirin123",  # MUTLAKA DEĞİŞTİRİN!
            "aktif": True,
            "olusturma_tarihi": tarih_formatla()
        },
        "kullanici1": {
            "ad_soyad": "Test Kullanıcı",
            "email": "kullanici@kurumadi.gov.tr",  # Kendi email adresinizi girin
            "rol": "kullanici",
            "sifre": "degistirin456",  # MUTLAKA DEĞİŞTİRİN!
            "aktif": True,
            "olusturma_tarihi": tarih_formatla()
        }
    }

def varsayilan_email_konfigurasyonu():
    """
    Email sistemi için varsayılan konfigürasyon döndürür.
    
    UYARI: Bu konfigürasyon örnek amaçlıdır. Gerçek SMTP bilgilerinizi
    girmeniz gerekmektedir!
    
    Returns:
        dict: Email konfigürasyon verisi
    """
    return {
        "_aciklama": "Bu dosyayı düzenleyerek email ayarlarınızı yapın",
        "smtp_sunucu": {
            "sunucu": "smtp.gmail.com",  # SMTP sunucu adresi
            "port": 587,                 # SMTP port numarası
            "guvenlik": "TLS",          # TLS veya SSL
            "kullanici_adi": "sizin_email@gmail.com",  # DEĞİŞTİRİN!
            "sifre": "uygulama_sifresi_buraya",        # DEĞİŞTİRİN!
            "gonderici_adi": "ADANA ASKİ Talep Sistemi"
        },
        "alici_gruplari": {
            "yoneticiler": [
                "yonetici1@kurumadi.gov.tr",  # Gerçek email adresleri girin
                "yonetici2@kurumadi.gov.tr"
            ],
            "muhendisler": [
                "muhendis1@kurumadi.gov.tr",
                "muhendis2@kurumadi.gov.tr"
            ],
            "diğer": [
                "diger1@kurumadi.gov.tr"
            ]
        },
        "bildirim_kurallari": EMAIL_BILDIRIM_KURALLARI.copy()
    }

# ==================== TEST FONKSİYONU ====================

if __name__ == "__main__":
    """
    Bu bölüm, config dosyasının doğru çalıştığını test etmek içindir.
    python config-example.py komutu ile çalıştırabilirsiniz.
    """
    print(f"📋 {PROJE_ADI} v{PROJE_VERSIYONU}")
    print(f"🏢 {KURUM_ADI}")
    print(f"📍 {BIRIM_ADI}")
    print("\n" + "="*50 + "\n")
    
    print("🔍 Sistem Kontrolleri:")
    
    # Klasör kontrolü
    print("\n📁 Klasör Yapısı:")
    klasor_sonuclari = sistem_klasorlerini_hazirla()
    for klasor, basarili in klasor_sonuclari.items():
        durum = "✅ Oluşturuldu" if basarili else "❌ Oluşturulamadı"
        print(f"   {klasor}: {durum}")
    
    # Örnek kullanımlar
    print("\n📅 Tarih Formatları:")
    print(f"   Tam format: {tarih_formatla()}")
    print(f"   Sadece tarih: {tarih_formatla(format_tipi='tarih')}")
    print(f"   Sadece saat: {tarih_formatla(format_tipi='saat')}")
    print(f"   Dosya adı için: {tarih_formatla(format_tipi='dosya_adi')}")
    
    # Email validasyon örnekleri
    print("\n📧 Email Validasyon Örnekleri:")
    test_emails = [
        "gecerli@email.com",
        "gecersiz.email.com",
        "@sadece-domain.com",
        "sadece-kullanici@",
        ""
    ]
    for email in test_emails:
        durum = "✅ Geçerli" if email_gecerli_mi(email) else "❌ Geçersiz"
        print(f"   '{email}': {durum}")
    
    print("\n✨ Config dosyası örneği başarıyla yüklendi!")
    print("\n⚠️  UYARI: Bu dosyadaki şifre ve email bilgileri örnek amaçlıdır.")
    print("Gerçek kullanımda kendi bilgilerinizi girmeyi unutmayın!")
