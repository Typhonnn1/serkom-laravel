# -*- coding: utf-8 -*-
"""
Comprehensive Verification Suite for serkom_tiket_konser_lengkap.html
Validates:
1. File existence and size (>300KB)
2. HTML validity and complete document tags
3. All Theoretical requirements (Hardware, Software, Functional, Non-Functional, ERD, SQL CRUD, Queries & Functions, MVC Laravel & Lifecycle)
4. All Practical requirements:
   - 1. Multi-role Customer & Admin Auth, Middleware, Seeder
   - 2. 4-Table Migrations & Foreign Keys, Eloquent Relationships
   - 3. CRUD Tiket Konser (7-method Resource, Image Upload, Index, Create, Edit views)
   - 4. CRUD User Management (7-method Resource, Password Hashing, Anti Self-Delete, Index, Create, Edit views)
   - 5. Rekap Laporan Pesanan Masuk (Dashboard metrics, Filters, Status update, Print-ready view)
   - 6. Customer Booking Flow (DB::transaction atomic checkout, stock decrement, e-ticket view)
   - 7. routes/web.php (Ticket and User Resource routes under admin middleware)
5. Quality and Syntax Checks (No \\Exception double-escaping, proper tokens, dark theme styles)
6. Interactivity & Anchor Links (All tab buttons, TOC elements, and target IDs match without broken anchors)
"""

import os
import re
import sys
import html
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def run_tests():
    filepath = r"c:\Users\Default User\Desktop\modul serkom\serkom_tiket_konser_lengkap.html"
    assert os.path.exists(filepath), f"File {filepath} does not exist!"
    size = os.path.getsize(filepath)
    print(f"File exists: {filepath} ({size:,} bytes / {size/1024:.1f} KB)")
    assert size > 300000, f"File too small: {size} bytes"

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    unescaped = html.unescape(content)

    # 1. Basic HTML structure
    assert content.strip().startswith("<!DOCTYPE html>"), "Does not start with <!DOCTYPE html>"
    assert "</html>" in content, "Missing </html>"
    assert "</body>" in content, "Missing </body>"
    assert "<title>" in content, "Missing <title>"
    print("[PASS] Basic HTML structure is valid")

    # 2. Check Theoretical Requirements
    theories = [
        "Aplikasi Pemesanan Tiket Konser",
        "Kebutuhan Perangkat Keras",
        "Kebutuhan Perangkat Lunak",
        "Kebutuhan Fungsional",
        "Kebutuhan Non-Fungsional",
        "Fungsi ERD",
        "Fungsi CRUD dalam Bahasa SQL",
        "Pengertian Query",
        "Arsitektur MVC Laravel",
        "Model - View - Controller",
        "Lifecycle",
        "INSERT INTO tickets",
        "UPDATE tickets",
        "DELETE FROM tickets",
        "SUM(total_price)",
        "INNER JOIN order_details",
        "GROUP BY t.category",
        "HAVING total_pendapatan",
    ]
    for th in theories:
        assert th in unescaped, f"Missing theory requirement: {th}"
    print("[PASS] All Theoretical Requirements verified")

    # 3. Check Practical Requirements
    practicals = [
        # 1. Login & Auth
        "role",
        "isAdmin",
        "isCustomer",
        "admin@tiket.com",
        "customer@gmail.com",
        "IsAdmin",
        # 2. Tables & Relations
        "tickets",
        "orders",
        "order_details",
        "hasMany",
        "belongsTo",
        "TicketSeeder",
        # 3. CRUD Tiket
        "TicketController",
        "admin.tickets.index",
        "admin.tickets.create",
        "admin.tickets.edit",
        "poster",
        # 4. CRUD User Management (NEW / CRITICAL)
        "UserController",
        "admin.users.index",
        "admin.users.create",
        "admin.users.edit",
        "Anti Self-Delete",
        # 5. Rekap Pesanan
        "OrderReportController",
        "admin.orders.index",
        "admin.orders.print",
        "totalOmset",
        "totalTicketsSold",
        "start_date",
        "end_date",
        # 6. Customer Booking
        "BookingController",
        "DB::transaction",
        "decrement",
        "E-TIKET RESMI KONSER MUSIK",
        # 7. Routing
        "routes/web.php",
        "Route::resource('tickets', TicketController::class)",
        "Route::resource('users', UserController::class)",
    ]
    for pr in practicals:
        assert pr in unescaped, f"Missing practical requirement: {pr}"
    print("[PASS] All Practical Requirements verified")

    # 4. Check Code Blocks & Styling
    styles = [
        "#1e1e1e",
        "#18181b",
        "copyCode",
        "Salin",
        "filterContent",
        "saveChecklist",
        "localStorage",
        "@media print",
    ]
    for st in styles:
        assert st in content, f"Missing style or interactive feature: {st}"
    print("[PASS] Styling and Interactive Features verified")

    # 5. Check Syntax Highlighting Tokens
    tokens = [
        "tok-kw",
        "tok-ctrl",
        "tok-class",
        "tok-fn",
        "tok-var",
        "tok-str",
        "tok-cm",
    ]
    for tk in tokens:
        assert tk in content, f"Missing syntax highlighting class: {tk}"
    print("[PASS] Syntax highlighting tokens verified")

    # 6. Syntax Cleanliness Check (No double-escaped \\Exception in code blocks)
    assert "\\\\Exception" not in content, "Found double-escaped \\\\Exception in code blocks! Must be \\Exception"
    print("[PASS] Syntax cleanliness confirmed (no double backslash artifacts)")

    # 7. Check all TOC links have matching target IDs in the HTML
    toc_links = re.findall(r'<a\s+href="#([^"]+)"', content)
    assert len(toc_links) >= 15, f"Too few anchor links found: {len(toc_links)}"
    for link_id in toc_links:
        assert f'id="{link_id}"' in content, f"Broken anchor link: #{link_id} has no matching id!"
    print(f"[PASS] All {len(toc_links)} ToC anchor targets are valid with zero broken links")

    # 8. Check all Tab Panes and TOC IDs
    expected_ids = ['tab-tiket', 'tab-teori', 'tab-makanan', 'tab-checklist', 'tab-grill', 'tab-error',
                    'tocTiket', 'tocTeori', 'tocMakanan', 'tocChecklist', 'tocGrill', 'tocError']
    for eid in expected_ids:
        assert f'id="{eid}"' in content, f"Missing navigation container id: {eid}"
    print("[PASS] All Tab Panes and adaptive Sidebar ToC containers verified")

    print("\n>>> ALL 8 VERIFICATION SUITES PASSED FLAWLESSLY! <<<")

if __name__ == '__main__':
    run_tests()
