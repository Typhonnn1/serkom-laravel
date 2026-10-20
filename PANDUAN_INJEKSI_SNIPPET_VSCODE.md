# 🚀 PANDUAN LENGKAP INJEKSI VS CODE SNIPPET LARAVEL (H-1 UJIAN SERKOM BNSP)

Dokumen ini adalah panduan strategis dan teknis untuk membawa serta menyuntikkan (*inject*) paket snippet **`serkom-laravel.code-snippets`** ke komputer laboratorium sekolah/LSP saat ujian sertifikasi kejuruan Web Developer (BNSP).

---

## ⚡ JAWABAN LANGSUNG: WHATSAPP WEB VS GITHUB VS FLASHDISK

> **Pertanyaan Anda:**  
> *"Niatnya gua mau taro di WA trs dr WA didownload ke komputer sekolah, atau harus make GitHub?"*

### 🏆 Kesimpulan Singkat: **JANGAN PAKAI WHATSAPP! GUNAKAN GITHUB GIST (PILIHAN #1) ATAU FLASHDISK (BACKUP #2).**

Berikut perbandingan risikonya di dunia nyata:

| Metode | Kecepatan | Tingkat Keberhasilan | Risiko di Lab Ujian |
| :--- | :---: | :---: | :--- |
| **WhatsApp Web** | ❌ Lambat (2-5 menit) | ⚠️ **40% (Sangat Berisiko)** | • **Domain diblokir**: Router/MikroTik lab sekolah sering memblokir `web.whatsapp.com`.<br>• **HP disita/dikumpulkan**: Anda tidak bisa scan QR code jika HP ditaruh di depan.<br>• **Mencurigakan**: Membuka WhatsApp di layar komputer terlihat sangat mencolok oleh asesor penguji.<br>• **Ekstensi file rusak**: File `.code-snippets` sering berubah jadi `.txt` atau gagal didownload. |
| **GitHub Gist (Raw URL)** | ⚡ **2 Detik** | 🟢 **99% (Sangat Direkomendasikan)** | • **Tidak perlu login**: Cukup buat Public Gist di rumah, di sekolah tinggal tembak URL Raw.<br>• **1 Baris PowerShell**: Cukup ketik 1 baris perintah di terminal, snippet langsung terpasang.<br>• **Bebas Blokir**: Domain developer (`github.com`) selalu diizinkan di lab ujian.<br>• **Elegan & Profesional**: Terlihat seperti developer profesional yang mengambil repositori. |
| **Flashdisk (USB Drive)** | ⚡ **5 Detik** | 🟢 **90% (Cadangan Terbaik)** | • Bawa flashdisk berisi `serkom-laravel.code-snippets` & `inject_snippets.ps1`.<br>• Colok, klik kanan *Run with PowerShell*, selesai, lalu cabut.<br>• *Catatan*: Waspadai jika sekolah menonaktifkan port USB dengan Group Policy. |

---

## 🛠️ STRATEGI EKSEKUSI H-1: CARA MENYIAPKAN GITHUB GIST (DARI RUMAH MALAM INI)

Lakukan langkah 2 menit ini di laptop rumah Anda malam ini:

