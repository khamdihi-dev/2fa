

## Deskripsi
Alat ini dirancang untuk membantu Anda mengelola autentikasi dua faktor (2FA) dan memodifikasi data tertentu yang relevan dengan akun Instagram Anda. Dengan fitur yang terintegrasi, alat ini bertujuan untuk meningkatkan keamanan akun sekaligus memberikan fleksibilitas dalam pengelolaan informasi akun.

## Fitur Utama
1. **Manajemen 2FA:**
   - Mengaktifkan autentikasi dua faktor.
   - Mendapatkan kode cadangan (backup codes).
   - harap di salin karena hasil tidak di simpan

2. **Modifikasi Data Akun:**
   - Mengubah data profil nomor dan email.
   - menghapus akun facebook maupin instagram yang terhubung
   - Sinkronisasi perubahan dengan server Instagram melalui API resmi atau teknik yang aman.

3. **Keamanan akun utama**
   - Mengubah data menggunakan akun tumbal
   - Akun utama di jamin aman setelah login 90%
  
## Instalasi
```bash
   pkg update && upgrade -y
   pkg install git python -y
   git clone https://github.com/khamdihi-dev/2fa
   cd 2fa
   pip3.12 install bs4 requests pycryptodome
   python3.12 auto.py
   ```
