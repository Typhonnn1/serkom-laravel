# -*- coding: utf-8 -*-
"""
Generator Modul Serkom Tiket Konser - Clean Document Style
Menghasilkan serkom_tiket_konser.html persis dengan gaya visual, tata letak,
dan kemudahan baca serkom_guide.html (A4 clean document, dark VS Code code boxes,
tanpa widget rumit yang bikin pusing).
"""

import os
import sys
import html
import re

# Import syntax highlighting components from build_guide
from build_guide import (
    highlight_code_html,
    BladeHtmlLexer,
    EnvLexer,
    TerminalLexer
)

BASE_DIR = r"c:\Users\Default User\Desktop\modul serkom"
OUTPUT_HTML = os.path.join(BASE_DIR, "serkom_tiket_konser.html")

def render_step_box(step_num, title, file_badge, is_modified, code_str, explanation=""):
    """Render a clean step block identical to serkom_guide.html"""
    highlighted = highlight_code_html(code_str, file_badge)
    
    header_class = "diff-header-added" if is_modified else "diff-header-default"
    tag_class = "tag-modified" if is_modified else "tag-default"
    tag_text = "[TAMBAHKAN / UBAH]" if is_modified else "[KODE AWAL / LENGKAP]"
    code_class = "code-added" if is_modified else "code-default"
    
    html_out = f"""
    <h3 class="step-title"><b>[LANGKAH {step_num}]</b> {html.escape(title)}</h3>
    """
    if explanation:
        html_out += f"<p class='step-desc'>{html.escape(explanation)}</p>\n"
        
    html_out += f"""
    <div class="diff-box">
        <div class="diff-header {header_class}">
            <span>📄 File: <b>{html.escape(file_badge)}</b></span>
            <span class="{tag_class}">{tag_text}</span>
        </div>
        <div class="diff-body">
            <pre class="{code_class}"><code>{highlighted}</code></pre>
        </div>
    </div>
    """
    return html_out