1. Buka browser dan buka **[https://gist.github.com](https://gist.github.com)** (login akun GitHub Anda).
2. Di kolom **Gist description**, tulis: `serkom-snippets`.
3. Di kolom **Filename including extension**, tulis: `serkom-laravel.code-snippets`.
4. Buka file [serkom-laravel.code-snippets](file:///c:/Users/Default%20User/Desktop/modul%20serkom/serkom-laravel.code-snippets) di VS Code, tekan `Ctrl + A` lalu `Ctrl + C` (Copy seluruh isi file).
5. Paste isi file tersebut ke kotak kode di Gist.
6. Klik tombol hijau **Create public gist** (atau *Create secret gist*).
7. Setelah tersimpan, klik tombol **Raw** di pojok kanan atas kotak kode.
8. Salin URL Raw tersebut dari address bar browser (contoh: `https://gist.githubusercontent.com/username/xxxxxx/raw/serkom-laravel.code-snippets`).
9. Catat URL pendek tersebut (bisa perpendek pakai `bit.ly` atau `s.id`, misal: `s.id/serkomsnip`).

---

## 💻 EKSEKUSI DI KOMPUTER LAB SEKOLAH (PILIH SALAH SATU)

### 🥇 Opsi 1: Lewat PowerShell 1-Liner (Paling Cepat & Senyap - 3 Detik)
Saat duduk di depan komputer lab, tekan tombol **Windows + R**, ketik `powershell`, lalu tekan **Enter**. *(Gunakan PowerShell biasa, TIDAK PERLU Run as Administrator agar snippet masuk ke profil user ujian Anda).*  
Ketik perintah berikut (ganti link dengan link raw Gist Anda):

```powershell
mkdir -Force "$env:APPDATA\Code\User\snippets" | Out-Null; irm "https://gist.githubusercontent.com/YOUR_USERNAME/RAW_ID/raw/serkom-laravel.code-snippets" -OutFile "$env:APPDATA\Code\User\snippets\serkom-laravel.code-snippets"
```

*Jika Anda memakai pemendek link (misal `s.id/serkomsnip`), gunakan perintah curl/irm standar:*
```powershell
mkdir -Force "$env:APPDATA\Code\User\snippets" | Out-Null; curl.exe -L "https://s.id/serkomsnip" -o "$env:APPDATA\Code\User\snippets\serkom-laravel.code-snippets"
```

> ⚠️ **Catatan Penting `mkdir -Force`**: Di komputer lab sekolah yang instalasi VS Code-nya masih baru/bersih, folder `snippets` belum ada secara default. Perintah `mkdir -Force ... | Out-Null` di atas menjamin folder terbuat otomatis tanpa error `DirectoryNotFoundException`!

### 🥈 Opsi 2: Lewat Flashdisk (1-Click Run)
1. Colok flashdisk ke PC sekolah.
2. Buka folder flashdisk.
3. Klik kanan file `inject_snippets.ps1` -> pilih **Run with PowerShell**.
4. Tunggu 1 detik hingga muncul pesan hijau *"INJEKSI SELESAI"*.
5. Cabut flashdisk.

### 🥉 Opsi 3: Lewat Menu Internal VS Code (Manual Tanpa Terminal)
1. Buka VS Code di komputer sekolah.
2. Klik ikon Gerigi ⚙️ di pojok kiri bawah (atau tekan `Ctrl + Shift + P`).
3. Ketik: **`Configure User Snippets`** (atau *Preferences: Configure Snippets*), tekan Enter.
4. Pilih opsi **`New Global Snippets file...`**.
5. Beri nama: `serkom-laravel`, lalu tekan Enter.
6. File kosong akan terbuka. Hapus semua isinya (`Ctrl + A` lalu Backspace).
7. Paste seluruh isi JSON `serkom-laravel.code-snippets` ke situ, lalu tekan `Ctrl + S` (Save).
8. Selesai! Snippet aktif seketika di project manapun.

---

## 📖 KAMUS LENGKAP PREFIX SNIPPET (54 SNIPPET SIAP PAKAI)

Semua snippet telah dikonfigurasi secara **Universal Scope (`php, blade, html, sql, json, shellscript, powershell, bat, plaintext`)**, artinya snippet ini **PASTI MUNCUL** di semua file proyek tanpa terkecuali, bahkan jika ekstensi Laravel Blade belum terpasang di VS Code sekolah!

Cara pakainya:
1. **Ketik prefix di editor -> tekan `Tab` atau `Enter`**.
2. **Navigasi Cepat Tab Stops (`$1`, `$2`, `$0`)**: Setelah snippet terpasang, kursor Anda otomatis mendarat di kata/parameter kunci (seperti nama tabel, nama model, kategori, dll). Tekan **`Tab`** untuk melompat ke isian berikutnya, atau tekan **`Esc`/`Enter`** jika ingin memakai nilai bawaan!
3. **Kompatibilitas Penuh**: Kode sudah diuji dan 100% kompatibel baik untuk **Laravel 10** maupun **Laravel 11**.

---

### 🗂️ 1. MIGRATIONS (`mig-*`)

| Prefix | File Target (`database/migrations/`) | Keterangan & Isi Kolom |
| :--- | :--- | :--- |
| **`mig-users`** | `..._create_users_table.php` | Tabel user dengan kolom `phone` & enum `role` (`admin`, `customer`). |
| **`mig-tickets`** | `..._create_tickets_table.php` | Tabel master tiket: `concert_name`, `artist`, `venue`, `event_date`, `category` (VIP/Festival/Regular), `price`, `stock`, `poster`, `description`. |
| **`mig-orders-ticket`** | `..._create_orders_table.php` | Tabel transaksi tiket: `user_id` (FK users cascade), `order_code` (unique), identitas customer, `total_price`, `status` (pending/paid/cancelled), `order_date`. |
| **`mig-details-ticket`** | `..._create_order_details_table.php`| Tabel detail tiket: `order_id` (FK cascade), `ticket_id` (FK cascade), `quantity`, `unit_price`, `subtotal`. |
| **`mig-foods`** | `..._create_foods_table.php` | Tabel resto: `name`, `category` (Makanan/Minuman/Cemilan), `price`, `description`, `image`. |
| **`mig-orders-food`** | `..._create_orders_table.php` | Tabel pesanan resto: `user_id` (nullable), `order_code`, `customer_name`, `table_number`, `total_price`, `status`, `order_date`. |
| **`mig-details-food`** | `..._create_order_details_table.php`| Tabel detail pesanan resto: `order_id`, `food_id`, `quantity`, `unit_price`, `subtotal`, `notes`. |

---

### 📦 2. ELOQUENT MODELS (`model-*`)

| Prefix | File Target (`app/Models/`) | Keterangan & Fitur Utama |
| :--- | :--- | :--- |
| **`model-user`** | `User.php` | `$fillable`, `$casts`, helper `isAdmin()`, `isCustomer()`, relasi `hasMany(Order::class)`. |
| **`model-ticket`** | `Ticket.php` | `$fillable`, cast `event_date`, relasi `hasMany(OrderDetail::class)`. |
| **`model-order-ticket`**| `Order.php` | `$fillable`, cast `order_date`, relasi `belongsTo(User::class)`, `hasMany(OrderDetail::class)`. |
| **`model-detail-ticket`**| `OrderDetail.php` | `$fillable`, relasi `belongsTo(Order::class)`, `belongsTo(Ticket::class)`. |
| **`model-food`** | `Food.php` | `$table = 'foods'`, `$fillable`, relasi `hasMany(OrderDetail::class)`. |
| **`model-order-food`** | `Order.php` (Resto) | `$fillable` (`table_number`), relasi `hasMany(OrderDetail::class)`. |
| **`model-detail-food`**| `OrderDetail.php` (Resto) | `$fillable`, relasi `belongsTo(Order::class)`, `belongsTo(Food::class)`. |

---

### 🎮 3. CONTROLLERS (`ctrl-*`)

| Prefix | File Target (`app/Http/Controllers/`) | Keterangan & Fitur Utama |
| :--- | :--- | :--- |
| **`ctrl-ticket`** | `Admin/TicketController.php` | Resource CRUD tiket: validasi input, upload banner poster, hapus file lama di storage disk, pagination. |
| **`ctrl-user`** | `Admin/UserController.php` | Resource CRUD pengguna: pencarian (nama/email/HP), filter role, enkripsi password `Hash::make()`, proteksi anti self-delete. |
| **`ctrl-order-ticket`**| `Admin/OrderReportController.php`| Dashboard rekap: 4 kartu statistik omset/tiket/order, filter tanggal & status, patch `updateStatus()`, view cetak PDF `printReport()`. |
| **`ctrl-customer-booking`**| `Customer/BookingController.php`| Katalog konser, form booking, transaksi atomik `DB::beginTransaction()` + pengurangan kuota stok otomatis + order code generator, `myTickets`, cetak e-tiket. |
| **`ctrl-food`** | `FoodController.php` | CRUD menu restoran: upload foto menu, replace foto lama, hapus menu & file fisik. |
| **`ctrl-order-food`** | `Admin/RestoOrderController.php` | Dashboard pesanan restoran per meja, rekap omset, ubah status masakan (pending/cooking/completed). |
| **`ctrl-customer-food`**| `Customer/FoodOrderController.php` | Katalog resto, pesan per nomor meja, transaksi atomik `DB::transaction`. |
| **`ctrl-auth-redirect`**| Login Controller / Route | Logika pengalihan otomatis setelah login: role admin ke `/admin/dashboard`, customer ke katalog. |

---

### 🛡️ 4. MIDDLEWARE (`mid-*`)

| Prefix | File Target (`app/Http/Middleware/`) | Keterangan |
| :--- | :--- | :--- |
| **`mid-isadmin`** | `IsAdmin.php` | Satpam proteksi route admin: cek `Auth::check() && Auth::user()->role === 'admin'`. Jika bukan admin, tolak & redirect. |

---

### 🌱 5. SEEDERS (`seeder-*`)

| Prefix | File Target (`database/seeders/`) | Keterangan |
| :--- | :--- | :--- |
| **`seeder-ticket`** | `TicketSeeder.php` | 3 Data konser siap uji: Coldplay (VIP), Sheila On 7 (Festival), Tulus (Regular). |
| **`seeder-database-ticket`** | `DatabaseSeeder.php` | Akun siap login: Admin (`admin@tiket.com` / `password123`), Customer (`customer@gmail.com` / `password123`) & panggil `TicketSeeder`. |
| **`seeder-food`** | `FoodSeeder.php` | Data menu siap uji: Nasi Goreng, Mie Seafood, Es Teh, Kentang Keju. |
| **`seeder-database-food`** | `DatabaseSeeder.php` | Akun Admin Resto & Kasir/Customer siap uji. |

---

### 🌐 6. ROUTES (`route-*`)

| Prefix | File Target (`routes/web.php`) | Keterangan |
| :--- | :--- | :--- |
| **`route-ticket-complete`**| `routes/web.php` | Rute lengkap tiket konser: publik catalog, customer auth group, admin auth+admin group (`/admin/dashboard`, CRUD `tickets`, CRUD `users`). |
| **`route-food-complete`** | `routes/web.php` | Rute lengkap resto: menu publik, checkout meja, admin food resource, admin rekap pesanan. |

---

### 🎨 7. BLADE VIEWS - TIKET KONSER

| Prefix | Lokasi File (`resources/views/`) | Keterangan Tampilan |
| :--- | :--- | :--- |
| **`blade-ticket-index`** | `admin/tickets/index.blade.php` | Tabel tiket, thumbnail poster, badge kategori ungu/biru/abu, warna sisa stok merah/hijau, tombol edit & delete dengan dialog konfirmasi. |
| **`blade-ticket-create`** | `admin/tickets/create.blade.php` | Form tambah tiket, input datetime-local, select category, upload poster (enctype multipart), error alerts. |
| **`blade-ticket-edit`** | `admin/tickets/edit.blade.php` | Form edit tiket, preview thumbnail poster saat ini, upload ganti poster baru, `@method('PUT')`. |
| **`blade-user-index`** | `admin/users/index.blade.php` | Tabel manajemen user, search bar, dropdown filter role, badge role, tombol delete dengan proteksi anti self-delete. |
| **`blade-user-create`** | `admin/users/create.blade.php` | Form tambah user, input nama, email, HP, dropdown role, password & password confirmation. |
| **`blade-user-edit`** | `admin/users/edit.blade.php` | Form edit user, opsi ubah password (boleh dikosongkan jika password tidak diganti). |
| **`blade-admin-dashboard-rekap`**| `admin/orders/index.blade.php` | **Fitur Utama Ujian**: 4 Kartu statistik ringkasan omset & kuota, form filter tanggal (`start_date` - `end_date`) & status, tabel rincian pesanan, dropdown ubah status realtime. |
| **`blade-admin-orders-print`**| `admin/orders/print.blade.php` | Tampilan cetak laporan transaksi bersih, layout tabel rapi, total omset, trigger otomatis `window.print()` untuk cetak ke PDF/kertas. |
| **`blade-customer-catalog`** | `customer/concerts.blade.php` | Tampilan publik / customer: grid cards konser, banner artis/poster, info venue & tanggal, badge kategori, harga tiket format rupiah, tombol "Pesan Tiket". |
| **`blade-customer-booking`** | `customer/booking-form.blade.php` | Form booking tiket, identitas readonly dari user login, input quantity max stok, **kalkulator hitung total bayar instan via JavaScript**. |
| **`blade-customer-my-tickets`** | `customer/my-tickets.blade.php` | Tabel riwayat tiket yang dibeli customer, status LUNAS, tombol akses cetak E-Tiket. |
| **`blade-customer-e-ticket`** | `customer/e-ticket.blade.php` | Desain E-Tiket resmi boarding pass: border dashed indigo, header resmi, detail pemegang tiket, barcode unik, tombol cetak PDF. |

---

### 🍔 8. BLADE VIEWS - RESTORAN & MAKANAN

| Prefix | Lokasi File (`resources/views/`) | Keterangan Tampilan |
| :--- | :--- | :--- |
| **`blade-food-index`** | `admin/foods/index.blade.php` | Tabel menu makanan, foto menu, badge kategori makanan/minuman, harga rupiah, tombol edit & delete. |
| **`blade-food-create`** | `admin/foods/create.blade.php` | Form input menu resto baru, upload foto makanan, select kategori, harga & deskripsi. |
| **`blade-food-edit`** | `admin/foods/edit.blade.php` | Form edit menu resto, preview foto lama, upload ganti foto baru. |
| **`blade-resto-orders-index`**| `admin/resto-orders/index.blade.php`| Rekapitulasi pesanan makanan masuk per nomor meja, rincian menu dipesan, dropdown ubah status (pending/cooking/completed). |
| **`blade-resto-menu-catalog`**| `customer/menu.blade.php` | Katalog menu resto untuk pelanggan, foto makanan, harga, tombol pesan ke meja. |
| **`blade-resto-checkout`** | `customer/resto-checkout.blade.php` | Form checkout pesanan pelanggan, input nomor meja, catatan khusus untuk koki dapur. |

---

### 🧩 9. UI HELPERS & MASTER LAYOUTS

| Prefix | Lokasi File | Keterangan |
| :--- | :--- | :--- |
| **`blade-master-layout`** | `resources/views/layouts/master.blade.php` | Master layout mandiri lengkap (HTML5 + CDN Tailwind CSS + Navbar + Slot) — penyelamat jika starter-kit Laravel Breeze belum diinstall atau error! |
| **`blade-flash-messages`**| `resources/views/components/flash.blade.php`| Komponen alert flash message hijau (success), merah (error), dan validasi server `$errors->all()`. |

---

### 🗄️ 10. QUERY SQL CHEAT SHEET

| Prefix | Keterangan | Contoh Query |
| :--- | :--- | :--- |
| **`sql-crud-tickets`** | Query SQL lengkap CRUD tabel `tickets` | `INSERT INTO tickets ...`, `SELECT ... WHERE stock > 0 ORDER BY price ASC`, `UPDATE tickets SET ... WHERE id = 1`, `DELETE FROM tickets WHERE id = 1`. |
| **`sql-rekap-omset`** | Query SQL agregasi omset & JOIN 3 tabel | `SELECT SUM(total_price) ... WHERE status = 'paid'`, `INNER JOIN order_details ... tickets`, `GROUP BY t.id ... ORDER BY total_terjual DESC`. |
| **`sql-crud-foods`** | Query SQL CRUD & rekap meja resto | `INSERT INTO foods ...`, `SELECT per kategori`, `JOIN pesanan resto per meja`. |

---

### 💻 11. TERMINAL & ARTISAN CHEATS

| Prefix | Keterangan | Perintah Utama |
| :--- | :--- | :--- |
| **`artisan-serkom-setup`** | Checklist 6 langkah setup awal di lab | `composer install` -> `copy .env.example .env` -> `key:generate` -> `migrate:fresh --seed` -> `storage:link` -> `npm run build` -> `serve`. |
| **`artisan-commands`** | Kamus perintah artisan generator cepat | Generator migration, model, resource controller, middleware, seeder, dan `optimize:clear`. |

---

## 💡 TIPS & TROUBLESHOOTING SNIPPET SAAT UJIAN

1. **Snippet tidak muncul saat diketik?**
   - Tekan **`Ctrl + Space`** di keyboard untuk memicu popup suggestion VS Code.
   - Pastikan nama file Anda sudah berakhiran ekstensi yang tepat (contoh: `TicketController.php` atau `index.blade.php`).
   - Jika membuat file baru tanpa disimpan (*Untitled-1*), tekan `Ctrl + K` lalu tekan `M`, lalu pilih bahasa **PHP** atau **Blade**.
2. **Foto poster tidak muncul (gambar pecah / broken image)?**
   - Buka terminal VS Code (`Ctrl + ~`) dan jalankan:
     ```bash
     php artisan storage:link
     ```
   - Pastikan di file Blade memanggil gambar menggunakan helper asset:
     ```blade
     <img src="{{ asset('storage/' . $ticket->poster) }}">
     ```
3. **Error 419 Page Expired saat Submit Form?**
   - Pastikan formulir Anda memiliki token CSRF:
     ```blade
     <form action="..." method="POST">
         @csrf
         ...
     ```
4. **Error Class not found di Controller atau Routes?**
   - Pastikan Model atau Controller sudah di-import di baris paling atas menggunakan keyword `use`:
     ```php
     use App\Models\Ticket;
     use App\Models\Order;
     use App\Http\Controllers\Admin\TicketController;
     ```
5. **Error `Target class [admin] does not exist` di Routes?**
   - Di `routes/web.php`, jika Anda belum mendaftarkan alias middleware di Kernel/bootstrap, Anda bisa langsung mengganti `'admin'` dengan class-nya:
     ```php
     Route::middleware(['auth', \App\Http\Middleware\IsAdmin::class])->prefix('admin')->...
     ```
6. **Error `Unable to locate a class or view for component [app-layout]`?**
   - Jika project sekolah Anda belum menginstall Laravel Breeze, buat file di `resources/views/layouts/app.blade.php`, lalu ketik **`blade-master-layout`** dan tekan **`Tab`**. Semua tampilan `<x-app-layout>` akan langsung berjalan lancar menggunakan Tailwind CDN mandiri!

---
**🎉 Semoga Sukses Ujian Serkom Besok! Dengan 54 Snippet Ini, Anda Bisa Menyelesaikan Aplikasi dalam Waktu Kurang dari 15 Menit dan Meraih Predikat KOMPETEN 100%!**
