<#
.SYNOPSIS
    Script Injeksi Otomatis VS Code Snippet Ujian Serkom Laravel BNSP/LSP
.DESCRIPTION
    Script ini secara otomatis memasang file 'serkom-laravel.code-snippets'
    ke folder User Snippets VS Code di Windows (%APPDATA%\Code\User\snippets\).
    Snippet akan langsung aktif di semua project/folder tanpa perlu restart VS Code.
.EXAMPLE
    powershell -ExecutionPolicy Bypass -File .\inject_snippets.ps1
#>

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "   🚀 INJEKTOR SNIPPET LARAVEL SERKOM BNSP (VS CODE)" -ForegroundColor Yellow
Write-Host "==========================================================" -ForegroundColor Cyan

# 1. Tentukan Path Snippets VS Code di Windows
$targetDir = [System.IO.Path]::Combine($env:APPDATA, "Code", "User", "snippets")
$targetFile = [System.IO.Path]::Combine($targetDir, "serkom-laravel.code-snippets")
$sourceFile = [System.IO.Path]::Combine($PSScriptRoot, "serkom-laravel.code-snippets")

# Fallback jika sourceFile tidak di folder script
if (-not (Test-Path $sourceFile)) {
    $sourceFile = Join-Path (Get-Location) "serkom-laravel.code-snippets"
}

Write-Host "[1/3] Memeriksa direktori snippets VS Code..." -ForegroundColor White
if (-not (Test-Path $targetDir)) {
    Write-Host "      Folder belum ada. Membuat: $targetDir" -ForegroundColor Gray
    New-Item -ItemType Directory -Force -Path $targetDir | Out-Null
} else {
    Write-Host "      Folder ditemukan: $targetDir" -ForegroundColor Green
}

# 2. Salin File Snippet
Write-Host "[2/3] Menyalin serkom-laravel.code-snippets..." -ForegroundColor White
if (Test-Path $sourceFile) {
    Copy-Item -Path $sourceFile -Destination $targetFile -Force
    Write-Host "      Berhasil disalin ke: $targetFile" -ForegroundColor Green
} else {
    Write-Host "      [ERROR] File sumber '$sourceFile' tidak ditemukan!" -ForegroundColor Red
    Write-Host "      Pastikan file 'serkom-laravel.code-snippets' berada di folder yang sama." -ForegroundColor Yellow
    exit 1
}

# 3. Verifikasi Ukuran & Status
$fileInfo = Get-Item $targetFile
Write-Host "[3/3] Verifikasi file snippets..." -ForegroundColor White
Write-Host "      Ukuran: $($fileInfo.Length) bytes" -ForegroundColor Green
Write-Host "      Status: AKTIF SECARA GLOBAL DI SEMUA PROJECT VS CODE!" -ForegroundColor Yellow

Write-Host ""
Write-Host "==========================================================" -ForegroundColor Green
Write-Host "   🎉 INJEKSI SELESAI DALAM 1 DETIK! SIAP UJIAN SERKOM" -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Green
Write-Host ""
Write-Host "💡 DAFTAR PREFIX SNIPPET UTAMA (Ketik di VS Code lalu tekan Tab):" -ForegroundColor Cyan
Write-Host "   - Migrations : mig-users, mig-tickets, mig-orders-ticket, mig-details-ticket, mig-foods" -ForegroundColor White
Write-Host "   - Models     : model-user, model-ticket, model-order-ticket, model-detail-ticket, model-food" -ForegroundColor White
Write-Host "   - Controller : ctrl-ticket, ctrl-user, ctrl-order-ticket, ctrl-customer-booking, ctrl-food" -ForegroundColor White
Write-Host "   - Views      : blade-ticket-index, blade-ticket-create, blade-ticket-edit, blade-user-index" -ForegroundColor White
Write-Host "   - Dashboard  : blade-admin-dashboard-rekap, blade-admin-orders-print" -ForegroundColor White
Write-Host "   - Customer   : blade-customer-catalog, blade-customer-booking, blade-customer-e-ticket" -ForegroundColor White
Write-Host "   - Routes     : route-ticket-complete, route-food-complete" -ForegroundColor White
Write-Host "   - Seeders    : seeder-ticket, seeder-database-ticket, seeder-food" -ForegroundColor White
Write-Host "   - SQL & Cheat: sql-crud-tickets, sql-rekap-omset, artisan-serkom-setup" -ForegroundColor White
Write-Host ""
