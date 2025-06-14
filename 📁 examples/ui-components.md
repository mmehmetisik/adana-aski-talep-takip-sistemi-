# 🎨 UI Bileşenleri Örnekleri

Bu dokümanda, ADANA ASKİ Talep Takip Sistemi'nde kullanılan modern UI bileşenlerinin kod örnekleri ve kullanım şekilleri açıklanmaktadır. Her bileşen, hem Tkinter hem de CustomTkinter versiyonları ile birlikte sunulmuştur.

## Modern Butonlar

### Gradient Efektli Buton

Ana sistemde kullanılan modern buton tasarımı, hover efektleri ve gölgelendirme içerir.

```python
def modern_buton_olustur(parent, text, bg_color, command, icon="", width=None):
    """
    Modern görünümlü buton oluşturur.
    
    Args:
        parent: Ana container
        text: Buton metni
        bg_color: Arka plan rengi
        command: Tıklama fonksiyonu
        icon: İkon karakteri (emoji)
        width: Buton genişliği
    """
    # Buton frame'i (gölge efekti için)
    buton_frame = tk.Frame(parent, bg=parent["bg"])
    
    # Gölge frame
    golge = tk.Frame(buton_frame, bg="#e2e8f0", height=3)
    golge.pack(fill=tk.X, side=tk.BOTTOM, padx=1, pady=(0, 1))
    
    # Ana buton
    buton_text = f"{icon} {text}" if icon else text
    buton = tk.Button(
        buton_frame,
        text=buton_text,
        font=("Segoe UI", 10, "bold"),
        bg=bg_color,
        fg="white",
        activebackground=bg_color,
        activeforeground="white",
        relief=tk.FLAT,
        bd=0,
        padx=20 if not width else 0,
        pady=12,
        cursor="hand2",
        command=command
    )
    
    if width:
        buton.config(width=width)
    
    buton.pack(fill=tk.BOTH, expand=True)
    
    # Hover efektleri
    hover_colors = {
        "#3b82f6": "#2563eb",  # Mavi
        "#10b981": "#059669",  # Yeşil
        "#ef4444": "#dc2626",  # Kırmızı
        "#f59e0b": "#d97706",  # Turuncu
        "#8b5cf6": "#7c3aed"   # Mor
    }
    
    hover_color = hover_colors.get(bg_color, bg_color)
    
    def on_enter(e):
        buton.config(bg=hover_color)
        golge.config(bg="#cbd5e1")
    
    def on_leave(e):
        buton.config(bg=bg_color)
        golge.config(bg="#e2e8f0")
    
    buton.bind("<Enter>", on_enter)
    buton.bind("<Leave>", on_leave)
    
    return buton_frame
```
**Kullanım Örneği:**

```
# Başarılı işlem butonu
self.modern_buton_olustur(
    parent_frame,
    "Talebi Kaydet",
    "#10b981",  # Yeşil
    self.talep_kaydet,
    icon="💾"
)

# Tehlikeli işlem butonu
self.modern_buton_olustur(
    parent_frame,
    "Sil",
    "#ef4444",  # Kırmızı
    self.talep_sil,
    icon="🗑️"
)
```
### CustomTkinter Buton

Viewer uygulamasında kullanılan daha modern buton stili.

```
import customtkinter as ctk

# Modern rounded buton
kaydet_btn = ctk.CTkButton(
    parent_frame,
    text="💾 Kaydet",
    font=ctk.CTkFont(size=14, weight="bold"),
    fg_color="#10b981",
    hover_color="#059669",
    text_color="white",
    height=45,
    width=200,
    corner_radius=25,
    command=self.kaydet
)
kaydet_btn.pack(pady=10)
```
### Form Alanları

### Modern Entry (Input) Alanı

Focus efektleri ve placeholder desteği olan modern input alanı.

```
def modern_form_alani_olustur(parent, alan_adi, label_text, placeholder="", icon=""):
    """
    Modern görünümlü form alanı oluşturur.
    """
    # Ana container
    alan_frame = tk.Frame(parent, bg="white")
    alan_frame.pack(fill=tk.X, pady=8)
    
    # Label
    label_frame = tk.Frame(alan_frame, bg="white")
    label_frame.pack(fill=tk.X, pady=(0, 5))
    
    label_text_full = f"{icon} {label_text}" if icon else label_text
    tk.Label(
        label_frame,
        text=label_text_full,
        font=("Segoe UI", 10),
        bg="white",
        fg="#1e293b"
    ).pack(side=tk.LEFT)
    
    # Input container (focus efekti için)
    input_container = tk.Frame(alan_frame, bg="#f1f5f9", relief=tk.FLAT, bd=1)
    input_container.pack(fill=tk.X)
    
    # Entry
    entry = tk.Entry(
        input_container,
        font=("Segoe UI", 10),
        relief=tk.FLAT,
        bd=0,
        bg="white",
        fg="#1e293b",
        insertbackground="#3b82f6"
    )
    entry.pack(fill=tk.X, padx=10, pady=10)
    
    # Placeholder
    if placeholder:
        entry.insert(0, placeholder)
        entry.config(fg="#64748b")
        
        def on_focus_in(e):
            if entry.get() == placeholder:
                entry.delete(0, tk.END)
                entry.config(fg="#1e293b")
        
        def on_focus_out(e):
            if not entry.get():
                entry.insert(0, placeholder)
                entry.config(fg="#64748b")
        
        entry.bind("<FocusIn>", on_focus_in)
        entry.bind("<FocusOut>", on_focus_out)
    
    # Focus efektleri
    def on_entry_focus_in(e):
        input_container.config(bg="#3b82f6")
    
    def on_entry_focus_out(e):
        input_container.config(bg="#f1f5f9")
    
    entry.bind("<FocusIn>", lambda e: on_entry_focus_in(e))
    entry.bind("<FocusOut>", lambda e: on_entry_focus_out(e))
    
    return entry
```

