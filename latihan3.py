import csv
from datetime import datetime

def kasir_kembalian_pro():
    print("=== 💰 Sistem Kasir Kembalian Pro MAX ===")

    tanggal_hari_ini = datetime.now().strftime("%Y-%m-%d")
    nama_file = f"data_kembalian_{tanggal_hari_ini}.csv"

    header = ["Tanggal & Waktu", "Nama Pelanggan", "Total Bayar", "Uang Dibayar", "Kembalian", "Rincian"]

    # Bikin file CSV kalau belum ada
    try:
        with open(nama_file, "x", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(header)
    except FileExistsError:
        pass

    total_pendapatan = 0
    total_kembalian_semua = 0
    transaksi_ke = 0

    while True:
        transaksi_ke += 1
        print(f"\n🧾 Transaksi #{transaksi_ke}")
        nama = input("Nama pelanggan        : ")
        total_belanja = int(input("Total yang harus dibayar (Rp): "))
        uang_dibayar = int(input("Jumlah uang dibayar (Rp): "))

        # Validasi
        if uang_dibayar < total_belanja:
            print("❌ Uang tidak cukup. Transaksi dibatalkan.")
            continue

        # Hitung kembalian
        kembalian = uang_dibayar - total_belanja
        total_pendapatan += total_belanja
        total_kembalian_semua += kembalian

        print(f"\nTotal kembalian: Rp {kembalian:,.0f}".replace(",", "."))

        # Pecahan uang
        pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
        rincian = []
        print("\nRincian uang kembalian:")

        for p in pecahan:
            lembar = kembalian // p
            if lembar > 0:
                rincian.append(f"{lembar} lembar Rp {p:,}".replace(",", "."))
                print(f"Rp {p:>6,}".replace(",", ".") + f" : {lembar} lembar")
            kembalian %= p

        if kembalian > 0:
            rincian.append(f"Sisa Rp {kembalian}")
            print(f"Sisa Rp {kembalian}")

        # Simpan ke CSV
        waktu = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        with open(nama_file, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                waktu,
                nama,
                total_belanja,
                uang_dibayar,
                uang_dibayar - total_belanja,
                "; ".join(rincian)
            ])

        print("\n✅ Data transaksi berhasil disimpan.")

        # Lanjut atau keluar
        lanjut = input("\nTambah transaksi lagi? (y/n): ").lower()
        if lanjut != "y":
            break

    # === Laporan Harian ===
    print("\n📊 === Laporan Harian ===")
    print(f"Tanggal hari ini     : {tanggal_hari_ini}")
    print(f"Jumlah transaksi     : {transaksi_ke}")
    print(f"Total pendapatan     : Rp {total_pendapatan:,.0f}".replace(",", "."))
    print(f"Total uang kembalian : Rp {total_kembalian_semua:,.0f}".replace(",", "."))
    print(f"📁 File tersimpan di  : {nama_file}")
    print("\nTerima kasih sudah pakai Kasir Kembalian Pro MAX 😎")


# Jalankan program
kasir_kembalian_pro()