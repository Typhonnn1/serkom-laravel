#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator script for VS Code Laravel Serkom Global Snippets
Produces: serkom-laravel.code-snippets
Contains 54 complete, production-grade snippets covering:
1. Tiket Konser (VIP/Festival/Regular, Orders, Order Details, Customer vs Admin, Rekap Laporan)
2. Makanan & Restoran (Foods, Orders, Order Details, Breeze Auth, Table numbers, Rekap Meja)
All snippets feature tab stops ($1, $2, $0, etc.), universal multi-language scope,
and 100% syntactically valid PHP/Blade/SQL/Bash code.
"""

import json
import os
import re

def escape_code_for_snippet(raw_code):
    r"""
    Escapes PHP/Blade variables for VS Code snippet format.
    In VS Code snippets:
    - $ followed by a letter/underscore ($ticket, $request) must be escaped as \$
      so VS Code outputs a literal dollar sign instead of expanding it as an empty snippet variable.
    - $ followed by a digit ($1, $2, $0) or ${...} represents a snippet tabstop and must NOT be escaped.
    - Negative lookbehind (?<!\\) prevents double escaping if a variable was already escaped.
    """
    lines = raw_code.strip("\r\n").splitlines()
    escaped_lines = []
    for line in lines:
        line_escaped = re.sub(r'(?<!\\)\$([a-zA-Z_])', lambda m: '\\$' + m.group(1), line)
        escaped_lines.append(line_escaped)
    return escaped_lines

# Universal scope including php, blade, html, sql, json, shellscript, powershell, bat, plaintext
GLOBAL_SCOPE = "php,blade,html,sql,json,shellscript,powershell,bat,plaintext"

snippets = {}

def add_snippet(name, prefix, description, code, scope=GLOBAL_SCOPE):
    snippets[name] = {
        "prefix": prefix,
        "body": escape_code_for_snippet(code),
        "description": description,
        "scope": scope
    }

print("Building 54 comprehensive snippets with tab stops...")

# ==========================================
# 1. MIGRATIONS (7 snippets)
# ==========================================

add_snippet(
    "Laravel Migration: Users Table Multi-Role (Serkom)",
    "mig-users",
    "Serkom: Migration tabel users dengan kolom phone dan enum role: admin, customer",
    """Schema::create('${1:users}', function (Blueprint $table) {
    $table->id();
    $table->string('name');
    $table->string('email')->unique();
    $table->string('phone')->nullable();
    $table->timestamp('email_verified_at')->nullable();
    $table->string('password');
    $table->enum('role', [${2:'admin', 'customer'}])->default('customer');
    $table->rememberToken();
    $table->timestamps();
    $0
});"""
)

add_snippet(
    "Laravel Migration: Tickets Table (Konser)",
    "mig-tickets",
    "Serkom: Migration tabel tickets konser (concert_name, artist, venue, event_date, category VIP/Festival/Regular, price, stock, poster, description)",
    """Schema::create('${1:tickets}', function (Blueprint $table) {
    $table->id();
    $table->string('concert_name');
    $table->string('artist');
    $table->string('venue');
    $table->dateTime('event_date');
    $table->enum('category', [${2:'VIP', 'Festival', 'Regular'}])->default('${3:Regular}');
    $table->integer('price');
    $table->integer('stock');
    $table->string('poster')->nullable();
    $table->text('description')->nullable();
    $table->timestamps();
    $0
});"""
)

add_snippet(
    "Laravel Migration: Orders Table (Tiket Konser)",
    "mig-orders-ticket",
    "Serkom: Migration tabel orders tiket konser (user_id FK users cascade, order_code unique, customer data, total_price, status, order_date)",
    """Schema::create('${1:orders}', function (Blueprint $table) {
    $table->id();
    $table->foreignId('user_id')->constrained('${2:users}')->onDelete('cascade');
    $table->string('order_code')->unique();
    $table->string('customer_name');
    $table->string('customer_email');
    $table->string('customer_phone');
    $table->integer('total_price');
    $table->enum('status', [${3:'pending', 'paid', 'cancelled'}])->default('pending');
    $table->date('order_date');
    $table->timestamps();
    $0
});"""
)

add_snippet(
    "Laravel Migration: Order Details Table (Tiket Konser)",
    "mig-details-ticket",
    "Serkom: Migration tabel order_details tiket konser (order_id FK orders cascade, ticket_id FK tickets cascade, quantity, unit_price, subtotal)",
    """Schema::create('${1:order_details}', function (Blueprint $table) {
    $table->id();
    $table->foreignId('order_id')->constrained('${2:orders}')->onDelete('cascade');
    $table->foreignId('ticket_id')->constrained('${3:tickets}')->onDelete('cascade');
    $table->integer('quantity');
    $table->integer('unit_price');
    $table->integer('subtotal');
    $table->timestamps();
    $0
});"""
)

add_snippet(
    "Laravel Migration: Foods Table (Restoran)",
    "mig-foods",
    "Serkom: Migration tabel foods restoran (name, category: Makanan/Minuman/Cemilan, price, description, image)",
    """Schema::create('${1:foods}', function (Blueprint $table) {
    $table->id();
    $table->string('name');
    $table->enum('category', [${2:'Makanan', 'Minuman', 'Cemilan'}])->default('${3:Makanan}');
    $table->integer('price');
    $table->text('description');
    $table->string('image')->nullable();
    $table->timestamps();
    $0
});"""
)

add_snippet(
    "Laravel Migration: Orders Table (Restoran)",
    "mig-orders-food",
    "Serkom: Migration tabel orders pesanan restoran (user_id nullable FK, order_code unique, customer_name, table_number, total_price, status, order_date)",
    """Schema::create('${1:orders}', function (Blueprint $table) {
    $table->id();
    $table->foreignId('user_id')->nullable()->constrained('${2:users}')->onDelete('set null');
    $table->string('order_code')->unique();
    $table->string('customer_name');
    $table->string('table_number');
    $table->integer('total_price');
    $table->enum('status', [${3:'pending', 'cooking', 'completed', 'cancelled'}])->default('pending');
    $table->date('order_date');
    $table->timestamps();
    $0
});"""
)

add_snippet(
    "Laravel Migration: Order Details Table (Restoran)",
    "mig-details-food",
    "Serkom: Migration tabel order_details restoran (order_id FK orders cascade, food_id FK foods cascade, quantity, unit_price, subtotal, notes)",
    """Schema::create('${1:order_details}', function (Blueprint $table) {
    $table->id();
    $table->foreignId('order_id')->constrained('${2:orders}')->onDelete('cascade');
    $table->foreignId('food_id')->constrained('${3:foods}')->onDelete('cascade');
    $table->integer('quantity');
    $table->integer('unit_price');
    $table->integer('subtotal');
    $table->string('notes')->nullable();
    $table->timestamps();
    $0
});"""
)

# ==========================================
# 2. ELOQUENT MODELS (7 snippets)
# ==========================================

add_snippet(
    "Laravel Model: User Model Multi-Role (Serkom)",
    "model-user",
    "Serkom: Model User dengan fillable, casts, helper isAdmin() & isCustomer(), dan relasi hasMany orders()",
    """<?php

namespace App\\Models;

use Illuminate\\Database\\Eloquent\\Factories\\HasFactory;
use Illuminate\\Foundation\\Auth\\User as Authenticatable;
use Illuminate\\Notifications\\Notifiable;

class ${1:User} extends Authenticatable
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

    // Kompatibel 100% untuk Laravel 10 dan Laravel 11
    protected $casts = [
        'email_verified_at' => 'datetime',
        'password' => 'hashed',
    ];

    // Helper pengecekan role
    public function isAdmin(): bool
    {
        return $this->role === 'admin';
    }

    public function isCustomer(): bool
    {
        return $this->role === 'customer';
    }

    // Relasi ke tabel orders (1 User has many Orders)
    public function orders()
    {
        return $this->hasMany(Order::class);
    }
    $0
}"""
)

add_snippet(
    "Laravel Model: Ticket Model (Konser)",
    "model-ticket",
    "Serkom: Model Ticket konser dengan fillable, casts event_date, dan relasi hasMany orderDetails()",
    """<?php

namespace App\\Models;

use Illuminate\\Database\\Eloquent\\Factories\\HasFactory;
use Illuminate\\Database\\Eloquent\\Model;

class ${1:Ticket} extends Model
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

    // Relasi ke order_details (1 Ticket has many OrderDetails)
    public function orderDetails()
    {
        return $this->hasMany(OrderDetail::class);
    }
    $0
}"""
)

add_snippet(
    "Laravel Model: Order Model (Tiket Konser)",
    "model-order-ticket",
    "Serkom: Model Order tiket konser dengan fillable, casts order_date, relasi belongsTo user(), hasMany orderDetails()",
    """<?php

namespace App\\Models;

use Illuminate\\Database\\Eloquent\\Factories\\HasFactory;
use Illuminate\\Database\\Eloquent\\Model;

class ${1:Order} extends Model
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

    // Relasi ke User pemesan
    public function user()
    {
        return $this->belongsTo(User::class);
    }

    // Relasi ke rincian pesanan
    public function orderDetails()
    {
        return $this->hasMany(OrderDetail::class);
    }
    $0
}"""
)

add_snippet(
    "Laravel Model: OrderDetail Model (Tiket Konser)",
    "model-detail-ticket",
    "Serkom: Model OrderDetail tiket konser dengan fillable, belongsTo order(), belongsTo ticket()",
    """<?php

namespace App\\Models;

use Illuminate\\Database\\Eloquent\\Factories\\HasFactory;
use Illuminate\\Database\\Eloquent\\Model;

class ${1:OrderDetail} extends Model
{
    use HasFactory;

    protected $fillable = [
        'order_id',
        'ticket_id',
        'quantity',
        'unit_price',
        'subtotal',
    ];

    // Relasi ke tabel Order
    public function order()
    {
        return $this->belongsTo(Order::class);
    }

    // Relasi ke tabel Ticket
    public function ticket()
    {
        return $this->belongsTo(Ticket::class);
    }
    $0
}"""
)

add_snippet(
    "Laravel Model: Food Model (Restoran)",
    "model-food",
    "Serkom: Model Food restoran dengan fillable dan relasi hasMany orderDetails()",
    """<?php

namespace App\\Models;

use Illuminate\\Database\\Eloquent\\Factories\\HasFactory;
use Illuminate\\Database\\Eloquent\\Model;

class ${1:Food} extends Model
{
    use HasFactory;

    protected $table = '${2:foods}';

    protected $fillable = [
        'name',
        'category',
        'price',
        'description',
        'image',
    ];

    // Relasi ke rincian pesanan makanan
    public function orderDetails()
    {
        return $this->hasMany(OrderDetail::class);
    }
    $0
}"""
)

add_snippet(
    "Laravel Model: Order Model (Restoran)",
    "model-order-food",
    "Serkom: Model Order restoran dengan table_number, relasi belongsTo user(), hasMany orderDetails()",
    """<?php

namespace App\\Models;

use Illuminate\\Database\\Eloquent\\Factories\\HasFactory;
use Illuminate\\Database\\Eloquent\\Model;

class ${1:Order} extends Model
{
    use HasFactory;

    protected $fillable = [
        'user_id',
        'order_code',
        'customer_name',
        'table_number',
        'total_price',
        'status',
        'order_date',
    ];

    protected $casts = [
        'order_date' => 'date',
    ];

