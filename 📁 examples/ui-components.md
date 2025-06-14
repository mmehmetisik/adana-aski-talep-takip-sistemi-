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

#### Modern Entry (Input) Alanı

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

#### Bilgi Kartı

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
#### Renkli Durum Badge'i
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

### Loading/Progress Göstergeleri
#### Animasyonlu Loading Ekranı

```
def loading_goster(parent, mesaj="Yükleniyor..."):
    """
    Animasyonlu loading ekranı gösterir.
    """
    # Loading frame
    loading_frame = tk.Frame(parent, bg="white")
    loading_frame.pack(fill=tk.BOTH, expand=True)
    
    # İç container
    ic_container = tk.Frame(loading_frame, bg="white")
    ic_container.pack(expand=True)
    
    # Animasyonlu spinner (basit versiyon)
    spinner_frame = tk.Frame(ic_container, bg="white")
    spinner_frame.pack()
    
    # Spinner karakterleri
    spinner_chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    spinner_index = [0]
    
    spinner_label = tk.Label(
        spinner_frame,
        text=spinner_chars[0],
        font=("Segoe UI", 24),
        bg="white",
        fg="#3b82f6"
    )
    spinner_label.pack()
    
    # Loading metni
    tk.Label(
        ic_container,
        text=mesaj,
        font=("Segoe UI", 12),
        bg="white",
        fg="#1e293b"
    ).pack(pady=(10, 0))
    
    # Animasyon fonksiyonu
    def animate_spinner():
        spinner_index[0] = (spinner_index[0] + 1) % len(spinner_chars)
        spinner_label.config(text=spinner_chars[spinner_index[0]])
        parent.after(100, animate_spinner)
    
    # Animasyonu başlat
    animate_spinner()
    
    return loading_frame
```

### Modal Dialog
#### Modern Popup Pencere

```
def modern_popup_goster(parent, baslik, icerik, tip="bilgi"):
    """
    Modern görünümlü popup pencere gösterir.
    """
    # Popup pencere
    popup = tk.Toplevel(parent)
    popup.title(baslik)
    popup.geometry("400x300")
    popup.configure(bg="white")
    popup.resizable(False, False)
    
    # Pencereyi ortala
    popup.update_idletasks()
    x = (popup.winfo_screenwidth() - 400) // 2
    y = (popup.winfo_screenheight() - 300) // 2
    popup.geometry(f"400x300+{x}+{y}")
    
    # Modal yap
    popup.transient(parent)
    popup.grab_set()
    
    # Renk şeması
    renkler = {
        "bilgi": {"ana": "#3b82f6", "ikon": "ℹ️"},
        "basari": {"ana": "#10b981", "ikon": "✅"},
        "uyari": {"ana": "#f59e0b", "ikon": "⚠️"},
        "hata": {"ana": "#ef4444", "ikon": "❌"}
    }
    
    renk_info = renkler.get(tip, renkler["bilgi"])
    
    # Üst renkli bar
    ust_bar = tk.Frame(popup, bg=renk_info["ana"], height=60)
    ust_bar.pack(fill=tk.X)
    ust_bar.pack_propagate(False)
    
    # İkon ve başlık
    tk.Label(
        ust_bar,
        text=f"{renk_info['ikon']} {baslik}",
        font=("Segoe UI", 16, "bold"),
        bg=renk_info["ana"],
        fg="white"
    ).pack(expand=True)
    
    # İçerik
    icerik_frame = tk.Frame(popup, bg="white", padx=30, pady=20)
    icerik_frame.pack(fill=tk.BOTH, expand=True)
    
    tk.Label(
        icerik_frame,
        text=icerik,
        font=("Segoe UI", 11),
        bg="white",
        fg="#374151",
        wraplength=340,
        justify=tk.LEFT
    ).pack()
    
    # Tamam butonu
    tk.Button(
        icerik_frame,
        text="Tamam",
        font=("Segoe UI", 10, "bold"),
        bg=renk_info["ana"],
        fg="white",
        relief=tk.FLAT,
        padx=30,
        pady=10,
        cursor="hand2",
        command=popup.destroy
    ).pack(side=tk.BOTTOM, pady=(20, 0))
    
    return popup
```

### Tablo/Liste Görünümleri
#### Modern Treeview Stili

```
def modern_treeview_olustur(parent):
    """
    Özelleştirilmiş modern treeview oluşturur.
    """
    # Style tanımlamaları
    style = ttk.Style()
    style.theme_use("clam")
    
    # Treeview stilleri
    style.configure("Treeview",
        background="white",
        foreground="#1e293b",
        rowheight=40,
        fieldbackground="white",
        borderwidth=0,
        font=("Segoe UI", 10)
    )
    
    style.configure("Treeview.Heading",
        background="#f8fafc",
        foreground="#1e293b",
        relief="flat",
        font=("Segoe UI", 10, "bold")
    )
    
    style.map("Treeview",
        background=[("selected", "#e0f2fe")],
        foreground=[("selected", "#0c4a6e")]
    )
    
    # Treeview oluştur
    columns = ("Talep No", "İş Adı", "Durum", "Tarih")
    tree = ttk.Treeview(parent, columns=columns, show="headings", style="Treeview")
    
    # Sütun başlıkları
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")
    
    # Örnek veri ekleme
    tree.insert("", "end", values=("2025/001", "Pompa Bakımı", "Beklemede", "14.06.2025"))
    tree.insert("", "end", values=("2025/002", "Klor Pompası", "Onaylandı", "14.06.2025"))
    
    # Scrollbar
    scrollbar = ttk.Scrollbar(parent, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    
    # Pack
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    return tree
```
### Animasyon Örnekleri
#### Yumuşak Geçiş Animasyonu

