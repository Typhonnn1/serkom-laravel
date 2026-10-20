# -*- coding: utf-8 -*-
"""
Full Generator for serkom_tiket_konser_lengkap.html
Comprehensive, standalone, interactive guide for Serkom Junior Web Developer
Covers all theoretical and practical requirements:
1. Login customer & admin (Multi-role Auth, Middleware, Seeder)
2. Relasi antar tabel (4-tabel migrations, Eloquent relations)
3. Rekap laporan pesanan masuk (Dashboard metrics, date/status filter, print report)
4. CRUD tiket konser & user (Full resource controllers, upload poster, user management)
Plus customer booking transaction (atomic DB::transaction, stock decrement, e-ticket).
"""

import os
import sys
import html
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import build_tiket_konser_html as btk

OUTPUT_FILE = r"c:\Users\Default User\Desktop\modul serkom\serkom_tiket_konser_lengkap.html"

def make_html():
    h = []

    # Head & CSS
    h.append("""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PANDUAN LENGKAP SERKOM H-1: APLIKASI PEMESANAN TIKET KONSER (LARAVEL & MYSQL)</title>
    <style>
        :root {
            --bg-primary: #0f172a;
            --bg-secondary: #1e293b;
            --bg-card: #ffffff;
            --text-main: #1e293b;
            --text-muted: #64748b;
            --border-color: #e2e8f0;
            --primary: #4f46e5;
            --primary-hover: #4338ca;
            --accent-green: #10b981;
            --accent-yellow: #f59e0b;
            --accent-red: #ef4444;
            --code-bg: #18181b;
            --code-inner: #1e1e1e;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background: #f8fafc;
            color: var(--text-main);
            line-height: 1.6;
            font-size: 13.5px;
        }

        /* Top Bar */
        .top-navbar {
            position: sticky;
            top: 0;
            z-index: 100;
            background: rgba(15, 23, 42, 0.96);
            backdrop-filter: blur(8px);
            border-bottom: 1px solid #334155;
            color: #fff;
            padding: 10px 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }

        .brand-box {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .brand-icon {
            font-size: 24px;
            background: #312e81;
            padding: 6px 10px;
            border-radius: 8px;
            border: 1px solid #4f46e5;
        }

        .brand-title {
            font-size: 15px;
            font-weight: 800;
            letter-spacing: 0.5px;
            color: #f8fafc;
        }

        .brand-subtitle {
            font-size: 11px;
            color: #94a3b8;
            font-weight: 500;
        }

        .nav-controls {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .search-box {
            position: relative;
        }

        .search-input {
            background: #1e293b;
            border: 1px solid #475569;
            color: #f1f5f9;
            padding: 7px 14px 7px 32px;
            border-radius: 6px;
            font-size: 12px;
            width: 240px;
            transition: all 0.2s;
        }

        .search-input:focus {
            outline: none;
            border-color: #6366f1;
            width: 280px;
            background: #0f172a;
        }

        .search-icon {
            position: absolute;
            left: 10px;
            top: 50%;
            transform: translateY(-50%);
            font-size: 12px;
            color: #94a3b8;
        }

        .btn-print {
            background: #4f46e5;
            color: #fff;
            border: none;
            padding: 7px 14px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 700;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
            transition: background 0.2s;
        }

        .btn-print:hover {
            background: #4338ca;
        }

        /* Tabs Navigation */
        .tabs-bar {
            background: #1e293b;
            border-bottom: 1px solid #334155;
            padding: 0 24px;
            display: flex;
            gap: 4px;
            overflow-x: auto;
            position: sticky;
            top: 57px;
            z-index: 90;
        }

        .tab-btn {
            background: transparent;
            border: none;
            color: #94a3b8;
            padding: 12px 18px;
            font-size: 12.5px;
            font-weight: 700;
            cursor: pointer;
            border-bottom: 3px solid transparent;
            transition: all 0.2s;
            white-space: nowrap;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .tab-btn:hover {
            color: #f8fafc;
            background: rgba(255,255,255,0.03);
        }

        .tab-btn.active {
            color: #38bdf8;
            border-bottom-color: #38bdf8;
            background: rgba(56, 189, 248, 0.08);
        }

        /* Main Layout */
        .layout-container {
            display: flex;
            max-width: 1440px;
            margin: 0 auto;
            padding: 24px;
            gap: 24px;
        }

        /* Sidebar ToC */
        .sidebar {
            width: 280px;
            flex-shrink: 0;
            position: sticky;
            top: 115px;
            height: calc(100vh - 140px);
            overflow-y: auto;
            background: #fff;
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 16px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.03);
        }

        .sidebar h4 {
            font-size: 12px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.6px;
            color: #475569;
            margin-bottom: 12px;
            border-bottom: 2px solid #f1f5f9;
            padding-bottom: 6px;
        }

        .toc-list {
            list-style: none;
        }

        .toc-item {
            margin-bottom: 4px;
        }

        .toc-link {
            display: block;
            padding: 6px 10px;
            color: #334155;
            text-decoration: none;
            font-size: 12px;
            font-weight: 600;
            border-radius: 6px;
            transition: all 0.15s;
            line-height: 1.4;
        }

        .toc-link:hover {
            background: #f1f5f9;
            color: var(--primary);
            padding-left: 14px;
        }

        .toc-badge {
            font-size: 9.5px;
            font-weight: 700;
            padding: 2px 5px;
            border-radius: 4px;
            margin-left: 4px;
            text-transform: uppercase;
        }

        .badge-core { background: #e0e7ff; color: #4338ca; }
        .badge-theory { background: #fef3c7; color: #b45309; }
        .badge-code { background: #dcfce7; color: #15803d; }
        .badge-danger { background: #fee2e2; color: #b91c1c; }

        /* Content Area */
        .content-area {
            flex: 1;
            min-width: 0;
        }

        .tab-pane {
            display: none;
        }

        .tab-pane.active {
            display: block;
            animation: fadeIn 0.25s ease-in-out;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(6px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Banner Hero */
        .hero-banner {
            background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4338ca 100%);
            color: #fff;
            padding: 28px;
            border-radius: 12px;
            margin-bottom: 24px;
            box-shadow: 0 8px 20px -4px rgba(79, 70, 229, 0.3);
            border: 1px solid #4338ca;
            position: relative;
            overflow: hidden;
        }

        .hero-badge {
            display: inline-block;
            background: #fbbf24;
            color: #78350f;
            font-weight: 800;
            font-size: 11px;
            padding: 4px 10px;
            border-radius: 999px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 12px;
        }

        .hero-title {
            font-size: 23px;
            font-weight: 900;
            line-height: 1.3;
            margin-bottom: 8px;
        }

        .hero-desc {
            font-size: 13.5px;
            color: #e0e7ff;
            max-width: 860px;
            line-height: 1.6;
        }

        .hero-meta {
            display: flex;
            flex-wrap: wrap;
            gap: 16px;
            margin-top: 16px;
            padding-top: 16px;
            border-top: 1px solid rgba(255,255,255,0.15);
            font-size: 12px;
            color: #cbd5e1;
        }

        /* Sections */
        .section-card {
            background: #fff;
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.03);
            scroll-margin-top: 130px;
        }

        .section-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 2px solid #f1f5f9;
            padding-bottom: 12px;
            margin-bottom: 18px;
        }

        .section-title {
            font-size: 18px;
            font-weight: 800;
            color: #0f172a;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .step-pill {
            background: #4f46e5;
            color: #fff;
            font-size: 11px;
            padding: 3px 8px;
            border-radius: 6px;
            font-weight: 800;
        }

        .step-desc {
            font-size: 13.5px;
            color: #475569;
            margin-bottom: 16px;
            line-height: 1.6;
        }

        h3.sub-title {
            font-size: 15px;
            font-weight: 700;
            color: #1e293b;
            margin: 20px 0 10px 0;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        /* Callouts */
        .callout {
            border-left: 4px solid;
            padding: 14px 18px;
            border-radius: 0 8px 8px 0;
            margin: 16px 0;
            font-size: 13px;
        }

        .callout-info {
            background: #eff6ff;
            border-color: #3b82f6;
            color: #1e40af;
        }

        .callout-warning {
            background: #fffbeb;
            border-color: #f59e0b;
            color: #92400e;
        }

        .callout-success {
            background: #f0fdf4;
            border-color: #10b981;
            color: #065f46;
        }

        .callout-danger {
            background: #fef2f2;
            border-color: #ef4444;
            color: #991b1b;
        }

        .callout-title {
            font-weight: 800;
            margin-bottom: 4px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        /* Tables */
        .custom-table {
            width: 100%;
            border-collapse: collapse;
            margin: 14px 0 18px 0;
            font-size: 12.5px;
        }

        .custom-table th, .custom-table td {
            border: 1px solid #cbd5e1;
            padding: 8px 12px;
            text-align: left;
            vertical-align: top;
        }

        .custom-table th {
            background: #f8fafc;
            color: #1e293b;
            font-weight: 700;
        }

        .custom-table tr:hover td {
            background: #f8fafc;
        }

        /* Code Containers (VS Code Dark Theme) */
        .code-container {
            background: var(--code-bg);
            border-radius: 8px;
            margin: 14px 0 20px 0;
            border: 1px solid #27272a;
            box-shadow: 0 4px 14px rgba(0, 0, 0, 0.15);
            overflow: hidden;
        }

        .code-header {
            background: #27272a;
            padding: 7px 14px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #3f3f46;
            font-size: 12px;
        }

        .code-file-info {
            display: flex;
            align-items: center;
            gap: 8px;
            font-family: Consolas, "Fira Code", monospace;
            color: #e4e4e7;
        }

        .file-icon {
            font-size: 14px;
        }

        .file-path {
            font-weight: 700;
            color: #38bdf8;
        }

        .code-label {
            background: #3f3f46;
            color: #a1a1aa;
            font-size: 10px;
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: 700;
            text-transform: uppercase;
        }

        .code-actions {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .lang-badge {
            background: #18181b;
            color: #a1a1aa;
            font-size: 10px;
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: 700;
            border: 1px solid #3f3f46;
        }

        .copy-btn {
            background: #3f3f46;
            border: 1px solid #52525b;
            color: #e4e4e7;
            padding: 4px 10px;
            border-radius: 5px;
            font-size: 11.5px;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 5px;
            font-weight: 600;
            transition: all 0.15s;
        }

        .copy-btn:hover {
            background: #52525b;
            color: #fff;
        }

        .code-body {
            background: var(--code-inner);
            padding: 14px;
            overflow-x: auto;
            color: #d4d4d8;
            font-family: Consolas, "Fira Code", "Courier New", monospace;
            font-size: 12.2px;
            line-height: 1.5;
            white-space: pre;
        }

        /* Token Colors for VS Code Dark Theme */
        .tok-kw { color: #569cd6; font-weight: bold; }
        .tok-ctrl { color: #c586c0; font-weight: bold; }
        .tok-class { color: #4ec9b0; }
        .tok-fn { color: #dcdcaa; }
        .tok-var { color: #9cdcfe; }
        .tok-str { color: #ce9178; }
        .tok-num { color: #b5cea8; }
        .tok-cm { color: #6a9955; font-style: italic; }
        .tok-tag { color: #569cd6; }
        .tok-attr { color: #9cdcfe; }
        .tok-op { color: #d4d4d4; }
        .tok-punc { color: #d4d4d4; }

        .marker-tambahkan {
            background: rgba(16, 185, 129, 0.18);
            color: #34d399;
            font-weight: bold;
            border-left: 3px solid #10b981;
            padding: 1px 4px;
            border-radius: 2px;
        }
        .marker-ubah {
            background: rgba(56, 189, 248, 0.18);
            color: #38bdf8;
            font-weight: bold;
            border-left: 3px solid #38bdf8;
            padding: 1px 4px;
            border-radius: 2px;
        }
        .marker-wajib {
            background: rgba(248, 113, 113, 0.18);
            color: #f87171;
            font-weight: bold;
            border-left: 3px solid #f87171;
            padding: 1px 4px;
            border-radius: 2px;
        }
        .marker-kunci {
            background: rgba(250, 204, 21, 0.18);
            color: #facc15;
            font-weight: bold;
            border-left: 3px solid #facc15;
            padding: 1px 4px;
            border-radius: 2px;
        }

        /* ERD Visual Diagram */
        .erd-board {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 16px;
            margin: 18px 0;
            padding: 16px;
            background: #f1f5f9;
            border-radius: 10px;
            border: 1px dashed #cbd5e1;
        }

        .erd-table {
            background: #fff;
            border-radius: 8px;
            border: 1px solid #cbd5e1;
            overflow: hidden;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }

        .erd-header {
            background: #1e293b;
            color: #fff;
            padding: 8px 12px;
            font-size: 13px;
            font-weight: 800;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .erd-badge {
            font-size: 9.5px;
            background: #4f46e5;
            padding: 2px 6px;
            border-radius: 4px;
        }

        .erd-fields {
            list-style: none;
            padding: 8px 12px;
            font-size: 11.5px;
            font-family: Consolas, monospace;
        }

        .erd-field {
            display: flex;
            justify-content: space-between;
            padding: 3px 0;
            border-bottom: 1px solid #f8fafc;
        }

        .erd-field:last-child {
            border-bottom: none;
        }

        .field-pk { color: #dc2626; font-weight: bold; }
        .field-fk { color: #4f46e5; font-weight: bold; }
        .field-type { color: #64748b; font-size: 10.5px; }

        /* MVC Lifecycle Flow */
        .mvc-flow {
            display: flex;
            flex-direction: column;
            gap: 10px;
            margin: 18px 0;
        }

        .mvc-step {
            display: flex;
            align-items: center;
            gap: 14px;
            background: #fff;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 12px 16px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.02);
        }

        .step-circle {
            width: 32px;
            height: 32px;
            border-radius: 50%;
            background: #4f46e5;
            color: #fff;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 800;
            font-size: 13px;
            flex-shrink: 0;
        }

        .step-info h5 {
            font-size: 13.5px;
            font-weight: 800;
            color: #0f172a;
        }

        .step-info p {
            font-size: 12px;
            color: #64748b;
        }

        /* Interactive Checklist */
        .checklist-item {
            display: flex;
            align-items: flex-start;
            gap: 12px;
            padding: 10px 14px;
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            margin-bottom: 8px;
            transition: all 0.15s;
        }

        .checklist-item:hover {
            background: #f1f5f9;
        }

        .checklist-item input[type="checkbox"] {
            margin-top: 3px;
            width: 17px;
            height: 17px;
            accent-color: #4f46e5;
            cursor: pointer;
        }

        .checklist-text {
            font-size: 13px;
            font-weight: 600;
            color: #1e293b;
        }

        .checklist-sub {
            font-size: 11.5px;
            color: #64748b;
            font-weight: normal;
            margin-top: 2px;
        }

        /* Print styles */
        @media print {
            .top-navbar, .tabs-bar, .sidebar, .btn-print, .copy-btn {
                display: none !important;
            }
            .layout-container {
                display: block !important;
                padding: 0 !important;
            }
            .tab-pane {
                display: block !important;
                page-break-after: always;
            }
            .section-card {
                border: none !important;
                box-shadow: none !important;
                padding: 10px 0 !important;
                page-break-inside: avoid;
            }
            body {
                background: #fff !important;
                font-size: 11px !important;
            }
            .code-body {
                font-size: 10px !important;
            }
        }

        @media (max-width: 900px) {
            .sidebar { display: none; }
            .layout-container { padding: 12px; }
            .search-input { width: 160px; }
        }
    </style>
</head>
<body>

    <!-- TOP NAVBAR -->
    <header class="top-navbar">
        <div class="brand-box">
            <span class="brand-icon">🎟️</span>
            <div>
                <div class="brand-title">PANDUAN LENGKAP SERKOM BNSP (H-1)</div>
                <div class="brand-subtitle">Junior Web Developer: Aplikasi Pemesanan Tiket Konser & Makanan</div>
            </div>
        </div>
        <div class="nav-controls">
            <div class="search-box">
                <span class="search-icon">🔍</span>
                <input type="text" id="searchInput" class="search-input" placeholder="Cari materi / kode..." onkeyup="filterContent()">
            </div>
            <button class="btn-print" onclick="window.print()">
                <span>🖨️</span> Cetak / Simpan PDF
            </button>
        </div>
    </header>

    <!-- TABS BAR -->
    <nav class="tabs-bar">
        <button class="tab-btn active" onclick="switchTab('tab-tiket', this)">
            🎟️ Kasus Tiket Konser (Pra Serkom)
        </button>
        <button class="tab-btn" onclick="switchTab('tab-teori', this)">
            🧠 Teori & Wawancara Asesor
        </button>
        <button class="tab-btn" onclick="switchTab('tab-makanan', this)">
            🍽️ Kasus Referensi (Makanan/Resto)
        </button>
        <button class="tab-btn" onclick="switchTab('tab-checklist', this)">
            ⚡ Checklist 15 Menit Anti-Panik
        </button>
        <button class="tab-btn" onclick="switchTab('tab-grill', this)">
            🔥 Sesi Grill-Me Asesor (10 Q&A)
        </button>
        <button class="tab-btn" onclick="switchTab('tab-error', this)">
            🚨 Kamus Error & Solusi Kilat
        </button>
    </nav>

    <!-- MAIN LAYOUT -->
    <div class="layout-container">

        <!-- SIDEBAR TOC -->
        <aside class="sidebar">
            <h4>📑 DAFTAR ISI MATERI</h4>
            <ul class="toc-list" id="tocTiket">
                <li class="toc-item"><a href="#sec-tiket-praktek1" class="toc-link">1. Login & Multi-Role <span class="toc-badge badge-core">Auth</span></a></li>
                <li class="toc-item"><a href="#sec-tiket-praktek2" class="toc-link">2. Relasi 4 Tabel <span class="toc-badge badge-code">Schema</span></a></li>
                <li class="toc-item"><a href="#sec-tiket-praktek3" class="toc-link">3. CRUD Tiket Konser <span class="toc-badge badge-core">Admin</span></a></li>
                <li class="toc-item"><a href="#sec-tiket-praktek4" class="toc-link">4. CRUD Kelola User <span class="toc-badge badge-core">User</span></a></li>
                <li class="toc-item"><a href="#sec-tiket-praktek5" class="toc-link">5. Rekap Pesanan Masuk <span class="toc-badge badge-code">Dashboard</span></a></li>
                <li class="toc-item"><a href="#sec-tiket-praktek6" class="toc-link">6. Booking & E-Tiket <span class="toc-badge badge-core">Customer</span></a></li>
                <li class="toc-item"><a href="#sec-tiket-praktek7" class="toc-link">7. Routing Lengkap <span class="toc-badge badge-theory">Routes</span></a></li>
            </ul>
            <ul class="toc-list" id="tocTeori" style="display:none;">
                <li class="toc-item"><a href="#sec-teori-1" class="toc-link">1. Kebutuhan Aplikasi Tiket <span class="toc-badge badge-theory">Spesifikasi</span></a></li>
                <li class="toc-item"><a href="#sec-teori-2" class="toc-link">2. Fungsi ERD & SQL CRUD <span class="toc-badge badge-theory">Database</span></a></li>
                <li class="toc-item"><a href="#sec-teori-3" class="toc-link">3. Apa Itu Query & Contoh <span class="toc-badge badge-theory">Query</span></a></li>
                <li class="toc-item"><a href="#sec-teori-4" class="toc-link">4. Arsitektur MVC Laravel <span class="toc-badge badge-theory">Arsitektur</span></a></li>
                <li class="toc-item"><a href="#sec-teori-5" class="toc-link">5. Tools & Stack Teknologi <span class="toc-badge badge-theory">Tools</span></a></li>
            </ul>
            <ul class="toc-list" id="tocMakanan" style="display:none;">
                <li class="toc-item"><a href="#sec-resto-perbandingan" class="toc-link">1. Perbandingan Logika <span class="toc-badge badge-theory">Konsep</span></a></li>
                <li class="toc-item"><a href="#sec-resto-skema" class="toc-link">2. Skema 3 Tabel Resto <span class="toc-badge badge-code">Migration</span></a></li>
                <li class="toc-item"><a href="#sec-resto-crud" class="toc-link">3. CRUD Menu Makanan <span class="toc-badge badge-core">Admin</span></a></li>
            </ul>
            <ul class="toc-list" id="tocChecklist" style="display:none;">
                <li class="toc-item"><a href="#checklistContainer" class="toc-link">⚡ Checklist 15 Menit <span class="toc-badge badge-core">Aksi</span></a></li>
            </ul>
            <ul class="toc-list" id="tocGrill" style="display:none;">
                <li class="toc-item"><a href="#sec-grill-box" class="toc-link">🔥 10 Tanya Jawab Emas <span class="toc-badge badge-theory">Wawancara</span></a></li>
            </ul>
            <ul class="toc-list" id="tocError" style="display:none;">
                <li class="toc-item"><a href="#sec-error-box" class="toc-link">🚨 Kamus Error 10 Detik <span class="toc-badge badge-danger">Troubleshoot</span></a></li>
            </ul>
        </aside>

        <!-- CONTENT AREA -->
        <main class="content-area">
""")
    # TAB 1: KASUS TIKET KONSER (PRA SERKOM - UTAMA)
    h.append("""
        <!-- TAB 1: KASUS TIKET KONSER (UTAMA) -->
        <div id="tab-tiket" class="tab-pane active">
            <div class="hero-banner">
                <span class="hero-badge">⭐ STUDI KASUS UTAMA PRA SERKOM</span>
                <h1 class="hero-title">Aplikasi Pemesanan Tiket Konser Berbasis Web</h1>
                <p class="hero-desc">
                    Panduan lengkap step-by-step membangun aplikasi pemesanan tiket konser dari nol hingga siap uji kompetensi BNSP.
                    Mencakup autentikasi multi-role (Customer & Admin), perancangan relasi 4 tabel basis data, dashboard rekapitulasi pesanan masuk dengan filter periode,
                    master CRUD tiket konser dengan upload gambar poster, CRUD manajemen data pengguna (Admin & Customer), serta alur transaksi booking atomik dengan pencegahan overbooking.
                </p>
                <div class="hero-meta">
                    <span><strong>Framework:</strong> Laravel 10/11</span>
                    <span><strong>Database:</strong> MySQL (InnoDB)</span>
                    <span><strong>Frontend:</strong> Tailwind CSS & Blade</span>
                    <span><strong>Auth:</strong> Laravel Breeze</span>
                </div>
            </div>

            <!-- ERD DIAGRAM VISUAL -->
            <div class="section-card">
                <div class="section-header">
                    <div class="section-title">
                        <span>🗺️ Arsitektur Relasi Basis Data (ERD Tiket Konser)</span>
                    </div>
                    <span class="step-pill">Kardinalitas 1:N & N:M</span>
                </div>
                <p class="step-desc">
                    Struktur 4 tabel yang ternormalisasi (3NF). Hubungan antara Transaksi (<code>orders</code>) dan Tiket Konser (<code>tickets</code>)
                    adalah Many-to-Many yang dihubungkan melalui tabel pivot <code>order_details</code>.
                </p>

                <div class="erd-board">
                    <!-- Table: users -->
                    <div class="erd-table">
                        <div class="erd-header">
                            <span>users</span>
                            <span class="erd-badge">Master Akun</span>
                        </div>
                        <ul class="erd-fields">
                            <li class="erd-field"><span class="field-pk">🔑 id</span> <span class="field-type">BIGINT (PK)</span></li>
                            <li class="erd-field"><span>name</span> <span class="field-type">VARCHAR(255)</span></li>
                            <li class="erd-field"><span>email</span> <span class="field-type">VARCHAR(255) [UNIQUE]</span></li>
                            <li class="erd-field"><span>phone</span> <span class="field-type">VARCHAR(20)</span></li>
                            <li class="erd-field"><span>password</span> <span class="field-type">VARCHAR(255)</span></li>
                            <li class="erd-field"><span class="field-pk">role</span> <span class="field-type">ENUM('admin','customer')</span></li>
                        </ul>
                    </div>

                    <!-- Table: orders -->
                    <div class="erd-table">
                        <div class="erd-header">
                            <span>orders</span>
                            <span class="erd-badge">Header Transaksi</span>
                        </div>
                        <ul class="erd-fields">
                            <li class="erd-field"><span class="field-pk">🔑 id</span> <span class="field-type">BIGINT (PK)</span></li>
                            <li class="erd-field"><span class="field-fk">🔗 user_id</span> <span class="field-type">FK -> users.id</span></li>
                            <li class="erd-field"><span>order_code</span> <span class="field-type">VARCHAR [UNIQUE]</span></li>
                            <li class="erd-field"><span>customer_name</span> <span class="field-type">VARCHAR(255)</span></li>
                            <li class="erd-field"><span>customer_phone</span> <span class="field-type">VARCHAR(20)</span></li>
                            <li class="erd-field"><span>total_price</span> <span class="field-type">INT</span></li>
                            <li class="erd-field"><span>status</span> <span class="field-type">ENUM('pending','paid','cancelled')</span></li>
                            <li class="erd-field"><span>order_date</span> <span class="field-type">DATE</span></li>
                        </ul>
                    </div>

                    <!-- Table: order_details -->
                    <div class="erd-table">
                        <div class="erd-header">
                            <span>order_details</span>
                            <span class="erd-badge">Pivot / Rincian</span>
                        </div>
                        <ul class="erd-fields">
                            <li class="erd-field"><span class="field-pk">🔑 id</span> <span class="field-type">BIGINT (PK)</span></li>
                            <li class="erd-field"><span class="field-fk">🔗 order_id</span> <span class="field-type">FK -> orders.id [CASCADE]</span></li>
                            <li class="erd-field"><span class="field-fk">🔗 ticket_id</span> <span class="field-type">FK -> tickets.id [CASCADE]</span></li>
                            <li class="erd-field"><span>quantity</span> <span class="field-type">INT</span></li>
                            <li class="erd-field"><span>unit_price</span> <span class="field-type">INT (Harga Historis)</span></li>
                            <li class="erd-field"><span>subtotal</span> <span class="field-type">INT</span></li>
                        </ul>
                    </div>

                    <!-- Table: tickets -->
                    <div class="erd-table">
                        <div class="erd-header">
                            <span>tickets</span>
                            <span class="erd-badge">Master Konser</span>
                        </div>
                        <ul class="erd-fields">
                            <li class="erd-field"><span class="field-pk">🔑 id</span> <span class="field-type">BIGINT (PK)</span></li>
                            <li class="erd-field"><span>concert_name</span> <span class="field-type">VARCHAR(255)</span></li>
                            <li class="erd-field"><span>artist</span> <span class="field-type">VARCHAR(255)</span></li>
                            <li class="erd-field"><span>venue</span> <span class="field-type">VARCHAR(255)</span></li>
                            <li class="erd-field"><span>event_date</span> <span class="field-type">DATETIME</span></li>
                            <li class="erd-field"><span>category</span> <span class="field-type">ENUM('VIP','Festival','Regular')</span></li>
                            <li class="erd-field"><span>price</span> <span class="field-type">INT</span></li>
                            <li class="erd-field"><span>stock</span> <span class="field-type">INT</span></li>
                            <li class="erd-field"><span>poster</span> <span class="field-type">VARCHAR (Path Gambar)</span></li>
                        </ul>
                    </div>
                </div>
            </div>
    """)

    # Step 1: Login & Multi-Role
    code_mig_users = r"""// database/migrations/xxxx_create_users_table.php
public function up(): void
{
    Schema::create('users', function (Blueprint $table) {
        $table->id();
        $table->string('name');
        $table->string('email')->unique();
        $table->string('phone')->nullable(); // [TAMBAHKAN] Nomor HP pemesan tiket
        $table->timestamp('email_verified_at')->nullable();
        $table->string('password');
        // [TAMBAHKAN] Kolom role: 'admin' atau 'customer'
        $table->enum('role', ['admin', 'customer'])->default('customer');
        $table->rememberToken();
        $table->timestamps();
    });
}"""

    code_model_user = r"""<?php
// app/Models/User.php
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
        'role', // [TAMBAHKAN]
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

    // [TAMBAHKAN] Helper pengecekan hak akses
    public function isAdmin(): bool
    {
        return $this->role === 'admin';
    }

    public function isCustomer(): bool
    {
        return $this->role === 'customer';
    }

    // [TAMBAHKAN] Relasi One-to-Many ke Transaksi Pemesanan
    public function orders()
    {
        return $this->hasMany(Order::class);
    }
}"""

    code_seeder = r"""<?php
// database/seeders/DatabaseSeeder.php
namespace Database\Seeders;

use App\Models\User;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\Hash;

class DatabaseSeeder extends Seeder
{
    public function run(): void
    {
        // 1. Akun Default Administrator
        User::create([
            'name'     => 'Administrator Konser',
            'email'    => 'admin@tiket.com',
            'phone'    => '081122334455',
            'password' => Hash::make('password123'),
            'role'     => 'admin',
        ]);

        // 2. Akun Default Customer
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
}"""

    code_middleware = r"""<?php
// app/Http/Middleware/IsAdmin.php
namespace App\Http\Middleware;

use Closure;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Symfony\Component\HttpFoundation\Response;

class IsAdmin
{
    public function handle(Request $request, Closure $next): Response
    {
        // Cek login & role admin
        if (Auth::check() && Auth::user()->role === 'admin') {
            return $next($request);
        }

        // Jika bukan admin, tolak & kembalikan ke katalog
        return redirect()->route('concerts.index')->with('error', 'Akses ditolak! Halaman ini khusus Administrator.');
    }
}"""

    h.append(f"""
            <!-- PRAKTEK 1 -->
            <div id="sec-tiket-praktek1" class="section-card">
                <div class="section-header">
                    <div class="section-title">
                        <span>🚀 Praktek 1: Halaman Login & Multi-Role (Customer & Admin)</span>
                    </div>
                    <span class="step-pill">Autentikasi & Otorisasi</span>
                </div>
                <p class="step-desc">
                    Secara bawaan Laravel Breeze menyediakan login & register. Kita menambahkan kolom <code>role</code>
                    ('admin' dan 'customer') pada tabel users, middleware proteksi, serta seeder akun default agar langsung siap demonstrasi.
                </p>

                <h3 class="sub-title">1.1 Tambahkan Kolom Role & Phone pada Migration Users</h3>
                {btk.render_code_box(code_mig_users, "database/migrations/xxxx_create_users_table.php", "php", "Migration")}

                <h3 class="sub-title">1.2 Daftarkan Role & Relasi pada Model User</h3>
                {btk.render_code_box(code_model_user, "app/Models/User.php", "php", "Model")}

                <h3 class="sub-title">1.3 Seeder Akun Default Siap Login</h3>
                {btk.render_code_box(code_seeder, "database/seeders/DatabaseSeeder.php", "php", "Seeder")}

                <h3 class="sub-title">1.4 Middleware Proteksi Administrator (IsAdmin)</h3>
                {btk.render_code_box(code_middleware, "app/Http/Middleware/IsAdmin.php", "php", "Middleware")}
                <div class="callout callout-info">
                    <div class="callout-title">💡 Pendaftaran Middleware di Laravel 11 (bootstrap/app.php):</div>
                    Buka <code>bootstrap/app.php</code>, tambahkan alias: <code>$middleware->alias(['admin' => \\App\\Http\\Middleware\\IsAdmin::class]);</code>
                </div>
            </div>
    """)

    # Step 2: Relasi 4 Tabel
    code_mig_tickets = r"""// database/migrations/xxxx_create_tickets_table.php
public function up(): void
{
    Schema::create('tickets', function (Blueprint $table) {
        $table->id();
        $table->string('concert_name');
        $table->string('artist');
        $table->string('venue');
        $table->dateTime('event_date');
        $table->enum('category', ['VIP', 'Festival', 'Regular']);
        $table->integer('price');
        $table->integer('stock');
        $table->string('poster')->nullable();
        $table->text('description')->nullable();
        $table->timestamps();
    });
}"""

    code_mig_orders = r"""// database/migrations/xxxx_create_orders_table.php
public function up(): void
{
    Schema::create('orders', function (Blueprint $table) {
        $table->id();
        $table->foreignId('user_id')->constrained('users')->onDelete('cascade');
        $table->string('order_code')->unique();
        $table->string('customer_name');
        $table->string('customer_email');
        $table->string('customer_phone');
        $table->integer('total_price');
        $table->enum('status', ['pending', 'paid', 'cancelled'])->default('pending');
        $table->date('order_date');
        $table->timestamps();
    });
}"""

    code_mig_details = r"""// database/migrations/xxxx_create_order_details_table.php
public function up(): void
{
    Schema::create('order_details', function (Blueprint $table) {
        $table->id();
        $table->foreignId('order_id')->constrained('orders')->onDelete('cascade');
        $table->foreignId('ticket_id')->constrained('tickets')->onDelete('cascade');
        $table->integer('quantity');
        $table->integer('unit_price'); // Harga historis saat transaksi
        $table->integer('subtotal');
        $table->timestamps();
    });
}"""

    code_model_ticket = r"""<?php
// app/Models/Ticket.php
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

    // Relasi One-to-Many ke OrderDetail
    public function orderDetails()
    {
        return $this->hasMany(OrderDetail::class);
    }
}"""

    code_model_order = r"""<?php
// app/Models/Order.php
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

    // Relasi ke User pemesan
    public function user()
    {
        return $this->belongsTo(User::class);
    }

    // Relasi ke rincian tiket pesanan
    public function orderDetails()
    {
        return $this->hasMany(OrderDetail::class);
    }
}"""

    code_model_detail = r"""<?php
// app/Models/OrderDetail.php
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

    public function order()
    {
        return $this->belongsTo(Order::class);
    }

    public function ticket()
    {
        return $this->belongsTo(Ticket::class);
    }
}"""

    code_seeder_tickets = r"""<?php
// database/seeders/TicketSeeder.php
namespace Database\Seeders;

use App\Models\Ticket;
use Illuminate\Database\Seeder;

class TicketSeeder extends Seeder
{
    public function run(): void
    {
        $tickets = [
            [
                'concert_name' => 'Coldplay: Music of the Spheres Tour',
                'artist'       => 'Coldplay',
                'venue'        => 'Gelora Bung Karno Stadium Jakarta',
                'event_date'   => '2026-11-15 19:30:00',
                'category'     => 'VIP',
                'price'        => 3500000,
                'stock'        => 120,
                'poster'       => null,
                'description'  => 'Akses VIP Lounge eksklusif, merchandise resmi, dan tempat duduk barisan terdepan.',
            ],
            [
                'concert_name' => 'Coldplay: Music of the Spheres Tour',
                'artist'       => 'Coldplay',
                'venue'        => 'Gelora Bung Karno Stadium Jakarta',
                'event_date'   => '2026-11-15 19:30:00',
                'category'     => 'Festival',
                'price'        => 1850000,
                'stock'        => 350,
                'poster'       => null,
                'description'  => 'Area berdiri bebas di lapangan utama depan panggung megah.',
            ],
            [
                'concert_name' => 'Sheila on 7: Tunggu Aku di Jakarta',
                'artist'       => 'Sheila on 7',
                'venue'        => 'JIEXPO Kemayoran Hall A',
                'event_date'   => '2026-12-05 20:00:00',
                'category'     => 'Festival',
                'price'        => 750000,
                'stock'        => 200,
                'poster'       => null,
                'description'  => 'Nostalgia lagu hits sepanjang masa bersama Duta dan kawan-kawan.',
            ],
            [
                'concert_name' => 'Bruno Mars Live in Jakarta',
                'artist'       => 'Bruno Mars',
                'venue'        => 'Jakarta International Stadium (JIS)',
                'event_date'   => '2026-12-20 19:00:00',
                'category'     => 'VIP',
                'price'        => 4200000,
                'stock'        => 80,
                'poster'       => null,
                'description'  => 'Pengalaman panggung spektakuler dengan tata suara kelas dunia.',
            ],
            [
                'concert_name' => 'Tulus Konser Manusia',
                'artist'       => 'Tulus',
                'venue'        => 'Istora Senayan Jakarta',
                'event_date'   => '2026-10-30 19:30:00',
                'category'     => 'Regular',
                'price'        => 450000,
                'stock'        => 150,
                'poster'       => null,
                'description'  => 'Konser intim persembahan lagu-lagu album Manusia.',
            ],
        ];

        foreach ($tickets as $t) {
            Ticket::create($t);
        }
    }
}"""

    h.append(f"""
            <!-- PRAKTEK 2 -->
            <div id="sec-tiket-praktek2" class="section-card">
                <div class="section-header">
                    <div class="section-title">
                        <span>🗄️ Praktek 2: Relasi Antar Tabel (4 Tabel Utama, Migration & Model)</span>
                    </div>
                    <span class="step-pill">Foreign Key & Eloquent</span>
                </div>
                <p class="step-desc">
                    Skema basis data relasional dengan 4 tabel: <code>users</code> (akun), <code>tickets</code> (master konser),
                    <code>orders</code> (header pesanan), dan <code>order_details</code> (pivot rincian pesanan).
                    Semua relasi menggunakan foreign key dengan opsi <code>onDelete('cascade')</code> untuk menjamin integritas referensial.
                </p>

                <h3 class="sub-title">2.1 Migration Tabel Master Tiket Konser (`tickets`)</h3>
                {btk.render_code_box(code_mig_tickets, "database/migrations/xxxx_create_tickets_table.php", "php", "Migration")}

                <h3 class="sub-title">2.2 Migration Header Transaksi Pemesanan (`orders`)</h3>
                {btk.render_code_box(code_mig_orders, "database/migrations/xxxx_create_orders_table.php", "php", "Migration")}

                <h3 class="sub-title">2.3 Migration Rincian Tiket yang Dipesan (`order_details`)</h3>
                {btk.render_code_box(code_mig_details, "database/migrations/xxxx_create_order_details_table.php", "php", "Migration")}

                <h3 class="sub-title">2.4 Model Eloquent Lengkap dengan Relasi</h3>
                {btk.render_code_box(code_model_ticket, "app/Models/Ticket.php", "php", "Model")}
                {btk.render_code_box(code_model_order, "app/Models/Order.php", "php", "Model")}
                {btk.render_code_box(code_model_detail, "app/Models/OrderDetail.php", "php", "Model")}

                <h3 class="sub-title">2.5 Seeder Tiket Konser Awal Siap Demo</h3>
                {btk.render_code_box(code_seeder_tickets, "database/seeders/TicketSeeder.php", "php", "Seeder")}
            </div>
    """)

    # Step 3: CRUD Tiket Konser Admin
    code_ctrl_ticket = r"""<?php
// app/Http/Controllers/Admin/TicketController.php
namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\Ticket;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Storage;

class TicketController extends Controller
{
    // 1. Tampilkan Semua Tiket Konser
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

        // Upload banner poster jika ada
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

        if ($request->hasFile('poster')) {
            // Hapus file lama jika ada
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
        if ($ticket->poster && Storage::disk('public')->exists($ticket->poster)) {
            Storage::disk('public')->delete($ticket->poster);
        }

        $ticket->delete();

        return redirect()->route('admin.tickets.index')->with('success', 'Tiket konser berhasil dihapus!');
    }
}"""

    code_view_tickets_index = r"""<!-- resources/views/admin/tickets/index.blade.php -->
<x-app-layout>
    <x-slot name="header">
        <div class="flex justify-between items-center">
            <h2 class="font-semibold text-xl text-gray-800 leading-tight">
                🎟️ Master Data Tiket Konser
            </h2>
            <a href="{{ route('admin.tickets.create') }}" class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded text-sm">
                ➕ Tambah Tiket Konser Baru
            </a>
        </div>
    </x-slot>

    <div class="py-6 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        @if(session('success'))
            <div class="bg-emerald-100 border-l-4 border-emerald-500 text-emerald-800 p-4 mb-4 rounded text-sm font-semibold">
                ✓ {{ session('success') }}
            </div>
        @endif

        <div class="bg-white rounded-lg shadow-sm border border-gray-200 overflow-x-auto">
            <table class="w-full text-left text-sm text-gray-600">
                <thead class="bg-gray-50 border-b text-xs uppercase text-gray-500">
                    <tr>
                        <th class="px-4 py-3">Poster</th>
                        <th class="px-4 py-3">Konser & Musisi</th>
                        <th class="px-4 py-3">Venue & Waktu</th>
                        <th class="px-4 py-3">Kategori</th>
                        <th class="px-4 py-3">Harga</th>
                        <th class="px-4 py-3">Sisa Stok</th>
                        <th class="px-4 py-3 text-center">Aksi</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-gray-100">
                    @forelse($tickets as $ticket)
                    <tr class="hover:bg-gray-50">
                        <td class="px-4 py-3">
                            @if($ticket->poster)
                                <img src="{{ asset('storage/' . $ticket->poster) }}" alt="Poster" class="w-12 h-12 object-cover rounded shadow">
                            @else
                                <div class="w-12 h-12 bg-gray-200 rounded flex items-center justify-center text-gray-400 text-xs">No Pic</div>
                            @endif
                        </td>
                        <td class="px-4 py-3">
                            <span class="font-bold text-gray-900 block">{{ $ticket->concert_name }}</span>
                            <span class="text-xs text-indigo-600 font-semibold">{{ $ticket->artist }}</span>
                        </td>
                        <td class="px-4 py-3 text-xs">
                            <span class="block font-medium">{{ $ticket->venue }}</span>
                            <span class="text-gray-400">{{ \Carbon\Carbon::parse($ticket->event_date)->format('d M Y - H:i') }} WIB</span>
                        </td>
                        <td class="px-4 py-3">
                            <span class="px-2 py-0.5 rounded text-xs font-bold {{ $ticket->category === 'VIP' ? 'bg-amber-100 text-amber-800' : 'bg-blue-100 text-blue-800' }}">
                                {{ $ticket->category }}
                            </span>
                        </td>
                        <td class="px-4 py-3 font-bold text-gray-800">Rp {{ number_format($ticket->price, 0, ',', '.') }}</td>
                        <td class="px-4 py-3">
                            <span class="font-bold {{ $ticket->stock > 10 ? 'text-emerald-600' : 'text-rose-600' }}">
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
            <div class="p-4 border-t">
                {{ $tickets->links() }}
            </div>
        </div>
    </div>
</x-app-layout>"""

    code_view_tickets_create = r"""<!-- resources/views/admin/tickets/create.blade.php -->
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
                        <label class="block text-sm font-semibold text-gray-700 mb-1">Nama Konser</label>
                        <input type="text" name="concert_name" value="{{ old('concert_name') }}" required class="w-full border-gray-300 rounded shadow-sm text-sm" placeholder="Coldplay World Tour">
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-1">Artis / Musisi</label>
                        <input type="text" name="artist" value="{{ old('artist') }}" required class="w-full border-gray-300 rounded shadow-sm text-sm" placeholder="Coldplay">
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-1">Lokasi / Venue</label>
                        <input type="text" name="venue" value="{{ old('venue') }}" required class="w-full border-gray-300 rounded shadow-sm text-sm" placeholder="Stadion GBK Jakarta">
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-1">Tanggal & Waktu Acara</label>
                        <input type="datetime-local" name="event_date" value="{{ old('event_date') }}" required class="w-full border-gray-300 rounded shadow-sm text-sm">
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-1">Kategori</label>
                        <select name="category" required class="w-full border-gray-300 rounded shadow-sm text-sm">
                            <option value="VIP">VIP</option>
                            <option value="Festival">Festival</option>
                            <option value="Regular" selected>Regular</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-1">Harga Satuan (Rp)</label>
                        <input type="number" name="price" value="{{ old('price') }}" required min="0" class="w-full border-gray-300 rounded shadow-sm text-sm" placeholder="750000">
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-1">Kuota Stok Tiket</label>
                        <input type="number" name="stock" value="{{ old('stock') }}" required min="1" class="w-full border-gray-300 rounded shadow-sm text-sm" placeholder="100">
                    </div>
                </div>

                <div>
                    <label class="block text-sm font-semibold text-gray-700 mb-1">Upload Banner Poster</label>
                    <input type="file" name="poster" accept="image/*" class="w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded file:border-0 file:bg-indigo-50 file:text-indigo-700 hover:file:bg-indigo-100">
                </div>

                <div>
                    <label class="block text-sm font-semibold text-gray-700 mb-1">Deskripsi / Aturan Acara</label>
                    <textarea name="description" rows="3" class="w-full border-gray-300 rounded shadow-sm text-sm" placeholder="Info gate dibuka jam 17:00 WIB, dilarang membawa kamera profesional...">{{ old('description') }}</textarea>
                </div>

                <div class="flex justify-end space-x-2 pt-4 border-t">
                    <a href="{{ route('admin.tickets.index') }}" class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded text-sm">Batal</a>
                    <button type="submit" class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded text-sm">Simpan Tiket</button>
                </div>
            </form>
        </div>
    </div>
</x-app-layout>"""

    code_view_tickets_edit = r"""<!-- resources/views/admin/tickets/edit.blade.php -->
<x-app-layout>
    <div class="py-6 max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
            <h2 class="text-xl font-bold text-gray-800 mb-4 border-b pb-2">✏️ Edit Master Data Tiket Konser</h2>

            @if($errors->any())
                <div class="bg-rose-100 border-l-4 border-rose-500 text-rose-700 p-3 mb-4 rounded text-sm">
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
                        <label class="block text-sm font-semibold text-gray-700 mb-1">Nama Konser</label>
                        <input type="text" name="concert_name" value="{{ old('concert_name', $ticket->concert_name) }}" required class="w-full border-gray-300 rounded shadow-sm text-sm">
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-1">Artis / Musisi</label>
                        <input type="text" name="artist" value="{{ old('artist', $ticket->artist) }}" required class="w-full border-gray-300 rounded shadow-sm text-sm">
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-1">Lokasi / Venue</label>
                        <input type="text" name="venue" value="{{ old('venue', $ticket->venue) }}" required class="w-full border-gray-300 rounded shadow-sm text-sm">
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-1">Tanggal & Waktu Acara</label>
                        <input type="datetime-local" name="event_date" value="{{ old('event_date', \Carbon\Carbon::parse($ticket->event_date)->format('Y-m-d\TH:i')) }}" required class="w-full border-gray-300 rounded shadow-sm text-sm">
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-1">Kategori</label>
                        <select name="category" required class="w-full border-gray-300 rounded shadow-sm text-sm">
                            <option value="VIP" {{ old('category', $ticket->category) === 'VIP' ? 'selected' : '' }}>VIP</option>
                            <option value="Festival" {{ old('category', $ticket->category) === 'Festival' ? 'selected' : '' }}>Festival</option>
                            <option value="Regular" {{ old('category', $ticket->category) === 'Regular' ? 'selected' : '' }}>Regular</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-1">Harga Satuan (Rp)</label>
                        <input type="number" name="price" value="{{ old('price', $ticket->price) }}" required min="0" class="w-full border-gray-300 rounded shadow-sm text-sm">
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-1">Sisa Kuota Stok Tiket</label>
                        <input type="number" name="stock" value="{{ old('stock', $ticket->stock) }}" required min="0" class="w-full border-gray-300 rounded shadow-sm text-sm">
                    </div>
                </div>

                <div>
                    <label class="block text-sm font-semibold text-gray-700 mb-1">Banner Poster</label>
                    @if($ticket->poster)
                        <div class="mb-2 flex items-center gap-3">
                            <img src="{{ asset('storage/' . $ticket->poster) }}" alt="Poster" class="w-20 h-20 object-cover rounded shadow">
                            <span class="text-xs text-gray-500">Poster saat ini terpasang. Pilih file baru di bawah jika ingin mengganti.</span>
                        </div>
                    @endif
                    <input type="file" name="poster" accept="image/*" class="w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded file:border-0 file:bg-indigo-50 file:text-indigo-700 hover:file:bg-indigo-100">
                </div>

                <div>
                    <label class="block text-sm font-semibold text-gray-700 mb-1">Deskripsi / Aturan Acara</label>
                    <textarea name="description" rows="3" class="w-full border-gray-300 rounded shadow-sm text-sm">{{ old('description', $ticket->description) }}</textarea>
                </div>

                <div class="flex justify-end space-x-2 pt-4 border-t">
                    <a href="{{ route('admin.tickets.index') }}" class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded text-sm">Batal</a>
                    <button type="submit" class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded text-sm">Perbarui Tiket</button>
                </div>
            </form>
        </div>
    </div>
</x-app-layout>"""

    h.append(f"""
            <!-- PRAKTEK 3 -->
            <div id="sec-tiket-praktek3" class="section-card">
                <div class="section-header">
                    <div class="section-title">
                        <span>📋 Praktek 3: CRUD Master Data Tiket Konser (Sisi Admin)</span>
                    </div>
                    <span class="step-pill">CRUD Lengkap & File Upload</span>
                </div>
                <p class="step-desc">
                    Fitur bagi administrator untuk menambah konser baru, mengunggah banner poster ke disk storage public,
                    mengubah kuota tiket, melihat preview gambar, dan menghapus tiket dengan konfirmasi modal.
                </p>

                <h3 class="sub-title">3.1 Controller TicketController (Resource 7 Method)</h3>
                {btk.render_code_box(code_ctrl_ticket, "app/Http/Controllers/Admin/TicketController.php", "php", "Controller")}

                <h3 class="sub-title">3.2 View Index Tabel Tiket Konser</h3>
                {btk.render_code_box(code_view_tickets_index, "resources/views/admin/tickets/index.blade.php", "blade", "Blade View")}

                <h3 class="sub-title">3.3 View Form Tambah Tiket Konser</h3>
                {btk.render_code_box(code_view_tickets_create, "resources/views/admin/tickets/create.blade.php", "blade", "Blade View")}

                <h3 class="sub-title">3.4 View Form Edit Tiket Konser</h3>
                {btk.render_code_box(code_view_tickets_edit, "resources/views/admin/tickets/edit.blade.php", "blade", "Blade View")}
            </div>
    """)
    # Step 4: CRUD Manajemen Pengguna / User Management (Admin)
    code_ctrl_user = r"""<?php
// app/Http/Controllers/Admin/UserController.php
namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\User;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\Hash;
use Illuminate\Validation\Rule;

class UserController extends Controller
{
    // 1. Tampilkan Daftar Semua Pengguna (Admin & Customer)
    public function index(Request $request)
    {
        $query = User::query();

        // Filter Pencarian (Nama / Email)
        if ($request->filled('search')) {
            $search = $request->search;
            $query->where(function($q) use ($search) {
                $q->where('name', 'like', "%{$search}%")
                  ->orWhere('email', 'like', "%{$search}%")
                  ->orWhere('phone', 'like', "%{$search}%");
            });
        }

        // Filter Role (Admin / Customer)
        if ($request->filled('role')) {
            $query->where('role', $request->role);
        }

        $users = $query->latest()->paginate(10)->withQueryString();

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

        // Jika password diisi, enkripsi password baru; jika kosong jangan diubah
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
        // PENTING: Mencegah admin menghapus akunnya sendiri yang sedang aktif
        if (Auth::id() === $user->id) {
            return back()->with('error', 'Tindakan ditolak! Anda tidak dapat menghapus akun Anda sendiri yang sedang aktif.');
        }

        $user->delete();

        return redirect()->route('admin.users.index')->with('success', 'Akun pengguna berhasil dihapus!');
    }
}"""

    code_view_users_index = r"""<!-- resources/views/admin/users/index.blade.php -->
<x-app-layout>
    <x-slot name="header">
        <div class="flex justify-between items-center">
            <h2 class="font-semibold text-xl text-gray-800 leading-tight">
                👥 Kelola Data Pengguna (User Management)
            </h2>
            <a href="{{ route('admin.users.create') }}" class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded text-sm flex items-center gap-2">
                ➕ Tambah Pengguna Baru
            </a>
        </div>
    </x-slot>

    <div class="py-6 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-4">
        <!-- Notifikasi Flash Message -->
        @if(session('success'))
            <div class="bg-emerald-100 border-l-4 border-emerald-500 text-emerald-800 p-4 rounded text-sm font-semibold">
                ✓ {{ session('success') }}
            </div>
        @endif
        @if(session('error'))
            <div class="bg-rose-100 border-l-4 border-rose-500 text-rose-800 p-4 rounded text-sm font-semibold">
                ⚠️ {{ session('error') }}
            </div>
        @endif

        <!-- Filter & Search Bar -->
        <div class="bg-white p-4 rounded-lg shadow-sm border border-gray-200">
            <form method="GET" action="{{ route('admin.users.index') }}" class="grid grid-cols-1 md:grid-cols-3 gap-3">
                <input type="text" name="search" value="{{ request('search') }}" placeholder="Cari nama, email, atau no HP..." class="border-gray-300 rounded text-sm w-full">
                <select name="role" class="border-gray-300 rounded text-sm w-full">
                    <option value="">-- Semua Role --</option>
                    <option value="admin" {{ request('role') == 'admin' ? 'selected' : '' }}>Administrator</option>
                    <option value="customer" {{ request('role') == 'customer' ? 'selected' : '' }}>Customer (Pembeli)</option>
                </select>
                <div class="flex gap-2">
                    <button type="submit" class="bg-gray-800 hover:bg-gray-900 text-white font-bold px-4 py-2 rounded text-sm">
                        Filter
                    </button>
                    <a href="{{ route('admin.users.index') }}" class="bg-gray-200 hover:bg-gray-300 text-gray-700 font-bold px-3 py-2 rounded text-sm">
                        Reset
                    </a>
                </div>
            </form>
        </div>

        <!-- Tabel Pengguna -->
        <div class="bg-white rounded-lg shadow-sm border border-gray-200 overflow-x-auto">
            <table class="w-full text-left text-sm text-gray-600">
                <thead class="bg-gray-50 border-b text-xs uppercase text-gray-500">
                    <tr>
                        <th class="px-4 py-3">No</th>
                        <th class="px-4 py-3">Nama Lengkap</th>
                        <th class="px-4 py-3">Email</th>
                        <th class="px-4 py-3">No HP</th>
                        <th class="px-4 py-3">Role</th>
                        <th class="px-4 py-3">Terdaftar</th>
                        <th class="px-4 py-3 text-center">Aksi</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-gray-100">
                    @forelse($users as $index => $user)
                    <tr class="hover:bg-gray-50">
                        <td class="px-4 py-3">{{ $users->firstItem() + $index }}</td>
                        <td class="px-4 py-3 font-bold text-gray-900">{{ $user->name }}</td>
                        <td class="px-4 py-3 font-mono text-xs">{{ $user->email }}</td>
                        <td class="px-4 py-3 text-xs">{{ $user->phone ?? '-' }}</td>
                        <td class="px-4 py-3">
                            @if($user->role === 'admin')
                                <span class="bg-purple-100 text-purple-800 text-xs font-bold px-2.5 py-0.5 rounded border border-purple-200">
                                    👑 Administrator
                                </span>
                            @else
                                <span class="bg-emerald-100 text-emerald-800 text-xs font-bold px-2.5 py-0.5 rounded border border-emerald-200">
                                    👤 Customer
                                </span>
                            @endif
                        </td>
                        <td class="px-4 py-3 text-xs">{{ $user->created_at->format('d M Y') }}</td>
                        <td class="px-4 py-3 text-center space-x-2">
                            <a href="{{ route('admin.users.edit', $user->id) }}" class="text-indigo-600 hover:text-indigo-900 font-bold text-xs">
                                Edit
                            </a>
                            @if(auth()->id() !== $user->id)
                            <form action="{{ route('admin.users.destroy', $user->id) }}" method="POST" class="inline" onsubmit="return confirm('Yakin ingin menghapus pengguna {{ $user->name }}?')">
                                @csrf
                                @method('DELETE')
                                <button type="submit" class="text-rose-600 hover:text-rose-900 font-bold text-xs ml-2">
                                    Hapus
                                </button>
                            </form>
                            @else
                            <span class="text-gray-400 text-xs italic ml-2">(Akun Anda)</span>
                            @endif
                        </td>
                    </tr>
                    @empty
                    <tr>
                        <td colspan="7" class="px-4 py-8 text-center text-gray-400">Tidak ada pengguna yang cocok dengan kriteria pencarian.</td>
                    </tr>
                    @endforelse
                </tbody>
            </table>
            <div class="p-4 border-t">
                {{ $users->links() }}
            </div>
        </div>
    </div>
</x-app-layout>"""

    code_view_users_create = r"""<!-- resources/views/admin/users/create.blade.php -->
<x-app-layout>
    <div class="py-6 max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
            <h2 class="text-xl font-bold text-gray-800 mb-4 border-b pb-2">➕ Tambah Pengguna Baru</h2>

            @if($errors->any())
                <div class="bg-rose-100 border-l-4 border-rose-500 text-rose-700 p-3 mb-4 rounded text-sm">
                    <ul class="list-disc list-inside">
                        @foreach($errors->all() as $error)
                            <li>{{ $error }}</li>
                        @endforeach
                    </ul>
                </div>
            @endif

            <form action="{{ route('admin.users.store') }}" method="POST" class="space-y-4">
                @csrf
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-1">Nama Lengkap</label>
                        <input type="text" name="name" value="{{ old('name') }}" required class="w-full border-gray-300 rounded shadow-sm text-sm" placeholder="Contoh: Rian Anggoro">
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-1">Alamat Email</label>
                        <input type="email" name="email" value="{{ old('email') }}" required class="w-full border-gray-300 rounded shadow-sm text-sm" placeholder="user@contoh.com">
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-1">Nomor HP / WhatsApp</label>
                        <input type="text" name="phone" value="{{ old('phone') }}" class="w-full border-gray-300 rounded shadow-sm text-sm" placeholder="081234567890">
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-1">Peran / Role</label>
                        <select name="role" required class="w-full border-gray-300 rounded shadow-sm text-sm">
                            <option value="customer" {{ old('role') === 'customer' ? 'selected' : '' }}>Customer (Pembeli Tiket)</option>
                            <option value="admin" {{ old('role') === 'admin' ? 'selected' : '' }}>Administrator (Panitia Konser)</option>
                        </select>
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-1">Kata Sandi (Password)</label>
                        <input type="password" name="password" required minlength="6" class="w-full border-gray-300 rounded shadow-sm text-sm" placeholder="Minimal 6 karakter">
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-1">Konfirmasi Kata Sandi</label>
                        <input type="password" name="password_confirmation" required minlength="6" class="w-full border-gray-300 rounded shadow-sm text-sm" placeholder="Ulangi kata sandi">
                    </div>
                </div>

                <div class="flex justify-end space-x-2 pt-4 border-t">
                    <a href="{{ route('admin.users.index') }}" class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded text-sm">Batal</a>
                    <button type="submit" class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded text-sm">Simpan Pengguna</button>
                </div>
            </form>
        </div>
    </div>
</x-app-layout>"""

    code_view_users_edit = r"""<!-- resources/views/admin/users/edit.blade.php -->
<x-app-layout>
    <div class="py-6 max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="bg-white p-6 rounded-lg shadow-sm border border-gray-200">
            <h2 class="text-xl font-bold text-gray-800 mb-4 border-b pb-2">✏️ Edit Data Pengguna</h2>

            @if($errors->any())
                <div class="bg-rose-100 border-l-4 border-rose-500 text-rose-700 p-3 mb-4 rounded text-sm">
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
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-1">Nama Lengkap</label>
                        <input type="text" name="name" value="{{ old('name', $user->name) }}" required class="w-full border-gray-300 rounded shadow-sm text-sm">
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-1">Alamat Email</label>
                        <input type="email" name="email" value="{{ old('email', $user->email) }}" required class="w-full border-gray-300 rounded shadow-sm text-sm">
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-1">Nomor HP / WhatsApp</label>
                        <input type="text" name="phone" value="{{ old('phone', $user->phone) }}" class="w-full border-gray-300 rounded shadow-sm text-sm">
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-1">Peran / Role</label>
                        <select name="role" required class="w-full border-gray-300 rounded shadow-sm text-sm">
                            <option value="customer" {{ old('role', $user->role) === 'customer' ? 'selected' : '' }}>Customer (Pembeli Tiket)</option>
                            <option value="admin" {{ old('role', $user->role) === 'admin' ? 'selected' : '' }}>Administrator (Panitia Konser)</option>
                        </select>
                    </div>
                </div>

                <div class="bg-amber-50 border border-amber-200 p-3 rounded text-xs text-amber-800">
                    💡 <strong>Catatan Password:</strong> Kosongkan kolom password di bawah jika Anda tidak ingin mengganti password pengguna ini.
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-1">Password Baru (Opsional)</label>
                        <input type="password" name="password" minlength="6" class="w-full border-gray-300 rounded shadow-sm text-sm" placeholder="Kosongkan jika tidak diganti">
                    </div>
                    <div>
                        <label class="block text-sm font-semibold text-gray-700 mb-1">Konfirmasi Password Baru</label>
                        <input type="password" name="password_confirmation" minlength="6" class="w-full border-gray-300 rounded shadow-sm text-sm" placeholder="Ulangi password baru">
                    </div>
                </div>

                <div class="flex justify-end space-x-2 pt-4 border-t">
                    <a href="{{ route('admin.users.index') }}" class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-2 px-4 rounded text-sm">Batal</a>
                    <button type="submit" class="bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded text-sm">Perbarui Pengguna</button>
                </div>
            </form>
        </div>
    </div>
</x-app-layout>"""

    h.append(f"""
            <!-- PRAKTEK 4 -->
            <div id="sec-tiket-praktek4" class="section-card">
                <div class="section-header">
                    <div class="section-title">
                        <span>👥 Praktek 4: CRUD Manajemen Data Pengguna (User Management)</span>
                    </div>
                    <span class="step-pill">CRUD User & Proteksi Akun</span>
                </div>
                <p class="step-desc">
                    Fitur esensial administrator untuk mengelola pengguna (Admin & Customer).
                    Mencakup pencarian user berdasarkan nama/email, filtering peran, penambahan akun baru,
                    pembaruan profil tanpa harus mengganti password, serta proteksi keamanan agar admin tidak dapat menghapus akunnya sendiri yang sedang aktif.
                </p>

                <h3 class="sub-title">4.1 Controller UserController (Resource CRUD & Proteksi Self-Delete)</h3>
                {btk.render_code_box(code_ctrl_user, "app/Http/Controllers/Admin/UserController.php", "php", "Controller")}

                <h3 class="sub-title">4.2 View Index Tabel Pengguna (Admin & Customer)</h3>
                {btk.render_code_box(code_view_users_index, "resources/views/admin/users/index.blade.php", "blade", "Blade View")}

                <h3 class="sub-title">4.3 View Form Tambah Pengguna Baru</h3>
                {btk.render_code_box(code_view_users_create, "resources/views/admin/users/create.blade.php", "blade", "Blade View")}

                <h3 class="sub-title">4.4 View Form Edit Data Pengguna</h3>
                {btk.render_code_box(code_view_users_edit, "resources/views/admin/users/edit.blade.php", "blade", "Blade View")}
            </div>
    """)

    # Step 5: Rekap Laporan Pesanan Masuk
    code_ctrl_rekap = r"""<?php
// app/Http/Controllers/Admin/OrderReportController.php
namespace App\Http\Controllers\Admin;

use App\Http\Controllers\Controller;
use App\Models\Order;
use App\Models\OrderDetail;
use Illuminate\Http\Request;

class OrderReportController extends Controller
{
    public function index(Request $request)
    {
        $query = Order::with(['user', 'orderDetails.ticket']);

        // 1. Filter Rentang Tanggal
        if ($request->filled('start_date') && $request->filled('end_date')) {
            $query->whereBetween('order_date', [$request->start_date, $request->end_date]);
        }

        // 2. Filter Status Pembayaran
        if ($request->filled('status')) {
            $query->where('status', $request->status);
        }

        // 3. Pencarian Kode Booking / Nama Customer
        if ($request->filled('search')) {
            $search = $request->search;
            $query->where(function($q) use ($search) {
                $q->where('order_code', 'like', "%{$search}%")
                  ->orWhere('customer_name', 'like', "%{$search}%");
            });
        }

        $orders = $query->latest()->paginate(10)->withQueryString();

        // 4. Ringkasan Statistik untuk Card Dashboard
        $totalOmset = Order::where('status', 'paid')->sum('total_price');
        $totalTicketsSold = OrderDetail::whereHas('order', function ($q) {
            $q->where('status', 'paid');
        })->sum('quantity');
        $totalPaidOrders = Order::where('status', 'paid')->count();
        $totalPendingOrders = Order::where('status', 'pending')->count();

        return view('admin.orders.index', compact(
            'orders',
            'totalOmset',
            'totalTicketsSold',
            'totalPaidOrders',
            'totalPendingOrders'
        ));
    }

    // 5. Update Status Pembayaran (Pending -> Paid / Cancelled)
    public function updateStatus(Request $request, $id)
    {
        $request->validate([
            'status' => 'required|in:pending,paid,cancelled'
        ]);

        $order = Order::findOrFail($id);
        $order->update(['status' => $request->status]);

        return back()->with('success', "Status pesanan {$order->order_code} berhasil diperbarui!");
    }

    // 6. Tampilan Cetak Laporan Resmi
    public function printReport(Request $request)
    {
        $query = Order::with(['user', 'orderDetails.ticket']);

        if ($request->filled('start_date') && $request->filled('end_date')) {
            $query->whereBetween('order_date', [$request->start_date, $request->end_date]);
        }
        if ($request->filled('status')) {
            $query->where('status', $request->status);
        }

        $orders = $query->latest()->get();

        return view('admin.orders.print', compact('orders'));
    }
}"""

    code_view_orders_index = r"""<!-- resources/views/admin/orders/index.blade.php -->
<x-app-layout>
    <x-slot name="header">
        <h2 class="font-semibold text-xl text-gray-800 leading-tight">
            📊 Rekapitulasi & Laporan Pesanan Masuk
        </h2>
    </x-slot>

    <div class="py-6 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6">
        @if(session('success'))
            <div class="bg-emerald-100 border-l-4 border-emerald-500 text-emerald-800 p-4 rounded text-sm font-semibold">
                ✓ {{ session('success') }}
            </div>
        @endif

        <!-- Card Statistik Dashboard -->
        <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
            <div class="bg-white p-5 rounded-lg border border-gray-200 shadow-sm flex items-center justify-between">
                <div>
                    <span class="text-xs font-bold text-gray-400 uppercase tracking-wider block">Total Omset Lunas</span>
                    <span class="text-xl font-black text-emerald-600 mt-1 block">Rp {{ number_format($totalOmset, 0, ',', '.') }}</span>
                </div>
                <div class="p-3 bg-emerald-50 rounded-full text-emerald-600 text-2xl">💰</div>
            </div>

            <div class="bg-white p-5 rounded-lg border border-gray-200 shadow-sm flex items-center justify-between">
                <div>
                    <span class="text-xs font-bold text-gray-400 uppercase tracking-wider block">Tiket Terjual</span>
                    <span class="text-xl font-black text-indigo-600 mt-1 block">{{ number_format($totalTicketsSold) }} Tiket</span>
                </div>
                <div class="p-3 bg-indigo-50 rounded-full text-indigo-600 text-2xl">🎟️</div>
            </div>

            <div class="bg-white p-5 rounded-lg border border-gray-200 shadow-sm flex items-center justify-between">
                <div>
                    <span class="text-xs font-bold text-gray-400 uppercase tracking-wider block">Pesanan Lunas</span>
                    <span class="text-xl font-black text-blue-600 mt-1 block">{{ $totalPaidOrders }} Transaksi</span>
                </div>
                <div class="p-3 bg-blue-50 rounded-full text-blue-600 text-2xl">✅</div>
            </div>

            <div class="bg-white p-5 rounded-lg border border-gray-200 shadow-sm flex items-center justify-between">
                <div>
                    <span class="text-xs font-bold text-gray-400 uppercase tracking-wider block">Menunggu Bayar</span>
                    <span class="text-xl font-black text-amber-500 mt-1 block">{{ $totalPendingOrders }} Pesanan</span>
                </div>
                <div class="p-3 bg-amber-50 rounded-full text-amber-600 text-2xl">⏳</div>
            </div>
        </div>

        <!-- Filter & Search Bar -->
        <div class="bg-white p-4 rounded-lg shadow-sm border border-gray-200">
            <form method="GET" action="{{ route('admin.orders.index') }}" class="grid grid-cols-1 md:grid-cols-5 gap-3 items-end">
                <div>
                    <label class="block text-xs font-bold text-gray-600 mb-1">Dari Tanggal</label>
                    <input type="date" name="start_date" value="{{ request('start_date') }}" class="w-full border-gray-300 rounded text-xs shadow-sm">
                </div>
                <div>
                    <label class="block text-xs font-bold text-gray-600 mb-1">Sampai Tanggal</label>
                    <input type="date" name="end_date" value="{{ request('end_date') }}" class="w-full border-gray-300 rounded text-xs shadow-sm">
                </div>
                <div>
                    <label class="block text-xs font-bold text-gray-600 mb-1">Status Transaksi</label>
                    <select name="status" class="w-full border-gray-300 rounded text-xs shadow-sm">
                        <option value="">Semua Status</option>
                        <option value="paid" {{ request('status') === 'paid' ? 'selected' : '' }}>Paid (Lunas)</option>
                        <option value="pending" {{ request('status') === 'pending' ? 'selected' : '' }}>Pending</option>
                        <option value="cancelled" {{ request('status') === 'cancelled' ? 'selected' : '' }}>Cancelled</option>
                    </select>
                </div>
                <div>
                    <label class="block text-xs font-bold text-gray-600 mb-1">Cari Kode / Nama</label>
                    <input type="text" name="search" value="{{ request('search') }}" placeholder="TKT-2026..." class="w-full border-gray-300 rounded text-xs shadow-sm">
                </div>
                <div class="flex space-x-2">
                    <button type="submit" class="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-bold py-2 px-3 rounded text-xs">
                        Filter
                    </button>
                    <a href="{{ route('admin.orders.print', request()->all()) }}" target="_blank" class="w-full bg-gray-800 hover:bg-gray-900 text-white font-bold py-2 px-3 rounded text-xs text-center flex items-center justify-center gap-1">
                        🖨️ Cetak
                    </a>
                </div>
            </form>
        </div>

        <!-- Tabel Transaksi Pesanan -->
        <div class="bg-white rounded-lg shadow-sm border border-gray-200 overflow-x-auto">
            <table class="w-full text-left text-sm text-gray-600">
                <thead class="bg-gray-50 border-b text-xs uppercase text-gray-500">
                    <tr>
                        <th class="px-4 py-3">Kode Booking</th>
                        <th class="px-4 py-3">Pemesan</th>
                        <th class="px-4 py-3">Rincian Tiket</th>
                        <th class="px-4 py-3">Total Bayar</th>
                        <th class="px-4 py-3">Status</th>
                        <th class="px-4 py-3">Tanggal</th>
                        <th class="px-4 py-3 text-center">Ubah Status</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-gray-100">
                    @forelse($orders as $order)
                    <tr class="hover:bg-gray-50">
                        <td class="px-4 py-3 font-mono font-bold text-indigo-600">{{ $order->order_code }}</td>
                        <td class="px-4 py-3">
                            <span class="font-bold text-gray-900 block">{{ $order->customer_name }}</span>
                            <span class="text-xs text-gray-400">{{ $order->customer_phone }}</span>
                        </td>
                        <td class="px-4 py-3 text-xs">
                            @foreach($order->orderDetails as $detail)
                                <div class="font-medium text-gray-700">
                                    {{ $detail->ticket->concert_name }}
                                    <span class="text-indigo-600">({{ $detail->quantity }}x {{ $detail->ticket->category }})</span>
                                </div>
                            @endforeach
                        </td>
                        <td class="px-4 py-3 font-bold text-gray-900">
                            Rp {{ number_format($order->total_price, 0, ',', '.') }}
                        </td>
                        <td class="px-4 py-3">
                            @if($order->status === 'paid')
                                <span class="bg-emerald-100 text-emerald-800 text-xs font-bold px-2 py-0.5 rounded">Paid</span>
                            @elseif($order->status === 'pending')
                                <span class="bg-amber-100 text-amber-800 text-xs font-bold px-2 py-0.5 rounded">Pending</span>
                            @else
                                <span class="bg-rose-100 text-rose-800 text-xs font-bold px-2 py-0.5 rounded">Cancelled</span>
                            @endif
                        </td>
                        <td class="px-4 py-3 text-xs text-gray-500">
                            {{ \Carbon\Carbon::parse($order->order_date)->format('d M Y') }}
                        </td>
                        <td class="px-4 py-3 text-center">
                            <form action="{{ route('admin.orders.updateStatus', $order->id) }}" method="POST" class="inline-flex items-center gap-1">
                                @csrf
                                @method('PATCH')
                                <select name="status" class="text-xs border-gray-300 rounded py-1 px-2" onchange="this.form.submit()">
                                    <option value="pending" {{ $order->status === 'pending' ? 'selected' : '' }}>Pending</option>
                                    <option value="paid" {{ $order->status === 'paid' ? 'selected' : '' }}>Paid</option>
                                    <option value="cancelled" {{ $order->status === 'cancelled' ? 'selected' : '' }}>Cancelled</option>
                                </select>
                            </form>
                        </td>
                    </tr>
                    @empty
                    <tr>
                        <td colspan="7" class="px-4 py-8 text-center text-gray-400">Belum ada transaksi pada periode yang dipilih.</td>
                    </tr>
                    @endforelse
                </tbody>
            </table>
            <div class="p-4 border-t">
                {{ $orders->links() }}
            </div>
        </div>
    </div>
</x-app-layout>"""

    code_view_orders_print = r"""<!-- resources/views/admin/orders/print.blade.php -->
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Laporan Rekapitulasi Pesanan Masuk</title>
    <style>
        body { font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; margin: 20px; color: #1e293b; }
        .header { text-align: center; border-bottom: 3px double #334155; padding-bottom: 12px; margin-bottom: 16px; }
        .header h1 { margin: 0; font-size: 18px; text-transform: uppercase; }
        .header p { margin: 3px 0; color: #64748b; font-size: 11px; }
        table.data-table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        table.data-table th, table.data-table td { border: 1px solid #94a3b8; padding: 6px 8px; text-align: left; }
        table.data-table th { background: #f1f5f9; font-weight: bold; }
        .text-right { text-align: right; }
        .total-row { font-weight: bold; background: #f8fafc; }
        .signature-box { margin-top: 40px; float: right; width: 220px; text-align: center; }
        @media print {
            .no-print { display: none; }
        }
    </style>
</head>
<body onload="window.print()">
    <div class="no-print" style="margin-bottom: 15px;">
        <button onclick="window.print()" style="padding: 6px 12px; background: #4f46e5; color: #fff; border: none; border-radius: 4px; cursor: pointer;">
            🖨️ Cetak Dokumen
        </button>
    </div>

    <div class="header">
        <h1>PANITIA PENYELENGGARA KONSER MUSIK INDONESIA</h1>
        <p>Laporan Resmi Rekapitulasi Pemesanan & Penjualan Tiket Konser Masuk</p>
        <p>Tanggal Cetak: {{ now()->translatedFormat('d F Y, H:i') }} WIB</p>
    </div>

    <table class="data-table">
        <thead>
            <tr>
                <th style="width: 5%;">No</th>
                <th>Kode Booking</th>
                <th>Nama Customer</th>
                <th>Tiket & Kategori</th>
                <th>Jumlah</th>
                <th>Total Bayar</th>
                <th>Status</th>
                <th>Tanggal Order</th>
            </tr>
        </thead>
        <tbody>
            @php $grandTotal = 0; @endphp
            @forelse($orders as $idx => $order)
                @php $grandTotal += $order->total_price; @endphp
                <tr>
                    <td>{{ $idx + 1 }}</td>
                    <td style="font-family: monospace; font-weight: bold;">{{ $order->order_code }}</td>
                    <td>{{ $order->customer_name }}</td>
                    <td>
                        @foreach($order->orderDetails as $d)
                            <div>{{ $d->ticket->concert_name }} ({{ $d->ticket->category }})</div>
                        @endforeach
                    </td>
                    <td>
                        @foreach($order->orderDetails as $d)
                            <div>{{ $d->quantity }} tiket</div>
                        @endforeach
                    </td>
                    <td class="text-right">Rp {{ number_format($order->total_price, 0, ',', '.') }}</td>
                    <td style="text-transform: uppercase; font-weight: bold;">{{ $order->status }}</td>
                    <td>{{ \Carbon\Carbon::parse($order->order_date)->format('d/m/Y') }}</td>
                </tr>
            @empty
                <tr>
                    <td colspan="8" style="text-align: center; color: #94a3b8;">Tidak ada data pesanan pada periode ini.</td>
                </tr>
            @endforelse
            <tr class="total-row">
                <td colspan="5" class="text-right">TOTAL PENDAPATAN REKAPITULASI:</td>
                <td class="text-right">Rp {{ number_format($grandTotal, 0, ',', '.') }}</td>
                <td colspan="2"></td>
            </tr>
        </tbody>
    </table>

    <div class="signature-box">
        <p>Jakarta, {{ now()->translatedFormat('d F Y') }}</p>
        <p style="margin-top: 5px;">Mengetahui,<br><strong>Penanggung Jawab Acara</strong></p>
        <div style="height: 50px;"></div>
        <p><strong>( Panitia Serkom )</strong></p>
    </div>
</body>
</html>"""

    h.append(f"""
            <!-- PRAKTEK 5 -->
            <div id="sec-tiket-praktek5" class="section-card">
                <div class="section-header">
                    <div class="section-title">
                        <span>📊 Praktek 5: Rekap Laporan Pesanan Masuk (Dashboard Admin)</span>
                    </div>
                    <span class="step-pill">Agregasi, Filter & Print</span>
                </div>
                <p class="step-desc">
                    Dashboard administrator untuk memantau ringkasan omset penjualan secara real-time,
                    memfilter pesanan berdasarkan rentang tanggal dan status, mengubah status bayar secara cepat,
                    serta mencetak laporan rekapitulasi ke format siap cetak/PDF.
                </p>

                <h3 class="sub-title">5.1 Controller OrderReportController (Statistik & Filter)</h3>
                {btk.render_code_box(code_ctrl_rekap, "app/Http/Controllers/Admin/OrderReportController.php", "php", "Controller")}

                <h3 class="sub-title">5.2 View Dashboard Rekap Pesanan</h3>
                {btk.render_code_box(code_view_orders_index, "resources/views/admin/orders/index.blade.php", "blade", "Blade View")}

                <h3 class="sub-title">5.3 View Cetak Laporan Rekapitulasi (Print-Ready)</h3>
                {btk.render_code_box(code_view_orders_print, "resources/views/admin/orders/print.blade.php", "blade", "Blade View")}
            </div>
    """)

    # Step 6: Sisi Customer
    code_ctrl_booking = r"""<?php
// app/Http/Controllers/Customer/BookingController.php
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

    // 2. Form Booking Tiket
    public function showBookingForm($id)
    {
        $ticket = Ticket::findOrFail($id);
        return view('customer.booking-form', compact('ticket'));
    }

    // 3. Checkout Transaksi Atomik (DB::transaction & Pengurangan Stok)
    public function checkout(Request $request)
    {
        $request->validate([
            'ticket_id' => 'required|exists:tickets,id',
            'quantity'  => 'required|integer|min:1|max:5',
        ]);

        $ticket = Ticket::findOrFail($request->ticket_id);

        if ($ticket->stock < $request->quantity) {
            return back()->with('error', 'Maaf, kuota tiket tidak mencukupi sisa stok!');
        }

        // Jalankan Database Transaction untuk Menjamin Integritas Data
        DB::beginTransaction();
        try {
            $user = Auth::user();
            $subtotal = $ticket->price * $request->quantity;
            $orderCode = 'TKT-' . date('Ymd') . '-' . strtoupper(substr(uniqid(), -4));

            // Simpan Data Order Header
            $order = Order::create([
                'user_id'        => $user->id,
                'order_code'     => $orderCode,
                'customer_name'  => $user->name,
                'customer_email' => $user->email,
                'customer_phone' => $user->phone ?? '08123456789',
                'total_price'    => $subtotal,
                'status'         => 'paid', // Default lunas untuk simulasi ujian
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

            return redirect()->route('customer.myTickets')->with('success', "Pemesanan berhasil! Kode Booking: {$orderCode}");
        } catch (\Exception $e) {
            DB::rollBack();
            return back()->with('error', 'Terjadi kesalahan transaksi: ' . $e->getMessage());
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
}"""

    code_view_customer_katalog = r"""<!-- resources/views/customer/concerts.blade.php -->
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Katalog Konser Musik - TiketFest</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-50 min-h-screen">
    <header class="bg-indigo-900 text-white py-4 px-6 flex justify-between items-center shadow-md">
        <a href="{{ route('concerts.index') }}" class="text-xl font-bold flex items-center gap-2">
            🎟️ TiketFest Indonesia
        </a>
        <div class="space-x-3 text-sm">
            @auth
                <a href="{{ route('customer.myTickets') }}" class="hover:text-indigo-200 font-medium">Tiket Saya</a>
                <span class="text-indigo-300">|</span>
                <span class="font-bold">{{ auth()->user()->name }}</span>
                <form action="{{ route('logout') }}" method="POST" class="inline">
                    @csrf
                    <button type="submit" class="bg-rose-600 hover:bg-rose-700 px-3 py-1.5 rounded font-bold text-xs">Logout</button>
                </form>
            @else
                <a href="{{ route('login') }}" class="hover:text-indigo-200 font-bold">Login</a>
                <a href="{{ route('register') }}" class="bg-indigo-600 hover:bg-indigo-700 px-3 py-1.5 rounded font-bold text-xs">Daftar</a>
            @endauth
        </div>
    </header>

    <main class="max-w-7xl mx-auto py-8 px-4 sm:px-6 lg:px-8">
        <h1 class="text-2xl font-black text-gray-800 mb-6 border-b pb-3">🔥 Konser Musik Mendatang</h1>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            @forelse($tickets as $t)
            <div class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-md transition">
                <div class="h-44 bg-gray-100 flex items-center justify-center overflow-hidden">
                    @if($t->poster)
                        <img src="{{ asset('storage/' . $t->poster) }}" alt="{{ $t->concert_name }}" class="w-full h-full object-cover">
                    @else
                        <span class="text-4xl text-gray-300">🎵</span>
                    @endif
                </div>
                <div class="p-5">
                    <span class="bg-indigo-100 text-indigo-800 text-xs font-bold px-2 py-0.5 rounded">{{ $t->category }}</span>
                    <h3 class="font-bold text-lg text-gray-900 mt-2">{{ $t->concert_name }}</h3>
                    <p class="text-indigo-600 text-sm font-semibold">🎤 {{ $t->artist }}</p>
                    <p class="text-gray-500 text-xs mt-1">📍 {{ $t->venue }}</p>
                    <p class="text-gray-500 text-xs">📅 {{ \Carbon\Carbon::parse($t->event_date)->format('d M Y - H:i') }} WIB</p>
                    <div class="mt-4 pt-3 border-t flex justify-between items-center">
                        <div>
                            <span class="text-xs text-gray-400 block">Harga</span>
                            <span class="font-black text-indigo-700 text-base">Rp {{ number_format($t->price, 0, ',', '.') }}</span>
                        </div>
                        <a href="{{ route('customer.book', $t->id) }}" class="bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-bold py-2 px-4 rounded-lg">
                            Pesan Tiket
                        </a>
                    </div>
                </div>
            </div>
            @empty
            <div class="col-span-3 text-center py-12 text-gray-400 font-medium">
                Belum ada tiket konser yang tersedia saat ini.
            </div>
            @endforelse
        </div>
    </main>
</body>
</html>"""

    code_view_customer_book = r"""<!-- resources/views/customer/booking-form.blade.php -->
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pesan Tiket - {{ $ticket->concert_name }}</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-50 min-h-screen py-10 px-4">
    <div class="max-w-2xl mx-auto bg-white rounded-xl shadow-md border border-gray-200 p-6">
        <a href="{{ route('concerts.index') }}" class="text-indigo-600 hover:underline text-xs font-bold block mb-4">← Kembali ke Katalog</a>
        <h2 class="text-xl font-black text-gray-800 border-b pb-3 mb-4">Konfirmasi Pemesanan Tiket</h2>

        <div class="bg-indigo-50 border border-indigo-200 rounded-lg p-4 mb-6">
            <h3 class="font-bold text-indigo-900 text-lg">{{ $ticket->concert_name }}</h3>
            <p class="text-xs text-indigo-700 font-semibold">Musisi: {{ $ticket->artist }} | Venue: {{ $ticket->venue }}</p>
            <p class="text-xs text-indigo-600 mt-1">Kategori: <strong>{{ $ticket->category }}</strong> | Sisa Kuota: <strong>{{ $ticket->stock }} tiket</strong></p>
            <p class="text-sm font-black text-indigo-900 mt-2">Harga Satuan: Rp {{ number_format($ticket->price, 0, ',', '.') }}</p>
        </div>

        <form action="{{ route('customer.checkout') }}" method="POST" class="space-y-4">
            @csrf
            <input type="hidden" name="ticket_id" value="{{ $ticket->id }}">

            <div>
                <label class="block text-sm font-semibold text-gray-700 mb-1">Jumlah Tiket yang Ingin Dipesan (Maks. 5)</label>
                <input type="number" id="qtyInput" name="quantity" min="1" max="{{ min(5, $ticket->stock) }}" value="1" required class="w-full border-gray-300 rounded shadow-sm text-sm" oninput="calcTotal()">
            </div>

            <div class="p-4 bg-gray-50 rounded-lg border border-gray-200 flex justify-between items-center">
                <span class="text-sm font-bold text-gray-700">Total Pembayaran:</span>
                <span id="totalDisplay" class="text-xl font-black text-emerald-600">Rp {{ number_format($ticket->price, 0, ',', '.') }}</span>
            </div>

            <button type="submit" class="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-black py-3 rounded-lg shadow transition">
                Bayar & Terbitkan Tiket Sekarang (Checkout)
            </button>
        </form>
    </div>

    <script>
        const unitPrice = {{ $ticket->price }};
        function calcTotal() {
            const qty = parseInt(document.getElementById('qtyInput').value) || 1;
            const total = qty * unitPrice;
            document.getElementById('totalDisplay').innerText = 'Rp ' + total.toLocaleString('id-ID');
        }
    </script>
</body>
</html>"""

    code_view_customer_print = r"""<!-- resources/views/customer/e-ticket.blade.php -->
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>E-Tiket Konser - {{ $order->order_code }}</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f3f4f6; margin: 0; padding: 20px; }
        .ticket-card { max-width: 650px; margin: 20px auto; background: #fff; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.1); border: 2px dashed #cbd5e1; }
        .ticket-header { background: #312e81; color: #fff; padding: 20px; text-align: center; }
        .ticket-code { font-size: 20px; font-weight: 800; letter-spacing: 2px; color: #fbbf24; margin-top: 5px; }
        .ticket-body { padding: 24px; }
        .ticket-row { display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #f1f5f9; font-size: 13px; }
        .ticket-label { color: #64748b; font-weight: 600; }
        .ticket-val { font-weight: 800; color: #1e293b; }
        .barcode { text-align: center; margin-top: 20px; padding: 10px; background: #f8fafc; border-radius: 6px; font-family: monospace; letter-spacing: 4px; font-size: 18px; }
        @media print {
            body { background: #fff; padding: 0; }
            .ticket-card { box-shadow: none; border: 2px solid #000; }
            .no-print { display: none; }
        }
    </style>
</head>
<body>
    <div class="no-print" style="text-align: center; margin-bottom: 15px;">
        <button onclick="window.print()" style="background: #4f46e5; color: #fff; border: none; padding: 8px 16px; border-radius: 6px; font-weight: bold; cursor: pointer;">
            🖨️ Cetak / Simpan PDF
        </button>
    </div>

    <div class="ticket-card">
        <div class="ticket-header">
            <h2 style="margin: 0; font-size: 18px;">E-TIKET RESMI KONSER MUSIK</h2>
            <div class="ticket-code">{{ $order->order_code }}</div>
        </div>
        <div class="ticket-body">
            @foreach($order->orderDetails as $detail)
            <div class="ticket-row">
                <span class="ticket-label">Nama Acara</span>
                <span class="ticket-val">{{ $detail->ticket->concert_name }}</span>
            </div>
            <div class="ticket-row">
                <span class="ticket-label">Artis / Musisi</span>
                <span class="ticket-val">{{ $detail->ticket->artist }}</span>
            </div>
            <div class="ticket-row">
                <span class="ticket-label">Lokasi / Venue</span>
                <span class="ticket-val">{{ $detail->ticket->venue }}</span>
            </div>
            <div class="ticket-row">
                <span class="ticket-label">Kategori & Jumlah</span>
                <span class="ticket-val">{{ $detail->ticket->category }} ({{ $detail->quantity }} Tiket)</span>
            </div>
            @endforeach
            <div class="ticket-row">
                <span class="ticket-label">Nama Pemesan</span>
                <span class="ticket-val">{{ $order->customer_name }}</span>
            </div>
            <div class="ticket-row">
                <span class="ticket-label">Status Pembayaran</span>
                <span class="ticket-val" style="color: #15803d;">LUNAS (PAID)</span>
            </div>
            <div class="ticket-row">
                <span class="ticket-label">Total Tagihan</span>
                <span class="ticket-val">Rp {{ number_format($order->total_price, 0, ',', '.') }}</span>
            </div>
            <div class="barcode">
                ||| | ||||| || |||||| |||| | ||||||||<br>
                <span>*{{ $order->order_code }}*</span>
            </div>
        </div>
    </div>
</body>
</html>"""

    code_routes = r"""<?php
// routes/web.php
use App\Http\Controllers\ProfileController;
use App\Http\Controllers\Customer\BookingController;
use App\Http\Controllers\Admin\TicketController;
use App\Http\Controllers\Admin\UserController;
use App\Http\Controllers\Admin\OrderReportController;
use Illuminate\Support\Facades\Route;

// 1. SISI PUBLIK (KATALOG KONSER)
Route::get('/', [BookingController::class, 'index'])->name('concerts.index');

// 2. SISI CUSTOMER (WAJIB LOGIN)
Route::middleware('auth')->group(function () {
    Route::get('/booking/{id}', [BookingController::class, 'showBookingForm'])->name('customer.book');
    Route::post('/checkout', [BookingController::class, 'checkout'])->name('customer.checkout');
    Route::get('/my-tickets', [BookingController::class, 'myTickets'])->name('customer.myTickets');
    Route::get('/my-tickets/{id}/print', [BookingController::class, 'printTicket'])->name('customer.printTicket');

    // Profil Breeze
    Route::get('/profile', [ProfileController::class, 'edit'])->name('profile.edit');
    Route::patch('/profile', [ProfileController::class, 'update'])->name('profile.update');
    Route::delete('/profile', [ProfileController::class, 'destroy'])->name('profile.destroy');
});

// 3. SISI ADMINISTRATOR (WAJIB LOGIN & ROLE ADMIN)
Route::middleware(['auth', 'admin'])->prefix('admin')->name('admin.')->group(function () {
    // Dashboard Rekapitulasi Pesanan Masuk
    Route::get('/dashboard', [OrderReportController::class, 'index'])->name('orders.index');
    Route::patch('/orders/{id}/status', [OrderReportController::class, 'updateStatus'])->name('orders.updateStatus');
    Route::get('/orders/print', [OrderReportController::class, 'printReport'])->name('orders.print');

    // CRUD Master Data Tiket Konser
    Route::resource('tickets', TicketController::class);

    // CRUD Manajemen Data Pengguna (Admin & Customer)
    Route::resource('users', UserController::class);
});

require __DIR__.'/auth.php';"""

    h.append(f"""
            <!-- PRAKTEK 6 -->
            <div id="sec-tiket-praktek6" class="section-card">
                <div class="section-header">
                    <div class="section-title">
                        <span>🛒 Praktek 6: Sisi Customer (Katalog, Pemesanan Atomik & E-Tiket)</span>
                    </div>
                    <span class="step-pill">DB::transaction & Pengurangan Stok</span>
                </div>
                <p class="step-desc">
                    Customer dapat menjelajahi konser yang masih memiliki kuota stok > 0, memilih tiket,
                    menjalankan checkout atomik dengan <code>DB::transaction()</code> dan <code>decrement('stock')</code>,
                    serta mencetak e-tiket resmi dengan layout digital.
                </p>

                <h3 class="sub-title">6.1 Controller BookingController (Customer Flow)</h3>
                {btk.render_code_box(code_ctrl_booking, "app/Http/Controllers/Customer/BookingController.php", "php", "Controller")}

                <h3 class="sub-title">6.2 View Katalog Konser Publik</h3>
                {btk.render_code_box(code_view_customer_katalog, "resources/views/customer/concerts.blade.php", "blade", "Blade View")}

                <h3 class="sub-title">6.3 View Form Pemesanan Tiket</h3>
                {btk.render_code_box(code_view_customer_book, "resources/views/customer/booking-form.blade.php", "blade", "Blade View")}

                <h3 class="sub-title">6.4 View Cetak E-Tiket Digital</h3>
                {btk.render_code_box(code_view_customer_print, "resources/views/customer/e-ticket.blade.php", "blade", "Blade View")}
            </div>

            <!-- PRAKTEK 7 -->
            <div id="sec-tiket-praktek7" class="section-card">
                <div class="section-header">
                    <div class="section-title">
                        <span>🌐 Praktek 7: File Routing Lengkap (routes/web.php)</span>
                    </div>
                    <span class="step-pill">Routes & Middleware Group</span>
                </div>
                <p class="step-desc">
                    Pemisahan rute publik, rute terproteksi customer, dan rute terproteksi middleware admin (termasuk CRUD tickets dan users) secara rapi.
                </p>
                {btk.render_code_box(code_routes, "routes/web.php", "php", "Routes")}
            </div>
        </div>
    """)
    # TAB 2: TEORI & KISI-KISI ASESOR (4 MATERI TAMBAHAN LENGKAP)
    code_sql_crud = r"""-- 1. Tambah Tiket Konser Baru (Create - INSERT INTO)
INSERT INTO tickets (concert_name, artist, venue, event_date, category, price, stock, created_at, updated_at)
VALUES ('Coldplay World Tour', 'Coldplay', 'Stadion GBK Jakarta', '2026-11-15 19:30:00', 'VIP', 3500000, 150, NOW(), NOW());

-- 2. Tampil Tiket Konser Aktif yang Memiliki Kuota (Read - SELECT)
SELECT id, concert_name, artist, category, price, stock 
FROM tickets 
WHERE stock > 0 
ORDER BY price ASC;

-- 3. Edit Harga & Tambah Stok Tiket Konser (Update - UPDATE ... SET ... WHERE)
-- PENTING: Wajib sertakan klausul WHERE agar tidak mengubah seluruh baris tabel!
UPDATE tickets 
SET price = 3750000, stock = stock + 50, updated_at = NOW() 
WHERE id = 1;

-- 4. Hapus Data Tiket Konser (Delete - DELETE FROM ... WHERE)
-- PENTING: Wajib WHERE agar tidak mengosongkan seluruh isi tabel!
DELETE FROM tickets 
WHERE id = 5;"""

    code_sql_query = r"""-- Contoh 1: Query Agregasi Total Omset Pendapatan Lunas (Statistik Dashboard)
SELECT 
    COUNT(id) AS total_transaksi,
    SUM(total_price) AS total_omset_rupiah,
    AVG(total_price) AS rata_rata_per_pesanan
FROM orders 
WHERE status = 'paid';

-- Contoh 2: Relasi Multi-Tabel (INNER JOIN) Rekap Rincian Pesanan
SELECT 
    o.order_code,
    o.customer_name,
    o.customer_phone,
    t.concert_name,
    t.category,
    od.quantity,
    od.unit_price,
    od.subtotal,
    o.status,
    o.order_date
FROM orders o
INNER JOIN order_details od ON o.id = od.order_id
INNER JOIN tickets t ON od.ticket_id = t.id
WHERE o.status = 'paid'
ORDER BY o.order_date DESC;

-- Contoh 3: Query Analisis Penjualan per Kategori Tiket (GROUP BY & HAVING)
SELECT 
    t.category,
    SUM(od.quantity) AS total_tiket_terjual,
    SUM(od.subtotal) AS total_pendapatan
FROM order_details od
JOIN tickets t ON od.ticket_id = t.id
JOIN orders o ON od.order_id = o.id
WHERE o.status = 'paid'
GROUP BY t.category
HAVING total_pendapatan > 5000000;

-- Contoh 4: Subquery Tiket yang Harganya di Atas Rata-Rata
SELECT concert_name, artist, category, price 
FROM tickets 
WHERE price > (SELECT AVG(price) FROM tickets);"""

    h.append(f"""
        <!-- TAB 2: TEORI & KISI-KISI ASESOR -->
        <div id="tab-teori" class="tab-pane">
            <div class="hero-banner" style="background: linear-gradient(135deg, #1e3a8a 0%, #1d4ed8 50%, #2563eb 100%); border-color: #2563eb;">
                <span class="hero-badge" style="background: #fde047; color: #713f12;">🧠 MATERI TEORI SERKOM BNSP</span>
                <h1 class="hero-title">Jawaban Emas Pertanyaan Wawancara Asesor BNSP</h1>
                <p class="hero-desc">
                    Mencakup 4 pilar teori utama uji kompetensi Junior Web Developer: Analisis Kebutuhan Sistem & Perangkat,
                    Fungsi ERD & Operasi SQL CRUD, Pengertian & Implementasi Query Agregasi/Relasional, serta Arsitektur MVC Laravel beserta alur siklus request-response.
                </p>
            </div>

            <!-- TEORI 1 -->
            <div id="sec-teori-1" class="section-card">
                <div class="section-header">
                    <div class="section-title">
                        <span>1. Analisis Kebutuhan Membangun Aplikasi Pemesanan Tiket Konser</span>
                    </div>
                    <span class="step-pill">Requirement Engineering</span>
                </div>
                <p class="step-desc">
                    Jika asesor bertanya: <em>"Apa saja yang Anda butuhkan dalam membangun Aplikasi Pemesanan Tiket Konser?"</em>, jawablah terstruktur dalam 5 aspek berikut:
                </p>

                <h3 class="sub-title">A. Kebutuhan Perangkat Keras (Hardware Requirements)</h3>
                <ul style="padding-left: 20px; line-height: 1.7; margin-bottom: 14px;">
                    <li><strong>Processor:</strong> Minimal Dual-Core 2.0 GHz (Direkomendasikan Intel Core i3/i5 atau AMD Ryzen 3/5) untuk kompilasi asset frontend Vite dan eksekusi server PHP.</li>
                    <li><strong>RAM (Memory):</strong> Minimal 4 GB (Disarankan 8 GB / 16 GB) agar mampu menjalankan VS Code, browser multi-tab, XAMPP (Apache & MySQL), serta terminal serentak tanpa lag.</li>
                    <li><strong>Media Penyimpanan:</strong> Minimal 10 GB ruang kosong SSD untuk instalasi OS, XAMPP, folder dependensi <code>vendor/</code>, <code>node_modules/</code>, dan file upload poster konser.</li>
                    <li><strong>Perangkat Input/Output & Jaringan:</strong> Keyboard, mouse, monitor minimal 1366x768, serta network interface aktif untuk localhost port 8000 dan 3306.</li>
                </ul>

                <h3 class="sub-title">B. Kebutuhan Perangkat Lunak (Software Stack Requirements)</h3>
                <ul style="padding-left: 20px; line-height: 1.7; margin-bottom: 14px;">
                    <li><strong>Sistem Operasi:</strong> Windows 10/11, Ubuntu Linux, atau macOS.</li>
                    <li><strong>Web Server & DBMS:</strong> XAMPP (Apache 2.4 sebagai web server lokal dan MySQL 8.0/MariaDB 10.4 sebagai RDBMS InnoDB).</li>
                    <li><strong>Bahasa Pemrograman:</strong> PHP 8.1 / 8.2+ dengan ekstensi aktif: <code>pdo_mysql</code>, <code>mbstring</code>, <code>openssl</code>, <code>fileinfo</code>, <code>gd</code>.</li>
                    <li><strong>Package Manager:</strong> Composer (dependensi PHP Laravel) dan Node.js v18+ & NPM (kompilasi Vite asset frontend).</li>
                    <li><strong>Code Editor:</strong> Visual Studio Code dengan ekstensi <em>PHP Intelephense</em> dan <em>Laravel Blade Snippets</em>.</li>
                    <li><strong>Database Client:</strong> phpMyAdmin / HeidiSQL untuk verifikasi struktur tabel dan foreign key.</li>
                </ul>

                <h3 class="sub-title">C. Kebutuhan Fungsional (Functional Requirements)</h3>
                <table class="custom-table">
                    <thead>
                        <tr>
                            <th style="width: 20%;">Peran Pengguna</th>
                            <th>Fitur-Fitur Kunci yang Wajib Tersedia</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>Role Customer (Pembeli)</strong></td>
                            <td>
                                1. Registrasi akun baru & Login terotentikasi.<br>
                                2. Menjelajahi katalog konser aktif yang kuota stoknya masih tersedia (stok > 0).<br>
                                3. Memilih kategori tiket (VIP/Festival/Regular) dan kuantitas pesanan.<br>
                                4. Checkout transaksi secara atomik (kode booking unik otomatis <code>TKT-YYYYMMDD-XXXX</code>) & kuota berkurang seketika.<br>
                                5. Riwayat pembelian tiket pada menu <em>Tiket Saya</em> dan cetak E-Tiket digital.
                            </td>
                        </tr>
                        <tr>
                            <td><strong>Role Administrator</strong></td>
                            <td>
                                1. Login dengan otentikasi role admin terproteksi middleware <code>IsAdmin</code>.<br>
                                2. Dashboard Rekapitulasi: Kartu ringkasan omset total penjualan rupiah, total tiket terjual, filter tanggal & status transaksi.<br>
                                3. Perubahan status transaksi (Pending -> Paid / Cancelled) dan cetak laporan resmi rekapitulasi.<br>
                                4. CRUD Master Tiket Konser lengkap dengan upload gambar poster ke storage public.<br>
                                5. CRUD Manajemen Data Pengguna (Admin & Customer) dengan pencarian, filter peran, dan proteksi anti self-delete.
                            </td>
                        </tr>
                    </tbody>
                </table>

                <h3 class="sub-title">D. Kebutuhan Non-Fungsional (Non-Functional Requirements)</h3>
                <ul style="padding-left: 20px; line-height: 1.7;">
                    <li><strong>Keamanan (Security):</strong> Password di-hash menggunakan algoritma Bcrypt (<code>Hash::make()</code>), pencegahan CSRF via token <code>@csrf</code> di seluruh formulir, proteksi SQL Injection menggunakan PDO Prepared Statements (Eloquent ORM), dan otorisasi hak akses berbasis middleware.</li>
                    <li><strong>Integritas Data (Data Integrity):</strong> Menggunakan MySQL InnoDB dengan Database Transaction (<code>DB::transaction</code>) untuk mencegah race condition / overbooking, serta aturan Foreign Key <code>ON DELETE CASCADE</code>.</li>
                    <li><strong>Performa & Kemudahan Penggunaan:</strong> Antarmuka responsif ramah perangkat bergerak menggunakan Tailwind CSS, validasi server informatif, dan waktu muat halaman di bawah 2 detik.</li>
                </ul>
            </div>

            <!-- TEORI 2 -->
            <div id="sec-teori-2" class="section-card">
                <div class="section-header">
                    <div class="section-title">
                        <span>2. Fungsi ERD & Operasi CRUD dalam Bahasa SQL</span>
                    </div>
                    <span class="step-pill">Database Design & Manipulation</span>
                </div>

                <h3 class="sub-title">A. Fungsi ERD (Entity Relationship Diagram)</h3>
                <p style="margin-bottom: 12px; line-height: 1.6;">
                    ERD adalah diagram pemodelan visual yang mendeskripsikan struktur basis data, entitas, atribut, dan relasi logis antar-tabel sebelum diterapkan ke dalam database fisik.
                    Fungsi utamanya meliputi:
                </p>
                <ol style="padding-left: 20px; line-height: 1.7; margin-bottom: 16px;">
                    <li><strong>Cetak Biru (Blueprint) Perancangan:</strong> Panduan visual utama bagi developer untuk menyusun migration file dan model Eloquent secara terstruktur.</li>
                    <li><strong>Mendefinisikan Entitas & Atribut:</strong> Menetapkan tabel apa saja yang ada (<code>users</code>, <code>tickets</code>, <code>orders</code>, <code>order_details</code>) beserta tipe data dan Primary Key (PK).</li>
                    <li><strong>Menetapkan Kardinalitas Relasi:</strong> Menentukan keterkaitan 1:N (Satu User memiliki banyak Orders, Satu Order memiliki banyak OrderDetails) dan N:M (Orders ke Tickets melalui tabel pivot OrderDetails).</li>
                    <li><strong>Menjaga Integritas Referensial:</strong> Menentukan aturan Foreign Key seperti <code>ON DELETE CASCADE</code> agar tidak timbul data yatim (<em>orphan records</em>).</li>
                    <li><strong>Mencegah Redundansi Data:</strong> Membantu normalisasi database (1NF, 2NF, 3NF) agar data tidak terduplikasi.</li>
                </ol>

                <h3 class="sub-title">B. Fungsi CRUD dalam Bahasa SQL & Contoh Nyata Kasus Tiket Konser</h3>
                <p style="margin-bottom: 12px;">CRUD adalah singkatan dari 4 operasi inti manipulasi data pada basis data relasional:</p>
                <table class="custom-table">
                    <thead>
                        <tr>
                            <th style="width: 10%;">Huruf</th>
                            <th style="width: 15%;">Operasi</th>
                            <th style="width: 25%;">Perintah SQL</th>
                            <th>Fungsi Utama & Penjelasan</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong style="color: #10b981;">C</strong></td>
                            <td><strong>Create</strong></td>
                            <td><code>INSERT INTO ... VALUES</code></td>
                            <td>Menambahkan baris rekaman baru ke dalam tabel basis data.</td>
                        </tr>
                        <tr>
                            <td><strong style="color: #3b82f6;">R</strong></td>
                            <td><strong>Read</strong></td>
                            <td><code>SELECT ... FROM ... WHERE</code></td>
                            <td>Membaca, mengambil, menyaring, dan menampilkan data rekaman tabel.</td>
                        </tr>
                        <tr>
                            <td><strong style="color: #f59e0b;">U</strong></td>
                            <td><strong>Update</strong></td>
                            <td><code>UPDATE ... SET ... WHERE</code></td>
                            <td>Memperbarui atau mengubah nilai data yang telah ada pada baris tabel tertentu.</td>
                        </tr>
                        <tr>
                            <td><strong style="color: #ef4444;">D</strong></td>
                            <td><strong>Delete</strong></td>
                            <td><code>DELETE FROM ... WHERE</code></td>
                            <td>Menghapus baris rekaman data dari tabel basis data.</td>
                        </tr>
                    </tbody>
                </table>

                {btk.render_code_box(code_sql_crud, "Contoh Perintah SQL CRUD Tiket Konser", "sql", "SQL Query")}
            </div>

            <!-- TEORI 3 -->
            <div id="sec-teori-3" class="section-card">
                <div class="section-header">
                    <div class="section-title">
                        <span>3. Apa Itu Query, Fungsi SQL, dan Contoh Nyata</span>
                    </div>
                    <span class="step-pill">SQL Queries & Functions</span>
                </div>

                <h3 class="sub-title">A. Pengertian Query</h3>
                <p style="margin-bottom: 12px; line-height: 1.6;">
                    <strong>Query</strong> adalah instruksi atau perintah terstruktur dalam bahasa SQL yang dikirimkan oleh aplikasi ke Relational Database Management System (RDBMS)
                    untuk meminta data, memfilter kondisi tertentu, melakukan perhitungan matematika, mengupdate rekaman, atau memanipulasi struktur tabel.
                </p>

                <h3 class="sub-title">B. Fungsi & Manfaat Query</h3>
                <ul style="padding-left: 20px; line-height: 1.7; margin-bottom: 14px;">
                    <li><strong>Penyaringan Data Presisi (<code>WHERE</code>, <code>LIKE</code>):</strong> Mengambil data secara spesifik tanpa membuang memori server.</li>
                    <li><strong>Penggabungan Relasi Multi-Tabel (<code>JOIN</code>):</strong> Menyajikan data terpadu dari beberapa tabel yang terpisah (misal: menyajikan nama customer dari tabel orders bersama judul konser dari tabel tickets).</li>
                    <li><strong>Kalkulasi & Agregasi Statistik Cepat (<code>SUM</code>, <code>COUNT</code>, <code>AVG</code>):</strong> Menghitung omset kotor, total tiket terjual, dan jumlah order langsung di level mesin database secara instan.</li>
                    <li><strong>Pengelompokan Analisis (<code>GROUP BY</code>):</strong> Mengelompokkan transaksi untuk mengetahui kategori tiket mana yang paling laris.</li>
                    <li><strong>Efisiensi Bandwidth:</strong> Menghindari penarikan data yang tidak perlu (<code>SELECT id, concert_name</code> vs <code>SELECT *</code>).</li>
                </ul>

                <h3 class="sub-title">C. Contoh Query Relasional & Agregasi Kasus Tiket Konser</h3>
                {btk.render_code_box(code_sql_query, "Query SQL Relasional & Agregasi", "sql", "SQL Query")}
            </div>

            <!-- TEORI 4 -->
            <div id="sec-teori-4" class="section-card">
                <div class="section-header">
                    <div class="section-title">
                        <span>4. Arsitektur MVC Laravel (Model - View - Controller)</span>
                    </div>
                    <span class="step-pill">Software Architecture</span>
                </div>

                <h3 class="sub-title">A. Definisi Konsep Tiga Komponen MVC</h3>
                <ul style="padding-left: 20px; line-height: 1.7; margin-bottom: 14px;">
                    <li><strong>Model (M):</strong> Bertanggung jawab mengelola data dan struktur tabel, berkomunikasi langsung dengan database MySQL melalui Eloquent ORM, dan mendefinisikan relasi antar-tabel (terletak di <code>app/Models/</code>, contoh: <code>Ticket.php</code>, <code>User.php</code>, <code>Order.php</code>).</li>
                    <li><strong>View (V):</strong> Bertanggung jawab menyajikan antarmuka grafis kepada pengguna (UI/UX) menggunakan Blade template engine yang modular (terletak di <code>resources/views/</code>, contoh: <code>customer/concerts.blade.php</code>, <code>admin/orders/index.blade.php</code>).</li>
                    <li><strong>Controller (C):</strong> Bertindak sebagai otak atau jembatan penghubung (<em>traffic controller</em>). Menerima HTTP Request dari rute (<em>route</em>), memanggil Model untuk mengambil atau menyimpan data, menerapkan logika bisnis (misal validasi input atau transaksi atomik kuota tiket), lalu mengoper data ke View untuk dirender ke browser (terletak di <code>app/Http/Controllers/</code>).</li>
                    <li><strong>Routing (<code>routes/web.php</code>):</strong> Pintu gerbang utama yang memetakan URL dan method HTTP (GET, POST, PUT, DELETE, PATCH) ke Controller yang sesuai.</li>
                </ul>

                <h3 class="sub-title">B. Diagram Alur Kerja Request-Response Lifecycle di Laravel</h3>
                <div class="mvc-flow">
                    <div class="mvc-step">
                        <div class="step-circle">1</div>
                        <div class="step-info">
                            <h5>Client Browser Mengirim Request</h5>
                            <p>Pengguna mengklik tombol "Beli Tiket" (mengirimkan HTTP POST ke <code>/checkout</code>).</p>
                        </div>
                    </div>
                    <div class="mvc-step">
                        <div class="step-circle">2</div>
                        <div class="step-info">
                            <h5>Routing (routes/web.php)</h5>
                            <p>Route mencocokkan URL dan mengarahkan request ke <code>BookingController@checkout</code>.</p>
                        </div>
                    </div>
                    <div class="mvc-step">
                        <div class="step-circle">3</div>
                        <div class="step-info">
                            <h5>Middleware Filter</h5>
                            <p>Middleware <code>auth</code> dan <code>VerifyCsrfToken</code> memeriksa apakah pengguna sudah login dan token CSRF valid.</p>
                        </div>
                    </div>
                    <div class="mvc-step">
                        <div class="step-circle">4</div>
                        <div class="step-info">
                            <h5>Controller Logic & Model Execution</h5>
                            <p>Controller memvalidasi input, lalu memanggil Model <code>Ticket</code> dan <code>Order</code> untuk menyimpan data dan mengurangi kuota tiket.</p>
                        </div>
                    </div>
                    <div class="mvc-step">
                        <div class="step-circle">5</div>
                        <div class="step-info">
                            <h5>Database Execution & Commit</h5>
                            <p>Mesin MySQL mengeksekusi perintah SQL secara atomik (ACID) dan menyimpan record ke disk storage.</p>
                        </div>
                    </div>
                    <div class="mvc-step">
                        <div class="step-circle">6</div>
                        <div class="step-info">
                            <h5>View Rendering & HTTP Response</h5>
                            <p>Controller merender file Blade View dengan flash message sukses, dan mengembalikannya ke browser sebagai HTML utuh.</p>
                        </div>
                    </div>
                </div>

                <h3 class="sub-title">C. Keuntungan Menggunakan Pola MVC di Laravel</h3>
                <ol style="padding-left: 20px; line-height: 1.7;">
                    <li><strong>Separation of Concerns:</strong> Pemisahan tugas yang jelas sehingga kode program rapi, mudah dibaca, dan tidak campur aduk (kode HTML terpisah dari baris SQL).</li>
                    <li><strong>Kemudahan Pemeliharaan (Maintainability):</strong> Jika ada revisi desain UI, developer cukup mengubah file Blade tanpa takut merusak logika transaksi di Controller.</li>
                    <li><strong>Reusability Kode:</strong> Satu Model dapat digunakan oleh banyak Controller yang berbeda secara efisien.</li>
                    <li><strong>Standar Penilaian Sertifikasi BNSP:</strong> Menunjukkan kompetensi pemrograman web berorientasi objek yang terstruktur dan profesional.</li>
                </ol>
            </div>

            <!-- TEORI 5 -->
            <div id="sec-teori-5" class="section-card">
                <div class="section-header">
                    <div class="section-title">
                        <span>5. Tools & Stack Teknologi yang Digunakan</span>
                    </div>
                    <span class="step-pill">Development Ecosystem</span>
                </div>
                <p class="step-desc">
                    Penjelasan komprehensif seluruh ekosistem tools, framework, dan dependensi pendukung yang digunakan dalam membangun dan menguji aplikasi:
                </p>

                <table class="custom-table">
                    <thead>
                        <tr>
                            <th style="width: 25%;">Nama Tool / Teknologi</th>
                            <th style="width: 20%;">Kategori</th>
                            <th>Fungsi & Peranan Utama dalam Proyek</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>Laravel 10/11</strong></td>
                            <td>Backend Framework</td>
                            <td>Menyediakan struktur MVC yang kokoh, Eloquent ORM, migrasi skema database, routing ekspresif, middleware otentikasi, dan sistem proteksi keamanan CSRF/XSS.</td>
                        </tr>
                        <tr>
                            <td><strong>PHP 8.2+</strong></td>
                            <td>Programming Language</td>
                            <td>Bahasa pemrograman server-side utama dengan fitur modern (Typed Properties, Match Expressions, Readonly Classes, dan performa JIT engine cepat).</td>
                        </tr>
                        <tr>
                            <td><strong>MySQL 8.0 (InnoDB)</strong></td>
                            <td>RDBMS</td>
                            <td>Mesin basis data relasional yang menjamin transaksi ACID, referential integrity via Foreign Keys, serta penguncian data tingkat baris (row-level locking).</td>
                        </tr>
                        <tr>
                            <td><strong>Laravel Breeze</strong></td>
                            <td>Auth Starter Kit</td>
                            <td>Menyediakan boilerplate sistem autentikasi lengkap (Login, Register, Password Reset, Profile Management) yang bersih dan terintegrasi Tailwind CSS.</td>
                        </tr>
                        <tr>
                            <td><strong>Tailwind CSS 3.x</strong></td>
                            <td>CSS Framework</td>
                            <td>Utility-first CSS framework untuk menghasilkan antarmuka modern, elegan, responsif, dan ringan tanpa menulis file CSS kustom yang berantakan.</td>
                        </tr>
                        <tr>
                            <td><strong>Vite & Node.js</strong></td>
                            <td>Frontend Build Tool</td>
                            <td>Bundler asset frontend generasi terbaru dengan Hot Module Replacement (HMR) kilat untuk mengompilasi file JS dan Tailwind CSS ke folder <code>public/build/</code>.</td>
                        </tr>
                        <tr>
                            <td><strong>Visual Studio Code</strong></td>
                            <td>Source Code Editor</td>
                            <td>IDE utama dilengkapi ekstensi PHP Intelephense, Laravel Blade Snippets, dan Tailwind CSS IntelliSense untuk mempercepat penulisan sintaks.</td>
                        </tr>
                        <tr>
                            <td><strong>XAMPP</strong></td>
                            <td>Local Server Suite</td>
                            <td>Paket server lokal terpadu yang menjalankan modul web server Apache 2.4 dan database server MySQL/MariaDB pada komputer pengembang.</td>
                        </tr>
                        <tr>
                            <td><strong>phpMyAdmin</strong></td>
                            <td>Database GUI Tool</td>
                            <td>Antarmuka grafis berbasis web untuk memantau struktur tabel, memvalidasi index/relasi foreign key, dan mengeksekusi kueri SQL secara langsung.</td>
                        </tr>
                        <tr>
                            <td><strong>Git & GitHub</strong></td>
                            <td>Version Control System</td>
                            <td>Mencatat riwayat perubahan kode (commit), kolaborasi tim, dan manajemen repositori proyek secara profesional.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    """)

    # TAB 3: KASUS REFERENSI RESTORAN / FOOD
    code_resto_mig = r"""// database/migrations/xxxx_create_foods_table.php
public function up(): void
{
    Schema::create('foods', function (Blueprint $table) {
        $table->id();
        $table->string('name');
        $table->enum('category', ['Makanan', 'Minuman', 'Cemilan']);
        $table->integer('price');
        $table->text('description');
        $table->string('image')->nullable();
        $table->timestamps();
    });
}"""

    code_resto_ctrl = r"""<?php
// app/Http/Controllers/FoodController.php
namespace App\Http\Controllers;

use App\Models\Food;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Storage;

class FoodController extends Controller
{
    public function index()
    {
        $foods = Food::latest()->paginate(10);
        return view('foods.index', compact('foods'));
    }

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
        return redirect()->route('foods.index')->with('success', 'Menu berhasil ditambahkan!');
    }
}"""

    h.append(f"""
        <!-- TAB 3: KASUS REFERENSI MAKANAN/RESTO -->
        <div id="tab-makanan" class="tab-pane">
            <div class="hero-banner" style="background: linear-gradient(135deg, #7c2d12 0%, #c2410c 50%, #ea580c 100%); border-color: #ea580c;">
                <span class="hero-badge" style="background: #fed7aa; color: #7c2d12;">🍔 KASUS REFERENSI (RESTORAN)</span>
                <h1 class="hero-title">Aplikasi Pemesanan Makanan & Resto Berbasis Web</h1>
                <p class="hero-desc">
                    Jika asesor penguji besok memberikan kasus restoran / pemesanan makanan, struktur logikanya 100% analog dengan tiket konser:
                    tabel <code>foods</code> (pengganti <code>tickets</code>), <code>orders</code> (dengan <code>table_number</code>),
                    dan <code>order_details</code>.
                </p>
            </div>

            <div id="sec-resto-perbandingan" class="section-card">
                <div class="section-header">
                    <div class="section-title">
                        <span>🔄 1. Perbandingan Langsung: Tiket Konser vs Restoran</span>
                    </div>
                    <span class="step-pill">Pemetaan Logika</span>
                </div>

                <table class="custom-table">
                    <thead>
                        <tr>
                            <th>Fitur / Komponen</th>
                            <th>Kasus Tiket Konser</th>
                            <th>Kasus Restoran / Food</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>Tabel Master Produk</strong></td>
                            <td><code>tickets</code> (nama konser, venue, harga, stok tiket)</td>
                            <td><code>foods</code> (nama menu, kategori makanan/minuman, harga)</td>
                        </tr>
                        <tr>
                            <td><strong>Tabel Transaksi</strong></td>
                            <td><code>orders</code> (order_code, total_price, status)</td>
                            <td><code>orders</code> (customer_name, table_number, total_price)</td>
                        </tr>
                        <tr>
                            <td><strong>Tabel Rincian</strong></td>
                            <td><code>order_details</code> (order_id, ticket_id, qty, subtotal)</td>
                            <td><code>order_details</code> (order_id, food_id, quantity, subtotal)</td>
                        </tr>
                        <tr>
                            <td><strong>Dashboard Admin</strong></td>
                            <td>Rekapitulasi pesanan tiket, filter tanggal, status update</td>
                            <td>Rekapitulasi pesanan per meja, filter tanggal, status pesanan</td>
                        </tr>
                        <tr>
                            <td><strong>Halaman Customer</strong></td>
                            <td>Katalog konser, booking tiket, cetak E-Tiket</td>
                            <td>Katalog menu makanan, pilih meja, checkout pesanan</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div id="sec-resto-skema" class="section-card">
                <div class="section-header">
                    <div class="section-title">
                        <span>🗂️ 2. Skema Migration Tabel Makanan (`foods`)</span>
                    </div>
                    <span class="step-pill">Migration</span>
                </div>
                {btk.render_code_box(code_resto_mig, "database/migrations/xxxx_create_foods_table.php", "php", "Migration")}
            </div>

            <div id="sec-resto-crud" class="section-card">
                <div class="section-header">
                    <div class="section-title">
                        <span>📋 3. Controller CRUD Master Menu Makanan</span>
                    </div>
                    <span class="step-pill">Controller</span>
                </div>
                {btk.render_code_box(code_resto_ctrl, "app/Http/Controllers/FoodController.php", "php", "Controller")}
            </div>
        </div>
    """)

    # TAB 4: CHECKLIST 15 MENIT ANTI-PANIK
    h.append("""
        <!-- TAB 4: CHECKLIST 15 MENIT -->
        <div id="tab-checklist" class="tab-pane">
            <div class="hero-banner" style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%); border-color: #475569;">
                <span class="hero-badge" style="background: #fde047; color: #713f12;">⚡ URUTAN EKSEKUSI H-1</span>
                <h1 class="hero-title">Checklist 15 Menit Anti-Panik di Hadapan Asesor</h1>
                <p class="hero-desc">
                    Ikuti urutan langkah demi langkah ini tepat setelah Anda duduk di depan komputer penguji.
                    Centang setiap kotak tugas yang telah selesai dijalankan (progres tersimpan otomatis di browser).
                </p>
            </div>

            <div class="section-card">
                <div class="section-header">
                    <div class="section-title">
                        <span>✅ Daftar Tugas Praktik Mandiri</span>
                    </div>
                    <span class="step-pill">15 Menit Selesai</span>
                </div>

                <div id="checklistContainer">
                    <div class="checklist-item">
                        <input type="checkbox" id="chk1" onchange="saveChecklist()">
                        <div>
                            <div class="checklist-text">1. Nyalakan XAMPP Control Panel</div>
                            <div class="checklist-sub">Klik tombol "Start" pada modul Apache dan MySQL hingga berlatar hijau.</div>
                        </div>
                    </div>

                    <div class="checklist-item">
                        <input type="checkbox" id="chk2" onchange="saveChecklist()">
                        <div>
                            <div class="checklist-text">2. Buat Database Baru di phpMyAdmin</div>
                            <div class="checklist-sub">Buka browser <code>http://localhost/phpmyadmin</code>, buat database <code>tiketkonser</code> (Collation: utf8mb4_unicode_ci).</div>
                        </div>
                    </div>

                    <div class="checklist-item">
                        <input type="checkbox" id="chk3" onchange="saveChecklist()">
                        <div>
                            <div class="checklist-text">3. Buka Folder Proyek di VS Code & Konfigurasi .env</div>
                            <div class="checklist-sub">Pastikan <code>DB_DATABASE=tiketkonser</code>, <code>DB_USERNAME=root</code>, dan <code>DB_PASSWORD=</code>.</div>
                        </div>
                    </div>

                    <div class="checklist-item">
                        <input type="checkbox" id="chk4" onchange="saveChecklist()">
                        <div>
                            <div class="checklist-text">4. Eksekusi Migrasi & Seeder Database</div>
                            <div class="checklist-sub">Jalankan di terminal: <code>php artisan migrate:fresh --seed</code> (pastikan tabel & akun default terbuat tanpa error).</div>
                        </div>
                    </div>

                    <div class="checklist-item">
                        <input type="checkbox" id="chk5" onchange="saveChecklist()">
                        <div>
                            <div class="checklist-text">5. Buat Tautan Symbolic Link Folder Storage</div>
                            <div class="checklist-sub">Jalankan di terminal: <code>php artisan storage:link</code> agar banner poster dapat diakses publik.</div>
                        </div>
                    </div>

                    <div class="checklist-item">
                        <input type="checkbox" id="chk6" onchange="saveChecklist()">
                        <div>
                            <div class="checklist-text">6. Kompilasi Asset Frontend Vite (Tailwind CSS)</div>
                            <div class="checklist-sub">Jalankan di terminal: <code>npm run build</code> (mencegah error Vite manifest not found).</div>
                        </div>
                    </div>

                    <div class="checklist-item">
                        <input type="checkbox" id="chk7" onchange="saveChecklist()">
                        <div>
                            <div class="checklist-text">7. Jalankan Server Lokal Laravel</div>
                            <div class="checklist-sub">Jalankan di terminal: <code>php artisan serve</code> lalu buka <code>http://127.0.0.1:8000</code>.</div>
                        </div>
                    </div>

                    <div class="checklist-item">
                        <input type="checkbox" id="chk8" onchange="saveChecklist()">
                        <div>
                            <div class="checklist-text">8. Demonstrasikan Alur Customer ke Asesor</div>
                            <div class="checklist-sub">Login sebagai <code>customer@gmail.com</code> (password: <code>password123</code>), lakukan pemesanan tiket, dan cetak E-Tiket.</div>
                        </div>
                    </div>

                    <div class="checklist-item">
                        <input type="checkbox" id="chk9" onchange="saveChecklist()">
                        <div>
                            <div class="checklist-text">9. Demonstrasikan Alur Admin ke Asesor</div>
                            <div class="checklist-sub">Login sebagai <code>admin@tiket.com</code> (password: <code>password123</code>), buka dashboard rekap, kelola tiket konser, dan manajemen pengguna.</div>
                        </div>
                    </div>
                </div>

                <div style="margin-top: 14px; text-align: right;">
                    <button onclick="resetChecklist()" style="background: #e2e8f0; border: none; padding: 6px 12px; border-radius: 6px; font-size: 11.5px; font-weight: bold; cursor: pointer;">
                        Reset Checklist
                    </button>
                </div>
            </div>
        </div>
    """)

    # TAB 5: SESI GRILL-ME ASESOR (10 Q&A EMAS)
    grill_data = [
        ("Mengapa Anda memisahkan tabel orders dan order_details, bukan langsung menyimpan tiket di tabel orders?",
         "Karena hubungan antara pesanan dan tiket adalah One-to-Many (1 pemesan bisa membeli beberapa tiket sekaligus). Memisahkan tabel ke dalam order_details menerapkan kaidah Normalisasi Basis Data (3NF), mencegah redundansi data, dan memungkinkan pencatatan harga satuan historis saat transaksi terjadi."),
        
        ("Bagaimana sistem Anda mencegah race condition ketika tiket tersisa 1 namun dibeli oleh dua customer bersamaan?",
         "Saya membungkus alur checkout menggunakan Database Transaction (DB::beginTransaction() dan DB::commit()) serta validasi pengecekan stok di level backend server. Pada aplikasi enterprise skala besar, kita dapat menerapkan Pessimistic Locking dengan menambahkan lockForUpdate() pada query tiket."),
        
        ("Apa fungsi perintah php artisan storage:link?",
         "Membuat tautan pintasan (symbolic link) dari direktori privat storage/app/public ke direktori publik public/storage, sehingga file upload (seperti banner poster konser) dapat diakses dan ditampilkan dengan aman oleh browser melalui URL publik."),
        
        ("Apa itu Mass Assignment Vulnerability dan bagaimana Laravel melindunginya?",
         "Kerentanan keamanan di mana penyerang menyisipkan field berbahaya ke dalam formulir HTTP (seperti menyusupkan input role=admin saat registrasi). Laravel memproteksinya dengan mewajibkan array properti $fillable pada Model, sehingga hanya kolom yang didefinisikan secara eksplisit yang diizinkan diisi secara massal."),
        
        ("Jelaskan fungsi sintaks @csrf pada setiap formulir Blade!",
         "Menghasilkan token rahasia satu kali pakai (*anti-forgery token*) yang divalidasi oleh VerifyCsrfToken Middleware untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF)."),
        
        ("Apa perbedaan query Eloquent menggunakan with() dibanding tanpa with()?",
         "with() menerapkan teknik Eager Loading yang menggabungkan query relasi di awal, sehingga menghindari masalah N+1 Query Problem yang dapat memperlambat kinerja server secara signifikan."),
        
        ("Kapan kita menggunakan relasi belongsTo dan kapan hasMany?",
         "belongsTo diletakkan pada model tabel anak yang memegang kolom Foreign Key (seperti OrderDetail yang memegang order_id dan ticket_id). Sedangkan hasMany diletakkan pada model tabel induk yang memiliki banyak relasi (seperti Order yang memiliki banyak OrderDetail)."),
        
        ("Mengapa harga tiket disimpan ulang di kolom unit_price pada order_details padahal sudah ada di tabel tickets?",
         "Untuk menjaga integritas data historis keuangan. Jika suatu saat panitia menaikkan harga tiket master dari 500 ribu menjadi 700 ribu, total omset pesanan masa lalu tidak akan ikut berubah secara keliru."),
        
        ("Bagaimana cara Anda membatasi agar customer biasa tidak bisa mengakses URL /admin/dashboard?",
         "Menggunakan Middleware otorisasi khusus (IsAdmin) yang memeriksa apakah Auth::user()->role === 'admin'. Jika bukan admin, pengguna otomatis ditolak dan diarahkan kembali."),
        
        ("Sebutkan tahapan siklus hidup request dari browser sampai tampilan konser muncul!",
         "Client HTTP Request -> routes/web.php -> Middleware (Auth/CSRF) -> Controller -> Model Eloquent -> Database MySQL (InnoDB) -> Controller mengolah data -> Blade View Render HTML -> Browser Client menampilkan halaman.")
    ]

    h.append("""
        <!-- TAB 5: SESI GRILL-ME ASESOR -->
        <div id="tab-grill" class="tab-pane">
            <div class="hero-banner" style="background: linear-gradient(135deg, #831843 0%, #be185d 50%, #db2777 100%); border-color: #db2777;">
                <span class="hero-badge" style="background: #fbcfe8; color: #831843;">🔥 SESI GRILL-ME WAWANCARA</span>
                <h1 class="hero-title">10 Pertanyaan Jebakan Asesor & Jawaban Ilmiah</h1>
                <p class="hero-desc">
                    Hafalkan konsep dan kata kunci dari 10 pertanyaan teknis berikut. Asesor menguji kedalaman pemahaman Anda
                    terhadap arsitektur sistem, keamanan data, dan integritas basis data.
                </p>
            </div>

            <div id="sec-grill-box" class="section-card">
    """)

    for idx, (q, a) in enumerate(grill_data, 1):
        h.append(f"""
                <div class="callout callout-warning" style="margin-bottom: 14px;">
                    <div class="callout-title">❓ Pertanyaan {idx}: "{html.escape(q)}"</div>
                    <div style="margin-top: 6px; font-weight: 600; color: #1e293b;">
                        🗣️ <span style="color: #15803d;">Jawaban Rekomendasi:</span> {html.escape(a)}
                    </div>
                </div>
        """)

    h.append("""
            </div>
        </div>
    """)

    # TAB 6: KAMUS ERROR & TROUBLESHOOTING INSTAN
    errors_data = [
        ("419 Page Expired",
         "Formulir HTML tidak memiliki direktif token proteksi CSRF.",
         "Tambahkan direktif @csrf tepat di bawah tag pembuka <form>."),
        
        ("SQLSTATE[23000]: Foreign key constraint fails",
         "Urutan penghapusan atau penyisipan tabel relasi keliru, atau ID relasi tidak ditemukan.",
         "Pastikan tabel induk (tickets/users) sudah terisi sebelum order_details. Jalankan php artisan migrate:fresh --seed."),
        
        ("The GET method is not supported for route admin/tickets/1",
         "Formulir HTML menggunakan method POST namun di route terdaftar sebagai DELETE, PUT, atau PATCH.",
         "Tambahkan @method('DELETE') atau @method('PATCH') di dalam formulir."),
        
        ("Vite manifest not found",
         "Asset frontend Tailwind CSS belum dikompilasi oleh Node.js.",
         "Buka terminal dan jalankan perintah: npm run build."),
        
        ("Target class [TicketController] does not exist",
         "Controller belum diimpor (use) di baris teratas file routes/web.php.",
         "Tambahkan: use App\\Http\\Controllers\\Admin\\TicketController; pada bagian atas routes/web.php."),
        
        ("Gambar poster tidak muncul (Broken Link)",
         "Folder storage/app/public belum ditautkan ke public/storage.",
         "Jalankan di terminal: php artisan storage:link, dan panggil dengan asset('storage/' . $ticket->poster)."),
        
        ("Access denied for user 'root'@'localhost'",
         "Konfigurasi kredensial MySQL di file .env keliru.",
         "Buka file .env, ubah DB_USERNAME=root dan kosongkan DB_PASSWORD=."),
        
        ("Class 'App\\Models\\Order' not found",
         "Namespace Model belum diimpor pada bagian atas file Controller.",
         "Tambahkan deklarasi: use App\\Models\\Order; di bagian atas Controller.")
    ]

    h.append("""
        <!-- TAB 6: KAMUS ERROR -->
        <div id="tab-error" class="tab-pane">
            <div class="hero-banner" style="background: linear-gradient(135deg, #7f1d1d 0%, #b91c1c 50%, #dc2626 100%); border-color: #dc2626;">
                <span class="hero-badge" style="background: #fecaca; color: #7f1d1d;">🚨 TROUBLESHOOTING KILAT</span>
                <h1 class="hero-title">Kamus Error & Solusi Instan 10 Detik</h1>
                <p class="hero-desc">
                    Jika saat ujian besok muncul pesan error merah di layar Anda, jangan panik!
                    Cari pesan error di tabel ini dan perbaiki langsung dalam hitungan detik.
                </p>
            </div>

            <div id="sec-error-box" class="section-card">
                <table class="custom-table">
                    <thead>
                        <tr>
                            <th style="width: 25%;">Pesan Error / Gejala</th>
                            <th style="width: 35%;">Penyebab Utama</th>
                            <th style="width: 40%;">Solusi Instan 10 Detik</th>
                        </tr>
                    </thead>
                    <tbody>
    """)

    for err, cause, sol in errors_data:
        h.append(f"""
                        <tr>
                            <td style="color: #dc2626; font-weight: bold; font-family: Consolas, monospace;">{html.escape(err)}</td>
                            <td>{html.escape(cause)}</td>
                            <td style="font-weight: bold; color: #15803d;">{html.escape(sol)}</td>
                        </tr>
        """)

    h.append("""
                    </tbody>
                </table>
            </div>
        </div>
    """)

    # Footer & Scripts
    h.append("""
        </main>
    </div>

    <script>
        // Tab Switcher
        function switchTab(tabId, btn) {
            document.querySelectorAll('.tab-pane').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
            
            const target = document.getElementById(tabId);
            if (target) {
                target.classList.add('active');
            }
            if (btn) {
                btn.classList.add('active');
            }

            // Adaptive Sidebar ToC for Active Tab
            const tocs = {
                'tab-tiket': 'tocTiket',
                'tab-teori': 'tocTeori',
                'tab-makanan': 'tocMakanan',
                'tab-checklist': 'tocChecklist',
                'tab-grill': 'tocGrill',
                'tab-error': 'tocError'
            };

            for (const key in tocs) {
                const el = document.getElementById(tocs[key]);
                if (el) {
                    el.style.display = (key === tabId) ? 'block' : 'none';
                }
            }

            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        // Copy Code to Clipboard
        function copyCode(btn) {
            const rawCode = btn.getAttribute('data-code');
            if (!rawCode) return;

            navigator.clipboard.writeText(rawCode).then(() => {
                const origText = btn.innerHTML;
                btn.innerHTML = '✓ Tersalin!';
                btn.style.background = '#15803d';
                btn.style.color = '#fff';
                setTimeout(() => {
                    btn.innerHTML = origText;
                    btn.style.background = '';
                    btn.style.color = '';
                }, 2000);
            }).catch(err => {
                // Fallback via textarea if clipboard permissions restricted
                const ta = document.createElement('textarea');
                ta.value = rawCode;
                document.body.appendChild(ta);
                ta.select();
                document.execCommand('copy');
                document.body.removeChild(ta);
                btn.innerHTML = '✓ Tersalin!';
                setTimeout(() => { btn.innerHTML = 'Salin'; }, 2000);
            });
        }

        // Search Content Filter
        function filterContent() {
            const q = document.getElementById('searchInput').value.toLowerCase().trim();
            const cards = document.querySelectorAll('.section-card, .callout');

            cards.forEach(card => {
                const text = card.innerText.toLowerCase();
                if (!q || text.includes(q)) {
                    card.style.display = '';
                } else {
                    card.style.display = 'none';
                }
            });
        }

        // Checklist State Persistence (localStorage)
        function saveChecklist() {
            const checks = {};
            for (let i = 1; i <= 9; i++) {
                const el = document.getElementById('chk' + i);
                if (el) checks['chk' + i] = el.checked;
            }
            localStorage.setItem('serkom_checklist', JSON.stringify(checks));
        }

        function loadChecklist() {
            const saved = localStorage.getItem('serkom_checklist');
            if (saved) {
                try {
                    const checks = JSON.parse(saved);
                    for (const key in checks) {
                        const el = document.getElementById(key);
                        if (el) el.checked = checks[key];
                    }
                } catch(e) {}
            }
        }

        function resetChecklist() {
            localStorage.removeItem('serkom_checklist');
            for (let i = 1; i <= 9; i++) {
                const el = document.getElementById('chk' + i);
                if (el) el.checked = false;
            }
        }

        // Init on load
        window.addEventListener('DOMContentLoaded', () => {
            loadChecklist();
        });
    </script>
</body>
</html>
""")

    full_html = "".join(h)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(full_html)

    size_kb = len(full_html.encode('utf-8')) / 1024
    print(f"Generated successfully: {OUTPUT_FILE} ({size_kb:.1f} KB)")

if __name__ == "__main__":
    make_html()