**Kullanım Örneği:**

```
# Talep numarası alanı
talep_no_entry = self.modern_form_alani_olustur(
    form_frame,
    "talep_no",
    "Talep No",
    placeholder="2025/001",
    icon="📋"
)

# İş adı alanı
is_adi_entry = self.modern_form_alani_olustur(
    form_frame,
    "is_adi",
    "İşin Adı",
    placeholder="Örn: Pompa bakımı",
    icon="⚙️"
)
```

### Modern ComboBox (Dropdown)
Özelleştirilmiş dropdown menü tasarımı.

```
# Durum seçimi için modern dropdown
durum_frame = tk.Frame(parent, bg="white")
durum_frame.pack(fill=tk.X, pady=10)

tk.Label(
    durum_frame,
    text="📊 Talep Durumu",
    font=("Segoe UI", 10),
    bg="white",
    fg="#1e293b"
).pack(anchor=tk.W, pady=(0, 5))

# Combo container
combo_container = tk.Frame(durum_frame, bg="#f1f5f9", relief=tk.FLAT, bd=1)
combo_container.pack(fill=tk.X)

durum_combo = ttk.Combobox(
    combo_container,
    values=TALEP_DURUMLARI,
    state="readonly",
    font=("Segoe UI", 10)
)
durum_combo.pack(fill=tk.X, padx=8, pady=8)
durum_combo.set(TALEP_DURUMLARI[0])

# Style ayarları
style = ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", 
    fieldbackground="white",
    bordercolor="#f1f5f9",
    arrowcolor="#3b82f6"
)
```
### Kart Tasarımları

### Bilgi Kartı

Modern görünümlü bilgi kartı tasarımı.

```
def bilgi_karti_olustur(parent, baslik, deger, ikon="", renk="#3b82f6"):
    """
    Dashboard için bilgi kartı oluşturur.
    """
    # Kart frame
    kart = tk.Frame(parent, bg="white", relief=tk.FLAT)
    kart.pack(side=tk.LEFT, padx=10, pady=10)
    
    # İç container
    ic_frame = tk.Frame(kart, bg="white", padx=20, pady=15)
    ic_frame.pack()
    
    # İkon ve başlık
    baslik_frame = tk.Frame(ic_frame, bg="white")
    baslik_frame.pack(anchor=tk.W)
    
    tk.Label(
        baslik_frame,
        text=f"{ikon} {baslik}",
        font=("Segoe UI", 9),
        bg="white",
        fg="#64748b"
    ).pack(side=tk.LEFT)
    
    # Değer
    tk.Label(
        ic_frame,
        text=deger,
        font=("Segoe UI", 24, "bold"),
        bg="white",
        fg=renk
    ).pack(anchor=tk.W, pady=(5, 0))
    
    # Alt çizgi (dekoratif)
    alt_cizgi = tk.Frame(ic_frame, bg=renk, height=3)
    alt_cizgi.pack(fill=tk.X, pady=(10, 0))
    
    # Gölge efekti
    golge = tk.Frame(kart, bg="#e2e8f0", height=2)
    golge.pack(fill=tk.X, side=tk.BOTTOM)
    
    return kart
```

**Kullanım Örneği:**

```
# Dashboard kartları
bilgi_karti_olustur(
    dashboard_frame,
    "Toplam Talep",
    "156",
    ikon="📊",
    renk="#3b82f6"
)

bilgi_karti_olustur(
    dashboard_frame,
    "Bekleyen",
    "23",
    ikon="⏳",
    renk="#f59e0b"
)

bilgi_karti_olustur(
    dashboard_frame,
    "Tamamlanan",
    "133",
    ikon="✅",
    renk="#10b981"
)
```

### Durum Göstergeleri
### Renkli Durum Badge'i
Talep durumlarını görsel olarak ifade eden badge bileşeni.

```
def durum_badge_olustur(parent, durum_text):
    """
    Durum için renkli badge oluşturur.
    """
    # Durum renkleri
    durum_renkleri = {
        "Ceyhandan Gönderildi": "#10b981",
        "Burakda Bekliyor": "#eab308",
        "Şube Müdüründe İmzada": "#3b82f6",
        "Daire Başkanında İmzada": "#6366f1",
        "Genel Müdür Yardımcısında İmzada": "#8b5cf6",
        "Destek Biriminde": "#06b6d4",
        "Fiyat Araştırmasında": "#f59e0b",
        "Firmada": "#22c55e",
        "İade Edildi": "#ef4444"
    }
    
    renk = durum_renkleri.get(durum_text, "#64748b")
    
    # Badge frame
    badge = tk.Frame(parent, bg=renk, relief=tk.FLAT)
    badge.pack(side=tk.LEFT, padx=5)
    
    # Badge içeriği
    tk.Label(
        badge,
        text=durum_text,
        font=("Segoe UI", 9, "bold"),
        bg=renk,
        fg="white",
        padx=15,
        pady=5
    ).pack()
    
    # Yuvarlak köşeler için
    badge.configure(highlightthickness=0)
    
    return badge
```