    public function user()
    {
        return $this->belongsTo(User::class);
    }

    public function orderDetails()
    {
        return $this->hasMany(OrderDetail::class);
    }
    $0
}"""
)

add_snippet(
    "Laravel Model: OrderDetail Model (Restoran)",
    "model-detail-food",
    "Serkom: Model OrderDetail resto dengan fillable, relasi belongsTo order(), belongsTo food()",
    """<?php

namespace App\\Models;

use Illuminate\\Database\\Eloquent\\Factories\\HasFactory;
use Illuminate\\Database\\Eloquent\\Model;

class ${1:OrderDetail} extends Model
{
    use HasFactory;

    protected $fillable = [
        'order_id',
        'food_id',
        'quantity',
        'unit_price',
        'subtotal',
        'notes',
    ];

    public function order()
    {
        return $this->belongsTo(Order::class);
    }

    public function food()
    {
        return $this->belongsTo(Food::class);
    }
    $0
}"""
)

# ==========================================
# 3. CONTROLLERS (8 snippets)
# ==========================================

add_snippet(
    "Laravel Controller: Admin TicketController Resource Lengkap (Konser)",
    "ctrl-ticket",
    "Serkom: Admin TicketController CRUD Resource (index pagination, create, store upload poster, edit, update poster lama, destroy file fisik)",
    """<?php

namespace App\\Http\\Controllers\\Admin;

use App\\Http\\Controllers\\Controller;
use App\\Models\\Ticket;
use Illuminate\\Http\\Request;
use Illuminate\\Support\\Facades\\Storage;

class ${1:TicketController} extends Controller
{
    // 1. Tampilkan Semua Tiket Konser
    public function index()
    {
        $tickets = Ticket::latest()->paginate(${2:10});
        return view('admin.tickets.index', compact('tickets'));
    }

    // 2. Form Tambah Tiket
    public function create()
    {
        return view('admin.tickets.create');
    }

    // 3. Simpan Tiket Baru + Upload Poster
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

    // 5. Update Tiket + Ganti Poster Lama
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

        if ($request->hasFile('poster')) {
            // Hapus poster lama dari storage disk public jika ada
            if ($ticket->poster && Storage::disk('public')->exists($ticket->poster)) {
                Storage::disk('public')->delete($ticket->poster);
            }
            $validated['poster'] = $request->file('poster')->store('posters', 'public');
        }

        $ticket->update($validated);

        return redirect()->route('admin.tickets.index')->with('success', 'Data tiket konser berhasil diperbarui!');
    }

    // 6. Hapus Tiket + Hapus File Poster Fisik
    public function destroy(Ticket $ticket)
    {
        if ($ticket->poster && Storage::disk('public')->exists($ticket->poster)) {
            Storage::disk('public')->delete($ticket->poster);
        }

        $ticket->delete();

        return redirect()->route('admin.tickets.index')->with('success', 'Tiket konser berhasil dihapus!');
    }
    $0
}"""
)

add_snippet(
    "Laravel Controller: Admin UserController CRUD & Self-Delete Protection (Serkom)",
    "ctrl-user",
    "Serkom: Admin UserController Resource (index search & role filter, store hash password, update ignore unique email, destroy anti-self-delete)",
    """<?php

namespace App\\Http\\Controllers\\Admin;

use App\\Http\\Controllers\\Controller;
use App\\Models\\User;
use Illuminate\\Http\\Request;
use Illuminate\\Support\\Facades\\Auth;
use Illuminate\\Support\\Facades\\Hash;
use Illuminate\\Validation\\Rule;

class ${1:UserController} extends Controller
{
    // 1. Tampilkan Daftar Semua Pengguna (Admin & Customer)
    public function index(Request $request)
    {
        $query = User::query();

        // Filter Pencarian (Nama, Email, No HP)
        if ($request->filled('search')) {
            $search = $request->search;
            $query->where(function ($q) use ($search) {
                $q->where('name', 'like', "%{$search}%")
                  ->orWhere('email', 'like', "%{$search}%")
                  ->orWhere('phone', 'like', "%{$search}%");
            });
        }

        // Filter Role (Admin / Customer)
        if ($request->filled('role')) {
            $query->where('role', $request->role);
        }

        $users = $query->latest()->paginate(${2:10})->withQueryString();

        return view('admin.users.index', compact('users'));
    }

    // 2. Tampilkan Form Tambah Pengguna Baru
    public function create()
    {
        return view('admin.users.create');
    }

    // 3. Simpan Pengguna Baru ke Database
    public function store(Request $request)
    {
        $validated = $request->validate([
            'name'     => 'required|string|max:255',
            'email'    => 'required|email|max:255|unique:users,email',
            'phone'    => 'nullable|string|max:20',
            'role'     => 'required|in:admin,customer',
            'password' => 'required|string|min:6|confirmed',
        ]);

        $validated['password'] = Hash::make($validated['password']);

        User::create($validated);

        return redirect()->route('admin.users.index')->with('success', 'Pengguna baru berhasil ditambahkan!');
    }

    // 4. Form Edit Data Pengguna
    public function edit(User $user)
    {
        return view('admin.users.edit', compact('user'));
    }

    // 5. Perbarui Data Pengguna
    public function update(Request $request, User $user)
    {
        $validated = $request->validate([
            'name'     => 'required|string|max:255',
            'email'    => ['required', 'email', 'max:255', Rule::unique('users')->ignore($user->id)],
            'phone'    => 'nullable|string|max:20',
            'role'     => 'required|in:admin,customer',
            'password' => 'nullable|string|min:6|confirmed',
        ]);

        if (!empty($validated['password'])) {
            $validated['password'] = Hash::make($validated['password']);
        } else {
            unset($validated['password']);
        }

        $user->update($validated);

        return redirect()->route('admin.users.index')->with('success', 'Data pengguna berhasil diperbarui!');
    }

    // 6. Hapus Data Pengguna (Dengan Proteksi Anti Self-Delete)
    public function destroy(User $user)
    {
        // Mencegah admin menghapus akunnya sendiri yang sedang aktif
        if (Auth::id() === $user->id) {
            return back()->with('error', 'Tindakan ditolak! Anda tidak dapat menghapus akun Anda sendiri yang sedang aktif.');
        }

        $user->delete();

        return redirect()->route('admin.users.index')->with('success', 'Akun pengguna berhasil dihapus!');
    }
    $0
}"""
)

add_snippet(
    "Laravel Controller: Admin OrderReportController Dashboard Rekap Omset (Tiket)",
    "ctrl-order-ticket",
    "Serkom: Admin OrderReportController (Dashboard rekap omset, 4 stat cards, filter tanggal & status, patch updateStatus, view printReport)",
    """<?php

namespace App\\Http\\Controllers\\Admin;

use App\\Http\\Controllers\\Controller;
use App\\Models\\Order;
use App\\Models\\OrderDetail;
use Illuminate\\Http\\Request;

class ${1:OrderReportController} extends Controller
{
    // 1. Tampilkan Dashboard Rekap Pesanan
    public function index(Request $request)
    {
        // Hitung Kartu Statistik Ringkasan (null safe dengan ?? 0)
        $totalRevenue = Order::where('status', 'paid')->sum('total_price') ?? 0;
        $totalTicketsSold = OrderDetail::whereHas('order', function ($q) {
            $q->where('status', 'paid');
        })->sum('quantity') ?? 0;
        $pendingOrdersCount = Order::where('status', 'pending')->count();
        $paidOrdersCount = Order::where('status', 'paid')->count();

        // Query Rekap Pesanan Masuk (Eager Loading untuk cegah N+1 problem)
        $query = Order::with(['user', 'orderDetails.ticket'])->latest();

        // Filter Rentang Tanggal
        if ($request->filled('start_date') && $request->filled('end_date')) {
            $query->whereBetween('order_date', [$request->start_date, $request->end_date]);
        }

        // Filter Status Pembayaran
        if ($request->filled('status')) {
            $query->where('status', $request->status);
        }

        $orders = $query->paginate(${2:15})->withQueryString();

        return view('admin.orders.index', compact(
            'orders',
            'totalRevenue',
            'totalTicketsSold',
            'pendingOrdersCount',
            'paidOrdersCount'
        ));
    }

    // 2. Ubah Status Pesanan (Pending -> Paid / Cancelled)
    public function updateStatus(Request $request, $id)
    {
        $request->validate([
            'status' => 'required|in:pending,paid,cancelled',
        ]);

        $order = Order::findOrFail($id);
        $order->update(['status' => $request->status]);

        return back()->with('success', "Status pesanan {$order->order_code} berhasil diubah menjadi " . strtoupper($request->status));
    }

    // 3. Tampilan Cetak Laporan (Print / PDF Ready)
    public function printReport(Request $request)
    {
        $query = Order::with(['user', 'orderDetails.ticket'])->latest();

        if ($request->filled('start_date') && $request->filled('end_date')) {
            $query->whereBetween('order_date', [$request->start_date, $request->end_date]);
        }

        if ($request->filled('status')) {
            $query->where('status', $request->status);
        }

        $orders = $query->get();
        $totalRevenue = $orders->where('status', 'paid')->sum('total_price') ?? 0;

        return view('admin.orders.print', compact('orders', 'totalRevenue'));
    }
    $0
}"""
)

add_snippet(
    "Laravel Controller: Customer BookingController Transaksi Atomik (Tiket)",
    "ctrl-customer-booking",
    "Serkom: Customer BookingController (Katalog konser publik, form booking, checkout atomik DB::transaction + stok decrement, myTickets, printTicket e-tiket)",
    """<?php

namespace App\\Http\\Controllers\\Customer;

use App\\Http\\Controllers\\Controller;
use App\\Models\\Order;
use App\\Models\\OrderDetail;
use App\\Models\\Ticket;
use Illuminate\\Http\\Request;
use Illuminate\\Support\\Facades\\Auth;
use Illuminate\\Support\\Facades\\DB;

class ${1:BookingController} extends Controller
{
    // 1. Katalog Konser Publik
    public function index()
    {
        $tickets = Ticket::where('stock', '>', 0)->latest()->get();
        return view('customer.concerts', compact('tickets'));
    }