```
def fade_in_animasyon(widget, adim=0.1):
    """
    Widget'ı yumuşak bir şekilde görünür yapar.
    """
    alpha = 0.0
    
    def fade_step():
        nonlocal alpha
        if alpha < 1.0:
            alpha += adim
            widget.attributes("-alpha", alpha)
            widget.after(50, fade_step)
    
    widget.attributes("-alpha", 0.0)
    fade_step()
```

#### Logo Animasyonu

```
def logo_pulse_animasyon(logo_label):
    """
    Logo için pulse (nabız) efekti oluşturur.
    """
    import math
    
    frame = [0]
    
    def animate():
        frame[0] += 0.1
        scale = 1.0 + 0.05 * math.sin(frame[0])
        
        # Font boyutunu değiştir
        new_size = int(48 * scale)
        logo_label.config(font=("Arial", new_size))
        
        # Animasyonu devam ettir
        logo_label.after(50, animate)
    
    animate()
```
### Responsive Layout
#### Otomatik Boyutlandırma

```
def responsive_grid_olustur(parent, eleman_sayisi):
    """
    Pencere boyutuna göre otomatik grid layout oluşturur.
    """
    def pencere_boyut_degisti(event=None):
        genislik = parent.winfo_width()
        
        # Genişliğe göre sütun sayısını belirle
        if genislik < 600:
            sutun_sayisi = 1
        elif genislik < 900:
            sutun_sayisi = 2
        elif genislik < 1200:
            sutun_sayisi = 3
        else:
            sutun_sayisi = 4
        
        # Elemanları yeniden yerleştir
        for i, eleman in enumerate(parent.winfo_children()):
            row = i // sutun_sayisi
            col = i % sutun_sayisi
            eleman.grid(row=row, column=col, padx=10, pady=10, sticky="ew")
        
        # Sütunları eşit genişlikte yap
        for i in range(sutun_sayisi):
            parent.columnconfigure(i, weight=1)
    
    # Pencere boyut değişikliğini dinle
    parent.bind("<Configure>", pencere_boyut_degisti)
    
    # İlk yerleştirme
    pencere_boyut_degisti()
```

### Özel Widget'lar
#### Arama Kutusu

```
def arama_kutusu_olustur(parent, arama_callback):
    """
    Anlık arama özellikli modern arama kutusu.
    """
    # Arama container
    arama_frame = tk.Frame(parent, bg="#f8fafc", relief=tk.FLAT)
    arama_frame.pack(fill=tk.X, pady=10)
    
    # İç frame
    ic_frame = tk.Frame(arama_frame, bg="white", relief=tk.FLAT, bd=1)
    ic_frame.pack(fill=tk.X, padx=20, pady=10)
    
    # Arama ikonu
    tk.Label(
        ic_frame,
        text="🔍",
        font=("Segoe UI", 14),
        bg="white"
    ).pack(side=tk.LEFT, padx=(10, 5))
    
    # Arama entry
    arama_var = tk.StringVar()
    arama_entry = tk.Entry(
        ic_frame,
        textvariable=arama_var,
        font=("Segoe UI", 11),
        bg="white",
        fg="#1e293b",
        relief=tk.FLAT,
        bd=0
    )
    arama_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=8)
    
    # Placeholder
    placeholder_text = "Ara..."
    arama_entry.insert(0, placeholder_text)
    arama_entry.config(fg="#94a3b8")
    
    def on_focus_in(e):
        if arama_entry.get() == placeholder_text:
            arama_entry.delete(0, tk.END)
            arama_entry.config(fg="#1e293b")
    
    def on_focus_out(e):
        if not arama_entry.get():
            arama_entry.insert(0, placeholder_text)
            arama_entry.config(fg="#94a3b8")
    
    arama_entry.bind("<FocusIn>", on_focus_in)
    arama_entry.bind("<FocusOut>", on_focus_out)
    
    # Temizle butonu
    temizle_btn = tk.Button(
        ic_frame,
        text="✕",
        font=("Segoe UI", 10),
        bg="white",
        fg="#94a3b8",
        relief=tk.FLAT,
        bd=0,
        cursor="hand2",
        command=lambda: [arama_var.set(""), arama_callback("")]
    )
    temizle_btn.pack(side=tk.RIGHT, padx=(5, 10))
    
    # Anlık arama
    def arama_degisti(*args):
        arama_metni = arama_var.get()
        if arama_metni != placeholder_text:
            arama_callback(arama_metni)
    
    arama_var.trace("w", arama_degisti)
    
    return arama_frame
```







































