import csv
from datetime import datetime

def hitung_biaya_warnet():
    print("=== 💻 Sistem Billing Warnet Pro+ ===")

    file_csv = "data_warnet.csv"
    header = ["Tanggal", "Nama", "Jam Masuk", "Jam Keluar", "Durasi", "Biaya Asli", "Diskon", "Biaya Akhir"]

    # Buat file CSV kalau belum ada
    try:
        with open(file_csv, "x", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(header)
    except FileExistsError:
        pass  # kalau sudah ada, lanjut aja

    while True:
        print("\nMasukkan data pelanggan:")
        nama = input("Nama pelanggan : ")

        # Input waktu
        jam_masuk = int(input("Jam masuk      : "))
        menit_masuk = int(input("Menit masuk    : "))
        jam_keluar = int(input("Jam keluar     : "))
        menit_keluar = int(input("Menit keluar   : "))

        # Validasi waktu
        total_masuk = jam_masuk * 60 + menit_masuk
        total_keluar = jam_keluar * 60 + menit_keluar
        if total_keluar < total_masuk:
            print("❌ Error: Waktu keluar tidak boleh lebih kecil dari waktu masuk.")
            continue

        # Hitung durasi
        lama_menit = total_keluar - total_masuk
        jam = lama_menit // 60
        menit = lama_menit % 60

        # Hitung biaya
        biaya_per_menit = 5000 / 60
        biaya_asli = lama_menit * biaya_per_menit

        # Diskon (kalau member)
        is_member = input("Apakah pelanggan member? (y/n): ").lower()
        if is_member == 'y':
            diskon_persen = 10
            diskon = biaya_asli * diskon_persen / 100
        else:
            diskon_persen = 0
            diskon = 0

        biaya_akhir = biaya_asli - diskon

        # Tanggal otomatis
        tanggal = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        # Output hasil
        print("\n=== Hasil Perhitungan ===")
        print(f"Tanggal      : {tanggal}")
        print(f"Nama         : {nama}")
        print(f"Lama rental  : {lama_menit} menit ({jam} jam {menit} menit)")
        print(f"Biaya asli   : Rp {biaya_asli:,.0f}".replace(",", "."))
        if diskon_persen > 0:
            print(f"Diskon {diskon_persen}% : Rp {diskon:,.0f}".replace(",", "."))
        print(f"Biaya akhir  : Rp {biaya_akhir:,.0f}".replace(",", "."))

        # Simpan ke file CSV
        with open(file_csv, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                tanggal,
                nama,
                f"{jam_masuk:02d}:{menit_masuk:02d}",
                f"{jam_keluar:02d}:{menit_keluar:02d}",
                f"{jam} jam {menit} menit",
                round(biaya_asli),
                f"{diskon_persen}%",
                round(biaya_akhir)
            ])

        print("\n✅ Data berhasil disimpan ke data_warnet.csv")

        # Tanya lanjut
        lanjut = input("\nTambah pelanggan lain? (y/n): ").lower()
        if lanjut != 'y':
            break

    print("\n📁 Semua data tersimpan di file: data_warnet.csv")
    print("Terima kasih sudah pakai sistem warnet ini 😎")


# Jalankan program
hitung_biaya_warnet()