    // 2. Form Pemesanan Tiket (Booking Form)
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
            'quantity'  => 'required|integer|min:1|max:${2:5}',
        ]);

        $ticket = Ticket::findOrFail($request->ticket_id);

        // Validasi kuota ketersediaan tiket
        if ($ticket->stock < $request->quantity) {
            return back()->with('error', 'Maaf, kuota tiket yang diminta melebihi sisa stok yang tersedia!');
        }

        // Jalankan Database Transaction untuk Menjamin Integritas Data ACID
        DB::beginTransaction();
        try {
            $user = Auth::user();
            $subtotal = $ticket->price * $request->quantity;
            $orderCode = '${3:TKT}-' . date('Ymd') . '-' . strtoupper(substr(uniqid(), -4));

            // Simpan Data Header Order
            $order = Order::create([
                'user_id'        => $user->id,
                'order_code'     => $orderCode,
                'customer_name'  => $user->name,
                'customer_email' => $user->email,
                'customer_phone' => $user->phone ?? '081234567890',
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
        } catch (\\Exception $e) {
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
    $0
}"""
)

add_snippet(
    "Laravel Controller: Admin FoodController CRUD Resource (Restoran)",
    "ctrl-food",
    "Serkom: Admin FoodController Resource (index pagination, create, store upload image, edit, update ganti foto lama, destroy hapus file fisik)",
    """<?php

namespace App\\Http\\Controllers;

use App\\Models\\Food;
use Illuminate\\Http\\Request;
use Illuminate\\Support\\Facades\\Storage;

class ${1:FoodController} extends Controller
{
    // 1. Tampilkan tabel makanan (index)
    public function index()
    {
        $foods = Food::latest()->paginate(${2:10});
        return view('admin.foods.index', compact('foods'));
    }

    // 2. Tampilkan form tambah makanan (create)
    public function create()
    {
        return view('admin.foods.create');
    }

    // 3. Simpan data makanan baru + upload gambar (store)
    public function store(Request $request)
    {
        $validated = $request->validate([
            'name'        => 'required|string|max:255',
            'category'    => 'required|in:Makanan,Minuman,Cemilan',
            'price'       => 'required|numeric|min:0',
            'description' => 'required|string',
            'image'       => 'nullable|image|mimes:jpeg,png,jpg|max:2048',
        ]);

        if ($request->hasFile('image')) {
            $validated['image'] = $request->file('image')->store('foods', 'public');
        }

        Food::create($validated);

        return redirect()->route('admin.foods.index')->with('success', 'Menu makanan berhasil ditambahkan!');
    }

    // 4. Tampilkan form edit makanan (edit)
    public function edit(Food $food)
    {
        return view('admin.foods.edit', compact('food'));
    }

    // 5. Update data makanan + ganti gambar lama (update)
    public function update(Request $request, Food $food)
    {
        $validated = $request->validate([
            'name'        => 'required|string|max:255',
            'category'    => 'required|in:Makanan,Minuman,Cemilan',
            'price'       => 'required|numeric|min:0',
            'description' => 'required|string',
            'image'       => 'nullable|image|mimes:jpeg,png,jpg|max:2048',
        ]);

        if ($request->hasFile('image')) {
            if ($food->image && Storage::disk('public')->exists($food->image)) {
                Storage::disk('public')->delete($food->image);
            }
            $validated['image'] = $request->file('image')->store('foods', 'public');
        }

        $food->update($validated);

        return redirect()->route('admin.foods.index')->with('success', 'Menu makanan berhasil diperbarui!');
    }

    // 6. Hapus makanan + hapus gambar fisik (destroy)
    public function destroy(Food $food)
    {
        if ($food->image && Storage::disk('public')->exists($food->image)) {
            Storage::disk('public')->delete($food->image);
        }

        $food->delete();

        return redirect()->route('admin.foods.index')->with('success', 'Menu makanan berhasil dihapus!');
    }
    $0
}"""
)

add_snippet(
    "Laravel Controller: Admin Resto OrderController (Rekap Pesanan Meja)",
    "ctrl-order-food",
    "Serkom: Resto OrderController (Dashboard pesanan per meja resto, filter tanggal & status, update status pesanan, cetak struk/laporan)",
    """<?php

namespace App\\Http\\Controllers\\Admin;

use App\\Http\\Controllers\\Controller;
use App\\Models\\Order;
use Illuminate\\Http\\Request;

class ${1:RestoOrderController} extends Controller
{
    // 1. Dashboard Rekap Pesanan Meja Restoran
    public function index(Request $request)
    {
        $totalRevenue = Order::where('status', 'completed')->sum('total_price') ?? 0;
        $pendingOrders = Order::where('status', 'pending')->count();
        $cookingOrders = Order::where('status', 'cooking')->count();
        $completedOrders = Order::where('status', 'completed')->count();

        $query = Order::with(['orderDetails.food'])->latest();

        if ($request->filled('start_date') && $request->filled('end_date')) {
            $query->whereBetween('order_date', [$request->start_date, $request->end_date]);
        }

        if ($request->filled('status')) {
            $query->where('status', $request->status);
        }

        if ($request->filled('table_number')) {
            $query->where('table_number', $request->table_number);
        }

        $orders = $query->paginate(${2:15})->withQueryString();

        return view('admin.resto-orders.index', compact(
            'orders',
            'totalRevenue',
            'pendingOrders',
            'cookingOrders',
            'completedOrders'
        ));
    }

    // 2. Ubah Status Pesanan Meja (pending -> cooking -> completed -> cancelled)
    public function updateStatus(Request $request, $id)
    {
        $request->validate([
            'status' => 'required|in:pending,cooking,completed,cancelled',
        ]);

        $order = Order::findOrFail($id);
        $order->update(['status' => $request->status]);

        return back()->with('success', "Status pesanan Meja {$order->table_number} ({$order->order_code}) diubah menjadi " . strtoupper($request->status));
    }
    $0
}"""
)

add_snippet(
    "Laravel Controller: Customer FoodOrderController (Pemesanan Meja Resto)",
    "ctrl-customer-food",
    "Serkom: Customer FoodOrderController (Katalog menu makanan resto, pilih nomor meja, checkout transaksi DB::transaction)",
    """<?php

namespace App\\Http\\Controllers\\Customer;

use App\\Http\\Controllers\\Controller;
use App\\Models\\Food;
use App\\Models\\Order;
use App\\Models\\OrderDetail;
use Illuminate\\Http\\Request;
use Illuminate\\Support\\Facades\\Auth;
use Illuminate\\Support\\Facades\\DB;

class ${1:FoodOrderController} extends Controller
{
    // 1. Katalog Menu Makanan Resto
    public function index()
    {
        $foods = Food::latest()->get();
        return view('customer.menu', compact('foods'));
    }

    // 2. Form Pemesanan / Checkout Menu
    public function showCheckoutForm($id)
    {
        $food = Food::findOrFail($id);
        return view('customer.resto-checkout', compact('food'));
    }

    // 3. Simpan Pesanan Resto (Atomik)
    public function checkout(Request $request)
    {
        $request->validate([
            'food_id'      => 'required|exists:foods,id',
            'table_number' => 'required|string|max:10',
            'quantity'     => 'required|integer|min:1',
            'notes'        => 'nullable|string|max:255',
        ]);

        $food = Food::findOrFail($request->food_id);

        DB::beginTransaction();
        try {
            $subtotal = $food->price * $request->quantity;
            $orderCode = '${2:RESTO}-' . date('Ymd') . '-' . strtoupper(substr(uniqid(), -4));

            $order = Order::create([
                'user_id'       => Auth::id(),
                'order_code'    => $orderCode,
                'customer_name' => Auth::check() ? Auth::user()->name : 'Pelanggan Meja ' . $request->table_number,
                'table_number'  => $request->table_number,
                'total_price'   => $subtotal,
                'status'        => 'pending',
                'order_date'    => now()->toDateString(),
            ]);

            OrderDetail::create([
                'order_id'   => $order->id,
                'food_id'    => $food->id,
                'quantity'   => $request->quantity,
                'unit_price' => $food->price,
                'subtotal'   => $subtotal,
                'notes'      => $request->notes,
            ]);

            DB::commit();

            return redirect()->route('menu.index')->with('success', "Pesanan Meja {$request->table_number} berhasil dibuat! Kode: {$orderCode}");
        } catch (\\Exception $e) {
            DB::rollBack();
            return back()->with('error', 'Gagal memproses pesanan: ' . $e->getMessage());
        }
    }
    $0
}"""
)

add_snippet(
    "Laravel Controller: Auth Redirect Multi-Role Helper (Serkom)",
    "ctrl-auth-redirect",
    "Serkom: Custom redirect logic setelah login / register (Admin ke /admin/dashboard, Customer ke katalog)",
    """// Letakkan di AuthenticatedSessionController / LoginResponse atau routes:
if (Auth::user()->role === '${1:admin}') {
    return redirect()->intended(route('${2:admin.orders.index}'));
}

return redirect()->intended(route('${3:concerts.index}'));
$0"""
)

# ==========================================
# 4. MIDDLEWARE (1 snippet)
# ==========================================

add_snippet(
    "Laravel Middleware: IsAdmin Role Gatekeeper (Serkom)",
    "mid-isadmin",
    "Serkom: Middleware IsAdmin (Cek Auth::check() && Auth::user()->role === 'admin', redirect jika bukan admin)",
    """<?php

namespace App\\Http\\Middleware;

use Closure;
use Illuminate\\Http\\Request;
use Illuminate\\Support\\Facades\\Auth;
use Symfony\\Component\\HttpFoundation\\Response;

class ${1:IsAdmin}
{
    public function handle(Request $request, Closure $next): Response
    {
        // Cek apakah user sudah login dan rolenya admin
        if (Auth::check() && Auth::user()->role === '${2:admin}') {
            return $next($request);
        }

        // Jika bukan admin, tolak dan kembalikan ke halaman depan
        return redirect()->route('${3:concerts.index}')->with('error', 'Akses ditolak! Halaman ini khusus Administrator.');
    }
    $0
}"""
)

# ==========================================
# 5. SEEDERS (4 snippets)
# ==========================================

add_snippet(
    "Laravel Seeder: TicketSeeder Sample Data (Konser)",
    "seeder-ticket",
    "Serkom: TicketSeeder (3 sample tiket konser: Coldplay VIP, Sheila On 7 Festival, Tulus Regular)",
    """<?php

namespace Database\\Seeders;

use App\\Models\\Ticket;
use Illuminate\\Database\\Seeder;

class ${1:TicketSeeder} extends Seeder
{
    public function run(): void
    {
        Ticket::create([
            'concert_name' => '${2:Coldplay: Music of the Spheres World Tour}',
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
        $0
    }
}"""
)

add_snippet(
    "Laravel Seeder: DatabaseSeeder Lengkap (Tiket Konser)",
    "seeder-database-ticket",
    "Serkom: DatabaseSeeder Tiket Konser (Buat akun admin@tiket.com, customer@gmail.com, dan panggil TicketSeeder)",
    """<?php

namespace Database\\Seeders;

use App\\Models\\User;
use Illuminate\\Database\\Seeder;
use Illuminate\\Support\\Facades\\Hash;

class DatabaseSeeder extends Seeder
{
    public function run(): void
    {
        // 1. Akun Administrator (Panitia Konser)
        User::create([
            'name'     => 'Administrator Konser',
            'email'    => '${1:admin@tiket.com}',
            'phone'    => '081122334455',
            'password' => Hash::make('${2:password123}'),
            'role'     => 'admin',
        ]);

        // 2. Akun Customer (Pembeli Tiket)
        User::create([
            'name'     => 'Budi Pembeli',
            'email'    => '${3:customer@gmail.com}',
            'phone'    => '081234567890',
            'password' => Hash::make('${4:password123}'),
            'role'     => 'customer',
        ]);

        // 3. Panggil Seeder Tiket Konser
        $this->call([
            TicketSeeder::class,
        ]);
        $0
    }
}"""
)

add_snippet(
    "Laravel Seeder: FoodSeeder Sample Data (Restoran)",
    "seeder-food",
    "Serkom: FoodSeeder Restoran (Sample menu: Nasi Goreng, Mie Seafood, Es Teh, Cemilan)",
    """<?php

namespace Database\\Seeders;

use App\\Models\\Food;
use Illuminate\\Database\\Seeder;

class ${1:FoodSeeder} extends Seeder
{
    public function run(): void
    {
        Food::create([
            'name'        => '${2:Nasi Goreng Spesial}',
            'category'    => 'Makanan',
            'price'       => 28000,
            'description' => 'Nasi goreng dengan suwiran ayam, telur mata sapi, sosis, dan kerupuk renyah.',
        ]);

        Food::create([
            'name'        => 'Mie Goreng Seafood',
            'category'    => 'Makanan',
            'price'       => 32000,
            'description' => 'Mie kenyal digoreng gurih dengan udang, cumi, dan sayuran segar.',
        ]);

        Food::create([
            'name'        => 'Es Teh Manis Segar',
            'category'    => 'Minuman',
            'price'       => 6000,
            'description' => 'Teh melati seduh dingin dengan gula tebu asli dan es batu kristal.',
        ]);

        Food::create([
            'name'        => 'Kentang Goreng Keju',
            'category'    => 'Cemilan',
            'price'       => 18000,
            'description' => 'French fries renyah bertabur bumbu keju gurih dan saus sambal.',
        ]);
        $0
    }
}"""
)

add_snippet(
    "Laravel Seeder: DatabaseSeeder Lengkap (Restoran)",
    "seeder-database-food",
    "Serkom: DatabaseSeeder Resto (Buat akun admin resto, kasir/customer, dan panggil FoodSeeder)",
    """<?php

namespace Database\\Seeders;

use App\\Models\\User;
use Illuminate\\Database\\Seeder;
use Illuminate\\Support\\Facades\\Hash;

class DatabaseSeeder extends Seeder
{
    public function run(): void
    {
        User::create([
            'name'     => 'Admin Restoran',
            'email'    => '${1:admin@resto.com}',
            'phone'    => '08122334455',
            'password' => Hash::make('${2:password123}'),
            'role'     => 'admin',
        ]);

        User::create([
            'name'     => 'Pelanggan Meja 1',
            'email'    => '${3:customer@resto.com}',
            'phone'    => '081298765432',
            'password' => Hash::make('${4:password123}'),
            'role'     => 'customer',
        ]);

        $this->call([
            FoodSeeder::class,
        ]);
        $0
    }
}"""
)

# ==========================================
# 6. ROUTING (routes/web.php) (2 snippets)
# ==========================================

add_snippet(
    "Laravel Routes: File routes/web.php Lengkap (Tiket Konser)",
    "route-ticket-complete",
    "Serkom: routes/web.php Lengkap Kasus Tiket Konser (Publik, Customer auth group, Admin auth+admin group, CRUD tickets & users, reports)",
    """<?php

use App\\Http\\Controllers\\ProfileController;
use App\\Http\\Controllers\\Customer\\BookingController;
use App\\Http\\Controllers\\Admin\\TicketController;
use App\\Http\\Controllers\\Admin\\UserController;
use App\\Http\\Controllers\\Admin\\OrderReportController;
use Illuminate\\Support\\Facades\\Route;

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
// Catatan: Jika alias 'admin' belum didaftarkan di Kernel.php/bootstrap/app.php,
// Anda dapat langsung memakai class: \\App\\Http\\Middleware\\IsAdmin::class
Route::middleware(['auth', '${2:admin}'])->prefix('${1:admin}')->name('${1:admin}.')->group(function () {
    // Dashboard Rekap Laporan Pesanan Masuk
    Route::get('/dashboard', [OrderReportController::class, 'index'])->name('orders.index');
    Route::patch('/orders/{id}/status', [OrderReportController::class, 'updateStatus'])->name('orders.updateStatus');
    Route::get('/orders/print', [OrderReportController::class, 'printReport'])->name('orders.print');

    // CRUD Master Data Tiket Konser
    Route::resource('tickets', TicketController::class);

    // CRUD Master Data Pengguna (User Management)
    Route::resource('users', UserController::class);
    $0
});

require __DIR__.'/auth.php';"""
)

add_snippet(
    "Laravel Routes: File routes/web.php Lengkap (Restoran)",
    "route-food-complete",
    "Serkom: routes/web.php Lengkap Kasus Makanan / Restoran (Katalog menu, Customer order, Admin food resource & orders rekap)",
    """<?php

use App\\Http\\Controllers\\ProfileController;
use App\\Http\\Controllers\\FoodController;
use App\\Http\\Controllers\\Customer\\FoodOrderController;
use App\\Http\\Controllers\\Admin\\RestoOrderController;
use Illuminate\\Support\\Facades\\Route;

// 1. SISI PUBLIK & CUSTOMER
Route::get('/', [FoodOrderController::class, 'index'])->name('menu.index');
Route::get('/order/{id}', [FoodOrderController::class, 'showCheckoutForm'])->name('customer.order');
Route::post('/checkout', [FoodOrderController::class, 'checkout'])->name('customer.checkout');

// 2. SISI AUTH PROFILE
Route::middleware('auth')->group(function () {
    Route::get('/profile', [ProfileController::class, 'edit'])->name('profile.edit');
    Route::patch('/profile', [ProfileController::class, 'update'])->name('profile.update');
    Route::delete('/profile', [ProfileController::class, 'destroy'])->name('profile.destroy');
});

// 3. SISI ADMINISTRATOR (Wajib Login & Middleware Admin)
// Catatan: Jika alias 'admin' belum didaftarkan, bisa gunakan: \\App\\Http\\Middleware\\IsAdmin::class
Route::middleware(['auth', '${2:admin}'])->prefix('${1:admin}')->name('${1:admin}.')->group(function () {
    // Dashboard Rekap Pesanan Meja Resto
    Route::get('/dashboard', [RestoOrderController::class, 'index'])->name('resto.orders.index');
    Route::patch('/orders/{id}/status', [RestoOrderController::class, 'updateStatus'])->name('resto.orders.updateStatus');

    // CRUD Master Menu Makanan
    Route::resource('foods', FoodController::class);
    $0
});

require __DIR__.'/auth.php';"""
)

# ==========================================
# 7. BLADE VIEWS - TIKET KONSER (12 snippets)
# ==========================================

add_snippet(
    "Blade View: Admin Daftar Tiket Konser (index.blade.php)",
    "blade-ticket-index",
    "Serkom Blade: resources/views/admin/tickets/index.blade.php (Tabel tiket, poster, badge kategori, sisa stok, edit, hapus konfirmasi)",
    """<x-app-layout>
    <div class="py-6 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center mb-6">
            <div>
                <h2 class="text-2xl font-bold text-gray-800">🎟️ ${1:Master Data Tiket Konser}</h2>
                <p class="text-sm text-gray-500">Kelola daftar konser, kuota tiket, harga, dan banner poster.</p>
            </div>
            <a href="{{ route('admin.tickets.create') }}" class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded shadow text-sm">
                + Tambah Tiket Konser
            </a>
        </div>

        @if(session('success'))
            <div class="bg-green-100 border-l-4 border-green-500 text-green-700 p-4 mb-4 rounded shadow-sm text-sm">
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
    $0
</x-app-layout>"""
)

add_snippet(
    "Blade View: Admin Form Tambah Tiket Konser (create.blade.php)",
    "blade-ticket-create",
    "Serkom Blade: resources/views/admin/tickets/create.blade.php (Form input tiket baru, upload poster multipart, errors alert, datetime-local)",
    """<x-app-layout>
    <div class="py-6 max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
            <h2 class="text-xl font-bold text-gray-800 mb-4 border-b pb-2">➕ ${1:Tambah Tiket Konser Baru}</h2>

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
    $0
</x-app-layout>"""
)

add_snippet(
    "Blade View: Admin Form Edit Tiket Konser (edit.blade.php)",
    "blade-ticket-edit",
    "Serkom Blade: resources/views/admin/tickets/edit.blade.php (Form edit tiket konser, preview poster lama, upload ganti poster, method PUT)",
    """<x-app-layout>
    <div class="py-6 max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
            <h2 class="text-xl font-bold text-gray-800 mb-4 border-b pb-2">✏️ ${1:Edit Data Tiket Konser}</h2>

            @if($errors->any())
                <div class="bg-red-100 border-l-4 border-red-500 text-red-700 p-3 mb-4 rounded text-sm">
                    <ul class="list-disc list-inside">
                        @foreach($errors->all() as $error)
                            <li>{{ $error }}</li>
                        @endforeach
                    </ul>
                </div>
            @endif

            <form action="{{ route('admin.tickets.update', $ticket->id) }}" method="POST" enctype="multipart/form-data" class="space-y-4">
                @csrf
                @method('PUT')

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-sm font-semibold text-gray-700">Nama Konser</label>
                        <input type="text" name="concert_name" value="{{ old('concert_name', $ticket->concert_name) }}" required class="w-full border-gray-300 rounded shadow-sm text-sm">
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-gray-700">Artis / Musisi</label>
                        <input type="text" name="artist" value="{{ old('artist', $ticket->artist) }}" required class="w-full border-gray-300 rounded shadow-sm text-sm">
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-sm font-semibold text-gray-700">Lokasi / Venue</label>
                        <input type="text" name="venue" value="{{ old('venue', $ticket->venue) }}" required class="w-full border-gray-300 rounded shadow-sm text-sm">
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-gray-700">Tanggal & Jam Acara</label>
                        <input type="datetime-local" name="event_date" value="{{ old('event_date', $ticket->event_date->format('Y-m-d\\TH:i')) }}" required class="w-full border-gray-300 rounded shadow-sm text-sm">
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div>
                        <label class="block text-sm font-semibold text-gray-700">Kategori Tiket</label>
                        <select name="category" required class="w-full border-gray-300 rounded shadow-sm text-sm">
                            <option value="VIP" {{ old('category', $ticket->category) == 'VIP' ? 'selected' : '' }}>VIP</option>
                            <option value="Festival" {{ old('category', $ticket->category) == 'Festival' ? 'selected' : '' }}>Festival</option>
                            <option value="Regular" {{ old('category', $ticket->category) == 'Regular' ? 'selected' : '' }}>Regular</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-gray-700">Harga Satuan (Rp)</label>
                        <input type="number" name="price" value="{{ old('price', $ticket->price) }}" required min="0" class="w-full border-gray-300 rounded shadow-sm text-sm">
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-gray-700">Kuota Stok Tiket</label>
                        <input type="number" name="stock" value="{{ old('stock', $ticket->stock) }}" required min="0" class="w-full border-gray-300 rounded shadow-sm text-sm">
                    </div>
                </div>

                <div>
                    <label class="block text-sm font-semibold text-gray-700">Ganti Banner Poster (Opsional)</label>
                    @if($ticket->poster)
                        <div class="mb-2">
                            <img src="{{ asset('storage/' . $ticket->poster) }}" class="w-24 h-24 object-cover rounded shadow" alt="Poster Saat Ini">
                            <span class="text-xs text-gray-500">Poster saat ini</span>
                        </div>
                    @endif
                    <input type="file" name="poster" accept="image/*" class="w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded file:border-0 file:text-sm file:font-semibold file:bg-indigo-50 file:text-indigo-700 hover:file:bg-indigo-100">
                </div>

                <div>
                    <label class="block text-sm font-semibold text-gray-700">Deskripsi / Ketentuan Konser</label>
                    <textarea name="description" rows="3" class="w-full border-gray-300 rounded shadow-sm text-sm">{{ old('description', $ticket->description) }}</textarea>
                </div>

                <div class="flex justify-end space-x-2 pt-4 border-t">
                    <a href="{{ route('admin.tickets.index') }}" class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded text-sm">Batal</a>
                    <button type="submit" class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded text-sm">Simpan Perubahan</button>
                </div>
            </form>
        </div>
    </div>
    $0
</x-app-layout>"""
)

add_snippet(
    "Blade View: Admin User Management Index (index.blade.php)",
    "blade-user-index",
    "Serkom Blade: resources/views/admin/users/index.blade.php (Tabel kelola user, filter search nama/email, filter role, tombol hapus aman)",
    """<x-app-layout>
    <div class="py-6 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-4">
        <div class="flex justify-between items-center">
            <div>
                <h2 class="text-2xl font-bold text-gray-800">👥 ${1:Kelola Data Pengguna (User Management)}</h2>
                <p class="text-sm text-gray-500">Kelola akun administrator dan customer pembeli tiket.</p>
            </div>
            <a href="{{ route('admin.users.create') }}" class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded shadow text-sm">
                + Tambah Pengguna Baru
            </a>
        </div>

        @if(session('success'))
            <div class="bg-emerald-100 border-l-4 border-emerald-500 text-emerald-800 p-4 rounded text-sm font-semibold">
                {{ session('success') }}
            </div>
        @endif
        @if(session('error'))
            <div class="bg-rose-100 border-l-4 border-rose-500 text-rose-800 p-4 rounded text-sm font-semibold">
                {{ session('error') }}
            </div>
        @endif

        <div class="bg-white p-4 rounded-lg shadow-sm border border-gray-200">
            <form method="GET" action="{{ route('admin.users.index') }}" class="grid grid-cols-1 md:grid-cols-3 gap-3">
                <input type="text" name="search" value="{{ request('search') }}" placeholder="Cari nama, email, atau no HP..." class="border-gray-300 rounded text-sm w-full">
                <select name="role" class="border-gray-300 rounded text-sm w-full">
                    <option value="">-- Semua Role --</option>
                    <option value="admin" {{ request('role') == 'admin' ? 'selected' : '' }}>Administrator</option>
                    <option value="customer" {{ request('role') == 'customer' ? 'selected' : '' }}>Customer (Pembeli)</option>
                </select>
                <div class="flex gap-2">
                    <button type="submit" class="bg-gray-800 hover:bg-gray-900 text-white font-bold px-4 py-2 rounded text-sm">Filter</button>
                    <a href="{{ route('admin.users.index') }}" class="bg-gray-200 hover:bg-gray-300 text-gray-700 font-bold px-3 py-2 rounded text-sm">Reset</a>
                </div>
            </form>
        </div>

        <div class="bg-white rounded-lg shadow-sm border border-gray-200 overflow-x-auto">
            <table class="min-w-full divide-y divide-gray-200 text-sm">
                <thead class="bg-gray-50 text-xs uppercase text-gray-500">
                    <tr>
                        <th class="px-4 py-3 text-left">Nama Lengkap</th>
                        <th class="px-4 py-3 text-left">Email</th>
                        <th class="px-4 py-3 text-left">No HP</th>
                        <th class="px-4 py-3 text-left">Role</th>
                        <th class="px-4 py-3 text-center">Aksi</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-gray-200">
                    @forelse($users as $user)
                    <tr class="hover:bg-gray-50">
                        <td class="px-4 py-3 font-bold text-gray-900">{{ $user->name }}</td>
                        <td class="px-4 py-3 font-mono text-xs">{{ $user->email }}</td>
                        <td class="px-4 py-3 text-xs">{{ $user->phone ?? '-' }}</td>
                        <td class="px-4 py-3">
                            @if($user->role === 'admin')
                                <span class="bg-purple-100 text-purple-800 text-xs font-bold px-2.5 py-0.5 rounded">👑 Admin</span>
                            @else
                                <span class="bg-emerald-100 text-emerald-800 text-xs font-bold px-2.5 py-0.5 rounded">👤 Customer</span>
                            @endif
                        </td>
                        <td class="px-4 py-3 text-center space-x-2">
                            <a href="{{ route('admin.users.edit', $user->id) }}" class="text-indigo-600 hover:text-indigo-900 font-bold text-xs">Edit</a>
                            @if(Auth::id() !== $user->id)
                                <form action="{{ route('admin.users.destroy', $user->id) }}" method="POST" class="inline" onsubmit="return confirm('Hapus pengguna ini?')">
                                    @csrf
                                    @method('DELETE')
                                    <button type="submit" class="text-red-600 hover:text-red-900 font-bold text-xs ml-2">Hapus</button>
                                </form>
                            @endif
                        </td>
                    </tr>
                    @empty
                    <tr>
                        <td colspan="5" class="px-4 py-8 text-center text-gray-400">Tidak ada pengguna yang cocok.</td>
                    </tr>
                    @endforelse
                </tbody>
            </table>
            <div class="p-4">
                {{ $users->links() }}
            </div>
        </div>
    </div>
    $0
</x-app-layout>"""
)

add_snippet(
    "Blade View: Admin Form Tambah Pengguna Baru (create.blade.php)",
    "blade-user-create",
    "Serkom Blade: resources/views/admin/users/create.blade.php (Form tambah user admin/customer baru, password confirmation)",
    """<x-app-layout>
    <div class="py-6 max-w-2xl mx-auto px-4">
        <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
            <h2 class="text-xl font-bold text-gray-800 mb-4 border-b pb-2">➕ ${1:Tambah Pengguna Baru}</h2>

            @if($errors->any())
                <div class="bg-red-100 border-l-4 border-red-500 text-red-700 p-3 mb-4 rounded text-sm">
                    <ul class="list-disc list-inside">
                        @foreach($errors->all() as $error)
                            <li>{{ $error }}</li>
                        @endforeach
                    </ul>
                </div>
            @endif

            <form action="{{ route('admin.users.store') }}" method="POST" class="space-y-4">
                @csrf
                <div>
                    <label class="block text-sm font-semibold text-gray-700">Nama Lengkap</label>
                    <input type="text" name="name" value="{{ old('name') }}" required class="w-full border-gray-300 rounded text-sm">
                </div>

                <div>
                    <label class="block text-sm font-semibold text-gray-700">Alamat Email</label>
                    <input type="email" name="email" value="{{ old('email') }}" required class="w-full border-gray-300 rounded text-sm">
                </div>

                <div>
                    <label class="block text-sm font-semibold text-gray-700">Nomor Handphone (WhatsApp)</label>
                    <input type="text" name="phone" value="{{ old('phone') }}" class="w-full border-gray-300 rounded text-sm" placeholder="Contoh: 081234567890">
                </div>

                <div>
                    <label class="block text-sm font-semibold text-gray-700">Peran / Role</label>
                    <select name="role" required class="w-full border-gray-300 rounded text-sm">
                        <option value="customer" {{ old('role') == 'customer' ? 'selected' : '' }}>Customer (Pembeli)</option>
                        <option value="admin" {{ old('role') == 'admin' ? 'selected' : '' }}>Administrator (Panitia)</option>
                    </select>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-sm font-semibold text-gray-700">Password</label>
                        <input type="password" name="password" required class="w-full border-gray-300 rounded text-sm" placeholder="Minimal 6 karakter">
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-gray-700">Konfirmasi Password</label>
                        <input type="password" name="password_confirmation" required class="w-full border-gray-300 rounded text-sm" placeholder="Ulangi password">
                    </div>
                </div>

                <div class="flex justify-end space-x-2 pt-4 border-t">
                    <a href="{{ route('admin.users.index') }}" class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded text-sm">Batal</a>
                    <button type="submit" class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded text-sm">Simpan Pengguna</button>
                </div>
            </form>
        </div>
    </div>
    $0
</x-app-layout>"""
)

add_snippet(
    "Blade View: Admin Form Edit Pengguna (edit.blade.php)",
    "blade-user-edit",
    "Serkom Blade: resources/views/admin/users/edit.blade.php (Form edit user, ubah role, opsional ubah password, method PUT)",
    """<x-app-layout>
    <div class="py-6 max-w-2xl mx-auto px-4">
        <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
            <h2 class="text-xl font-bold text-gray-800 mb-4 border-b pb-2">✏️ ${1:Edit Data Pengguna}</h2>

            @if($errors->any())
                <div class="bg-red-100 border-l-4 border-red-500 text-red-700 p-3 mb-4 rounded text-sm">
                    <ul class="list-disc list-inside">
                        @foreach($errors->all() as $error)
                            <li>{{ $error }}</li>
                        @endforeach
                    </ul>
                </div>
            @endif

            <form action="{{ route('admin.users.update', $user->id) }}" method="POST" class="space-y-4">
                @csrf
                @method('PUT')

                <div>
                    <label class="block text-sm font-semibold text-gray-700">Nama Lengkap</label>
                    <input type="text" name="name" value="{{ old('name', $user->name) }}" required class="w-full border-gray-300 rounded text-sm">
                </div>

                <div>
                    <label class="block text-sm font-semibold text-gray-700">Alamat Email</label>
                    <input type="email" name="email" value="{{ old('email', $user->email) }}" required class="w-full border-gray-300 rounded text-sm">
                </div>

                <div>
                    <label class="block text-sm font-semibold text-gray-700">Nomor Handphone</label>
                    <input type="text" name="phone" value="{{ old('phone', $user->phone) }}" class="w-full border-gray-300 rounded text-sm">
                </div>

                <div>
                    <label class="block text-sm font-semibold text-gray-700">Peran / Role</label>
                    <select name="role" required class="w-full border-gray-300 rounded text-sm">
                        <option value="customer" {{ old('role', $user->role) == 'customer' ? 'selected' : '' }}>Customer (Pembeli)</option>
                        <option value="admin" {{ old('role', $user->role) == 'admin' ? 'selected' : '' }}>Administrator (Panitia)</option>
                    </select>
                </div>

                <div class="p-4 bg-gray-50 rounded border">
                    <p class="text-xs text-gray-500 mb-3 font-semibold">Kosongkan kolom password jika tidak ingin mengubah password lama.</p>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div>
                            <label class="block text-xs font-semibold text-gray-700">Password Baru</label>
                            <input type="password" name="password" class="w-full border-gray-300 rounded text-sm" placeholder="Minimal 6 karakter">
                        </div>
                        <div>
                            <label class="block text-xs font-semibold text-gray-700">Ulangi Password Baru</label>
                            <input type="password" name="password_confirmation" class="w-full border-gray-300 rounded text-sm" placeholder="Ulangi password">
                        </div>
                    </div>
                </div>

                <div class="flex justify-end space-x-2 pt-4 border-t">
                    <a href="{{ route('admin.users.index') }}" class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded text-sm">Batal</a>
                    <button type="submit" class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded text-sm">Simpan Perubahan</button>
                </div>
            </form>
        </div>
    </div>
    $0
</x-app-layout>"""
)

add_snippet(
    "Blade View: Admin Dashboard Rekap Laporan Pesanan Masuk (index.blade.php)",
    "blade-admin-dashboard-rekap",
    "Serkom Blade: resources/views/admin/orders/index.blade.php (Dashboard rekap 4 kartu statistik omset/tiket/order, filter tanggal & status, ubah status realtime)",
    """<x-app-layout>
    <div class="py-6 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6">
        <!-- 1. Header & Tombol Cetak -->
        <div class="flex justify-between items-center">
            <div>
                <h2 class="text-2xl font-bold text-gray-800">📊 ${1:Rekap Laporan Pesanan Masuk}</h2>
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
    $0
</x-app-layout>"""
)

add_snippet(
    "Blade View: Admin Cetak Rekapitulasi PDF (print.blade.php)",
    "blade-admin-orders-print",
    "Serkom Blade: resources/views/admin/orders/print.blade.php (Cetak rekapitulasi penjualan tiket siap PDF / print window.print())",
    """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>${1:Laporan Rekapitulasi Penjualan Tiket Konser}</title>
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
    $0
</body>
</html>"""
)

add_snippet(
    "Blade View: Customer Katalog Konser Musik (concerts.blade.php)",
    "blade-customer-catalog",
    "Serkom Blade: resources/views/customer/concerts.blade.php (Katalog konser grid cards, poster, artis, venue, tanggal, harga, tombol pesan)",
    """<x-app-layout>
    <div class="py-8 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-8">
            <h1 class="text-3xl font-extrabold text-gray-900">🎵 ${1:Jadwal Konser Musik & Tiket Resmi}</h1>
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
    $0
</x-app-layout>"""
)

add_snippet(
    "Blade View: Customer Form Pemesanan Tiket (booking-form.blade.php)",
    "blade-customer-booking",
    "Serkom Blade: resources/views/customer/booking-form.blade.php (Form booking tiket konser, kalkulasi total otomatis via JS, max qty)",
    """<x-app-layout>
    <div class="py-8 max-w-2xl mx-auto px-4">
        <div class="bg-white p-6 rounded-xl shadow-md border border-gray-200">
            <h2 class="text-xl font-bold text-gray-900 mb-4 border-b pb-2">🎟️ ${1:Konfirmasi Pemesanan Tiket}</h2>

            @if(session('error'))
                <div class="bg-red-100 border-l-4 border-red-500 text-red-700 p-4 mb-4 rounded text-sm">
                    {{ session('error') }}
                </div>
            @endif

            @if($errors->any())
                <div class="bg-red-100 border-l-4 border-red-500 text-red-700 p-3 mb-4 rounded text-sm">
                    <ul class="list-disc list-inside">
                        @foreach($errors->all() as $error)
                            <li>{{ $error }}</li>
                        @endforeach
                    </ul>
                </div>
            @endif

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
    $0
</x-app-layout>"""
)

add_snippet(
    "Blade View: Customer Riwayat Pemesanan (my-tickets.blade.php)",
    "blade-customer-my-tickets",
    "Serkom Blade: resources/views/customer/my-tickets.blade.php (Tabel riwayat tiket customer, status badge, tombol cetak e-tiket)",
    """<x-app-layout>
    <div class="py-8 max-w-6xl mx-auto px-4">
        <h2 class="text-2xl font-bold text-gray-900 mb-4">🎫 ${1:Riwayat Tiket Konser Saya}</h2>

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
    $0
</x-app-layout>"""
)

add_snippet(
    "Blade View: Customer Layout E-Tiket Digital (e-ticket.blade.php)",
    "blade-customer-e-ticket",
    "Serkom Blade: resources/views/customer/e-ticket.blade.php (Desain E-Tiket boarding pass resmi, barcode, data konser & pemesan, tombol print)",
    """<!DOCTYPE html>
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
            <h1>${1:OFFICIAL CONCERT PASS (E-TIKET)}</h1>
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
    $0
</body>
</html>"""
)

# ==========================================
# 8. BLADE VIEWS - MAKANAN & RESTORAN (6 snippets)
# ==========================================

add_snippet(
    "Blade View: Admin Daftar Menu Makanan (index.blade.php)",
    "blade-food-index",
    "Serkom Blade: resources/views/admin/foods/index.blade.php (Tabel menu makanan, foto menu, badge kategori makanan/minuman/cemilan, harga, edit & delete)",
    """<x-app-layout>
    <div class="py-6 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center mb-6">
            <div>
                <h2 class="text-2xl font-bold text-gray-800">🍔 ${1:Master Menu Restoran}</h2>
                <p class="text-sm text-gray-500">Kelola daftar menu makanan, minuman, harga, dan foto menu.</p>
            </div>
            <a href="{{ route('admin.foods.create') }}" class="bg-orange-600 hover:bg-orange-700 text-white font-bold py-2 px-4 rounded shadow text-sm">
                + Tambah Menu Baru
            </a>
        </div>

        @if(session('success'))
            <div class="bg-green-100 border-l-4 border-green-500 text-green-700 p-4 mb-4 rounded shadow-sm text-sm">
                {{ session('success') }}
            </div>
        @endif

        <div class="bg-white overflow-hidden shadow-sm sm:rounded-lg border border-gray-200">
            <table class="min-w-full divide-y divide-gray-200 text-sm">
                <thead class="bg-gray-50">
                    <tr>
                        <th class="px-4 py-3 text-left font-bold text-gray-700">Foto</th>
                        <th class="px-4 py-3 text-left font-bold text-gray-700">Nama Menu</th>
                        <th class="px-4 py-3 text-left font-bold text-gray-700">Kategori</th>
                        <th class="px-4 py-3 text-left font-bold text-gray-700">Harga</th>
                        <th class="px-4 py-3 text-center font-bold text-gray-700">Aksi</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-gray-200">
                    @forelse($foods as $food)
                    <tr class="hover:bg-gray-50">
                        <td class="px-4 py-3">
                            @if($food->image)
                                <img src="{{ asset('storage/' . $food->image) }}" class="w-14 h-14 object-cover rounded shadow" alt="Foto">
                            @else
                                <div class="w-14 h-14 bg-gray-200 flex items-center justify-center text-xs text-gray-500 rounded">No Pic</div>
                            @endif
                        </td>
                        <td class="px-4 py-3">
                            <span class="font-bold text-gray-900 block">{{ $food->name }}</span>
                            <span class="text-xs text-gray-500">{{ Str::limit($food->description, 50) }}</span>
                        </td>
                        <td class="px-4 py-3">
                            <span class="px-2 py-0.5 text-xs font-bold rounded {{ $food->category == 'Makanan' ? 'bg-orange-100 text-orange-800' : ($food->category == 'Minuman' ? 'bg-blue-100 text-blue-800' : 'bg-yellow-100 text-yellow-800') }}">
                                {{ $food->category }}
                            </span>
                        </td>
                        <td class="px-4 py-3 font-bold text-gray-900">
                            Rp {{ number_format($food->price, 0, ',', '.') }}
                        </td>
                        <td class="px-4 py-3 text-center space-x-2">
                            <a href="{{ route('admin.foods.edit', $food->id) }}" class="text-indigo-600 hover:text-indigo-900 font-bold text-xs">Edit</a>
                            <form action="{{ route('admin.foods.destroy', $food->id) }}" method="POST" class="inline" onsubmit="return confirm('Hapus menu ini?')">
                                @csrf
                                @method('DELETE')
                                <button type="submit" class="text-red-600 hover:text-red-900 font-bold text-xs ml-2">Hapus</button>
                            </form>
                        </td>
                    </tr>
                    @empty
                    <tr>
                        <td colspan="5" class="px-4 py-8 text-center text-gray-400">Belum ada menu yang didaftarkan.</td>
                    </tr>
                    @endforelse
                </tbody>
            </table>
            <div class="p-4">
                {{ $foods->links() }}
            </div>
        </div>
    </div>
    $0
</x-app-layout>"""
)

add_snippet(
    "Blade View: Admin Form Tambah Menu Makanan (create.blade.php)",
    "blade-food-create",
    "Serkom Blade: resources/views/admin/foods/create.blade.php (Form tambah menu makanan, upload gambar makanan, pilih kategori)",
    """<x-app-layout>
    <div class="py-6 max-w-2xl mx-auto px-4">
        <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
            <h2 class="text-xl font-bold text-gray-800 mb-4 border-b pb-2">➕ ${1:Tambah Menu Restoran Baru}</h2>

            @if($errors->any())
                <div class="bg-red-100 border-l-4 border-red-500 text-red-700 p-3 mb-4 rounded text-sm">
                    <ul class="list-disc list-inside">
                        @foreach($errors->all() as $error)
                            <li>{{ $error }}</li>
                        @endforeach
                    </ul>
                </div>
            @endif

            <form action="{{ route('admin.foods.store') }}" method="POST" enctype="multipart/form-data" class="space-y-4">
                @csrf
                <div>
                    <label class="block text-sm font-semibold text-gray-700">Nama Menu</label>
                    <input type="text" name="name" value="{{ old('name') }}" required class="w-full border-gray-300 rounded text-sm" placeholder="Contoh: Nasi Goreng Spesial">
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-sm font-semibold text-gray-700">Kategori</label>
                        <select name="category" required class="w-full border-gray-300 rounded text-sm">
                            <option value="Makanan" {{ old('category') == 'Makanan' ? 'selected' : '' }}>Makanan</option>
                            <option value="Minuman" {{ old('category') == 'Minuman' ? 'selected' : '' }}>Minuman</option>
                            <option value="Cemilan" {{ old('category') == 'Cemilan' ? 'selected' : '' }}>Cemilan</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-gray-700">Harga (Rp)</label>
                        <input type="number" name="price" value="{{ old('price') }}" required min="0" class="w-full border-gray-300 rounded text-sm" placeholder="Contoh: 25000">
                    </div>
                </div>

                <div>
                    <label class="block text-sm font-semibold text-gray-700">Foto Menu</label>
                    <input type="file" name="image" accept="image/*" class="w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded file:border-0 file:text-sm file:font-semibold file:bg-orange-50 file:text-orange-700 hover:file:bg-orange-100">
                </div>

                <div>
                    <label class="block text-sm font-semibold text-gray-700">Deskripsi Menu</label>
                    <textarea name="description" rows="3" required class="w-full border-gray-300 rounded text-sm" placeholder="Jelaskan bahan, porsi, atau rasa menu...">{{ old('description') }}</textarea>
                </div>

                <div class="flex justify-end space-x-2 pt-4 border-t">
                    <a href="{{ route('admin.foods.index') }}" class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded text-sm">Batal</a>
                    <button type="submit" class="bg-orange-600 hover:bg-orange-700 text-white font-bold py-2 px-4 rounded text-sm">Simpan Menu</button>
                </div>
            </form>
        </div>
    </div>
    $0
</x-app-layout>"""
)

add_snippet(
    "Blade View: Admin Form Edit Menu Makanan (edit.blade.php)",
    "blade-food-edit",
    "Serkom Blade: resources/views/admin/foods/edit.blade.php (Form edit menu makanan, preview foto lama, ganti foto, method PUT)",
    """<x-app-layout>
    <div class="py-6 max-w-2xl mx-auto px-4">
        <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
            <h2 class="text-xl font-bold text-gray-800 mb-4 border-b pb-2">✏️ ${1:Edit Menu Makanan}</h2>

            @if($errors->any())
                <div class="bg-red-100 border-l-4 border-red-500 text-red-700 p-3 mb-4 rounded text-sm">
                    <ul class="list-disc list-inside">
                        @foreach($errors->all() as $error)
                            <li>{{ $error }}</li>
                        @endforeach
                    </ul>
                </div>
            @endif

            <form action="{{ route('admin.foods.update', $food->id) }}" method="POST" enctype="multipart/form-data" class="space-y-4">
                @csrf
                @method('PUT')

                <div>
                    <label class="block text-sm font-semibold text-gray-700">Nama Menu</label>
                    <input type="text" name="name" value="{{ old('name', $food->name) }}" required class="w-full border-gray-300 rounded text-sm">
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-sm font-semibold text-gray-700">Kategori</label>
                        <select name="category" required class="w-full border-gray-300 rounded text-sm">
                            <option value="Makanan" {{ old('category', $food->category) == 'Makanan' ? 'selected' : '' }}>Makanan</option>
                            <option value="Minuman" {{ old('category', $food->category) == 'Minuman' ? 'selected' : '' }}>Minuman</option>
                            <option value="Cemilan" {{ old('category', $food->category) == 'Cemilan' ? 'selected' : '' }}>Cemilan</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-gray-700">Harga (Rp)</label>
                        <input type="number" name="price" value="{{ old('price', $food->price) }}" required min="0" class="w-full border-gray-300 rounded text-sm">
                    </div>
                </div>

                <div>
                    <label class="block text-sm font-semibold text-gray-700">Ganti Foto Menu (Opsional)</label>
                    @if($food->image)
                        <div class="mb-2">
                            <img src="{{ asset('storage/' . $food->image) }}" class="w-20 h-20 object-cover rounded shadow" alt="Foto">
                        </div>
                    @endif
                    <input type="file" name="image" accept="image/*" class="w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded file:border-0 file:text-sm file:font-semibold file:bg-orange-50 file:text-orange-700 hover:file:bg-orange-100">
                </div>

                <div>
                    <label class="block text-sm font-semibold text-gray-700">Deskripsi Menu</label>
                    <textarea name="description" rows="3" required class="w-full border-gray-300 rounded text-sm">{{ old('description', $food->description) }}</textarea>
                </div>

                <div class="flex justify-end space-x-2 pt-4 border-t">
                    <a href="{{ route('admin.foods.index') }}" class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded text-sm">Batal</a>
                    <button type="submit" class="bg-orange-600 hover:bg-orange-700 text-white font-bold py-2 px-4 rounded text-sm">Simpan Perubahan</button>
                </div>
            </form>
        </div>
    </div>
    $0
</x-app-layout>"""
)

add_snippet(
    "Blade View: Admin Dashboard Rekap Pesanan Meja Resto (resto-orders/index.blade.php)",
    "blade-resto-orders-index",
    "Serkom Blade: resources/views/admin/resto-orders/index.blade.php (Dashboard pesanan restoran per nomor meja, rincian menu, ubah status pesanan)",
    """<x-app-layout>
    <div class="py-6 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6">
        <div>
            <h2 class="text-2xl font-bold text-gray-800">📊 ${1:Rekap Pesanan Restoran Per Meja}</h2>
            <p class="text-sm text-gray-500">Monitor pesanan makanan dari pelanggan secara real-time.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
            <div class="bg-white p-5 rounded-lg border border-l-4 border-l-green-500 shadow-sm">
                <span class="text-xs font-bold text-gray-400 uppercase">Omset Selesai</span>
                <p class="text-2xl font-extrabold text-green-600 mt-1">Rp {{ number_format($totalRevenue, 0, ',', '.') }}</p>
            </div>
            <div class="bg-white p-5 rounded-lg border border-l-4 border-l-yellow-500 shadow-sm">
                <span class="text-xs font-bold text-gray-400 uppercase">Pesanan Menunggu</span>
                <p class="text-2xl font-extrabold text-yellow-600 mt-1">{{ $pendingOrders }} meja</p>
            </div>
            <div class="bg-white p-5 rounded-lg border border-l-4 border-l-blue-500 shadow-sm">
                <span class="text-xs font-bold text-gray-400 uppercase">Sedang Dimasak</span>
                <p class="text-2xl font-extrabold text-blue-600 mt-1">{{ $cookingOrders }} meja</p>
            </div>
            <div class="bg-white p-5 rounded-lg border border-l-4 border-l-emerald-500 shadow-sm">
                <span class="text-xs font-bold text-gray-400 uppercase">Pesanan Selesai</span>
                <p class="text-2xl font-extrabold text-emerald-600 mt-1">{{ $completedOrders }} meja</p>
            </div>
        </div>

        @if(session('success'))
            <div class="bg-green-100 border-l-4 border-green-500 text-green-700 p-4 rounded text-sm">
                {{ session('success') }}
            </div>
        @endif

        <div class="bg-white overflow-hidden shadow-sm rounded-lg border border-gray-200">
            <table class="min-w-full divide-y divide-gray-200 text-sm">
                <thead class="bg-gray-50 text-xs uppercase text-gray-600">
                    <tr>
                        <th class="px-4 py-3 text-left">Kode Order</th>
                        <th class="px-4 py-3 text-left">Meja & Pemesan</th>
                        <th class="px-4 py-3 text-left">Menu Dipesan</th>
                        <th class="px-4 py-3 text-left">Total</th>
                        <th class="px-4 py-3 text-left">Status</th>
                        <th class="px-4 py-3 text-center">Ubah Status</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-gray-200">
                    @forelse($orders as $order)
                    <tr class="hover:bg-gray-50">
                        <td class="px-4 py-3 font-mono font-bold text-orange-600">{{ $order->order_code }}</td>
                        <td class="px-4 py-3">
                            <span class="font-bold text-gray-900 block">Meja {{ $order->table_number }}</span>
                            <span class="text-xs text-gray-500">{{ $order->customer_name }}</span>
                        </td>
                        <td class="px-4 py-3 text-xs">
                            @foreach($order->orderDetails as $d)
                                <div>• {{ $d->food->name ?? 'Menu' }} x{{ $d->quantity }} (Rp {{ number_format($d->subtotal) }})</div>
                                @if($d->notes)
                                    <div class="text-gray-400 italic text-[11px]">Catatan: {{ $d->notes }}</div>
                                @endif
                            @endforeach
                        </td>
                        <td class="px-4 py-3 font-bold text-green-600">Rp {{ number_format($order->total_price) }}</td>
                        <td class="px-4 py-3">
                            <span class="px-2 py-0.5 text-xs font-bold rounded {{ $order->status == 'completed' ? 'bg-green-100 text-green-800' : ($order->status == 'cooking' ? 'bg-blue-100 text-blue-800' : ($order->status == 'pending' ? 'bg-yellow-100 text-yellow-800' : 'bg-red-100 text-red-800')) }}">
                                {{ strtoupper($order->status) }}
                            </span>
                        </td>
                        <td class="px-4 py-3 text-center">
                            <form action="{{ route('admin.resto.orders.updateStatus', $order->id) }}" method="POST">
                                @csrf
                                @method('PATCH')
                                <select name="status" onchange="this.form.submit()" class="text-xs border-gray-300 rounded font-semibold p-1">
                                    <option value="pending" {{ $order->status == 'pending' ? 'selected' : '' }}>Pending</option>
                                    <option value="cooking" {{ $order->status == 'cooking' ? 'selected' : '' }}>Cooking</option>
                                    <option value="completed" {{ $order->status == 'completed' ? 'selected' : '' }}>Completed</option>
                                    <option value="cancelled" {{ $order->status == 'cancelled' ? 'selected' : '' }}>Cancelled</option>
                                </select>
                            </form>
                        </td>
                    </tr>
                    @empty
                    <tr>
                        <td colspan="6" class="px-4 py-8 text-center text-gray-400">Belum ada pesanan makanan.</td>
                    </tr>
                    @endforelse
                </tbody>
            </table>
            <div class="p-4">
                {{ $orders->links() }}
            </div>
        </div>
    </div>
    $0
</x-app-layout>"""
)

add_snippet(
    "Blade View: Customer Menu Restoran Publik (menu.blade.php)",
    "blade-resto-menu-catalog",
    "Serkom Blade: resources/views/customer/menu.blade.php (Katalog menu makanan restoran untuk customer, kartu menu, harga, tombol pesan)",
    """<x-app-layout>
    <div class="py-8 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-8">
            <h1 class="text-3xl font-extrabold text-gray-900">🍽️ ${1:Daftar Menu Lezat Restoran}</h1>
            <p class="text-gray-600 mt-2">Pilih menu favoritmu dan pesan langsung dari mejamu tanpa antre.</p>
        </div>

        @if(session('success'))
            <div class="bg-green-100 border-l-4 border-green-500 text-green-700 p-4 mb-6 rounded">
                {{ session('success') }}
            </div>
        @endif

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            @forelse($foods as $food)
            <div class="bg-white rounded-xl shadow-md overflow-hidden border border-gray-100 hover:shadow-lg transition">
                @if($food->image)
                    <img src="{{ asset('storage/' . $food->image) }}" class="h-44 w-full object-cover" alt="Foto">
                @else
                    <div class="h-44 bg-gradient-to-r from-orange-400 to-amber-500 flex items-center justify-center text-white font-bold text-lg">
                        {{ $food->name }}
                    </div>
                @endif
                <div class="p-5">
                    <div class="flex justify-between items-center mb-2">
                        <span class="text-xs font-bold px-2 py-0.5 rounded bg-orange-100 text-orange-800">
                            {{ $food->category }}
                        </span>
                    </div>
                    <h3 class="text-lg font-bold text-gray-900 leading-snug">{{ $food->name }}</h3>
                    <p class="text-xs text-gray-500 mt-2">{{ $food->description }}</p>
                    
                    <div class="mt-4 pt-3 border-t flex justify-between items-center">
                        <span class="text-lg font-extrabold text-orange-600">Rp {{ number_format($food->price, 0, ',', '.') }}</span>
                        <a href="{{ route('customer.order', $food->id) }}" class="bg-orange-600 hover:bg-orange-700 text-white font-bold py-2 px-4 rounded text-xs shadow">
                            Pesan Sekarang
                        </a>
                    </div>
                </div>
            </div>
            @empty
            <div class="col-span-3 text-center py-12 text-gray-400">
                Belum ada menu makanan yang tersedia.
            </div>
            @endforelse
        </div>
    </div>
    $0
</x-app-layout>"""
)

add_snippet(
    "Blade View: Customer Form Checkout Pesanan Resto (resto-checkout.blade.php)",
    "blade-resto-checkout",
    "Serkom Blade: resources/views/customer/resto-checkout.blade.php (Form checkout pemesanan meja resto, input nomor meja, catatan porsi)",
    """<x-app-layout>
    <div class="py-8 max-w-xl mx-auto px-4">
        <div class="bg-white p-6 rounded-xl shadow-md border border-gray-200">
            <h2 class="text-xl font-bold text-gray-900 mb-4 border-b pb-2">🍽️ ${1:Konfirmasi Pesanan Makanan}</h2>

            @if(session('error'))
                <div class="bg-red-100 border-l-4 border-red-500 text-red-700 p-4 mb-4 rounded text-sm">
                    {{ session('error') }}
                </div>
            @endif

            @if($errors->any())
                <div class="bg-red-100 border-l-4 border-red-500 text-red-700 p-3 mb-4 rounded text-sm">
                    <ul class="list-disc list-inside">
                        @foreach($errors->all() as $error)
                            <li>{{ $error }}</li>
                        @endforeach
                    </ul>
                </div>
            @endif

            <div class="bg-orange-50 p-4 rounded-lg mb-6 flex items-center gap-4">
                @if($food->image)
                    <img src="{{ asset('storage/' . $food->image) }}" class="w-16 h-16 object-cover rounded shadow">
                @endif
                <div>
                    <h3 class="font-bold text-orange-900 text-base">{{ $food->name }}</h3>
                    <span class="text-xs text-orange-700 font-semibold">{{ $food->category }}</span>
                    <p class="text-sm font-bold text-orange-800 mt-1">Rp {{ number_format($food->price) }} / porsi</p>
                </div>
            </div>

            <form action="{{ route('customer.checkout') }}" method="POST">
                @csrf
                <input type="hidden" name="food_id" value="{{ $food->id }}">

                <div class="mb-4">
                    <label class="block text-sm font-semibold text-gray-700 mb-1">Nomor Meja Anda</label>
                    <input type="text" name="table_number" required class="w-full border-gray-300 rounded text-sm" placeholder="Contoh: 05, A2, VIP-1">
                </div>

                <div class="mb-4">
                    <label class="block text-sm font-semibold text-gray-700 mb-1">Jumlah Porsi</label>
                    <input type="number" name="quantity" value="1" min="1" max="20" required class="w-full border-gray-300 rounded text-sm">
                </div>

                <div class="mb-6">
                    <label class="block text-sm font-semibold text-gray-700 mb-1">Catatan Khusus (Opsional)</label>
                    <textarea name="notes" rows="2" class="w-full border-gray-300 rounded text-sm" placeholder="Contoh: Jangan terlalu pedas, kuah dipisah..."></textarea>
                </div>

                <div class="flex space-x-2">
                    <a href="{{ route('menu.index') }}" class="w-1/3 bg-gray-200 hover:bg-gray-300 text-gray-800 text-center font-bold py-2.5 rounded text-sm">Batal</a>
                    <button type="submit" class="w-2/3 bg-orange-600 hover:bg-orange-700 text-white font-bold py-2.5 rounded text-sm shadow">Kirim Pesanan ke Dapur</button>
                </div>
            </form>
        </div>
    </div>
    $0
</x-app-layout>"""
)

# ==========================================
# 9. MASTER LAYOUT & FLASH MESSAGES (2 snippets)
# ==========================================

add_snippet(
    "Blade Layout: Master Layout Mandiri (Tailwind CDN + Navbar + Slot)",
    "blade-master-layout",
    "Serkom Blade: resources/views/layouts/app.blade.php atau master.blade.php (Master layout mandiri lengkap Tailwind CDN + Navbar + Flash Alerts + Slot)",
    """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ $title ?? '${1:Aplikasi Ujian Serkom}' }}</title>
    <!-- Tailwind CSS CDN (Instant Setup tanpa npm) -->
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 font-sans antialiased text-gray-900">
    <!-- Navbar Header -->
    <nav class="bg-white border-b border-gray-200 shadow-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-16 items-center">
                <div class="flex items-center space-x-4">
                    <a href="/" class="text-xl font-extrabold text-indigo-600 tracking-wider">
                        🎫 ${2:TIKET KONSER SERKOM}
                    </a>
                    <a href="/" class="text-sm font-semibold text-gray-600 hover:text-indigo-600">Katalog</a>
                    @auth
                        @if(Auth::user()->role === 'admin')
                            <a href="{{ route('admin.orders.index') }}" class="text-sm font-semibold text-indigo-600 hover:underline">Dashboard Rekap</a>
                            <a href="{{ route('admin.tickets.index') }}" class="text-sm font-semibold text-gray-600 hover:text-indigo-600">Master Tiket</a>
                            <a href="{{ route('admin.users.index') }}" class="text-sm font-semibold text-gray-600 hover:text-indigo-600">Master User</a>
                        @else
                            <a href="{{ route('customer.myTickets') }}" class="text-sm font-semibold text-indigo-600 hover:underline">Tiket Saya</a>
                        @endif
                    @endauth
                </div>

                <div class="flex items-center space-x-3">
                    @auth
                        <span class="text-xs font-bold text-gray-700">{{ Auth::user()->name }} ({{ strtoupper(Auth::user()->role) }})</span>
                        <form method="POST" action="{{ route('logout') }}" class="inline">
                            @csrf
                            <button type="submit" class="text-xs bg-red-500 hover:bg-red-600 text-white font-bold py-1.5 px-3 rounded">
                                Logout
                            </button>
                        </form>
                    @else
                        <a href="{{ route('login') }}" class="text-xs font-bold text-indigo-600 hover:underline">Login</a>
                        <a href="{{ route('register') }}" class="text-xs bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-1.5 px-3 rounded">Register</a>
                    @endauth
                </div>
            </div>
        </div>
    </nav>

    <!-- Global Flash Alerts Container -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-4">
        @if(session('success'))
            <div class="bg-green-100 border-l-4 border-green-500 text-green-700 p-4 mb-4 rounded shadow-sm text-sm">
                {{ session('success') }}
            </div>
        @endif
        @if(session('error'))
            <div class="bg-red-100 border-l-4 border-red-500 text-red-700 p-4 mb-4 rounded shadow-sm text-sm">
                {{ session('error') }}
            </div>
        @endif
    </div>

    <!-- Content Slot -->
    <main>
        {{ $slot }}
    </main>
    $0
</body>
</html>"""
)

add_snippet(
    "Blade Component: Flash Messages Alert (Success, Error, Validation)",
    "blade-flash-messages",
    "Serkom Blade: resources/views/components/flash.blade.php (Komponen flash message alert: success, error, $errors->all())",
    """<div class="${1:mb-4}">
@if(session('success'))
    <div class="bg-green-100 border-l-4 border-green-500 text-green-700 p-4 mb-4 rounded shadow-sm text-sm">
        {{ session('success') }}
    </div>
@endif

@if(session('error'))
    <div class="bg-red-100 border-l-4 border-red-500 text-red-700 p-4 mb-4 rounded shadow-sm text-sm">
        {{ session('error') }}
    </div>
@endif

@if($errors->any())
    <div class="bg-red-100 border-l-4 border-red-500 text-red-700 p-3 mb-4 rounded text-sm">
        <ul class="list-disc list-inside">
            @foreach($errors->all() as $error)
                <li>{{ $error }}</li>
            @endforeach
        </ul>
    </div>
@endif
</div>
$0"""
)

# ==========================================
# 10. SQL QUERY CHEAT SHEET (3 snippets)
# ==========================================

add_snippet(
    "SQL Cheat: CRUD Lengkap Tabel Tickets Konser",
    "sql-crud-tickets",
    "Serkom SQL: Query SQL Lengkap CRUD Tabel Tickets Konser (INSERT, SELECT WHERE/ORDER, UPDATE harga/stok, DELETE)",
    """-- 1. CREATE (Insert Data Tiket Baru)
INSERT INTO tickets (concert_name, artist, venue, event_date, category, price, stock, poster, description, created_at, updated_at) 
VALUES ('${1:Coldplay: Music of the Spheres}', 'Coldplay', 'Stadion GBK Jakarta', '2026-11-15 19:30:00', 'VIP', ${2:3500000}, ${3:50}, NULL, 'Akses VIP Gate', NOW(), NOW());

-- 2. READ (Tampil Tiket yang Kuotanya Masih Tersedia Diurutkan dari yang Termurah)
SELECT id, concert_name, artist, category, price, stock 
FROM tickets 
WHERE stock > 0 
ORDER BY price ASC;

-- 3. UPDATE (Ubah Harga dan Tambah Kuota Tiket ID = 1)
UPDATE tickets 
SET price = ${4:3600000}, stock = stock + 20, updated_at = NOW() 
WHERE id = ${5:1};

-- 4. DELETE (Hapus Tiket Tertentu Berdasarkan ID)
DELETE FROM tickets 
WHERE id = ${6:1};
$0"""
)

add_snippet(
    "SQL Cheat: Agregasi Omset, COUNT, dan JOIN 3 Tabel (Laporan Serkom)",
    "sql-rekap-omset",
    "Serkom SQL: Query SQL Agregasi Omset & JOIN 3 Tabel orders-order_details-tickets & GROUP BY tiket terlaris",
    """-- 1. Query Agregasi Omset Pendapatan Lunas (Statistik Dashboard)
SELECT 
    SUM(total_price) AS total_pendapatan_bersih,
    COUNT(id) AS jumlah_transaksi_lunas
FROM orders 
WHERE status = '${1:paid}';

-- 2. Query JOIN 3 Tabel untuk Rekapitulasi Rincian Pesanan Masuk
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
WHERE o.order_date BETWEEN '${2:2026-10-01}' AND '${3:2026-10-31}'
ORDER BY o.created_at DESC;

-- 3. Query GROUP BY untuk Menganalisis Tiket Terlaris
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
$0"""
)

add_snippet(
    "SQL Cheat: CRUD & Laporan Restoran (Foods & Orders)",
    "sql-crud-foods",
    "Serkom SQL: Query SQL Lengkap CRUD Tabel Foods & Rekapitulasi Pesanan Restoran",
    """-- 1. INSERT Data Menu Makanan
INSERT INTO foods (name, category, price, description, created_at, updated_at)
VALUES ('${1:Nasi Goreng Spesial}', '${2:Makanan}', ${3:28000}, 'Nasi goreng suwir ayam dan telur', NOW(), NOW());

-- 2. READ Filter Menu Minuman
SELECT id, name, price, description 
FROM foods 
WHERE category = '${4:Minuman}' 
ORDER BY price ASC;

-- 3. Rekap Pesanan Resto per Meja (JOIN)
SELECT 
    o.order_code,
    o.table_number,
    f.name AS menu,
    od.quantity,
    od.subtotal,
    o.status
FROM orders o
INNER JOIN order_details od ON o.id = od.order_id
INNER JOIN foods f ON od.food_id = f.id
ORDER BY o.created_at DESC;
$0"""
)

# ==========================================
# 11. ARTISAN COMMANDS & CHECKLIST SETUP (2 snippets)
# ==========================================

add_snippet(
    "Terminal Command: Setup Kilat Laravel Ujian Serkom (H-1)",
    "artisan-serkom-setup",
    "Serkom Terminal: Urutan Perintah Eksekusi Setup Laravel H-1 (composer, env, key, migrate --seed, storage:link, npm build, serve)",
    """# 1. Masuk folder proyek & install dependensi
composer install

# 2. Setup file environment .env
copy .env.example .env
php artisan key:generate

# 3. Jalankan Migrasi & Seeder Database
php artisan migrate:fresh --seed

# 4. Buat Symbolic Link Storage (Agar upload foto poster tampil)
php artisan storage:link

# 5. Kompilasi Asset Frontend Vite (Tailwind CSS)
npm install
npm run build

# 6. Jalankan Server Lokal Laravel
php artisan serve
$0"""
)

add_snippet(
    "Terminal Command: Cheat Sheet Artisan Generator Lengkap",
    "artisan-commands",
    "Serkom Terminal: Kamus Perintah Artisan Cepat (make:model, make:controller, make:migration, route:list, optimize:clear)",
    """# Buat Migration
php artisan make:migration create_tickets_table
php artisan make:migration create_orders_table
php artisan make:migration create_order_details_table

# Buat Model
php artisan make:model Ticket
php artisan make:model Order
php artisan make:model OrderDetail

# Buat Controller Resource
php artisan make:controller Admin/TicketController --resource
php artisan make:controller Admin/UserController --resource
php artisan make:controller Admin/OrderReportController
php artisan make:controller Customer/BookingController

# Buat Middleware & Seeder
php artisan make:middleware IsAdmin
php artisan make:seeder TicketSeeder

# Perawatan & Cache Clear
php artisan route:list
php artisan storage:link
php artisan optimize:clear
$0"""
)

# ==========================================
# WRITE OUTPUT FILE
# ==========================================

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "serkom-laravel.code-snippets")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(snippets, f, indent=2, ensure_ascii=False)

print(f"Successfully generated {len(snippets)} snippets into: {output_path}")

# Validate JSON format
with open(output_path, "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(f"Validation OK: Loaded {len(loaded)} snippets successfully with 100% valid JSON!")
