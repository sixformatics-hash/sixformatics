def hitung_biaya_warnet():
    print("=== Program Hitung Biaya Rental Warnet ===")

    # Input waktu masuk dan keluar
    jam_masuk = int(input("Jam masuk   : "))
    menit_masuk = int(input("Menit masuk : "))
    jam_keluar = int(input("Jam keluar  : "))
    menit_keluar = int(input("Menit keluar: "))

    # Ubah ke total menit
    total_masuk = jam_masuk * 60 + menit_masuk
    total_keluar = jam_keluar * 60 + menit_keluar

    # Validasi waktu
    if total_keluar < total_masuk:
        print("\n❌ Error: Waktu keluar tidak boleh lebih kecil dari waktu masuk.")
        return

    # Hitung lama rental
    lama_menit = total_keluar - total_masuk
    jam = lama_menit // 60
    menit = lama_menit % 60

    # Hitung biaya (Rp 5.000 per jam → 5000 / 60 per menit)
    biaya_per_menit = 5000 / 60
    biaya = lama_menit * biaya_per_menit

    # Output
    print("\n=== Hasil Perhitungan ===")
    print(f"Lama rental : {lama_menit} menit ({jam} jam {menit} menit)")
    print(f"Biaya rental: Rp {biaya:,.0f}".replace(",", "."))


# Jalankan program
hitung_biaya_warnet()