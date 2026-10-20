# 🎯 KISI-KISI & PANDUAN LENGKAP UJIAN SERKOM (H-1 EMERGENCY GUIDE)
**Skema Sertifikasi: Junior Web Developer / Pemrograman Web (BNSP / LSP)**  
**Studi Kasus Utama: Aplikasi Pemesanan Tiket Konser (Pra Serkom)**  
**Studi Kasus Referensi: Aplikasi Pemesanan Makanan & Restoran**  
**Teknologi: PHP 8.x, Laravel 10/11, MySQL, Laravel Breeze, Tailwind CSS, Blade Engine**

---

## 📑 DAFTAR ISI CEPAT
1. [Bagian 1: Jawaban Kisi-Kisi Teori (Wawancara Asesor)](#-bagian-1-jawaban-kisi-kisi-teori-wawancara-asesor)
   - [1. Kebutuhan Membangun Aplikasi Pemesanan Tiket Konser](#1-kebutuhan-membangun-aplikasi-pemesanan-tiket-konser)
   - [2. Fungsi ERD & Fungsi CRUD dalam Bahasa SQL](#2-fungsi-erd-dan-fungsi-crud-dalam-bahasa-sql)
   - [3. Apa Itu Query, Fungsi, dan Contoh Nyata](#3-apa-itu-query-dan-fungsi-contoh-nyata)
   - [4. Arsitektur MVC Laravel](#4-arsitektur-mvc-laravel)
   - [5. Tools & Stack Teknologi yang Digunakan](#5-tools--stack-teknologi-yang-digunakan)
2. [Bagian 2: Panduan Praktek Utama - Aplikasi Pemesanan Tiket Konser](#-bagian-2-panduan-praktek-utama---aplikasi-pemesanan-tiket-konser-pra-serkom)
   - [Praktek 1: Login & Register Multi-Role (Customer & Admin)](#praktek-1-login--register-multi-role-customer--admin)
   - [Praktek 2: Relasi Antar Tabel (4 Tabel Utama, Migration & Model)](#praktek-2-relasi-antar-tabel-skema-database-migration--model)
   - [Praktek 3: CRUD Master Data Tiket Konser (Sisi Admin)](#praktek-3-crud-master-data-tiket-konser-sisi-admin)
   - [Praktek 4: Rekap Laporan Pesanan Masuk (Dashboard Admin)](#praktek-4-rekap-laporan-pesanan-masuk-dashboard-admin)
   - [Praktek 5: Sisi Customer (Katalog Konser, Pemesanan Atomik & E-Tiket)](#praktek-5-sisi-customer-katalog-konser-pemesanan-atomik--e-tiket)
   - [Praktek 6: File Routing Lengkap (routes/web.php)](#praktek-6-file-routing-lengkap-routeswebphp)
3. [Bagian 3: Panduan Kasus Referensi - Aplikasi Pemesanan Makanan](#-bagian-3-panduan-kasus-referensi---aplikasi-pemesanan-makanan-restoran)
4. [Bagian 4: Checklist Eksekusi H-1 Ujian (Urutan Kerja 15 Menit)](#-bagian-4-checklist-eksekusi-h-1-ujian-urutan-kerja-15-menit)
5. [Bagian 5: Sesi Grill-Me Asesor (10 Tanya Jawab Emas)](#-bagian-5-sesi-grill-me-asesor-10-tanya-jawab-emas)
6. [Bagian 6: Kamus Error & Troubleshooting Instan (10 Detik)](#-bagian-6-kamus-error--troubleshooting-instan-solusi-10-detik)

---

## 📌 BAGIAN 1: JAWABAN KISI-KISI TEORI (WAWANCARA ASESOR)

### 1. Kebutuhan Membangun Aplikasi Pemesanan Tiket Konser
Jika asesor bertanya: *"Apa saja yang dibutuhkan dalam membangun Aplikasi Pemesanan Tiket Konser?"*, jawablah secara terstruktur mencakup 5 aspek berikut:

#### A. Kebutuhan Perangkat Keras (Hardware Requirements)
1. **Processor**: Minimal Dual Core 2.0 GHz (Direkomendasikan Intel Core i3/i5 atau AMD Ryzen 3/5) untuk kelancaran kompilasi asset Vite dan eksekusi server PHP.
2. **RAM**: Minimal 4 GB (Disarankan 8 GB / 16 GB) agar mampu menjalankan VS Code, XAMPP (Apache & MySQL), browser multi-tab, dan terminal secara simultan tanpa *lag*.
3. **Penyimpanan (Storage)**: Minimal 10 GB ruang kosong SSD untuk instalasi OS, XAMPP, folder `node_modules`, `vendor`, database InnoDB, dan penyimpanan file upload poster konser.
4. **Perangkat Input/Output & Jaringan**: Keyboard, mouse, monitor dengan resolusi minimal 1366x768, serta antarmuka jaringan (LAN/Wi-Fi) untuk akses localhost port `80`, `3306`, dan `8000`.

#### B. Kebutuhan Perangkat Lunak (Software Stack Requirements)
1. **Sistem Operasi**: Windows 10/11, Linux (Ubuntu/Debian), atau macOS.
2. **Web Server & DBMS**: **XAMPP** (Apache 2.4 sebagai web server lokal dan MySQL 8.0/MariaDB 10.4 sebagai RDBMS).
3. **Bahasa Pemrograman**: **PHP 8.1 / 8.2+** (dengan ekstensi aktif: `pdo_mysql`, `mbstring`, `openssl`, `fileinfo`, `gd`).
4. **Package Manager**:
   - **Composer**: Mengelola dependensi backend PHP (Laravel Core, Breeze, Intervention Image).
   - **Node.js (v18+) & NPM**: Mengompilasi asset frontend modern menggunakan Vite (`npm run build`).
5. **Code Editor**: **Visual Studio Code (VS Code)** dilengkapi ekstensi *PHP Intelephense*, *Laravel Blade Snippets*, dan *Tailwind CSS IntelliSense*.
6. **Web Browser & Debugging Tools**: Google Chrome / Microsoft Edge (DevTools untuk Network request, Cookie, LocalStorage, dan Inspect Element).
7. **Database GUI Tool**: **phpMyAdmin** untuk memantau struktur tabel, relasi foreign key, dan eksekusi query SQL langsung.

#### C. Kebutuhan Arsitektur & Basis Data (Database Requirements)
1. **RDBMS**: MySQL berbasis mesin penyimpanan **InnoDB** (wajib InnoDB untuk mendukung *Foreign Key Constraints* dan transaksi ACID).
2. **Arsitektur Relasi Basis Data (4 Tabel Utama)**:
   - `users`: Menyimpan data akun pengguna (Admin & Customer).
   - `tickets`: Menyimpan master data tiket konser (nama konser, musisi, venue, tanggal, kategori VIP/Festival/Regular, harga, sisa stok kuota, dan poster).
   - `orders`: Menyimpan *header* transaksi pemesanan (kode booking unik, identitas pemesan, total tagihan, status bayar pending/paid/cancelled).
   - `order_details`: Menyimpan baris rincian tiket yang dipesan (relasi ke `orders` dan `tickets`, jumlah tiket, harga satuan, dan subtotal).
3. **Pola Arsitektur Aplikasi**: **MVC (Model-View-Controller)** menggunakan framework Laravel.

#### D. Kebutuhan Fungsional (Functional Requirements)
- **Role Customer (Pengunjung / Pembeli Tiket)**:
  1. Registrasi akun baru dan login ke sistem.
  2. Menjelajahi katalog konser aktif yang masih memiliki kuota tiket.
  3. Memilih kategori tiket (VIP, Festival, Regular) dan menentukan jumlah tiket yang ingin dipesan.
  4. Sistem memvalidasi ketersediaan stok tiket secara otomatis (*real-time*).
  5. Melakukan checkout pesanan dan memperoleh kode booking unik (misal: `TKT-20261021-001`).
  6. Melihat riwayat pemesanan tiket pada menu *My Tickets*.
  7. Mencetak E-Tiket / bukti booking konser digital.
- **Role Admin (Panitia Penyelenggara Konser)**:
  1. Login dengan otentikasi khusus administrator (`role = 'admin'`).
  2. Mengakses **Dashboard Rekapitulasi**:
     - Menampilkan kartu ringkasan statistik (Total Omset Penjualan dalam Rupiah, Total Tiket Terjual, Jumlah Pesanan Lunas, dan Pesanan Menunggu Konfirmasi).
     - Menampilkan tabel rekapitulasi seluruh pesanan masuk beserta rincian tiketnya.
     - Filter laporan transaksi berdasarkan rentang tanggal (`start_date` sampai `end_date`) dan status pembayaran.
     - Mengubah status pembayaran pesanan (*Pending* -> *Paid/Lunas* -> *Cancelled*).
     - Mencetak laporan rekapitulasi transaksi ke format PDF/kertas.
  3. Mengelola **Master Data Tiket Konser (CRUD)**:
     - Tambah tiket konser baru lengkap dengan upload file gambar poster.
     - Edit data tiket (nama konser, musisi, tanggal acara, lokasi venue, harga tiket, dan penambahan kuota stok).
     - Hapus tiket konser dengan konfirmasi keamanan.
     - Tampil data tiket dalam tabel yang rapi dan informatif.

#### E. Kebutuhan Non-Fungsional (Non-Functional Requirements)
1. **Keamanan (Security)**:
   - Enkripsi password menggunakan hashing algoritma Bcrypt (`Hash::make()`).
   - Proteksi CSRF (*Cross-Site Request Forgery*) pada seluruh formulir input (`@csrf`).
   - Pencegahan SQL Injection melalui Eloquent ORM (*Parameterized Prepared Statements*).
   - Autorisasi Hak Akses (*Role-Based Access Control*) via Middleware (`IsAdmin`).
2. **Integritas Data (Data Integrity)**:
   - Menggunakan Database Transaction (`DB::transaction`) saat proses pemesanan tiket untuk mencegah *race condition* (overbooking tiket).
   - Menggunakan *Foreign Key Constraints* dengan opsi `ON DELETE CASCADE` untuk menjaga konsistensi relasi tabel.
3. **Performa & Kemudahan Penggunaan (Usability)**:
   - Waktu muat halaman (*page load time*) cepat (< 2 detik).
   - Antarmuka responsif (*mobile-friendly*) menggunakan framework Tailwind CSS.
   - Pesan validasi formulir sisi server (*Server-side Validation*) yang jelas dan informatif (`$errors->all()`).

---

### 2. Fungsi ERD dan Fungsi CRUD dalam Bahasa SQL

#### A. Fungsi ERD (Entity Relationship Diagram)
ERD adalah diagram grafis yang memodelkan struktur data logis dan keterkaitan antar entitas dalam basis data relasional. Fungsinya meliputi:
1. **Cetak Biru (Blueprint) Perancangan Sistem**: Panduan visual utama bagi developer sebelum mengimplementasikan migrasi tabel pada framework atau SQL DDL.
2. **Mengidentifikasi Entitas & Atribut**: Mendefinisikan tabel apa saja yang ada (entitas: `users`, `tickets`, `orders`, `order_details`) beserta field/kolom (atribut: `id`, `concert_name`, `price`, `stock`), tipe data, serta *Primary Key* (PK).
3. **Menentukan Relasi & Kardinalitas Data**:
   - **One-to-Many (1:N)**: Satu `users` dapat memiliki banyak `orders`.
   - **One-to-Many (1:N)**: Satu `orders` memiliki banyak `order_details`.
   - **One-to-Many (1:N)**: Satu `tickets` dapat tertera di banyak `order_details`.
   - **Many-to-Many (N:M)**: Hubungan antara `orders` dan `tickets` adalah banyak-ke-banyak yang dinormalisasi menggunakan tabel penghubung (*pivot table*) `order_details`.
4. **Menjamin Integritas Referensial**: Mengatur aturan *Foreign Key* (FK) seperti `ON DELETE CASCADE` (jika data order dihapus, rincian order terkait otomatis ikut terhapus agar tidak ada data yatim/*orphan record*).
5. **Mencegah Redundansi & Anomali Data**: Membantu penerapan kaidah normalisasi (1NF, 2NF, 3NF) agar tidak terjadi duplikasi data yang memboroskan memori penyimpanan.

---

#### B. Fungsi CRUD dalam Bahasa SQL & Contoh Nyata (Kasus Tiket Konser)
CRUD merupakan singkatan dari 4 operasi inti manipulasi data pada basis data relasional:

| Huruf | Operasi | Perintah SQL | Fungsi Utama |
| :---: | :---: | :---: | :--- |
| **C** | **Create** | `INSERT INTO` | Menambahkan rekaman (*record*) data baru ke dalam tabel |
| **R** | **Read** | `SELECT` | Menampilkan, menyaring, dan mengambil data dari tabel |
| **U** | **Update** | `UPDATE ... SET` | Mengubah atau memperbarui nilai data yang sudah ada |
| **D** | **Delete** | `DELETE FROM` | Menghapus baris rekaman data dari tabel |

##### 1. Tambah Data (Create - `INSERT INTO`)
- **Fungsi**: Mendaftarkan rekaman baru ke tabel database.
- **Contoh SQL Tambah Tiket Konser Baru**:
  ```sql
  INSERT INTO tickets (concert_name, artist, venue, event_date, category, price, stock, poster, created_at, updated_at)
  VALUES ('Coldplay: Music of the Spheres', 'Coldplay', 'Gelora Bung Karno Jakarta', '2026-11-15 19:30:00', 'VIP', 3500000, 150, 'posters/coldplay.jpg', NOW(), NOW());
  ```
- **Contoh SQL Tambah Transaksi Pesanan Masuk (`orders`)**:
  ```sql
  INSERT INTO orders (user_id, order_code, customer_name, customer_email, customer_phone, total_price, status, order_date, created_at, updated_at)
  VALUES (2, 'TKT-20261021-001', 'Ahmad Dani', 'ahmad@gmail.com', '081234567890', 7000000, 'paid', '2026-10-21', NOW(), NOW());
  ```
- **Contoh SQL Tambah Rincian Tiket yang Dipesan (`order_details`)**:
  ```sql
  INSERT INTO order_details (order_id, ticket_id, quantity, unit_price, subtotal, created_at, updated_at)
  VALUES (1, 1, 2, 3500000, 7000000, NOW(), NOW());
  ```

##### 2. Nampilin Data (Read - `SELECT`)
- **Fungsi**: Membaca data dengan opsi penyaringan (*filter*), pengurutan (*sorting*), atau pembatasan kuantitas (*limit*).
- **Contoh SQL Tampil Tiket Konser yang Masih Memiliki Kuota Stok**:
  ```sql
  SELECT id, concert_name, artist, category, price, stock 
  FROM tickets 
  WHERE stock > 0 
  ORDER BY price ASC;
  ```
- **Contoh SQL Tampil Rekap Transaksi yang Masih Menunggu Pembayaran (Pending)**:
  ```sql
  SELECT order_code, customer_name, customer_phone, total_price, order_date, status 
  FROM orders 
  WHERE status = 'pending' 
  ORDER BY created_at DESC;
  ```

##### 3. Edit Data (Update - `UPDATE ... SET ... WHERE`)
- **Fungsi**: Memperbarui satu atau beberapa nilai kolom pada baris data tertentu.
- ⚠️ **CATATAN EMAS WAWANCARA ASESOR**: Klausul `WHERE` bersifat **mutlak wajib** disertakan! Jika Anda lupa menulis `WHERE`, seluruh data pada tabel tersebut akan terupdate secara massal dengan nilai yang sama.
- **Contoh SQL Update Harga & Penambahan Kuota Stok Tiket**:
  ```sql
  UPDATE tickets 
  SET price = 3200000, stock = stock + 50, updated_at = NOW() 
  WHERE id = 1;
  ```
- **Contoh SQL Ubah Status Pesanan Menjadi Lunas (Paid)**:
  ```sql
  UPDATE orders 
  SET status = 'paid', updated_at = NOW() 
  WHERE order_code = 'TKT-20261021-001';
  ```

##### 4. Hapus Data (Delete - `DELETE FROM ... WHERE`)
- **Fungsi**: Menghapus rekaman baris data tertentu dari tabel.
- ⚠️ **CATATAN EMAS WAWANCARA ASESOR**: Klausul `WHERE` wajib digunakan agar tidak menghapus seluruh isi tabel secara tidak sengaja (*accidental wipe*).
- **Contoh SQL Hapus Data Tiket Konser Tertentu**:
  ```sql
  DELETE FROM tickets 
  WHERE id = 5;
  ```

---

### 3. Apa Itu Query dan Fungsi, Contoh Nyata

#### A. Pengertian Query
**Query** adalah instruksi atau perintah terstruktur yang ditulis menggunakan bahasa query (seperti SQL - *Structured Query Language*) yang dikirimkan ke RDBMS (MySQL) untuk meminta mesin database mengambil, memfilter, mengolah, mengelompokkan, menghitung, atau memanipulasi data yang tersimpan di dalam tabel-tabel basis data.

#### B. Fungsi dan Manfaat Query
1. **Pengambilan Data yang Terfilter dan Presisi (`WHERE`, `LIKE`, `BETWEEN`)**: Menampilkan hanya data yang cocok dengan kriteria yang dicari user tanpa membebani memori server.
2. **Penggabungan Relasi Multi-Tabel (`JOIN`)**: Menyajikan informasi terpadu yang bersumber dari tabel yang berbeda berdasarkan *Foreign Key* (misal: menyajikan nama customer dari `orders` bersama judul konser dari `tickets`).
3. **Kalkulasi & Agregasi Statistik Cepat (`SUM`, `COUNT`, `AVG`, `MAX`, `MIN`)**: Menghitung omset pendapatan kotor, total tiket terjual, dan jumlah pesanan langsung di dalam mesin basis data secara instan.
4. **Analisis Pengelompokan Data (`GROUP BY` & `HAVING`)**: Memungkinkan pembuatan laporan berkala (misal: total penjualan tiket per kategori VIP vs Festival).
5. **Efisiensi Kinerja & Bandwidth**: Mengurangi beban transmisi data antara server aplikasi dan database karena hanya kolom dan baris yang dibutuhkan saja yang ditarik (`SELECT id, concert_name` vs `SELECT *`).

#### C. Contoh-Contoh Query Nyata (Kasus Tiket Konser)

##### Contoh 1: Query Agregasi Omset Pendapatan Lunas (Statistik Dashboard)
```sql
SELECT 
    SUM(total_price) AS total_pendapatan_bersih,
    COUNT(id) AS jumlah_transaksi_lunas
FROM orders 
WHERE status = 'paid';
```

##### Contoh 2: Query JOIN 3 Tabel untuk Rekapitulasi Rincian Pesanan Masuk
```sql
SELECT 
    o.order_code,
    o.customer_name,
    o.customer_phone,
    t.concert_name,
    t.category AS kategori_tiket,
    od.quantity AS jumlah_tiket,
    od.unit_price AS harga_satuan,
    od.subtotal,
    o.status AS status_pembayaran,
    o.order_date
FROM orders o
INNER JOIN order_details od ON o.id = od.order_id
INNER JOIN tickets t ON od.ticket_id = t.id
WHERE o.order_date BETWEEN '2026-10-01' AND '2026-10-31'
ORDER BY o.created_at DESC;
```

##### Contoh 3: Query GROUP BY untuk Menganalisis Tiket Terlaris
```sql
SELECT 
    t.concert_name,
    t.category,
    SUM(od.quantity) AS total_tiket_terjual,
    SUM(od.subtotal) AS total_omset_per_kategori
FROM order_details od
INNER JOIN tickets t ON od.ticket_id = t.id
INNER JOIN orders o ON od.order_id = o.id
WHERE o.status = 'paid'
GROUP BY t.id, t.concert_name, t.category
ORDER BY total_tiket_terjual DESC;
```

---

### 4. Arsitektur MVC Laravel

#### A. Definisi Konsep MVC
**MVC (Model - View - Controller)** adalah pola arsitektur perangkat lunak (*software design pattern*) yang memisahkan kode program aplikasi ke dalam tiga komponen independen berdasarkan tanggung jawabnya:

1. **Model (M)**:
   - Terletak di folder: `app/Models/` (contoh: `Ticket.php`, `Order.php`, `OrderDetail.php`).
   - Tanggung jawab: Pengelola data dan penghubung langsung ke database MySQL menggunakan **Eloquent ORM**.
   - Fitur utama: Menentukan nama tabel (`$table`), kolom yang boleh diisi (`$fillable`), dan mendefinisikan relasi antar-tabel (`hasMany`, `belongsTo`).
2. **View (V)**:
   - Terletak di folder: `resources/views/` (contoh: `admin/tickets/index.blade.php`, `customer/concerts.blade.php`).
   - Tanggung jawab: Menyajikan tampilan visual antarmuka pengguna (UI/UX) dan menangkap interaksi klik/input dari user.
   - Fitur utama: Menggunakan **Blade Template Engine** yang memungkinkan sintaks ekspresi `{{ $ticket->concert_name }}`, percabangan `@if()`, dan perulangan `@forelse()`.
3. **Controller (C)**:
   - Terletak di folder: `app/Http/Controllers/` (contoh: `TicketController.php`, `OrderReportController.php`, `BookingController.php`).
   - Tanggung jawab: Bertindak sebagai otak atau mediator (*traffic controller*).
   - Fitur utama: Menerima HTTP Request dari rute (*route*), memvalidasi formulir input, memanggil Model untuk mengambil atau menyimpan data, menerapkan logika bisnis (misal menghitung total atau mengurangi stok), lalu mengirimkan hasilnya ke file View untuk ditampilkan ke pengguna.

#### B. Komponen Pendukung MVC di Laravel
- **Route (`routes/web.php`)**: Gerbang pintu masuk yang memetakan URL yang diakses browser beserta metode HTTP-nya (`GET`, `POST`, `PUT`, `DELETE`) ke Controller dan method yang sesuai.
- **Middleware (`app/Http/Middleware/`)**: Lapisan penyaring/satpam keamanan yang memeriksa request sebelum diizinkan masuk ke Controller (misal memeriksa apakah user sudah login dan berstatus `admin`).

#### C. Alur Kerja Request-Response Lifecycle di Laravel
Jika asesor meminta Anda menjelaskan alur kerja aplikasi saat customer memesan tiket:
```
[Browser Client] 
     │ (1) User klik tombol "Beli Tiket" (Kirim HTTP POST /checkout)
     ▼
[routes/web.php] 
     │ (2) Route membaca URL dan mengarahkan ke Controller
     ▼
[Middleware: auth & IsCustomer] 
     │ (3) Memeriksa validitas sesi login dan role pengguna
     ▼
[BookingController@checkout] 
     │ (4) Controller memvalidasi input & stok tiket
     ▼
[Model: Ticket & Order] 
     │ (5) Eloquent ORM menjalankan INSERT orders & UPDATE pengurangan stok
     ▼
[Database MySQL (InnoDB)] 
     │ (6) Database mengeksekusi transaksi dan menyimpan data secara permanen
     ▼
[Controller] 
     │ (7) Controller menerima kepastian sukses dari database
     ▼
[View: my-tickets.blade.php] 
     │ (8) Blade me-render halaman HTML responsif beserta pesan sukses
     ▼
[Browser Client] (9) Browser menampilkan halaman struk E-Tiket kepada customer
```

#### D. Keuntungan Menggunakan Pola MVC di Laravel
1. **Separation of Concerns (Pemisahan Tanggung Jawab yang Jelas)**: Kode program sangat terstruktur dan bersih (kode HTML tidak tercampur aduk dengan baris query SQL dan logika PHP).
2. **Kemudahan Perawatan & Pengembangan (Maintainability)**: Jika panitia konser ingin mengganti desain tampilan kartu tiket, developer cukup mengubah file Blade View tanpa perlu khawatir merusak logika transaksi di Controller atau database.
3. **Dukungan Kolaborasi Tim**: Developer frontend dapat fokus mendesain View Blade, sementara developer backend fokus mengoptimalkan Model dan Controller.
4. **Keamanan Bawaan (Built-in Security)**: Laravel MVC secara otomatis menyediakan proteksi CSRF, sanitasi input XSS, dan prepared statements terhadap SQL Injection.
5. **Standar Penilaian Sertifikasi BNSP**: Penggunaan arsitektur MVC merupakan indikator utama kompetensi seorang *Junior Web Developer*.

---

### 5. Tools & Stack Teknologi yang Digunakan
Sampaikan kepada asesor jika ditanya tentang lingkungan pengembangan:
1. **Code Editor**: Visual Studio Code (VS Code).
2. **Web Server & Database**: XAMPP (Apache 2.4 & MySQL / MariaDB) dengan GUI phpMyAdmin.
3. **Bahasa Pemrograman**: PHP 8.x dan JavaScript ES6.
4. **Framework Backend**: Laravel (versi 10 atau 11) berarsitektur MVC dengan Eloquent ORM.
5. **Framework Frontend**: Tailwind CSS dipadukan dengan Blade Template Engine.
6. **Package Manager**: Composer (PHP) dan NPM / Vite (JavaScript).
7. **Version Control & Terminal**: Git Bash / PowerShell.
8. **Browser Debugging**: Google Chrome DevTools.

---

## 💻 BAGIAN 2: PANDUAN PRAKTEK UTAMA - APLIKASI PEMESANAN TIKET KONSER (PRA SERKOM)

---

### 🚀 PRAKTEK 1: LOGIN & REGISTER MULTI-ROLE (CUSTOMER & ADMIN)

Sistem menggunakan starter-kit **Laravel Breeze** yang dimodifikasi untuk mendukung 2 role pengguna: `admin` (panitia) dan `customer` (pembeli tiket).

#### Langkah 1.1: Tambahkan Kolom `role` pada Migration Users
Buka file migration bawaan di `database/migrations/0001_01_01_000000_create_users_table.php` (atau file migrasi create users yang ada):
```php
public function up(): void
{
    Schema::create('users', function (Blueprint $table) {
        $table->id();
        $table->string('name');
        $table->string('email')->unique();
        $table->string('phone')->nullable(); // [TAMBAHKAN] Nomor HP pemesan
        $table->timestamp('email_verified_at')->nullable();
        $table->string('password');
        // [TAMBAHKAN] Kolom role: 'admin' atau 'customer'
        $table->enum('role', ['admin', 'customer'])->default('customer');
        $table->rememberToken();
        $table->timestamps();
    });
}
```

#### Langkah 1.2: Daftarkan Kolom pada Model `app/Models/User.php`
Buka `app/Models/User.php`, tambahkan kolom baru ke array `$fillable` dan tambahkan helper method:
```php
<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;

class User extends Authenticatable
{
    use HasFactory, Notifiable;

    protected $fillable = [
        'name',
        'email',
        'phone',
        'password',
        'role',
    ];

    protected $hidden = [
        'password',
        'remember_token',
    ];

    protected function casts(): array
    {
        return [
            'email_verified_at' => 'datetime',
            'password' => 'hashed',
        ];
    }

    // [TAMBAHKAN] Helper pengecekan Role
    public function isAdmin(): bool
    {
        return $this->role === 'admin';
    }

    public function isCustomer(): bool
    {
        return $this->role === 'customer';
    }

    // [TAMBAHKAN] Relasi ke Transaksi Pemesanan (1 User has many Orders)
    public function orders()
    {
        return $this->hasMany(Order::class);
    }
}
```

#### Langkah 1.3: Buat Seeder Akun Default di `database/seeders/DatabaseSeeder.php`
Buka file `database/seeders/DatabaseSeeder.php` agar saat pengujian langsung memiliki akun siap login:
```php
<?php

namespace Database\Seeders;

use App\Models\User;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Hash;

class DatabaseSeeder extends Seeder
{
    public function run(): void
    {
        // 1. Akun Administrator (Panitia Konser)
        User::create([
            'name'     => 'Administrator Konser',
            'email'    => 'admin@tiket.com',
            'phone'    => '081122334455',
            'password' => Hash::make('password123'),
            'role'     => 'admin',
        ]);

        // 2. Akun Customer (Pembeli Tiket)
        User::create([
            'name'     => 'Budi Pembeli',
            'email'    => 'customer@gmail.com',
            'phone'    => '081234567890',
            'password' => Hash::make('password123'),
            'role'     => 'customer',
        ]);

        // 3. Panggil Seeder Tiket Konser
        $this->call([
            TicketSeeder::class,
        ]);
    }
}
```

#### Langkah 1.4: Buat Middleware Proteksi Admin
Jalankan di terminal:
```bash
php artisan make:middleware IsAdmin
```
Buka file `app/Http/Middleware/IsAdmin.php`, isi method `handle`:
```php
<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Symfony\Component\HttpFoundation\Response;

class IsAdmin
{
    public function handle(Request $request, Closure $next): Response
    {
        // Cek apakah user sudah login dan rolenya admin
        if (Auth::check() && Auth::user()->role === 'admin') {
            return $next($request);
        }

        // Jika bukan admin, tolak dan kembalikan ke katalog konser
        return redirect()->route('concerts.index')->with('error', 'Akses ditolak! Halaman ini khusus Administrator.');
    }
}
```

Daftarkan alias middleware:
- **Pada Laravel 11** (`bootstrap/app.php`):
  ```php
  ->withMiddleware(function (Middleware $middleware) {
      $middleware->alias([
          'admin' => \App\Http\Middleware\IsAdmin::class,
      ]);
  })
  ```
- **Pada Laravel 10** (`app/Http/Kernel.php` pada `$middlewareAliases`):
  ```php
  'admin' => \App\Http\Middleware\IsAdmin::class,
  ```

---

### 🎟️ PRAKTEK 2: RELASI ANTAR TABEL (SKEMA DATABASE, MIGRATION & MODEL)

Sistem Tiket Konser dirancang menggunakan **4 tabel relasional**:
```
┌──────────────┐         ┌──────────────┐         ┌────────────────────┐         ┌──────────────┐
│    users     │ 1     N │    orders    │ 1     N │   order_details    │ N     1 │   tickets    │
│──────────────│─────────│──────────────│─────────│────────────────────│─────────│──────────────│
│ id (PK)      │         │ id (PK)      │         │ id (PK)            │         │ id (PK)      │
│ name         │         │ user_id (FK) │         │ order_id (FK)      │         │ concert_name │
│ email        │         │ order_code   │         │ ticket_id (FK)     │         │ artist       │
│ phone        │         │ total_price  │         │ quantity           │         │ category     │
│ role         │         │ status       │         │ unit_price         │         │ price        │
└──────────────┘         └──────────────┘         └────────────────────┘         └──────────────┘
```

#### Langkah 2.1: Migration Master Tiket Konser (`tickets`)
Jalankan di terminal:
```bash
php artisan make:migration create_tickets_table
```
Buka file `database/migrations/xxxx_create_tickets_table.php`:
```php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('tickets', function (Blueprint $table) {
            $table->id();
            $table->string('concert_name');
            $table->string('artist');
            $table->string('venue');
            $table->dateTime('event_date');
            $table->enum('category', ['VIP', 'Festival', 'Regular'])->default('Regular');
            $table->integer('price');
            $table->integer('stock');
            $table->string('poster')->nullable();
            $table->text('description')->nullable();
            $table->timestamps();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('tickets');
    }
};
```

#### Langkah 2.2: Migration Transaksi Pesanan (`orders`)
Jalankan di terminal:
```bash
php artisan make:migration create_orders_table
```
Buka file `database/migrations/xxxx_create_orders_table.php`:
```php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('orders', function (Blueprint $table) {
            $table->id();
            // Foreign Key ke tabel users (onDelete cascade)
            $table->foreignId('user_id')->constrained('users')->onDelete('cascade');
            $table->string('order_code')->unique(); // Misal: TKT-20261021-001
            $table->string('customer_name');
            $table->string('customer_email');
            $table->string('customer_phone');
            $table->integer('total_price');
            $table->enum('status', ['pending', 'paid', 'cancelled'])->default('pending');
            $table->date('order_date');
            $table->timestamps();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('orders');
    }
};
```

#### Langkah 2.3: Migration Rincian Pesanan (`order_details`)
Jalankan di terminal:
```bash
php artisan make:migration create_order_details_table
```
Buka file `database/migrations/xxxx_create_order_details_table.php`:
```php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::create('order_details', function (Blueprint $table) {
            $table->id();
            // Foreign Key ke orders & tickets
            $table->foreignId('order_id')->constrained('orders')->onDelete('cascade');
            $table->foreignId('ticket_id')->constrained('tickets')->onDelete('cascade');
            $table->integer('quantity');
            $table->integer('unit_price'); // Menyimpan harga historis saat transaksi
            $table->integer('subtotal');
            $table->timestamps();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('order_details');
    }
};
```

#### Langkah 2.4: Model Eloquent Lengkap dengan Relasi

1. **Model `app/Models/Ticket.php`**:
   ```php
   <?php

   namespace App\Models;

   use Illuminate\Database\Eloquent\Factories\HasFactory;
   use Illuminate\Database\Eloquent\Model;

   class Ticket extends Model
   {
       use HasFactory;

       protected $fillable = [
           'concert_name',
           'artist',
           'venue',
           'event_date',
           'category',
           'price',
           'stock',
           'poster',
           'description',
       ];

       protected $casts = [
           'event_date' => 'datetime',
       ];

       // Relasi ke order_details
       public function orderDetails()
       {
           return $this->hasMany(OrderDetail::class);
       }
   }
   ```

2. **Model `app/Models/Order.php`**:
   ```php
   <?php

   namespace App\Models;

   use Illuminate\Database\Eloquent\Factories\HasFactory;
   use Illuminate\Database\Eloquent\Model;

   class Order extends Model
   {
       use HasFactory;

       protected $fillable = [
           'user_id',
           'order_code',
           'customer_name',
           'customer_email',
           'customer_phone',
           'total_price',
           'status',
           'order_date',
       ];

       protected $casts = [
           'order_date' => 'date',
       ];

       // Relasi belongsTo User
       public function user()
       {
           return $this->belongsTo(User::class);
       }

       // Relasi hasMany OrderDetail
       public function orderDetails()
       {
           return $this->hasMany(OrderDetail::class);
       }
   }
   ```

3. **Model `app/Models/OrderDetail.php`**:
   ```php
   <?php

   namespace App\Models;

   use Illuminate\Database\Eloquent\Factories\HasFactory;
   use Illuminate\Database\Eloquent\Model;

   class OrderDetail extends Model
   {
       use HasFactory;

       protected $fillable = [
           'order_id',
           'ticket_id',
           'quantity',
           'unit_price',
           'subtotal',
       ];

       // Relasi belongsTo Order
       public function order()
       {
           return $this->belongsTo(Order::class);
       }

       // Relasi belongsTo Ticket
       public function ticket()
       {
           return $this->belongsTo(Ticket::class);
       }
   }
   ```

#### Langkah 2.5: Seeder Tiket Konser Awal (`database/seeders/TicketSeeder.php`)
Jalankan di terminal:
```bash
php artisan make:seeder TicketSeeder
```
Buka file `database/seeders/TicketSeeder.php`:
```php
<?php

namespace Database\Seeders;

use App\Models\Ticket;
use Illuminate\Database\Seeder;

class TicketSeeder extends Seeder
{
    public function run(): void
    {
        Ticket::create([
            'concert_name' => 'Coldplay: Music of the Spheres World Tour',
            'artist'       => 'Coldplay',
            'venue'        => 'Stadion Utama Gelora Bung Karno, Jakarta',
            'event_date'   => '2026-11-15 19:30:00',
            'category'     => 'VIP',
            'price'        => 3500000,
            'stock'        => 50,
            'description'  => 'Akses gate utama VIP, merchandise eksklusif, dan tempat duduk bernomor di depan panggung.',
        ]);

        Ticket::create([
            'concert_name' => 'Sheila On 7: Tunggu Aku Di Jakarta',
            'artist'       => 'Sheila On 7',
            'venue'        => 'JIEXPO Kemayoran Hall A, Jakarta',
            'event_date'   => '2026-12-05 20:00:00',
            'category'     => 'Festival',
            'price'        => 750000,
            'stock'        => 200,
            'description'  => 'Area berdiri bebas (Festival Standing) paling seru bernyanyi bersama Duta & kawan-kawan.',
        ]);

        Ticket::create([
            'concert_name' => 'Tulus: Konser Monokrom Spesial',
            'artist'       => 'Tulus',
            'venue'        => 'Istora Senayan, Jakarta',
            'event_date'   => '2026-11-28 19:00:00',
            'category'     => 'Regular',
            'price'        => 450000,
            'stock'        => 150,
            'description'  => 'Area tribun duduk dengan pemandangan panggung menyeluruh dan tata suara akustik prima.',
        ]);
    }
}
```

---

### 📋 PRAKTEK 3: CRUD MASTER DATA TIKET KONSER (SISI ADMIN)

Admin memiliki hak penuh untuk menambah konser baru, mengunggah banner poster, mengubah kuota stok dan harga, serta menghapus data konser.

#### Langkah 3.1: Controller `app/Http/Controllers/Admin/TicketController.php`
Jalankan di terminal:
```bash
php artisan make:controller Admin/TicketController --resource
```
Buka file `app/Http/Controllers/Admin/TicketController.php`:
```php
<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\Ticket;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Storage;

class TicketController extends Controller
{
    // 1. Tampilkan Semua Tiket
    public function index()
    {
        $tickets = Ticket::latest()->paginate(10);
        return view('admin.tickets.index', compact('tickets'));
    }

    // 2. Form Tambah Tiket
    public function create()
    {
        return view('admin.tickets.create');
    }

    // 3. Simpan Tiket Baru (Create)
    public function store(Request $request)
    {
        $validated = $request->validate([
            'concert_name' => 'required|string|max:255',
            'artist'       => 'required|string|max:255',
            'venue'        => 'required|string|max:255',
            'event_date'   => 'required|date',
            'category'     => 'required|in:VIP,Festival,Regular',
            'price'        => 'required|numeric|min:0',
            'stock'        => 'required|integer|min:1',
            'description'  => 'nullable|string',
            'poster'       => 'nullable|image|mimes:jpeg,png,jpg|max:2048',
        ]);

        // Upload poster jika ada
        if ($request->hasFile('poster')) {
            $validated['poster'] = $request->file('poster')->store('posters', 'public');
        }

        Ticket::create($validated);

        return redirect()->route('admin.tickets.index')->with('success', 'Tiket konser berhasil ditambahkan!');
    }

    // 4. Form Edit Tiket
    public function edit(Ticket $ticket)
    {
        return view('admin.tickets.edit', compact('ticket'));
    }

    // 5. Update Tiket (Update)
    public function update(Request $request, Ticket $ticket)
    {
        $validated = $request->validate([
            'concert_name' => 'required|string|max:255',
            'artist'       => 'required|string|max:255',
            'venue'        => 'required|string|max:255',
            'event_date'   => 'required|date',
            'category'     => 'required|in:VIP,Festival,Regular',
            'price'        => 'required|numeric|min:0',
            'stock'        => 'required|integer|min:0',
            'description'  => 'nullable|string',
            'poster'       => 'nullable|image|mimes:jpeg,png,jpg|max:2048',
        ]);

        // Ganti poster jika file baru diupload
        if ($request->hasFile('poster')) {
            // Hapus poster lama jika ada
            if ($ticket->poster && Storage::disk('public')->exists($ticket->poster)) {
                Storage::disk('public')->delete($ticket->poster);
            }
            $validated['poster'] = $request->file('poster')->store('posters', 'public');
        }

        $ticket->update($validated);

        return redirect()->route('admin.tickets.index')->with('success', 'Data tiket konser berhasil diperbarui!');
    }

    // 6. Hapus Tiket (Delete)
    public function destroy(Ticket $ticket)
    {
        // Hapus file poster fisik
        if ($ticket->poster && Storage::disk('public')->exists($ticket->poster)) {
            Storage::disk('public')->delete($ticket->poster);
        }

        $ticket->delete();

        return redirect()->route('admin.tickets.index')->with('success', 'Tiket konser berhasil dihapus!');
    }
}
```

#### Langkah 3.2: View Daftar Tiket (`resources/views/admin/tickets/index.blade.php`)
```blade
<x-app-layout>
    <div class="py-6 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center mb-6">
            <div>
                <h2 class="text-2xl font-bold text-gray-800">🎟️ Master Data Tiket Konser</h2>
                <p class="text-sm text-gray-500">Kelola daftar konser, kuota tiket, harga, dan banner poster.</p>
            </div>
            <a href="{{ route('admin.tickets.create') }}" class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded shadow">
                + Tambah Tiket Konser
            </a>
        </div>

        @if(session('success'))
            <div class="bg-green-100 border-l-4 border-green-500 text-green-700 p-4 mb-4 rounded shadow-sm">
                {{ session('success') }}
            </div>
        @endif

        <div class="bg-white overflow-hidden shadow-sm sm:rounded-lg border border-gray-200">
            <table class="min-w-full divide-y divide-gray-200 text-sm">
                <thead class="bg-gray-50">
                    <tr>
                        <th class="px-4 py-3 text-left font-bold text-gray-700">Poster</th>
                        <th class="px-4 py-3 text-left font-bold text-gray-700">Nama Konser & Artis</th>
                        <th class="px-4 py-3 text-left font-bold text-gray-700">Venue & Tanggal</th>
                        <th class="px-4 py-3 text-left font-bold text-gray-700">Kategori</th>
                        <th class="px-4 py-3 text-left font-bold text-gray-700">Harga</th>
                        <th class="px-4 py-3 text-left font-bold text-gray-700">Sisa Stok</th>
                        <th class="px-4 py-3 text-center font-bold text-gray-700">Aksi</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-gray-200">
                    @forelse($tickets as $ticket)
                    <tr class="hover:bg-gray-50">
                        <td class="px-4 py-3">
                            @if($ticket->poster)
                                <img src="{{ asset('storage/' . $ticket->poster) }}" class="w-14 h-14 object-cover rounded shadow" alt="Poster">
                            @else
                                <div class="w-14 h-14 bg-gray-200 flex items-center justify-center text-xs text-gray-500 rounded">No Pic</div>
                            @endif
                        </td>
                        <td class="px-4 py-3">
                            <span class="font-bold text-gray-900 block">{{ $ticket->concert_name }}</span>
                            <span class="text-xs text-indigo-600 font-semibold">{{ $ticket->artist }}</span>
                        </td>
                        <td class="px-4 py-3 text-xs text-gray-600">
                            <div>📍 {{ $ticket->venue }}</div>
                            <div>📅 {{ $ticket->event_date->format('d M Y, H:i') }} WIB</div>
                        </td>
                        <td class="px-4 py-3">
                            @if($ticket->category === 'VIP')
                                <span class="bg-purple-100 text-purple-800 text-xs font-bold px-2.5 py-0.5 rounded">VIP</span>
                            @elseif($ticket->category === 'Festival')
                                <span class="bg-blue-100 text-blue-800 text-xs font-bold px-2.5 py-0.5 rounded">FESTIVAL</span>
                            @else
                                <span class="bg-gray-100 text-gray-800 text-xs font-bold px-2.5 py-0.5 rounded">REGULAR</span>
                            @endif
                        </td>
                        <td class="px-4 py-3 font-bold text-gray-900">
                            Rp {{ number_format($ticket->price, 0, ',', '.') }}
                        </td>
                        <td class="px-4 py-3">
                            <span class="px-2 py-1 text-xs font-bold rounded {{ $ticket->stock > 10 ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800' }}">
                                {{ $ticket->stock }} tiket
                            </span>
                        </td>
                        <td class="px-4 py-3 text-center space-x-2">
                            <a href="{{ route('admin.tickets.edit', $ticket->id) }}" class="text-indigo-600 hover:text-indigo-900 font-bold text-xs">Edit</a>
                            <form action="{{ route('admin.tickets.destroy', $ticket->id) }}" method="POST" class="inline" onsubmit="return confirm('Yakin ingin menghapus tiket konser ini?')">
                                @csrf
                                @method('DELETE')
                                <button type="submit" class="text-red-600 hover:text-red-900 font-bold text-xs ml-2">Hapus</button>
                            </form>
                        </td>
                    </tr>
                    @empty
                    <tr>
                        <td colspan="7" class="px-4 py-8 text-center text-gray-400">Belum ada tiket konser yang didaftarkan.</td>
                    </tr>
                    @endforelse
                </tbody>
            </table>
            <div class="p-4">
                {{ $tickets->links() }}
            </div>
        </div>
    </div>
</x-app-layout>
```

#### Langkah 3.3: View Form Tambah Tiket (`resources/views/admin/tickets/create.blade.php`)
```blade
<x-app-layout>
    <div class="py-6 max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
            <h2 class="text-xl font-bold text-gray-800 mb-4 border-b pb-2">➕ Tambah Tiket Konser Baru</h2>

            @if($errors->any())
                <div class="bg-red-100 border-l-4 border-red-500 text-red-700 p-3 mb-4 rounded text-sm">
                    <ul class="list-disc list-inside">
                        @foreach($errors->all() as $error)
                            <li>{{ $error }}</li>
                        @endforeach
                    </ul>
                </div>
            @endif

            <form action="{{ route('admin.tickets.store') }}" method="POST" enctype="multipart/form-data" class="space-y-4">
                @csrf
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-sm font-semibold text-gray-700">Nama Konser</label>
                        <input type="text" name="concert_name" value="{{ old('concert_name') }}" required class="w-full border-gray-300 rounded shadow-sm text-sm" placeholder="Contoh: Coldplay World Tour">
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-gray-700">Artis / Musisi</label>
                        <input type="text" name="artist" value="{{ old('artist') }}" required class="w-full border-gray-300 rounded shadow-sm text-sm" placeholder="Contoh: Coldplay">
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-sm font-semibold text-gray-700">Lokasi / Venue</label>
                        <input type="text" name="venue" value="{{ old('venue') }}" required class="w-full border-gray-300 rounded shadow-sm text-sm" placeholder="Contoh: Stadion GBK Jakarta">
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-gray-700">Tanggal & Jam Acara</label>
                        <input type="datetime-local" name="event_date" value="{{ old('event_date') }}" required class="w-full border-gray-300 rounded shadow-sm text-sm">
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div>
                        <label class="block text-sm font-semibold text-gray-700">Kategori Tiket</label>
                        <select name="category" required class="w-full border-gray-300 rounded shadow-sm text-sm">
                            <option value="VIP" {{ old('category') == 'VIP' ? 'selected' : '' }}>VIP</option>
                            <option value="Festival" {{ old('category') == 'Festival' ? 'selected' : '' }}>Festival</option>
                            <option value="Regular" {{ old('category') == 'Regular' ? 'selected' : '' }}>Regular</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-gray-700">Harga Satuan (Rp)</label>
                        <input type="number" name="price" value="{{ old('price') }}" required min="0" class="w-full border-gray-300 rounded shadow-sm text-sm" placeholder="Contoh: 750000">
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-gray-700">Kuota Stok Tiket</label>
                        <input type="number" name="stock" value="{{ old('stock') }}" required min="1" class="w-full border-gray-300 rounded shadow-sm text-sm" placeholder="Contoh: 100">
                    </div>
                </div>

                <div>
                    <label class="block text-sm font-semibold text-gray-700">Upload Banner Poster</label>
                    <input type="file" name="poster" accept="image/*" class="w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded file:border-0 file:text-sm file:font-semibold file:bg-indigo-50 file:text-indigo-700 hover:file:bg-indigo-100">
                </div>

                <div>
                    <label class="block text-sm font-semibold text-gray-700">Deskripsi / Ketentuan Konser</label>
                    <textarea name="description" rows="3" class="w-full border-gray-300 rounded shadow-sm text-sm" placeholder="Tuliskan info gate, dresscode, atau aturan venue...">{{ old('description') }}</textarea>
                </div>

                <div class="flex justify-end space-x-2 pt-4 border-t">
                    <a href="{{ route('admin.tickets.index') }}" class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded text-sm">Batal</a>
                    <button type="submit" class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded text-sm">Simpan Tiket</button>
                </div>
            </form>
        </div>
    </div>
</x-app-layout>
```

---

### 📊 PRAKTEK 4: REKAP LAPORAN PESANAN MASUK (DASHBOARD ADMIN)

Fitur rekapitulasi adalah syarat utama kelulusan sertifikasi. Dashboard ini menyajikan **ringkasan statistik omset**, **filter tanggal**, dan **tabel pesanan masuk dengan opsi ubah status instan**.

#### Langkah 4.1: Controller `app/Http/Controllers/Admin/OrderReportController.php`
Jalankan di terminal:
```bash
php artisan make:controller Admin/OrderReportController
```
Buka file `app/Http/Controllers/Admin/OrderReportController.php`:
```php
<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\Order;
use App\Models\OrderDetail;
use Illuminate\Http\Request;

class OrderReportController extends Controller
{
    public function index(Request $request)
    {
        // 1. Hitung Kartu Statistik Ringkasan
        $totalRevenue = Order::where('status', 'paid')->sum('total_price');
        $totalTicketsSold = OrderDetail::whereHas('order', function ($q) {
            $q->where('status', 'paid');
        })->sum('quantity');
        $pendingOrdersCount = Order::where('status', 'pending')->count();
        $paidOrdersCount = Order::where('status', 'paid')->count();

        // 2. Query Rekap Pesanan Masuk (Eager Loading untuk Mencegah N+1 Problem)
        $query = Order::with(['user', 'orderDetails.ticket'])->latest();

        // 3. Filter Rentang Tanggal
        if ($request->filled('start_date') && $request->filled('end_date')) {
            $query->whereBetween('order_date', [$request->start_date, $request->end_date]);
        }

        // 4. Filter Status Pembayaran
        if ($request->filled('status')) {
            $query->where('status', $request->status);
        }

        $orders = $query->paginate(15)->withQueryString();

        return view('admin.orders.index', compact(
            'orders',
            'totalRevenue',
            'totalTicketsSold',
            'pendingOrdersCount',
            'paidOrdersCount'
        ));
    }

    // Ubah Status Pesanan (Pending -> Paid / Cancelled)
    public function updateStatus(Request $request, $id)
    {
        $request->validate([
            'status' => 'required|in:pending,paid,cancelled',
        ]);

        $order = Order::findOrFail($id);
        $order->update(['status' => $request->status]);

        return back()->with('success', "Status pesanan {$order->order_code} berhasil diubah menjadi " . strtoupper($request->status));
    }

    // Tampilan Cetak Laporan (Print / PDF Ready)
    public function printReport(Request $request)
    {
        $query = Order::with(['user', 'orderDetails.ticket'])->latest();

        if ($request->filled('start_date') && $request->filled('end_date')) {
            $query->whereBetween('order_date', [$request->start_date, $request->end_date]);
        }

        $orders = $query->get();
        $totalRevenue = $orders->where('status', 'paid')->sum('total_price');

        return view('admin.orders.print', compact('orders', 'totalRevenue'));
    }
}
```

#### Langkah 4.2: View Dashboard Rekap Pesanan (`resources/views/admin/orders/index.blade.php`)
```blade
<x-app-layout>
    <div class="py-6 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6">
        <!-- 1. Header & Tombol Cetak -->
        <div class="flex justify-between items-center">
            <div>
                <h2 class="text-2xl font-bold text-gray-800">📊 Rekap Laporan Pesanan Masuk</h2>
                <p class="text-sm text-gray-500">Pantau transaksi pemesanan tiket konser dari customer secara real-time.</p>
            </div>
            <a href="{{ route('admin.orders.print', request()->query()) }}" target="_blank" class="bg-gray-800 hover:bg-black text-white font-bold py-2 px-4 rounded shadow text-sm">
                🖨️ Cetak Rekapitulasi (PDF)
            </a>
        </div>

        <!-- 2. Kartu Statistik Ringkasan (Stat Cards) -->
        <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
            <div class="bg-white p-5 rounded-lg border border-gray-200 shadow-sm border-l-4 border-l-green-500">
                <span class="text-xs font-bold text-gray-400 uppercase">Total Omset Lunas</span>
                <p class="text-2xl font-extrabold text-green-600 mt-1">Rp {{ number_format($totalRevenue, 0, ',', '.') }}</p>
            </div>
            <div class="bg-white p-5 rounded-lg border border-gray-200 shadow-sm border-l-4 border-l-indigo-500">
                <span class="text-xs font-bold text-gray-400 uppercase">Tiket Terjual</span>
                <p class="text-2xl font-extrabold text-indigo-600 mt-1">{{ number_format($totalTicketsSold) }} tiket</p>
            </div>
            <div class="bg-white p-5 rounded-lg border border-gray-200 shadow-sm border-l-4 border-l-yellow-500">
                <span class="text-xs font-bold text-gray-400 uppercase">Pesanan Pending</span>
                <p class="text-2xl font-extrabold text-yellow-600 mt-1">{{ $pendingOrdersCount }} order</p>
            </div>
            <div class="bg-white p-5 rounded-lg border border-gray-200 shadow-sm border-l-4 border-l-blue-500">
                <span class="text-xs font-bold text-gray-400 uppercase">Pesanan Lunas</span>
                <p class="text-2xl font-extrabold text-blue-600 mt-1">{{ $paidOrdersCount }} order</p>
            </div>
        </div>

        <!-- 3. Form Filter Periode Tanggal & Status -->
        <div class="bg-white p-4 rounded-lg border border-gray-200 shadow-sm">
            <form method="GET" action="{{ route('admin.orders.index') }}" class="grid grid-cols-1 md:grid-cols-4 gap-3 items-end">
                <div>
                    <label class="block text-xs font-bold text-gray-600 mb-1">Dari Tanggal:</label>
                    <input type="date" name="start_date" value="{{ request('start_date') }}" class="w-full border-gray-300 rounded text-xs">
                </div>
                <div>
                    <label class="block text-xs font-bold text-gray-600 mb-1">Sampai Tanggal:</label>
                    <input type="date" name="end_date" value="{{ request('end_date') }}" class="w-full border-gray-300 rounded text-xs">
                </div>
                <div>
                    <label class="block text-xs font-bold text-gray-600 mb-1">Status Pembayaran:</label>
                    <select name="status" class="w-full border-gray-300 rounded text-xs">
                        <option value="">Semua Status</option>
                        <option value="pending" {{ request('status') == 'pending' ? 'selected' : '' }}>Pending</option>
                        <option value="paid" {{ request('status') == 'paid' ? 'selected' : '' }}>Paid (Lunas)</option>
                        <option value="cancelled" {{ request('status') == 'cancelled' ? 'selected' : '' }}>Cancelled</option>
                    </select>
                </div>
                <div class="flex space-x-2">
                    <button type="submit" class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded text-xs flex-1">
                        Filter Laporan
                    </button>
                    @if(request()->hasAny(['start_date', 'end_date', 'status']))
                        <a href="{{ route('admin.orders.index') }}" class="bg-gray-200 hover:bg-gray-300 text-gray-700 font-bold py-2 px-3 rounded text-xs">
                            Reset
                        </a>
                    @endif
                </div>
            </form>
        </div>

        @if(session('success'))
            <div class="bg-green-100 border-l-4 border-green-500 text-green-700 p-4 rounded shadow-sm text-sm">
                {{ session('success') }}
            </div>
        @endif

        <!-- 4. Tabel Detail Transaksi Pesanan Masuk -->
        <div class="bg-white overflow-hidden shadow-sm sm:rounded-lg border border-gray-200">
            <table class="min-w-full divide-y divide-gray-200 text-sm">
                <thead class="bg-gray-100 text-xs font-bold text-gray-700 uppercase">
                    <tr>
                        <th class="px-4 py-3 text-left">Kode Booking</th>
                        <th class="px-4 py-3 text-left">Nama Pemesan</th>
                        <th class="px-4 py-3 text-left">Rincian Tiket Konser</th>
                        <th class="px-4 py-3 text-left">Total Tagihan</th>
                        <th class="px-4 py-3 text-left">Tanggal</th>
                        <th class="px-4 py-3 text-left">Status</th>
                        <th class="px-4 py-3 text-center">Ubah Status</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-gray-200">
                    @forelse($orders as $order)
                    <tr class="hover:bg-gray-50">
                        <td class="px-4 py-3 font-mono font-bold text-indigo-600">
                            {{ $order->order_code }}
                        </td>
                        <td class="px-4 py-3">
                            <span class="font-bold text-gray-900 block">{{ $order->customer_name }}</span>
                            <span class="text-xs text-gray-500">{{ $order->customer_phone }}</span>
                        </td>
                        <td class="px-4 py-3">
                            <ul class="text-xs space-y-1">
                                @foreach($order->orderDetails as $detail)
                                    <li>
                                        <strong>{{ $detail->ticket->concert_name ?? 'Tiket' }}</strong> 
                                        ({{ $detail->ticket->category ?? '-' }}) x{{ $detail->quantity }}
                                        <span class="text-gray-500">= Rp {{ number_format($detail->subtotal) }}</span>
                                    </li>
                                @endforeach
                            </ul>
                        </td>
                        <td class="px-4 py-3 font-bold text-green-600">
                            Rp {{ number_format($order->total_price, 0, ',', '.') }}
                        </td>
                        <td class="px-4 py-3 text-xs text-gray-500">
                            {{ $order->order_date->format('d/m/Y') }}
                        </td>
                        <td class="px-4 py-3">
                            @if($order->status === 'paid')
                                <span class="bg-green-100 text-green-800 text-xs font-bold px-2 py-0.5 rounded">PAID</span>
                            @elseif($order->status === 'pending')
                                <span class="bg-yellow-100 text-yellow-800 text-xs font-bold px-2 py-0.5 rounded">PENDING</span>
                            @else
                                <span class="bg-red-100 text-red-800 text-xs font-bold px-2 py-0.5 rounded">CANCELLED</span>
                            @endif
                        </td>
                        <td class="px-4 py-3 text-center">
                            <form action="{{ route('admin.orders.updateStatus', $order->id) }}" method="POST">
                                @csrf
                                @method('PATCH')
                                <select name="status" onchange="this.form.submit()" class="text-xs border-gray-300 rounded font-semibold p-1">
                                    <option value="pending" {{ $order->status == 'pending' ? 'selected' : '' }}>Pending</option>
                                    <option value="paid" {{ $order->status == 'paid' ? 'selected' : '' }}>Paid</option>
                                    <option value="cancelled" {{ $order->status == 'cancelled' ? 'selected' : '' }}>Cancelled</option>
                                </select>
                            </form>
                        </td>
                    </tr>
                    @empty
                    <tr>
                        <td colspan="7" class="px-4 py-8 text-center text-gray-400">Tidak ada data transaksi pesanan yang sesuai filter.</td>
                    </tr>
                    @endforelse
                </tbody>
            </table>
            <div class="p-4">
                {{ $orders->links() }}
            </div>
        </div>
    </div>
</x-app-layout>
```

#### Langkah 4.3: View Cetak Rekapitulasi (`resources/views/admin/orders/print.blade.php`)
```blade
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Laporan Rekapitulasi Penjualan Tiket Konser</title>
    <style>
        body { font-family: Arial, sans-serif; font-size: 12px; margin: 20px; color: #111; }
        .header { text-align: center; border-bottom: 2px solid #000; padding-bottom: 10px; margin-bottom: 15px; }
        .header h1 { margin: 0; font-size: 18px; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        th, td { border: 1px solid #333; padding: 6px 8px; text-align: left; }
        th { background-color: #eee; }
        .text-right { text-align: right; }
        .total-box { margin-top: 15px; font-weight: bold; font-size: 14px; text-align: right; }
    </style>
</head>
<body onload="window.print()">
    <div class="header">
        <h1>LAPORAN TRANSAKSI PENJUALAN TIKET KONSER</h1>
        <p>Dicetak pada: {{ now()->format('d/m/Y H:i') }} WIB</p>
    </div>

    <table>
        <thead>
            <tr>
                <th>No</th>
                <th>Kode Booking</th>
                <th>Nama Pemesan</th>
                <th>Konser & Kategori</th>
                <th>Qty</th>
                <th>Total Bayar</th>
                <th>Status</th>
                <th>Tanggal Order</th>
            </tr>
        </thead>
        <tbody>
            @foreach($orders as $idx => $order)
            <tr>
                <td>{{ $idx + 1 }}</td>
                <td>{{ $order->order_code }}</td>
                <td>{{ $order->customer_name }}</td>
                <td>
                    @foreach($order->orderDetails as $d)
                        {{ $d->ticket->concert_name ?? 'Tiket' }} ({{ $d->ticket->category ?? '-' }})<br>
                    @endforeach
                </td>
                <td>
                    @foreach($order->orderDetails as $d)
                        {{ $d->quantity }} tiket<br>
                    @endforeach
                </td>
                <td class="text-right">Rp {{ number_format($order->total_price, 0, ',', '.') }}</td>
                <td>{{ strtoupper($order->status) }}</td>
                <td>{{ $order->order_date->format('d/m/Y') }}</td>
            </tr>
            @endforeach
        </tbody>
    </table>

    <div class="total-box">
        TOTAL OMSET DITERIMA (LUNAS): Rp {{ number_format($totalRevenue, 0, ',', '.') }}
    </div>
</body>
</html>
```

---

### 🛒 PRAKTEK 5: SISI CUSTOMER (KATALOG KONSER, PEMESANAN ATOMIK & E-TIKET)

Customer dapat menjelajahi katalog konser aktif, memilih jumlah tiket, melakukan checkout aman (dengan pengurangan kuota stok otomatis dalam transaksi database), melihat riwayat pemesanan, dan mencetak E-Tiket.

#### Langkah 5.1: Controller `app/Http/Controllers/Customer/BookingController.php`
Jalankan di terminal:
```bash
php artisan make:controller Customer/BookingController
```
Buka file `app/Http/Controllers/Customer/BookingController.php`:
```php
<?php

namespace App\Http\Controllers\Customer;

use App\Http\Controllers\Controller;
use App\Models\Order;
use App\Models\OrderDetail;
use App\Models\Ticket;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\DB;

class BookingController extends Controller
{
    // 1. Katalog Konser Publik
    public function index()
    {
        $tickets = Ticket::where('stock', '>', 0)->latest()->get();
        return view('customer.concerts', compact('tickets'));
    }

    // 2. Form Pemesanan Tiket (Checkout)
    public function showBookingForm($id)
    {
        $ticket = Ticket::findOrFail($id);
        return view('customer.booking-form', compact('ticket'));
    }

    // 3. Proses Checkout Transaksi (Atomik DB::transaction)
    public function checkout(Request $request)
    {
        $request->validate([
            'ticket_id' => 'required|exists:tickets,id',
            'quantity'  => 'required|integer|min:1|max:5',
        ]);

        $ticket = Ticket::findOrFail($request->ticket_id);

        // Validasi kuota tiket
        if ($ticket->stock < $request->quantity) {
            return back()->with('error', 'Maaf, kuota tiket yang diminta melebihi sisa stok yang tersedia!');
        }

        // Jalankan Database Transaction untuk Menjamin Integritas Data ACID
        DB::beginTransaction();
        try {
            $user = Auth::user();
            $subtotal = $ticket->price * $request->quantity;
            $orderCode = 'TKT-' . date('Ymd') . '-' . strtoupper(substr(uniqid(), -4));

            // Simpan Data Header Order
            $order = Order::create([
                'user_id'        => $user->id,
                'order_code'     => $orderCode,
                'customer_name'  => $user->name,
                'customer_email' => $user->email,
                'customer_phone' => $user->phone ?? '08123456789',
                'total_price'    => $subtotal,
                'status'         => 'paid', // Simulasi langsung lunas untuk ujian serkom
                'order_date'     => now()->toDateString(),
            ]);

            // Simpan Detail Order
            OrderDetail::create([
                'order_id'   => $order->id,
                'ticket_id'  => $ticket->id,
                'quantity'   => $request->quantity,
                'unit_price' => $ticket->price,
                'subtotal'   => $subtotal,
            ]);

            // Kurangi Stok Tiket secara Atomik
            $ticket->decrement('stock', $request->quantity);

            DB::commit();

            return redirect()->route('customer.myTickets')->with('success', "Pemesanan berhasil! Kode Booking Anda: {$orderCode}");
        } catch (\Exception $e) {
            DB::rollBack();
            return back()->with('error', 'Terjadi kesalahan sistem saat memproses tiket: ' . $e->getMessage());
        }
    }

    // 4. Riwayat Tiket Saya
    public function myTickets()
    {
        $orders = Order::where('user_id', Auth::id())
            ->with('orderDetails.ticket')
            ->latest()
            ->get();

        return view('customer.my-tickets', compact('orders'));
    }

    // 5. Cetak E-Tiket Digital
    public function printTicket($id)
    {
        $order = Order::where('user_id', Auth::id())
            ->where('id', $id)
            ->with('orderDetails.ticket')
            ->firstOrFail();

        return view('customer.e-ticket', compact('order'));
    }
}
```

#### Langkah 5.2: View Katalog Konser (`resources/views/customer/concerts.blade.php`)
```blade
<x-app-layout>
    <div class="py-8 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-8">
            <h1 class="text-3xl font-extrabold text-gray-900">🎵 Jadwal Konser Musik & Tiket Resmi</h1>
            <p class="text-gray-600 mt-2">Dapatkan tiket konser musisi favoritmu secara resmi, aman, dan tanpa calo.</p>
        </div>

        @if(session('error'))
            <div class="bg-red-100 border-l-4 border-red-500 text-red-700 p-4 mb-6 rounded">
                {{ session('error') }}
            </div>
        @endif

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            @forelse($tickets as $ticket)
            <div class="bg-white rounded-xl shadow-md overflow-hidden border border-gray-100 hover:shadow-lg transition">
                @if($ticket->poster)
                    <img src="{{ asset('storage/' . $ticket->poster) }}" class="h-48 w-full object-cover" alt="Poster">
                @else
                    <div class="h-48 bg-gradient-to-r from-indigo-500 to-purple-600 flex items-center justify-center text-white font-bold text-lg">
                        {{ $ticket->artist }}
                    </div>
                @endif
                <div class="p-5">
                    <div class="flex justify-between items-center mb-2">
                        <span class="text-xs font-bold px-2 py-0.5 rounded {{ $ticket->category == 'VIP' ? 'bg-purple-100 text-purple-800' : 'bg-blue-100 text-blue-800' }}">
                            {{ $ticket->category }}
                        </span>
                        <span class="text-xs text-gray-500 font-semibold">Sisa {{ $ticket->stock }} tiket</span>
                    </div>
                    <h3 class="text-lg font-bold text-gray-900 leading-snug">{{ $ticket->concert_name }}</h3>
                    <p class="text-indigo-600 font-semibold text-sm mt-1">🎤 {{ $ticket->artist }}</p>
                    <p class="text-xs text-gray-500 mt-2">📍 {{ $ticket->venue }}</p>
                    <p class="text-xs text-gray-500">📅 {{ $ticket->event_date->format('d M Y, H:i') }} WIB</p>
                    
                    <div class="mt-4 pt-3 border-t flex justify-between items-center">
                        <div>
                            <span class="text-xs text-gray-400 block">Harga Tiket:</span>
                            <span class="text-lg font-extrabold text-indigo-700">Rp {{ number_format($ticket->price, 0, ',', '.') }}</span>
                        </div>
                        <a href="{{ route('customer.book', $ticket->id) }}" class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded text-xs shadow">
                            Pesan Tiket
                        </a>
                    </div>
                </div>
            </div>
            @empty
            <div class="col-span-3 text-center py-12 text-gray-400">
                Belum ada tiket konser yang tersedia saat ini.
            </div>
            @endforelse
        </div>
    </div>
</x-app-layout>
```

#### Langkah 5.3: View Form Booking Tiket (`resources/views/customer/booking-form.blade.php`)
```blade
<x-app-layout>
    <div class="py-8 max-w-2xl mx-auto px-4">
        <div class="bg-white p-6 rounded-xl shadow-md border border-gray-200">
            <h2 class="text-xl font-bold text-gray-900 mb-4 border-b pb-2">🎟️ Konfirmasi Pemesanan Tiket</h2>

            <div class="bg-indigo-50 p-4 rounded-lg mb-6">
                <h3 class="font-bold text-indigo-900 text-base">{{ $ticket->concert_name }}</h3>
                <p class="text-xs text-indigo-700 mt-1">Artis: {{ $ticket->artist }} | Kategori: {{ $ticket->category }}</p>
                <p class="text-xs text-gray-600 mt-1">📍 {{ $ticket->venue }}</p>
                <p class="text-xs text-gray-600">📅 {{ $ticket->event_date->format('d M Y, H:i') }} WIB</p>
                <p class="text-sm font-bold text-indigo-800 mt-2">Harga: Rp {{ number_format($ticket->price) }} / tiket</p>
            </div>

            <form action="{{ route('customer.checkout') }}" method="POST">
                @csrf
                <input type="hidden" name="ticket_id" value="{{ $ticket->id }}">

                <div class="mb-4">
                    <label class="block text-sm font-semibold text-gray-700 mb-1">Nama Pemesan</label>
                    <input type="text" value="{{ Auth::user()->name }}" readonly class="w-full bg-gray-100 border-gray-300 rounded text-sm">
                </div>

                <div class="mb-4">
                    <label class="block text-sm font-semibold text-gray-700 mb-1">Email Konfirmasi</label>
                    <input type="email" value="{{ Auth::user()->email }}" readonly class="w-full bg-gray-100 border-gray-300 rounded text-sm">
                </div>

                <div class="mb-6">
                    <label class="block text-sm font-semibold text-gray-700 mb-1">Jumlah Tiket (Maksimal 5)</label>
                    <input type="number" id="qtyInput" name="quantity" value="1" min="1" max="{{ min(5, $ticket->stock) }}" required class="w-full border-gray-300 rounded text-sm" oninput="updateTotal()">
                    <span class="text-xs text-gray-500">Sisa stok tersedia: {{ $ticket->stock }} tiket.</span>
                </div>

                <div class="bg-gray-50 p-4 rounded-lg mb-6 flex justify-between items-center border">
                    <span class="text-sm font-bold text-gray-700">Total Pembayaran:</span>
                    <span id="totalDisplay" class="text-xl font-extrabold text-green-600">Rp {{ number_format($ticket->price) }}</span>
                </div>

                <div class="flex space-x-2">
                    <a href="{{ route('concerts.index') }}" class="w-1/3 bg-gray-200 hover:bg-gray-300 text-gray-800 text-center font-bold py-2.5 rounded text-sm">Batal</a>
                    <button type="submit" class="w-2/3 bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2.5 rounded text-sm shadow">Bayar & Cetak Tiket</button>
                </div>
            </form>
        </div>
    </div>

    <script>
        const pricePerTicket = {{ $ticket->price }};
        function updateTotal() {
            const qty = document.getElementById('qtyInput').value || 1;
            const total = qty * pricePerTicket;
            document.getElementById('totalDisplay').innerText = 'Rp ' + total.toLocaleString('id-ID');
        }
    </script>
</x-app-layout>
```

#### Langkah 5.4: View Riwayat Pemesanan (`resources/views/customer/my-tickets.blade.php`)
```blade
<x-app-layout>
    <div class="py-8 max-w-6xl mx-auto px-4">
        <h2 class="text-2xl font-bold text-gray-900 mb-4">🎫 Riwayat Tiket Konser Saya</h2>

        @if(session('success'))
            <div class="bg-green-100 border-l-4 border-green-500 text-green-700 p-4 mb-6 rounded">
                {{ session('success') }}
            </div>
        @endif

        <div class="bg-white overflow-hidden shadow-sm rounded-lg border border-gray-200">
            <table class="min-w-full divide-y divide-gray-200 text-sm">
                <thead class="bg-gray-50 text-xs font-bold text-gray-600 uppercase">
                    <tr>
                        <th class="px-4 py-3 text-left">Kode Booking</th>
                        <th class="px-4 py-3 text-left">Konser</th>
                        <th class="px-4 py-3 text-left">Kategori</th>
                        <th class="px-4 py-3 text-left">Jumlah</th>
                        <th class="px-4 py-3 text-left">Total Bayar</th>
                        <th class="px-4 py-3 text-left">Status</th>
                        <th class="px-4 py-3 text-center">E-Tiket</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-gray-200">
                    @forelse($orders as $order)
                        @foreach($order->orderDetails as $detail)
                        <tr class="hover:bg-gray-50">
                            <td class="px-4 py-3 font-mono font-bold text-indigo-600">{{ $order->order_code }}</td>
                            <td class="px-4 py-3 font-semibold">{{ $detail->ticket->concert_name ?? '-' }}</td>
                            <td class="px-4 py-3">{{ $detail->ticket->category ?? '-' }}</td>
                            <td class="px-4 py-3">{{ $detail->quantity }} tiket</td>
                            <td class="px-4 py-3 font-bold text-green-600">Rp {{ number_format($order->total_price) }}</td>
                            <td class="px-4 py-3">
                                <span class="bg-green-100 text-green-800 text-xs font-bold px-2 py-0.5 rounded">{{ strtoupper($order->status) }}</span>
                            </td>
                            <td class="px-4 py-3 text-center">
                                <a href="{{ route('customer.printTicket', $order->id) }}" target="_blank" class="bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-bold py-1 px-3 rounded shadow">
                                    Cetak E-Tiket
                                </a>
                            </td>
                        </tr>
                        @endforeach
                    @empty
                    <tr>
                        <td colspan="7" class="px-4 py-8 text-center text-gray-400">Anda belum pernah memesan tiket konser.</td>
                    </tr>
                    @endforelse
                </tbody>
            </table>
        </div>
    </div>
</x-app-layout>
```

#### Langkah 5.5: View Layout E-Tiket (`resources/views/customer/e-ticket.blade.php`)
```blade
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>E-Ticket Resmi Konser - {{ $order->order_code }}</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 30px; background: #f3f4f6; color: #111; }
        .ticket-card { max-width: 650px; margin: 0 auto; background: #fff; border-radius: 12px; border: 2px dashed #4f46e5; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        .ticket-header { background: #4f46e5; color: #fff; padding: 20px; text-align: center; }
        .ticket-header h1 { margin: 0; font-size: 20px; letter-spacing: 1px; }
        .ticket-body { padding: 24px; }
        .row { display: flex; justify-content: space-between; margin-bottom: 12px; }
        .label { font-size: 11px; color: #6b7280; text-transform: uppercase; font-weight: bold; }
        .val { font-size: 14px; font-weight: bold; color: #111827; }
        .barcode { text-align: center; margin-top: 20px; padding-top: 15px; border-top: 1px solid #e5e7eb; font-family: monospace; font-size: 18px; letter-spacing: 4px; }
        .btn-print { display: block; width: 200px; margin: 20px auto; padding: 10px; background: #4f46e5; color: #fff; text-align: center; text-decoration: none; border-radius: 6px; font-weight: bold; }
        @media print { .btn-print { display: none; } body { background: #fff; margin: 0; } }
    </style>
</head>
<body>
    <a href="javascript:window.print()" class="btn-print">🖨️ Cetak / Simpan PDF</a>

    <div class="ticket-card">
        <div class="ticket-header">
            <h1>OFFICIAL CONCERT PASS (E-TIKET)</h1>
            <p style="margin: 5px 0 0 0; font-size: 12px;">Tunjukkan E-Tiket ini di Pintu Gate Masuk Venue</p>
        </div>
        <div class="ticket-body">
            @foreach($order->orderDetails as $detail)
            <div class="row">
                <div>
                    <div class="label">Konser</div>
                    <div class="val">{{ $detail->ticket->concert_name }}</div>
                </div>
                <div style="text-align: right;">
                    <div class="label">Kategori</div>
                    <div class="val" style="color: #4f46e5;">{{ $detail->ticket->category }}</div>
                </div>
            </div>

            <div class="row">
                <div>
                    <div class="label">Venue & Tanggal</div>
                    <div class="val">{{ $detail->ticket->venue }}</div>
                    <div style="font-size: 12px; color: #4b5563;">{{ $detail->ticket->event_date->format('d F Y, H:i') }} WIB</div>
                </div>
                <div style="text-align: right;">
                    <div class="label">Jumlah Tiket</div>
                    <div class="val">{{ $detail->quantity }} Orang</div>
                </div>
            </div>
            @endforeach

            <hr style="border: 0; border-top: 1px dashed #ccc; margin: 16px 0;">

            <div class="row">
                <div>
                    <div class="label">Nama Pemegang Tiket</div>
                    <div class="val">{{ $order->customer_name }} ({{ $order->customer_phone }})</div>
                </div>
                <div style="text-align: right;">
                    <div class="label">Status</div>
                    <div class="val" style="color: #10b981;">LUNAS (CONFIRMED)</div>
                </div>
            </div>

            <div class="barcode">
                ||| | ||||| |||| || |||||| |||| | ||<br>
                <span>{{ $order->order_code }}</span>
            </div>
        </div>
    </div>
</body>
</html>
```

---

### 🌐 PRAKTEK 6: FILE ROUTING LENGKAP (`routes/web.php`)

Seluruh alur Customer dan Admin disatukan di file `routes/web.php`:
```php
<?php

use App\Http\Controllers\ProfileController;
use App\Http\Controllers\Customer\BookingController;
use App\Http\Controllers\Admin\TicketController;
use App\Http\Controllers\Admin\OrderReportController;
use Illuminate\Support\Facades\Route;

// 1. SISI PUBLIK / CUSTOMER
Route::get('/', [BookingController::class, 'index'])->name('concerts.index');

// 2. SISI CUSTOMER (Wajib Login)
Route::middleware('auth')->group(function () {
    Route::get('/booking/{id}', [BookingController::class, 'showBookingForm'])->name('customer.book');
    Route::post('/checkout', [BookingController::class, 'checkout'])->name('customer.checkout');
    Route::get('/my-tickets', [BookingController::class, 'myTickets'])->name('customer.myTickets');
    Route::get('/my-tickets/{id}/print', [BookingController::class, 'printTicket'])->name('customer.printTicket');

    // Profil Bawaan Breeze
    Route::get('/profile', [ProfileController::class, 'edit'])->name('profile.edit');
    Route::patch('/profile', [ProfileController::class, 'update'])->name('profile.update');
    Route::delete('/profile', [ProfileController::class, 'destroy'])->name('profile.destroy');
});

// 3. SISI ADMINISTRATOR (Wajib Login & Middleware Admin)
Route::middleware(['auth', 'admin'])->prefix('admin')->name('admin.')->group(function () {
    // Dashboard Rekap Laporan Pesanan Masuk
    Route::get('/dashboard', [OrderReportController::class, 'index'])->name('orders.index');
    Route::patch('/orders/{id}/status', [OrderReportController::class, 'updateStatus'])->name('orders.updateStatus');
    Route::get('/orders/print', [OrderReportController::class, 'printReport'])->name('orders.print');

    // CRUD Master Data Tiket Konser
    Route::resource('tickets', TicketController::class);
});

require __DIR__.'/auth.php';
```

---

## 🍽️ BAGIAN 3: PANDUAN KASUS REFERENSI - APLIKASI PEMESANAN MAKANAN (RESTORAN)

Jika asesor penguji Anda memberikan studi kasus **Aplikasi Pemesanan Makanan / Resto**, strukturnya memiliki kemiripan 1:1:
1. Tabel `foods` (analog dengan `tickets`): Menyimpan nama makanan, kategori Makanan/Minuman, harga, deskripsi, gambar.
2. Tabel `orders`: Menyimpan nomor meja (`table_number`), nama pelanggan, total bayar, status (Pending, Diproses, Selesai).
3. Tabel `order_details`: Menyimpan relasi menu makanan yang dipesan per meja.
4. Dashboard Admin: Rekapitulasi pesanan per meja dan filter tanggal penjualan makanan harian.
*(Lihat file `serkom_guide.html` untuk panduan kode kasus makanan secara mendalam).*

---

## ⚡ BAGIAN 4: CHECKLIST EKSEKUSI H-1 UJIAN (URUTAN KERJA 15 MENIT)

Saat duduk di depan komputer asesor besok pagi, ikuti urutan anti-panik berikut:

1. **Nyalakan XAMPP**: Klik **Start** pada modul **Apache** dan **MySQL**.
2. **Buka phpMyAdmin**: Masuk ke `http://localhost/phpmyadmin`, buat database baru bernama `tiketkonser` (Collation: `utf8mb4_unicode_ci`).
3. **Cek Konfigurasi `.env`**:
   ```env
   DB_CONNECTION=mysql
   DB_HOST=127.0.0.1
   DB_PORT=3306
   DB_DATABASE=tiketkonser
   DB_USERNAME=root
   DB_PASSWORD=
   ```
4. **Jalankan Migrasi & Seeder Database**:
   ```bash
   php artisan migrate:fresh --seed
   ```
5. **Buat Tautan Symbolic Link Folder Storage**:
   ```bash
   php artisan storage:link
   ```
6. **Kompilasi Asset Frontend (Tailwind/Vite)**:
   ```bash
   npm run build
   ```
7. **Jalankan Server Lokal Laravel**:
   ```bash
   php artisan serve
   ```
8. **Demonstrasikan ke Asesor**:
   - Buka `http://127.0.0.1:8000`: Tunjukkan katalog tiket konser publik.
   - Login Customer: `customer@gmail.com` / `password123`. Lakukan booking tiket dan tunjukkan E-Tiket hasil cetak.
   - Logout lalu Login Admin: `admin@tiket.com` / `password123`.
   - Masuk ke `/admin/dashboard`: Tunjukkan statistik omset, tabel rekap pesanan, dan lakukan ubah status menjadi `PAID`.
   - Masuk ke `/admin/tickets`: Tambahkan satu tiket baru lengkap dengan upload poster.

---

## 🔥 BAGIAN 5: SESI GRILL-ME ASESOR (10 TANYA JAWAB EMAS)

Berikut 10 pertanyaan teknis yang paling sering diajukan asesor beserta jawaban berbobot:

1. **Asesor**: *"Mengapa Anda memisahkan tabel `orders` dan `order_details`, bukan langsung menyimpan detail tiket di tabel orders?"*  
   **Jawaban**: *"Karena hubungan antara pesanan dan tiket konser adalah One-to-Many (1 pemesan bisa membeli beberapa jenis tiket). Memisahkan tabel ke dalam `order_details` menerapkan kaidah Normalisasi Database (3NF) sehingga mencegah redundansi data dan memungkinkan pencatatan harga satuan historis saat transaksi terjadi."*

2. **Asesor**: *"Bagaimana sistem Anda mencegah race condition ketika sisa tiket tinggal 1 namun dibeli oleh dua customer bersamaan?"*  
   **Jawaban**: *"Saya membungkus proses checkout menggunakan `DB::beginTransaction()` dan validasi pengecekan stok di level server. Pada sistem skala besar industri, kita dapat mengaktifkan Pessimistic Locking menggunakan `lockForUpdate()` pada tabel tickets."*

3. **Asesor**: *"Apa fungsi perintah `php artisan storage:link`?"*  
   **Jawaban**: *"Membuat tautan pintasan (symbolic link) dari folder privat `storage/app/public` ke folder publik `public/storage`, sehingga file upload (seperti poster konser) dapat diakses dan ditampilkan dengan aman oleh browser melalui URL publik."*

4. **Asesor**: *"Apa itu Mass Assignment Vulnerability dan bagaimana Laravel melindunginya?"*  
   **Jawaban**: *"Kerentanan di mana pengguna menyisipkan field berbahaya ke dalam request HTTP (seperti mengubah `role` menjadi admin saat register). Laravel memproteksinya dengan properti `$fillable` pada Model, di mana hanya kolom yang didefinisikan secara eksplisit yang diizinkan untuk diisi secara massal."*

5. **Asesor**: *"Jelaskan fungsi sintaks `@csrf` pada setiap form Blade!"*  
   **Jawaban**: *"Berfungsi menghasilkan token rahasia satu kali pakai untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF), yaitu upaya penyerang mengeksekusi aksi ilegal atas nama pengguna yang sedang terautentikasi."*

6. **Asesor**: *"Apa perbedaan query Eloquent menggunakan `with()` dibanding tanpa `with()`?"*  
   **Jawaban**: *"`with()` menerapkan teknik Eager Loading yang menggabungkan query relasi di awal, sehingga menghindari masalah N+1 Query Problem yang dapat memperlambat performa aplikasi."*

7. **Asesor**: *"Kapan kita menggunakan relasi `belongsTo` dan `hasMany`?"*  
   **Jawaban**: *"`belongsTo` diletakkan pada model tabel yang memegang Foreign Key (seperti `OrderDetail` yang memegang `order_id`). Sedangkan `hasMany` diletakkan pada model tabel induk yang diacu (seperti `Order` yang memiliki banyak `OrderDetail`)."*

8. **Asesor**: *"Mengapa harga tiket disimpan ulang di kolom `unit_price` pada tabel `order_details`, padahal sudah ada kolom `price` di tabel `tickets`?"*  
   **Jawaban**: *"Untuk menjaga integritas data historis keuangan. Jika suatu saat panitia menaikkan harga tiket master, total pendapatan pada transaksi masa lalu tidak ikut berubah secara keliru."*

9. **Asesor**: *"Bagaimana cara Anda membatasi customer biasa agar tidak bisa membuka URL `/admin/dashboard`?"*  
   **Jawaban**: *"Menggunakan Middleware khusus (`IsAdmin`) yang mengecek apakah user memiliki `role === 'admin'`. Jika bukan admin, request langsung diblokir dan di-redirect kembali."*

10. **Asesor**: *"Sebutkan urutan siklus hidup request dari browser sampai view konser tampil!"*  
    **Jawaban**: *"Client mengirim HTTP Request -> Diterima `routes/web.php` -> Melewati Middleware (Auth/CSRF) -> Diteruskan ke Controller -> Controller memanggil Model Eloquent -> Database MySQL mengeksekusi SQL -> Data dikembalikan ke Controller -> Controller merender file Blade View -> HTML dikirimkan kembali ke browser."*

---

## 🚨 BAGIAN 6: KAMUS ERROR & TROUBLESHOOTING INSTAN (SOLUSI 10 DETIK)

| Pesan Error / Gejala | Penyebab Utama | Solusi Instan 10 Detik |
| :--- | :--- | :--- |
| **`419 Page Expired`** | Form input tidak memiliki token proteksi CSRF. | Tambahkan direktif `@csrf` tepat di bawah tag pembuka `<form>`. |
| **`SQLSTATE[23000]: Foreign key constraint fails`** | Urutan penghapusan atau penyisipan tabel relasi tidak sesuai. | Pastikan tabel induk (`tickets`) sudah terisi ID sebelum menyimpan `order_details`. Jalankan `php artisan migrate:fresh --seed`. |
| **`The GET method is not supported for route ...`** | Form menggunakan method POST tetapi di route terdaftar sebagai DELETE/PATCH/PUT. | Tambahkan `@method('DELETE')` atau `@method('PATCH')` di dalam form. |
| **`Vite manifest not found`** | Asset frontend Tailwind CSS belum dikompilasi oleh Node.js. | Buka terminal dan jalankan perintah `npm run build`. |
| **`Target class [TicketController] does not exist`** | Controller belum diimpor pada bagian atas file `routes/web.php`. | Tambahkan deklarasi `use App\Http\Controllers\Admin\TicketController;` di baris teratas `routes/web.php`. |
| **`Gambar poster konser tidak muncul (Broken link)`** | Belum membuat symbolic link folder storage ke public. | Jalankan terminal: `php artisan storage:link`, dan pastikan pemanggilan di Blade menggunakan `asset('storage/' . $ticket->poster)`. |
| **`Access denied for user 'root'@'localhost'`** | Konfigurasi username atau password database di `.env` keliru. | Buka file `.env`, ubah `DB_USERNAME=root` dan kosongkan `DB_PASSWORD=`. |
| **`Class "App\Models\Order" not found`** | Lupa mengimpor namespace Model di Controller. | Tambahkan `use App\Models\Order;` di bagian atas Controller Anda. |

---
**🎉 Selamat Menempuh Ujian Serkom! Tetap Tenang, Percaya Diri, dan Anda Pasti Kompeten 100%!**
