# 🤖 Telegram Bot Server Monitoring

## 📌 Deskripsi

Bot Telegram ini digunakan untuk melakukan monitoring server secara real-time dengan memanfaatkan REST API berbasis FastAPI. Bot akan mengambil data dari API dan menampilkan informasi seperti penggunaan CPU, RAM, dan Disk.

---

## ⚙️ Fitur Utama

Bot menyediakan beberapa command untuk monitoring server, yaitu:

### 🔹 `/start`

Menampilkan pesan pembuka serta daftar command yang tersedia.

### 🔹 `/status`

Menampilkan status server secara keseluruhan:

* CPU Usage
* RAM Usage
* Disk Usage

### 🔹 `/cpu`

Menampilkan penggunaan CPU server dalam persen.

### 🔹 `/ram`

Menampilkan penggunaan RAM server dalam persen.

### 🔹 `/disk`

Menampilkan penggunaan Disk server dalam persen.

### 🔹 `/uptime`

Menampilkan waktu uptime server.

### 🔹 `/ping`

Digunakan untuk mengecek apakah bot aktif (respon: Pong).

---

## 🔄 Cara Kerja

1. User mengirim command melalui Telegram.
2. Bot menerima pesan dan memproses command.
3. Bot mengirim request ke REST API (FastAPI).
4. API mengambil data server menggunakan library `psutil`.
5. Data dikembalikan ke bot.
6. Bot mengirimkan hasil ke user.

---

## 🧪 Contoh Penggunaan

```
/status
```

Output:

```
🖥 Server Status
CPU: 25%
RAM: 60%
Disk: 40%
```

---

## 🚀 Teknologi yang Digunakan

* Python
* FastAPI (REST API)
* aiogram (Telegram Bot)
* Docker & Docker Compose
* psutil (monitoring sistem)

---

## 📦 Cara Menjalankan

```bash
docker-compose up --build
```

---

## 📱 Pengujian

1. Buka aplikasi Telegram
2. Cari bot yang telah dibuat
3. Kirim salah satu command seperti:

   ```
   /status
   ```
4. Bot akan membalas dengan data monitoring server

---