def build_clean_tiket_guide():
    print("Building clean serkom_tiket_konser.html...")
    
    lines = []
    lines.append("""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>PANDUAN PRAKTIKUM & UJIAN SERKOM LARAVEL - TIKET KONSER</title>
    <style>
        * {
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
            box-sizing: border-box;
        }
        @page {
            size: A4;
            margin: 12mm 12mm 12mm 12mm;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            color: #111;
            line-height: 1.5;
            font-size: 12px;
            margin: 0 auto;
            padding: 20px;
            max-width: 900px;
            background: #fff;
        }
        .header-box {
            text-align: center;
            border-bottom: 3px double #000;
            padding-bottom: 14px;
            margin-bottom: 22px;
        }
        .header-box h1 {
            font-size: 21px;
            margin: 0 0 6px 0;
            color: #000;
            letter-spacing: 0.5px;
        }
        .header-box .subtitle {
            font-size: 12.5px;
            color: #333;
            font-weight: 600;
        }
        .badge-target {
            display: inline-block;
            background: #f0f0f0;
            color: #000;
            border: 1px solid #000;
            padding: 4px 12px;
            border-radius: 3px;
            font-weight: bold;
            font-size: 11px;
            margin-top: 10px;
        }
        h2.section-title {
            font-size: 14.5px;
            background: #eaeaea;
            border-left: 6px solid #000;
            padding: 8px 12px;
            margin-top: 28px;
            margin-bottom: 14px;
            page-break-after: avoid;
            break-after: avoid;
            color: #000;
        }
        h3.step-title {
            font-size: 13px;
            color: #000;
            margin-top: 20px;
            margin-bottom: 6px;
            page-break-after: avoid;
            break-after: avoid;
            border-bottom: 1px dashed #666;
            padding-bottom: 4px;
        }
        p {
            margin: 6px 0;
        }
        .step-desc {
            color: #333;
            font-size: 11.5px;
            margin-bottom: 6px;
        }
        .table-custom {
            width: 100%;
            border-collapse: collapse;
            margin: 10px 0 16px 0;
            page-break-inside: auto;
            break-inside: auto;
            font-size: 11.5px;
        }
        .table-custom tr {
            page-break-inside: avoid;
            break-inside: avoid;
        }
        .table-custom th, .table-custom td {
            border: 1px solid #333;
            padding: 5.5px 8px;
            vertical-align: top;
        }
        .table-custom th {
            background: #e2e2e2;
            font-weight: bold;
            color: #000;
        }

        /* Dark Theme Code Box (VS Code Style #1e1e1e) */
        .diff-box {
            margin: 12px 0 16px 0;
            border: 1px solid #333333;
            border-radius: 6px;
            background: #18181b;
            overflow: hidden;
            page-break-inside: auto;
            break-inside: auto;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
        }
        .diff-header {
            padding: 7px 12px;
            font-size: 11px;
            font-weight: 600;
            display: flex;
            justify-content: space-between;
            align-items: center;
            page-break-after: avoid;
            break-after: avoid;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }
        .diff-header-default {
            background: #27272a;
            border-bottom: 1px solid #3f3f46;
            color: #a1a1aa;
        }
        .diff-header-added {
            background: #182234;
            border-bottom: 1px solid #1e3a5f;
            color: #38bdf8;
        }
        .tag-default {
            background: #3f3f46;
            color: #e4e4e7;
            font-size: 10px;
            font-weight: 600;
            padding: 2px 8px;
            border-radius: 3px;
            letter-spacing: 0.3px;
        }
        .tag-modified {
            background: #0284c7;
            color: #ffffff;
            font-size: 10px;
            font-weight: bold;
            padding: 2px 8px;
            border-radius: 3px;
            letter-spacing: 0.3px;
        }
        .diff-body {
            padding: 0;
            background: #1e1e1e;
        }
        pre {
            background: #1e1e1e;
            color: #d4d4d4;
            padding: 10px 14px;
            font-family: "Consolas", "Courier New", monospace;
            font-size: 11px;
            line-height: 1.48;
            white-space: pre-wrap;
            word-break: break-word;
            margin: 0;
            border: none;
            border-radius: 0;
            tab-size: 4;
            page-break-inside: auto;
            break-inside: auto;
        }
        .code-added {
            border-left: 4px solid #38bdf8;
        }
        .code-default {
            border-left: 4px solid #71717a;
        }

        /* VS Code Dark+ Syntax Highlighting Colors */
        .tok-kw { color: #569cd6; font-weight: bold; }
        .tok-ctrl { color: #c586c0; font-weight: bold; }
        .tok-class { color: #4ec9b0; font-weight: bold; }
        .tok-fn { color: #dcdcaa; }
        .tok-var { color: #9cdcfe; }
        .tok-str { color: #ce9178; }
        .tok-num { color: #b5cea8; }
        .tok-cm { color: #6a9955; font-style: italic; }
        .tok-tag { color: #569cd6; font-weight: bold; }
        .tok-attr { color: #9cdcfe; }
        .tok-op { color: #d4d4d4; }
        .tok-punc { color: #cccccc; }

        .callout {
            background: #fafafa;
            border-left: 4px solid #222;
            border: 1px solid #bbb;
            border-left-width: 5px;
            padding: 8px 12px;
            margin: 8px 0;
            font-size: 11.2px;
            color: #111;
            page-break-inside: avoid;
            break-inside: avoid;
        }
        .callout-title {
            font-weight: bold;
            margin-bottom: 4px;
            color: #000;
        }
        .callout-info { border-left-color: #0284c7; background: #f0f9ff; }
        .callout-warning { border-left-color: #d97706; background: #fffbeb; }
        .callout-success { border-left-color: #16a34a; background: #f0fdf4; }

        .grill-card {
            border: 1px solid #222;
            padding: 10px 12px;
            margin-bottom: 12px;
            background: #fafafa;
            border-left: 5px solid #000;
            page-break-inside: avoid;
            break-inside: avoid;
        }
        .grill-q {
            font-weight: bold;
            font-size: 12px;
            color: #000;
            margin-bottom: 4px;
        }
        .grill-a {
            font-size: 11.2px;
            line-height: 1.45;
            color: #222;
        }
        @media print {
            body { padding: 0; max-width: 100%; }
            .diff-box { page-break-inside: auto; break-inside: auto; }
            pre { page-break-inside: auto; break-inside: auto; }
            .diff-header { page-break-after: avoid; break-after: avoid; }
            h2.section-title, h3.step-title { page-break-after: avoid; break-after: avoid; }
            .callout, .grill-card { page-break-inside: avoid; break-inside: avoid; }
            .table-custom { page-break-inside: auto; break-inside: auto; }
            .table-custom tr { page-break-inside: avoid; break-inside: avoid; }
        }
    </style>
</head>
<body>

    <div class="header-box">
        <h1>📘 PANDUAN PRAKTIKUM &amp; UJIAN SERKOM LARAVEL</h1>
        <div class="subtitle">Sistem Pemesanan Tiket Konser (Pra-Serkom &amp; Ujian Kejuruan BNSP)</div>
        <div class="badge-target">🎯 TARGET: Lulus Sertifikasi Kompetensi Pemrograman Web BNSP / LSP</div>
    </div>
""")

    # TIMELINE UJIAN
    lines.append("""
    <h2 class="section-title">🧭 TIMELINE &amp; STRATEGI PENGERJAAN 4 JAM UJIAN</h2>
    <table class="table-custom">
        <thead>
            <tr>
                <th width="140">Alokasi Waktu</th>
                <th width="180">Modul &amp; Target Utama</th>
                <th>Capaian Fungsional Wajib</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><b>00:00 - 00:30 (30 Menit)</b></td>
                <td><b>Modul 1: Database &amp; Model</b></td>
                <td>Konfigurasi .env, Migration 4 tabel (users role, tickets, orders, order_details), Seeder, dan Relasi Eloquent.</td>
            </tr>
            <tr>
                <td><b>00:30 - 01:45 (75 Menit)</b></td>
                <td><b>Modul 2: Breeze &amp; CRUD Admin</b></td>
                <td>Install Breeze, CRUD Master Tiket Konser (upload poster), dan CRUD User Management (Admin &amp; Customer).</td>
            </tr>
            <tr>
                <td><b>01:45 - 02:45 (60 Menit)</b></td>
                <td><b>Modul 3: Sisi Customer</b></td>
                <td>Katalog konser publik, filter kategori (VIP/Festival/Regular), dan transaksi booking checkout DB::transaction.</td>
            </tr>
            <tr>
                <td><b>02:45 - 03:30 (45 Menit)</b></td>
                <td><b>Modul 4: Sisi Admin &amp; Rekap</b></td>
                <td>Dashboard rekapitulasi pesanan tiket masuk, filter tanggal, hitung total omset, dan form ubah status transaksi.</td>
            </tr>
            <tr>
                <td><b>03:30 - 04:00 (30 Menit)</b></td>
                <td><b>Modul 5: Teori &amp; Finishing</b></td>
                <td>Persiapan wawancara asesor (Hardware/Software, ERD &amp; SQL CRUD, Query, MVC Laravel) &amp; storage:link.</td>
            </tr>
        </tbody>
    </table>
    """)

    # MODUL 1
    lines.append("""
    <h2 class="section-title">MODUL 1: SETUP DATABASE, MIGRATION, RELASI ELOQUENT &amp; SEEDER</h2>
    <p><i>Langkah awal konfigurasi koneksi database, skema 4 tabel relasional, relasi Eloquent, dan seeding akun penguji.</i></p>
    """)

    # Step 1.1: .env
    code_env = """DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=tiketkonser
DB_USERNAME=root
DB_PASSWORD="""
    lines.append(render_step_box("1.1", "Konfigurasi Koneksi Database di .env", ".env", True, code_env,
        "Buka file .env pada root project Anda dan sesuaikan konfigurasi database MySQL (buat database bernama tiketkonser di phpMyAdmin lebih dulu):"))

    # Step 1.2: Terminal Generator
    code_term1 = """php artisan make:model Ticket -mcr
php artisan make:model Order -mcr
php artisan make:model OrderDetail -m
php artisan make:seeder TicketSeeder
php artisan make:middleware IsAdmin"""
    lines.append(render_step_box("1.2", "Buat Model, Migration, Controller, Seeder & Middleware", "Terminal Command", True, code_term1,
        "Jalankan perintah sakti terminal (-mcr = Migration, Controller Resource, Model sekaligus):"))

    # Step 1.3: Migration Users
    code_mig_users = """public function up(): void
{
    Schema::create('users', function (Blueprint $table) {
        $table->id();
        $table->string('name');
        $table->string('email')->unique();
        $table->string('phone')->nullable(); // [TAMBAHKAN] Nomor HP pemesan
        $table->timestamp('email_verified_at')->nullable();
        $table->string('password');
        // [TAMBAHKAN] Kolom role: admin vs customer
        $table->enum('role', ['admin', 'customer'])->default('customer');
        $table->rememberToken();
        $table->timestamps();
    });
}"""
    lines.append(render_step_box("1.3", "Edit Migration Tabel Users (Tambah Kolom Role & Phone)", "database/migrations/xxxx_create_users_table.php", True, code_mig_users,
        "Buka file migration bawaan Laravel di database/migrations/ dan tambahkan kolom role serta phone:"))

    # Step 1.4: Migration Tickets
    code_mig_tickets = """public function up(): void
{
    Schema::create('tickets', function (Blueprint $table) {
        $table->id();
        $table->string('concert_name');       // Nama Konser (e.g. Coldplay Live in Jakarta)
        $table->string('artist');             // Nama Band / Musisi
        $table->string('venue');              // Lokasi Konser (e.g. Stadion GBK)
        $table->date('event_date');           // Tanggal Konser
        $table->enum('category', ['VIP', 'Festival', 'Regular']); // Kategori Tiket
        $table->integer('price');             // Harga Tiket (Rp)
        $table->integer('stock');             // Kuota Stok Tiket
        $table->text('description')->nullable();
        $table->string('poster')->nullable(); // Banner / Poster Konser
        $table->timestamps();
    });
}"""
    lines.append(render_step_box("1.4", "Edit Migration Tabel Tickets (Master Tiket Konser)", "database/migrations/xxxx_create_tickets_table.php", True, code_mig_tickets,
        "Buka file migration create_tickets_table.php dan isi kolom master tiket konser secara lengkap:"))

    # Step 1.5: Migration Orders
    code_mig_orders = """public function up(): void
{
    Schema::create('orders', function (Blueprint $table) {
        $table->id();
        $table->foreignId('user_id')->nullable()->constrained('users')->onDelete('cascade');
        $table->string('order_code')->unique(); // Kode Unik (e.g. TKT-20261021-001)
        $table->string('customer_name');
        $table->string('customer_phone');
        $table->integer('total_price');
        $table->enum('status', ['pending', 'paid', 'cancelled'])->default('pending');
        $table->date('order_date');
        $table->timestamps();
    });
}"""
    lines.append(render_step_box("1.5", "Edit Migration Tabel Orders (Header Transaksi Pemesanan)", "database/migrations/xxxx_create_orders_table.php", True, code_mig_orders,
        "Buka file migration create_orders_table.php untuk mencatat identitas pemesan tiket dan status bayar:"))

    # Step 1.6: Migration Order Details
    code_mig_details = """public function up(): void
{
    Schema::create('order_details', function (Blueprint $table) {
        $table->id();
        $table->foreignId('order_id')->constrained('orders')->onDelete('cascade');
        $table->foreignId('ticket_id')->constrained('tickets')->onDelete('cascade');
        $table->integer('quantity'); // Jumlah tiket dipesan
        $table->integer('subtotal'); // Harga x Quantity
        $table->timestamps();
    });
}"""
    lines.append(render_step_box("1.6", "Edit Migration Tabel Order Details (Rincian Item Tiket)", "database/migrations/xxxx_create_order_details_table.php", True, code_mig_details,
        "Buka file migration create_order_details_table.php. Foreign key cascade memastikan detail terhapus jika order dihapus:"))

    # Step 1.7: Models
    code_models = r"""// 1. app/Models/User.php
class User extends Authenticatable
{
    protected $fillable = ['name', 'email', 'phone', 'password', 'role'];
    protected $casts = ['email_verified_at' => 'datetime', 'password' => 'hashed'];

    public function orders() {
        return $this->hasMany(Order::class);
    }
}

// 2. app/Models/Ticket.php
class Ticket extends Model
{
    protected $guarded = ['id'];

    public function orderDetails() {
        return $this->hasMany(OrderDetail::class);
    }
}

// 3. app/Models/Order.php
class Order extends Model
{
    protected $guarded = ['id'];
    protected $casts = ['order_date' => 'date'];

    public function orderDetails() {
        return $this->hasMany(OrderDetail::class);
    }
    public function user() {
        return $this->belongsTo(User::class);
    }
}

// 4. app/Models/OrderDetail.php
class OrderDetail extends Model
{
    protected $guarded = ['id'];

    public function order() {
        return $this->belongsTo(Order::class);
    }
    public function ticket() {
        return $this->belongsTo(Ticket::class);
    }
}"""
    lines.append(render_step_box("1.7", "Setup Relasi Eloquent di File Models", "app/Models/{User, Ticket, Order, OrderDetail}.php", True, code_models,
        "Buka file model di folder app/Models/ dan pasang relasi One-to-Many (hasMany) dan Many-to-One (belongsTo):"))

    # Step 1.8: Seeder
    code_seeder = r"""// database/seeders/TicketSeeder.php
public function run(): void
{
    DB::table('tickets')->insert([
        [
            'concert_name' => 'Coldplay: Music of the Spheres',
            'artist'       => 'Coldplay',
            'venue'        => 'Stadion Utama Gelora Bung Karno',
            'event_date'   => '2026-11-15',
            'category'     => 'VIP',
            'price'        => 3500000,
            'stock'        => 50,
            'description'  => 'Tiket VIP area panggung utama + free merchandise.',
            'poster'       => null,
            'created_at'   => now(), 'updated_at' => now(),
        ],
        [
            'concert_name' => 'Sheila on 7: Tunggu Aku di Jakarta',
            'artist'       => 'Sheila on 7',
            'venue'        => 'JIEXPO Kemayoran Jakarta',
            'event_date'   => '2026-12-05',
            'category'     => 'Festival',
            'price'        => 750000,
            'stock'        => 150,
            'description'  => 'Area festival berdiri depan panggung spektakuler.',
            'poster'       => null,
            'created_at'   => now(), 'updated_at' => now(),
        ],
        [
            'concert_name' => 'Bruno Mars Live in Tour',
            'artist'       => 'Bruno Mars',
            'venue'        => 'Jakarta International Stadium (JIS)',
            'event_date'   => '2026-11-20',
            'category'     => 'Regular',
            'price'        => 1200000,
            'stock'        => 200,
            'description'  => 'Tribun duduk nyaman dengan view panggung luas.',
            'poster'       => null,
            'created_at'   => now(), 'updated_at' => now(),
        ],
    ]);
}

// database/seeders/DatabaseSeeder.php
public function run(): void
{
    // 1. Akun Administrator
    User::create([
        'name'     => 'Admin Konser',
        'email'    => 'admin@tiket.com',
        'phone'    => '081234567890',
        'password' => Hash::make('password123'),
        'role'     => 'admin',
    ]);

    // 2. Akun Customer
    User::create([
        'name'     => 'Budi Pembeli',
        'email'    => 'customer@gmail.com',
        'phone'    => '081987654321',
        'password' => Hash::make('password123'),
        'role'     => 'customer',
    ]);

    // 3. Panggil Seeder Tiket
    $this->call([TicketSeeder::class]);
}"""
    lines.append(render_step_box("1.8", "Buat Seeder Data Awal Konser & Akun Login Penguji", "database/seeders/{TicketSeeder, DatabaseSeeder}.php", True, code_seeder,
        "Isi data seeder agar penguji langsung melihat 3 konser awal dan 2 akun login (Admin & Customer):"))

    # Step 1.9: Migrate fresh
    code_term2 = """php artisan migrate:fresh --seed"""
    lines.append(render_step_box("1.9", "Jalankan Eksekusi Migrasi & Seeder ke MySQL", "Terminal Command", False, code_term2,
        "Jalankan migrasi fresh beserta seeder untuk membuat tabel dan mengisi akun secara otomatis:"))

    # MODUL 2
    lines.append("""
    <h2 class="section-title">MODUL 2: BREEZE AUTH, CRUD MASTER TIKET KONSER &amp; CRUD USER</h2>
    <p><i>Instalasi Laravel Breeze Blade, manajemen Master Data Tiket Konser (upload poster fisik), dan CRUD Data User.</i></p>
    """)

    # Step 2.1: Breeze install
    code_breeze = """composer require laravel/breeze --dev
php artisan breeze:install blade
# Opsi instalasi: Dark mode? -> NO | Testing? -> 0 (PHPUnit)

php artisan storage:link
npm install
npm run build"""
    lines.append(render_step_box("2.1", "Instalasi Laravel Breeze & Build Asset Frontend", "Terminal Command", False, code_breeze,
        "Jalankan instalasi autentikasi Breeze dan jangan lupa storage:link untuk menampilkan gambar:"))

    # Step 2.2: Middleware IsAdmin
    code_mid = r"""<?php

namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Symfony\Component\HttpFoundation\Response;

class IsAdmin
{
    public function handle(Request $request, Closure $next): Response
    {
        if (Auth::check() && Auth::user()->role === 'admin') {
            return $next($request);
        }

        return redirect('/')->with('error', 'Akses ditolak! Halaman ini khusus Administrator.');
    }
}"""
    lines.append(render_step_box("2.2", "Middleware Proteksi Khusus Admin (IsAdmin)", "app/Http/Middleware/IsAdmin.php", True, code_mid,
        "Buka app/Http/Middleware/IsAdmin.php untuk memblokir akun customer yang mencoba membuka halaman admin:"))

    # Step 2.3: TicketController
    code_ctrl_ticket = r"""<?php

namespace App\Http\Controllers;

use App\Models\Ticket;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Storage;

class TicketController extends Controller
{
    // 1. Tampilkan tabel master tiket konser
    public function index()
    {
        $tickets = Ticket::latest()->paginate(10);
        return view('admin.tickets.index', compact('tickets'));
    }

    // 2. Tampilkan form tambah tiket
    public function create()
    {
        return view('admin.tickets.create');
    }

    // 3. Simpan tiket baru + upload poster fisik
    public function store(Request $request)
    {
        $request->validate([
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

        $posterPath = null;
        if ($request->hasFile('poster')) {
            $posterPath = $request->file('poster')->store('posters', 'public');
        }

        Ticket::create([
            'concert_name' => $request->concert_name,
            'artist'       => $request->artist,
            'venue'        => $request->venue,
            'event_date'   => $request->event_date,
            'category'     => $request->category,
            'price'        => $request->price,
            'stock'        => $request->stock,
            'description'  => $request->description,
            'poster'       => $posterPath,
        ]);

        return redirect()->route('admin.tickets.index')->with('success', 'Tiket konser berhasil ditambahkan!');
    }

    // 4. Tampilkan form edit tiket
    public function edit(Ticket $ticket)
    {
        return view('admin.tickets.edit', compact('ticket'));
    }

    // 5. Update data tiket + ganti file poster lama
    public function update(Request $request, Ticket $ticket)
    {
        $request->validate([
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

        $posterPath = $ticket->poster;
        if ($request->hasFile('poster')) {
            if ($ticket->poster && Storage::disk('public')->exists($ticket->poster)) {
                Storage::disk('public')->delete($ticket->poster);
            }
            $posterPath = $request->file('poster')->store('posters', 'public');
        }

        $ticket->update([
            'concert_name' => $request->concert_name,
            'artist'       => $request->artist,
            'venue'        => $request->venue,
            'event_date'   => $request->event_date,
            'category'     => $request->category,
            'price'        => $request->price,
            'stock'        => $request->stock,
            'description'  => $request->description,
            'poster'       => $posterPath,
        ]);

        return redirect()->route('admin.tickets.index')->with('success', 'Data tiket konser berhasil diperbarui!');
    }

    // 6. Hapus tiket + hapus poster fisik dari disk
    public function destroy(Ticket $ticket)
    {
        if ($ticket->poster && Storage::disk('public')->exists($ticket->poster)) {
            Storage::disk('public')->delete($ticket->poster);
        }
        $ticket->delete();

        return redirect()->route('admin.tickets.index')->with('success', 'Tiket konser berhasil dihapus!');
    }
}"""
    lines.append(render_step_box("2.3", "Controller CRUD Master Tiket Konser Lengkap", "app/Http/Controllers/TicketController.php", True, code_ctrl_ticket,
        "Buka app/Http/Controllers/TicketController.php. Mencakup 7 method resource standar, upload dan hapus poster fisik:"))

    # Step 2.4: Views Tickets
    code_view_tickets = """<!-- resources/views/admin/tickets/index.blade.php -->
<x-app-layout>
    <x-slot name="header">
        <div class="flex justify-between items-center">
            <h2 class="font-semibold text-xl text-gray-800">Master Data Tiket Konser</h2>
            <a href="{{ route('admin.tickets.create') }}" class="bg-blue-600 text-white px-4 py-2 rounded text-sm font-semibold">+ Tambah Tiket</a>
        </div>
    </x-slot>

    <div class="p-6 max-w-7xl mx-auto">
        @if(session('success'))
            <div class="bg-green-100 text-green-700 p-3 rounded mb-4 border text-sm font-semibold">{{ session('success') }}</div>
        @endif

        <table class="w-full bg-white border rounded shadow-sm text-sm">
            <thead>
                <tr class="bg-gray-100 border-b text-gray-600 text-left">
                    <th class="p-3">Poster</th>
                    <th class="p-3">Nama Konser & Artis</th>
                    <th class="p-3">Venue & Tanggal</th>
                    <th class="p-3">Kategori</th>
                    <th class="p-3">Harga</th>
                    <th class="p-3">Sisa Stok</th>
                    <th class="p-3 text-center">Aksi</th>
                </tr>
            </thead>
            <tbody>
                @forelse($tickets as $t)
                <tr class="border-b hover:bg-gray-50">
                    <td class="p-3">
                        @if($t->poster)
                            <img src="{{ asset('storage/' . $t->poster) }}" class="w-14 h-14 object-cover rounded shadow">
                        @else
                            <div class="w-14 h-14 bg-gray-200 text-gray-400 flex items-center justify-center text-xs rounded">No Image</div>
                        @endif
                    </td>
                    <td class="p-3">
                        <strong class="text-gray-900 block">{{ $t->concert_name }}</strong>
                        <span class="text-xs text-gray-500">{{ $t->artist }}</span>
                    </td>
                    <td class="p-3 text-xs">{{ $t->venue }}<br><b>{{ date('d M Y', strtotime($t->event_date)) }}</b></td>
                    <td class="p-3">
                        <span class="px-2 py-0.5 rounded text-xs font-bold {{ $t->category == 'VIP' ? 'bg-purple-100 text-purple-700' : ($t->category == 'Festival' ? 'bg-blue-100 text-blue-700' : 'bg-gray-100 text-gray-700') }}">
                            {{ $t->category }}
                        </span>
                    </td>
                    <td class="p-3 font-bold text-green-600">Rp {{ number_format($t->price, 0, ',', '.') }}</td>
                    <td class="p-3 font-semibold">{{ $t->stock }} Tiket</td>
                    <td class="p-3 text-center">
                        <a href="{{ route('admin.tickets.edit', $t->id) }}" class="text-blue-600 font-semibold mr-2">Edit</a>
                        <form action="{{ route('admin.tickets.destroy', $t->id) }}" method="POST" class="inline" onsubmit="return confirm('Hapus tiket konser ini?')">
                            @csrf @method('DELETE')
                            <button type="submit" class="text-red-600 font-semibold">Hapus</button>
                        </form>
                    </td>
                </tr>
                @empty
                <tr><td colspan="7" class="p-4 text-center text-gray-400">Belum ada data tiket konser.</td></tr>
                @endforelse
            </tbody>
        </table>
        <div class="mt-4">{{ $tickets->links() }}</div>
    </div>
</x-app-layout>"""
    lines.append(render_step_box("2.4", "Tampilan Tabel Master Tiket Admin (Index)", "resources/views/admin/tickets/index.blade.php", True, code_view_tickets,
        "Buka resources/views/admin/tickets/index.blade.php untuk menampilkan daftar tiket konser lengkap:"))

    # Step 2.5: UserController
    code_ctrl_user = r"""<?php

namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Hash;

class UserController extends Controller
{
    public function index()
    {
        $users = User::latest()->paginate(10);
        return view('admin.users.index', compact('users'));
    }

    public function create()
    {
        return view('admin.users.create');
    }

    public function store(Request $request)
    {
        $request->validate([
            'name'     => 'required|string|max:255',
            'email'    => 'required|email|unique:users',
            'phone'    => 'nullable|string|max:20',
            'password' => 'required|min:6',
            'role'     => 'required|in:admin,customer',
        ]);

        User::create([
            'name'     => $request->name,
            'email'    => $request->email,
            'phone'    => $request->phone,
            'password' => Hash::make($request->password),
            'role'     => $request->role,
        ]);

        return redirect()->route('admin.users.index')->with('success', 'User berhasil ditambahkan!');
    }

    public function edit(User $user)
    {
        return view('admin.users.edit', compact('user'));
    }

    public function update(Request $request, User $user)
    {
        $request->validate([
            'name'  => 'required|string|max:255',
            'email' => 'required|email|unique:users,email,' . $user->id,
            'phone' => 'nullable|string|max:20',
            'role'  => 'required|in:admin,customer',
        ]);

        $data = [
            'name'  => $request->name,
            'email' => $request->email,
            'phone' => $request->phone,
            'role'  => $request->role,
        ];

        if ($request->filled('password')) {
            $request->validate(['password' => 'min:6']);
            $data['password'] = Hash::make($request->password);
        }

        $user->update($data);
        return redirect()->route('admin.users.index')->with('success', 'Data user berhasil diperbarui!');
    }

    public function destroy(User $user)
    {
        // Proteksi Anti Self-Delete
        if (auth()->id() === $user->id) {
            return back()->with('error', 'Anda tidak dapat menghapus akun Anda sendiri!');
        }

        $user->delete();
        return redirect()->route('admin.users.index')->with('success', 'User berhasil dihapus!');
    }
}"""
    lines.append(render_step_box("2.5", "Controller CRUD User Management (Admin & Customer)", "app/Http/Controllers/Admin/UserController.php", True, code_ctrl_user,
        "Buka app/Http/Controllers/Admin/UserController.php untuk mengelola akun pengguna serta proteksi anti self-delete:"))

    # MODUL 3
    lines.append("""
    <h2 class="section-title">MODUL 3: SISI CUSTOMER (KATALOG TIKET &amp; CHECKOUT TRANSAKSI)</h2>
    <p><i>Katalog konser publik, filter kategori (VIP/Festival/Regular), dan transaksi pemesanan tiket atomik DB::transaction.</i></p>
    """)

    # Step 3.1: BookingController
    code_booking = r"""<?php

namespace App\Http\Controllers;

use App\Models\Ticket;
use App\Models\Order;
use App\Models\OrderDetail;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Auth;

class BookingController extends Controller
{
    // 1. Katalog Tiket Konser Publik
    public function index(Request $request)
    {
        $query = Ticket::where('stock', '>', 0);

        // Filter Kategori
        if ($request->filled('category') && $request->category !== 'all') {
            $query->where('category', $request->category);
        }

        $tickets = $query->latest()->get();
        return view('customer.concerts', compact('tickets'));
    }

    // 2. Checkout Pemesanan Tiket (DB::transaction & Auto Decrement Stok)
    public function store(Request $request)
    {
        $request->validate([
            'ticket_id'      => 'required|exists:tickets,id',
            'quantity'       => 'required|integer|min:1',
            'customer_name'  => 'required|string|max:255',
            'customer_phone' => 'required|string|max:20',
        ]);

        DB::beginTransaction();
        try {
            $ticket = Ticket::findOrFail($request->ticket_id);

            // Cek Ketersediaan Stok Kuota Tiket
            if ($ticket->stock < $request->quantity) {
                return back()->with('error', "Gagal! Sisa kuota tiket hanya tersisa {$ticket->stock} kursi.");
            }

            $subtotal = $ticket->price * $request->quantity;
            $orderCode = 'TKT-' . date('Ymd') . '-' . strtoupper(substr(uniqid(), -4));

            // Simpan Header Order
            $order = Order::create([
                'user_id'        => Auth::id() ?? null,
                'order_code'     => $orderCode,
                'customer_name'  => $request->customer_name,
                'customer_phone' => $request->customer_phone,
                'total_price'    => $subtotal,
                'status'         => 'paid',
                'order_date'     => now(),
            ]);

            // Simpan Detail Order
            OrderDetail::create([
                'order_id'   => $order->id,
                'ticket_id'  => $ticket->id,
                'quantity'   => $request->quantity,
                'subtotal'   => $subtotal,
            ]);

            // Kurangi Stok Kuota Tiket Konser
            $ticket->decrement('stock', $request->quantity);

            DB::commit();

            return redirect()->route('customer.concerts')
                ->with('success', "Pesanan tiket {$ticket->concert_name} berhasil! Kode Booking: {$order->order_code}");

        } catch (\Exception $e) {
            DB::rollBack();
            return back()->with('error', 'Gagal memproses pesanan: ' . $e->getMessage());
        }
    }
}"""
    lines.append(render_step_box("3.1", "Controller Transaksi Tiket Konser (DB::transaction)", "app/Http/Controllers/BookingController.php", True, code_booking,
        "Buka app/Http/Controllers/BookingController.php. Checkout menggunakan DB::transaction dan otomatis mengurangi kuota tiket (decrement):"))

    # Step 3.2: View Katalog Customer
    code_view_customer = """<!-- resources/views/customer/concerts.blade.php -->
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Pemesanan Tiket Konser</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 p-6 font-sans">
    <div class="max-w-6xl mx-auto">
        <div class="text-center mb-6">
            <h1 class="text-3xl font-extrabold text-gray-800">Katalog Tiket Konser</h1>
            <p class="text-gray-500 text-sm mt-1">Pilih konser favorit Anda dan amankan tiketnya sekarang!</p>
        </div>

        @if(session('success'))
            <div class="bg-green-100 text-green-700 p-3 rounded mb-4 text-center font-bold border">{{ session('success') }}</div>
        @endif
        @if(session('error'))
            <div class="bg-red-100 text-red-700 p-3 rounded mb-4 text-center font-bold border">{{ session('error') }}</div>
        @endif

        <!-- Filter Tab Kategori Instan -->
        <div class="flex justify-center gap-2 mb-6">
            <button onclick="filterCat('all', this)" class="btn-cat px-4 py-2 rounded-full font-bold text-sm bg-blue-600 text-white">Semua Kategori</button>
            <button onclick="filterCat('VIP', this)" class="btn-cat px-4 py-2 rounded-full font-bold text-sm bg-white text-gray-700 border">VIP</button>
            <button onclick="filterCat('Festival', this)" class="btn-cat px-4 py-2 rounded-full font-bold text-sm bg-white text-gray-700 border">Festival</button>
            <button onclick="filterCat('Regular', this)" class="btn-cat px-4 py-2 rounded-full font-bold text-sm bg-white text-gray-700 border">Regular</button>
        </div>

        <!-- Grid Tiket Konser -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            @foreach($tickets as $ticket)
            <div class="card-ticket bg-white border rounded-lg p-4 shadow-sm flex flex-col justify-between" data-category="{{ $ticket->category }}">
                <div>
                    @if($ticket->poster)
                        <img src="{{ asset('storage/' . $ticket->poster) }}" class="w-full h-44 object-cover rounded mb-3">
                    @else
                        <div class="bg-gray-200 h-44 flex items-center justify-center text-gray-400 rounded mb-3">Poster Konser</div>
                    @endif
                    <div class="flex justify-between items-center mb-2">
                        <span class="text-xs bg-purple-100 text-purple-700 font-bold px-2 py-0.5 rounded">{{ $ticket->category }}</span>
                        <span class="text-xs text-gray-500">Sisa Kuota: <b>{{ $ticket->stock }}</b></span>
                    </div>
                    <h3 class="font-bold text-gray-800 text-lg">{{ $ticket->concert_name }}</h3>
                    <p class="text-xs text-indigo-600 font-semibold">{{ $ticket->artist }} &bull; {{ $ticket->venue }}</p>
                    <p class="text-xs text-gray-500 mt-1">Tanggal: <b>{{ date('d M Y', strtotime($ticket->event_date)) }}</b></p>
                    <p class="text-sm font-bold text-green-600 mt-2">Rp {{ number_format($ticket->price, 0, ',', '.') }}</p>
                </div>
                <form action="{{ route('customer.booking') }}" method="POST" class="mt-4 pt-3 border-t">
                    @csrf
                    <input type="hidden" name="ticket_id" value="{{ $ticket->id }}">
                    <div class="mb-2">
                        <label class="block text-xs font-medium text-gray-600 mb-1">Nama Pemesan</label>
                        <input type="text" name="customer_name" required class="w-full border rounded p-1.5 text-xs">
                    </div>
                    <div class="mb-2">
                        <label class="block text-xs font-medium text-gray-600 mb-1">Nomor WhatsApp / HP</label>
                        <input type="text" name="customer_phone" required class="w-full border rounded p-1.5 text-xs">
                    </div>
                    <div class="mb-3">
                        <label class="block text-xs font-medium text-gray-600 mb-1">Jumlah Tiket</label>
                        <input type="number" name="quantity" min="1" max="{{ $ticket->stock }}" value="1" required class="w-full border rounded p-1.5 text-xs text-center font-bold">
                    </div>
                    <button type="submit" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 rounded text-xs">Beli Tiket Sekarang</button>
                </form>
            </div>
            @endforeach
        </div>
    </div>

    <script>
        function filterCat(cat, btn) {
            document.querySelectorAll('.btn-cat').forEach(b => b.className = "btn-cat px-4 py-2 rounded-full font-bold text-sm bg-white text-gray-700 border");
            btn.className = "btn-cat px-4 py-2 rounded-full font-bold text-sm bg-blue-600 text-white";
            document.querySelectorAll('.card-ticket').forEach(card => {
                card.style.display = (cat === 'all' || card.getAttribute('data-category') === cat) ? 'flex' : 'none';
            });
        }
    </script>
</body>
</html>"""
    lines.append(render_step_box("3.2", "Tampilan Katalog Konser & Form Booking Pelanggan", "resources/views/customer/concerts.blade.php", True, code_view_customer,
        "Buka resources/views/customer/concerts.blade.php. Dilengkapi tab filter kategori instant dan form booking kuota tiket:"))

    # MODUL 4
    lines.append("""
    <h2 class="section-title">MODUL 4: SISI ADMIN (REKAP TRANSAKSI, UPDATE STATUS &amp; ROUTING)</h2>
    <p><i>Dashboard admin rekapitulasi pesanan tiket masuk, kartu metrik statistik, filter tanggal, dan routing lengkap.</i></p>
    """)

    # Step 4.1: OrderReportController
    code_ctrl_report = r"""<?php

namespace App\Http\Controllers;

use App\Models\Order;
use Illuminate\Http\Request;

class OrderReportController extends Controller
{
    // 1. Dashboard Rekap Transaksi Tiket Masuk
    public function index(Request $request)
    {
        $query = Order::with('orderDetails.ticket')->latest();

        // Filter Periode Tanggal
        if ($request->filled('start_date') && $request->filled('end_date')) {
            $query->whereBetween('order_date', [$request->start_date, $request->end_date]);
        }

        // Filter Status Bayar
        if ($request->filled('status')) {
            $query->where('status', $request->status);
        }

        $orders = $query->paginate(15);

        // Perhitungan Statistik Otomatis
        $totalIncome = Order::where('status', 'paid')->sum('total_price');
        $totalOrders = Order::count();
        $pendingOrders = Order::where('status', 'pending')->count();

        return view('dashboard', compact('orders', 'totalIncome', 'totalOrders', 'pendingOrders'));
    }

    // 2. Ubah Status Transaksi Pesanan
    public function updateStatus(Request $request, $id)
    {
        $request->validate(['status' => 'required|in:pending,paid,cancelled']);
        $order = Order::findOrFail($id);
        $order->update(['status' => $request->status]);

        return back()->with('success', "Status pesanan {$order->order_code} berhasil diubah!");
    }
}"""
    lines.append(render_step_box("4.1", "Controller Rekapan Pesanan Masuk & Update Status", "app/Http/Controllers/OrderReportController.php", True, code_ctrl_report,
        "Buka app/Http/Controllers/OrderReportController.php untuk mengelola dashboard rekapitulasi dan update status bayar:"))

    # Step 4.2: Dashboard Blade
    code_view_dashboard = """<!-- resources/views/dashboard.blade.php -->
<x-app-layout>
    <x-slot name="header">
        <div class="flex justify-between items-center">
            <h2 class="font-semibold text-xl text-gray-800">Rekapitulasi Pesanan Tiket Masuk</h2>
            <div class="flex gap-2">
                <a href="{{ route('admin.tickets.index') }}" class="px-3 py-1.5 bg-blue-600 text-white text-xs font-semibold rounded">Kelola Tiket</a>
                <a href="{{ route('admin.users.index') }}" class="px-3 py-1.5 bg-purple-600 text-white text-xs font-semibold rounded">Kelola User</a>
                <a href="{{ route('customer.concerts') }}" target="_blank" class="px-3 py-1.5 bg-gray-700 text-white text-xs font-semibold rounded">Katalog Customer</a>
            </div>
        </div>
    </x-slot>

    <div class="p-6 max-w-7xl mx-auto space-y-6">
        <!-- 1. Ringkasan Kartu Statistik -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div class="bg-white p-4 rounded border shadow-sm">
                <p class="text-xs text-gray-500 uppercase font-semibold">Total Seluruh Pesanan</p>
                <p class="text-2xl font-bold text-gray-800 mt-1">{{ $totalOrders }} Transaksi</p>
            </div>
            <div class="bg-white p-4 rounded border shadow-sm">
                <p class="text-xs text-yellow-600 uppercase font-semibold">Pesanan Pending</p>
                <p class="text-2xl font-bold text-yellow-600 mt-1">{{ $pendingOrders }} Antrean</p>
            </div>
            <div class="bg-white p-4 rounded border shadow-sm">
                <p class="text-xs text-green-600 uppercase font-semibold">Total Pendapatan (Paid)</p>
                <p class="text-2xl font-bold text-green-600 mt-1">Rp {{ number_format($totalIncome, 0, ',', '.') }}</p>
            </div>
        </div>

        <!-- 2. Form Filter Periode Tanggal -->
        <div class="bg-white p-4 rounded border shadow-sm">
            <form method="GET" action="{{ route('dashboard') }}" class="flex flex-wrap items-end gap-3">
                <div>
                    <label class="block text-xs font-semibold text-gray-600 mb-1">Dari Tanggal:</label>
                    <input type="date" name="start_date" value="{{ request('start_date') }}" class="border rounded p-1.5 text-xs">
                </div>
                <div>
                    <label class="block text-xs font-semibold text-gray-600 mb-1">Sampai Tanggal:</label>
                    <input type="date" name="end_date" value="{{ request('end_date') }}" class="border rounded p-1.5 text-xs">
                </div>
                <div>
                    <label class="block text-xs font-semibold text-gray-600 mb-1">Status:</label>
                    <select name="status" class="border rounded p-1.5 text-xs">
                        <option value="">Semua Status</option>
                        <option value="pending" {{ request('status') == 'pending' ? 'selected' : '' }}>Pending</option>
                        <option value="paid" {{ request('status') == 'paid' ? 'selected' : '' }}>Paid</option>
                        <option value="cancelled" {{ request('status') == 'cancelled' ? 'selected' : '' }}>Cancelled</option>
                    </select>
                </div>
                <button type="submit" class="bg-blue-600 text-white px-4 py-2 rounded text-xs font-semibold">Filter Rekap</button>
                @if(request('start_date') || request('status'))
                    <a href="{{ route('dashboard') }}" class="text-xs text-red-600 font-semibold self-center ml-2">Reset</a>
                @endif
            </form>
        </div>

        <!-- 3. Tabel Rekap Pesanan -->
        @if(session('success'))
            <div class="p-3 bg-green-100 text-green-700 rounded border text-sm font-semibold">{{ session('success') }}</div>
        @endif

        <div class="bg-white border rounded shadow-sm overflow-hidden">
            <table class="w-full text-left text-sm">
                <thead class="bg-gray-100 text-xs text-gray-600 border-b">
                    <tr>
                        <th class="p-3">Kode Order</th>
                        <th class="p-3">Pemesan</th>
                        <th class="p-3">Rincian Tiket</th>
                        <th class="p-3">Total Tagihan</th>
                        <th class="p-3">Tanggal</th>
                        <th class="p-3">Status</th>
                        <th class="p-3 text-center">Ubah Status</th>
                    </tr>
                </thead>
                <tbody>
                    @forelse($orders as $o)
                    <tr class="border-b hover:bg-gray-50">
                        <td class="p-3 font-mono font-bold text-indigo-600">{{ $o->order_code }}</td>
                        <td class="p-3">
                            <span class="font-bold block">{{ $o->customer_name }}</span>
                            <span class="text-xs text-gray-500">{{ $o->customer_phone }}</span>
                        </td>
                        <td class="p-3">
                            <ul class="text-xs list-disc list-inside">
                                @foreach($o->orderDetails as $d)
                                    <li><b>{{ $d->ticket->concert_name ?? 'Tiket' }}</b> ({{ $d->ticket->category ?? '-' }}) x{{ $d->quantity }}</li>
                                @endforeach
                            </ul>
                        </td>
                        <td class="p-3 font-bold text-green-600">Rp {{ number_format($o->total_price, 0, ',', '.') }}</td>
                        <td class="p-3 text-xs">{{ date('d/m/Y', strtotime($o->order_date)) }}</td>
                        <td class="p-3">
                            <span class="px-2 py-0.5 rounded text-xs font-bold {{ $o->status == 'paid' ? 'bg-green-100 text-green-800' : ($o->status == 'pending' ? 'bg-yellow-100 text-yellow-800' : 'bg-red-100 text-red-800') }}">
                                {{ strtoupper($o->status) }}
                            </span>
                        </td>
                        <td class="p-3 text-center">
                            <form action="{{ route('admin.orders.updateStatus', $o->id) }}" method="POST">
                                @csrf @method('PATCH')
                                <select name="status" onchange="this.form.submit()" class="text-xs border rounded p-1 font-semibold">
                                    <option value="pending" {{ $o->status == 'pending' ? 'selected' : '' }}>Pending</option>
                                    <option value="paid" {{ $o->status == 'paid' ? 'selected' : '' }}>Paid</option>
                                    <option value="cancelled" {{ $o->status == 'cancelled' ? 'selected' : '' }}>Cancelled</option>
                                </select>
                            </form>
                        </td>
                    </tr>
                    @empty
                    <tr><td colspan="7" class="p-6 text-center text-gray-400">Belum ada pesanan masuk.</td></tr>
                    @endforelse
                </tbody>
            </table>
        </div>
        <div class="mt-4">{{ $orders->links() }}</div>
    </div>
</x-app-layout>"""
    lines.append(render_step_box("4.2", "View Dashboard Rekapitulasi Pesanan Masuk (Admin)", "resources/views/dashboard.blade.php", True, code_view_dashboard,
        "Buka resources/views/dashboard.blade.php untuk menampilkan ringkasan metrik omset dan daftar pesanan masuk:"))

    # Step 4.3: Routes web.php
    code_routes = r"""<?php

use App\Http\Controllers\ProfileController;
use App\Http\Controllers\TicketController;
use App\Http\Controllers\BookingController;
use App\Http\Controllers\OrderReportController;
use App\Http\Controllers\Admin\UserController;
use Illuminate\Support\Facades\Route;

// 1. SISI CUSTOMER / PUBLIK
Route::get('/', [BookingController::class, 'index'])->name('customer.concerts');
Route::post('/booking', [BookingController::class, 'store'])->name('customer.booking');

// 2. DASHBOARD ADMIN (Wajib Login & Role Admin)
Route::get('/dashboard', [OrderReportController::class, 'index'])
    ->middleware(['auth', 'verified'])
    ->name('dashboard');

// 3. FITUR ADMIN (TERPROTEKSI AUTH & ISADMIN)
Route::middleware(['auth'])->group(function () {
    // Breeze Profile
    Route::get('/profile', [ProfileController::class, 'edit'])->name('profile.edit');
    Route::patch('/profile', [ProfileController::class, 'update'])->name('profile.update');
    Route::delete('/profile', [ProfileController::class, 'destroy'])->name('profile.destroy');

    // CRUD Master Data Tiket Konser
    Route::resource('/admin/tickets', TicketController::class)->names('admin.tickets');

    // CRUD Master Data User Management
    Route::resource('/admin/users', UserController::class)->names('admin.users');

    // Update Status Transaksi
    Route::patch('/admin/orders/{id}/status', [OrderReportController::class, 'updateStatus'])
        ->name('admin.orders.updateStatus');
});

require __DIR__.'/auth.php';"""
    lines.append(render_step_box("4.3", "File Routing Lengkap (Integrasi Seluruh Fitur)", "routes/web.php", True, code_routes,
        "Buka routes/web.php dan gabungkan seluruh rute customer, dashboard, dan resource controller:"))

    # MODUL 5: TEORI WAWANCARA ASESOR
    lines.append("""
    <h2 class="section-title">MODUL 5: KISI-KISI TEORI &amp; WAWANCARA ASESOR BNSP</h2>
    <p><i>Jawaban lugas dan berbobot untuk 4 pertanyaan teori yang paling sering diajukan asesor:</i></p>

    <!-- TEORI 1 -->
    <div class="grill-card">
        <div class="grill-q">1. Apa Saja yang Dibutuhkan dalam Membangun Aplikasi Pemesanan Tiket Konser?</div>
        <div class="grill-a">
            <p>Jelaskan secara terstruktur ke asesor terbagi menjadi 4 komponen:</p>
            <ol style="margin-left: 18px;">
                <li><b>Kebutuhan Hardware:</b> PC/Laptop minimal Core i3/Ryzen 3, RAM 8 GB (agar lancar menjalankan XAMPP, VS Code, dan browser), dan SSD min. 10 GB.</li>
                <li><b>Kebutuhan Software &amp; Environment:</b> 
                    <ul>
                        <li><b>Web Server &amp; Database:</b> XAMPP (Apache &amp; MySQL / MariaDB).</li>
                        <li><b>Bahasa Pemrograman:</b> PHP 8.x dan framework Laravel 10/11.</li>
                        <li><b>Package Manager:</b> Composer (PHP) dan Node.js / NPM (Frontend Vite).</li>
                        <li><b>Code Editor &amp; Browser:</b> VS Code dan Chrome DevTools.</li>
                    </ul>
                </li>
                <li><b>Kebutuhan Database:</b> RDBMS MySQL dengan perancangan 4 tabel relasional (users, tickets, orders, order_details) dengan mesin penyimpanan InnoDB yang mendukung relasi Foreign Key cascade dan transaksi ACID.</li>
                <li><b>Kebutuhan Fungsional &amp; Keamanan:</b> Autentikasi multi-role (Admin vs Customer), manajemen kuota tiket konser real-time, transaksi atomik (DB::transaction), dan proteksi keamanan (CSRF Token, Hash Password Bcrypt).</li>
            </ol>
        </div>
    </div>

    <!-- TEORI 2 -->
    <div class="grill-card">
        <div class="grill-q">2. Apa Fungsi ERD dan Fungsi Tambah, Edit, Hapus, Tampil dalam Bahasa SQL Beserta Contohnya?</div>
        <div class="grill-a">
            <p><b>A. Fungsi ERD (Entity Relationship Diagram):</b></p>
            <ul>
                <li><b>Blueprint Perancangan:</b> Sebagai cetak biru visual struktur tabel sebelum dikodekan ke dalam migrasi Laravel.</li>
                <li><b>Menentukan Kardinalitas Relasi:</b> Menentukan hubungan 1:N (1 User punya banyak Order, 1 Order punya banyak OrderDetail).</li>
                <li><b>Mencegah Redundansi Data:</b> Dasar proses normalisasi basis data sehingga tidak ada duplikasi data transaksi.</li>
            </ul>
            <p style="margin-top: 8px;"><b>B. Fungsi CRUD dalam Bahasa SQL (Kasus Tiket Konser):</b></p>
            <ul>
                <li><b>Create (Tambah - INSERT INTO):</b> Menambahkan baris data tiket baru.
                    <br><code>INSERT INTO tickets (concert_name, artist, venue, event_date, category, price, stock, created_at, updated_at) VALUES ('Coldplay Jakarta', 'Coldplay', 'GBK', '2026-11-15', 'VIP', 3500000, 50, NOW(), NOW());</code>
                </li>
                <li><b>Read (Tampil - SELECT):</b> Menampilkan dan menyaring data tiket.
                    <br><code>SELECT id, concert_name, category, price, stock FROM tickets WHERE category = 'VIP' AND stock > 0 ORDER BY price ASC;</code>
                </li>
                <li><b>Update (Edit - UPDATE ... SET ... WHERE):</b> Mengubah data kuota atau status pesanan.
                    <br><code>UPDATE tickets SET stock = stock - 2, updated_at = NOW() WHERE id = 1;</code>
                    <br><i>*Catatan: Wajib pakai WHERE agar tidak mengubah seluruh baris tabel!</i>
                </li>
                <li><b>Delete (Hapus - DELETE FROM ... WHERE):</b> Menghapus data tiket yang batal.
                    <br><code>DELETE FROM tickets WHERE id = 1;</code>
                    <br><i>*Catatan: Wajib pakai WHERE agar tidak menghapus seluruh isi tabel!</i>
                </li>
            </ul>
        </div>
    </div>

    <!-- TEORI 3 -->
    <div class="grill-card">
        <div class="grill-q">3. Apa yang Dimaksud Query, Fungsinya, Beserta Contohnya?</div>
        <div class="grill-a">
            <p><b>Pengertian Query:</b> Permintaan instruksi terstruktur (menggunakan sintaks SQL) yang dikirimkan ke DBMS untuk meminta, memfilter, mengolah, memanipulasi, atau merekap data dari tabel database.</p>
            <p><b>Fungsi &amp; Manfaat Utama:</b></p>
            <ol style="margin-left: 18px;">
                <li><b>Penyaringan Data Spesifik:</b> Menampilkan data yang tepat menggunakan klausul WHERE atau BETWEEN tanpa membebani memori.</li>
                <li><b>Penggabungan Multi-Tabel (JOIN):</b> Mengintegrasikan data dari tabel terpisah (misal: menggabungkan nomor order dengan nama konser dari tabel tickets).</li>
                <li><b>Kalkulasi Agregasi Cepat:</b> Menghitung omset pendapatan secara instan dengan fungsi SUM, COUNT, AVG di level database.</li>
            </ol>
            <p style="margin-top: 8px;"><b>Contoh Query Kompleks (Laporan Omset Konser):</b></p>
            <code>SELECT t.concert_name, t.category, SUM(od.quantity) AS tiket_terjual, SUM(od.subtotal) AS total_omset FROM order_details od INNER JOIN tickets t ON od.ticket_id = t.id INNER JOIN orders o ON od.order_id = o.id WHERE o.status = 'paid' GROUP BY t.id, t.concert_name, t.category;</code>
        </div>
    </div>

    <!-- TEORI 4 -->
    <div class="grill-card">
        <div class="grill-q">4. Jelaskan Konsep dan Arsitektur MVC pada Framework Laravel!</div>
        <div class="grill-a">
            <p><b>MVC (Model - View - Controller)</b> adalah pola arsitektur perangkat lunak yang memisahkan logika aplikasi menjadi 3 komponen utama:</p>
            <ul>
                <li><b>Model (M):</b> Mengelola logika data, relasi basis data via Eloquent ORM, dan aturan penyimpanan ke tabel MySQL (contoh: <code>Ticket.php</code>, <code>Order.php</code>).</li>
                <li><b>View (V):</b> Mengatur presentasi antarmuka pengguna (UI) menggunakan Blade template engine untuk menampilkan data ke layar browser (contoh: <code>concerts.blade.php</code>).</li>
                <li><b>Controller (C):</b> Jembatan penerima HTTP Request, pengatur alur validasi input, pemrosesan transaksi data ke Model, lalu mengirimkan hasilnya ke View (contoh: <code>TicketController.php</code>).</li>
            </ul>
            <p style="margin-top: 6px;"><b>Alur Lifecycle Request Laravel:</b></p>
            <p><code>Browser Request &rarr; routes/web.php &rarr; Middleware &rarr; Controller &rarr; Model (MySQL) &rarr; View (Blade) &rarr; Response HTML Browser</code>.</p>
        </div>
    </div>
    """)

    # MODUL 6: KAMUS ERROR
    lines.append("""
    <h2 class="section-title">MODUL 6: KAMUS ERROR &amp; SOLUSI INSTAN (TROUBLESHOOTING 10 DETIK)</h2>
    <table class="table-custom">
        <thead>
            <tr>
                <th width="200">Pesan Error di Browser</th>
                <th width="220">Penyebab Utama</th>
                <th>Solusi Instan 10 Detik</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><b>419 | Page Expired</b></td>
                <td>Lupa token pengaman CSRF pada tag form.</td>
                <td>Tambahkan <code>@csrf</code> tepat di bawah tag pembuka <code>&lt;form&gt;</code>.</td>
            </tr>
            <tr>
                <td><b>Gambar 404 (Gambar Rusak)</b></td>
                <td>Folder storage belum di-link ke public.</td>
                <td>Jalankan di terminal: <code>php artisan storage:link</code>.</td>
            </tr>
            <tr>
                <td><b>Foto Tidak Masuk ke Disk</b></td>
                <td>Tag form lupa atribut enctype multipart.</td>
                <td>Tambahkan atribut <code>enctype="multipart/form-data"</code> pada form.</td>
            </tr>
            <tr>
                <td><b>Route [admin.tickets.create] not defined</b></td>
                <td>Resource route tidak diberi alias names.</td>
                <td>Tambahkan <code>-&gt;names('admin.tickets')</code> pada Route::resource di <code>routes/web.php</code>.</td>
            </tr>
            <tr>
                <td><b>MassAssignmentException</b></td>
                <td>Kolom model diblokir mass assignment.</td>
                <td>Tambahkan di Model: <code>protected $guarded = ['id'];</code>.</td>
            </tr>
            <tr>
                <td><b>Foreign key constraint fails saat migrate</b></td>
                <td>Urutan migrasi salah / nama tabel salah.</td>
                <td>Pastikan urutan migrasi: users &rarr; tickets &rarr; orders &rarr; order_details.</td>
            </tr>
        </tbody>
    </table>

    <div style="text-align: center; margin-top: 30px; padding: 14px; border-top: 2px dashed #444; font-size: 11px; color: #555;">
        <b>PANDUAN UJIAN SERKOM LARAVEL BNSP &bull; SMKN / LSP JUNIOR WEB DEVELOPER &bull; SEMOGA SUKSES DAN KOMPETEN!</b>
    </div>

</body>
</html>
""")

    full_html = "".join(lines)
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(full_html)
        
    size_kb = len(full_html.encode('utf-8')) / 1024
    print(f"Generated clean guide: {OUTPUT_HTML} ({size_kb:.1f} KB)")
    
    # Also update serkom_guide.html if needed or keep both
    # Let's also update the GitHub repo!

if __name__ == "__main__":
    build_clean_tiket_guide()
