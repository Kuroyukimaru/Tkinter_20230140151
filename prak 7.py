#import tkinter as tk: Mengimpor modul tkinter yang digunakan untuk membuat aplikasi GUI di Python.
import tkinter as tk 

#from tkinter import messagebox: Mengimpor messagebox untuk menampilkan kotak pesan pop-up, seperti peringatan atau informasi kepada pengguna.
from tkinter import messagebox 

# Fungsi untuk menampilkan hasil prediksi
def hasil_prediksi(): #def hasil_prediksi():: Mendefinisikan fungsi hasil_prediksi yang akan dijalankan ketika tombol "Hasil Prediksi" diklik.
    # Mengecek apakah ada input yang kosong
    for entry in entries: #for entry in entries:: Ini adalah loop yang memeriksa setiap entry (kolom input) yang ada di dalam list entries (yang berisi objek input nilai).
        if entry.get() == "": #if entry.get() == "":: Mengecek apakah kolom input kosong. Fungsi get() digunakan untuk mendapatkan teks yang dimasukkan pengguna di kolom input.
            messagebox.showwarning("Peringatan", "Semua nilai mata pelajaran harus diisi!") #messagebox.showwarning(...): Jika ada kolom input yang kosong, maka fungsi ini akan menampilkan pesan peringatan di jendela pop-up.
            return  #return: Jika ada input kosong, maka fungsi hasil_prediksi akan dihentikan dan tidak melanjutkan ke langkah berikutnya.
        
    # Jika semua input terisi, tampilkan hasil prediksi
    label_hasil.config(text="Prediksi Prodi: Teknologi Informasi") #Jika semua input terisi, maka label yang menampilkan hasil prediksi akan diubah menjadi "Prediksi Prodi: Teknologi Informasi".

# Membuat jendela utama
root = tk.Tk() #root = tk.Tk(): Membuat objek root, yang merupakan jendela utama aplikasi Tkinter.
root.title("Aplikasi Prediksi Prodi Pilihan") #root.title("Aplikasi Prediksi Prodi Pilihan"): Mengatur judul jendela aplikasi menjadi "Aplikasi Prediksi Prodi Pilihan".
root.geometry("400x500")  #root.geometry("400x500"): Mengatur ukuran jendela aplikasi menjadi 400 piksel lebar dan 500 piksel tinggi.

# Label judul
label_judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16)) #label_judul = tk.Label(...): Membuat sebuah label di jendela root dengan teks "Aplikasi Prediksi Prodi Pilihan" dan menggunakan font Arial dengan ukuran 16.
label_judul.pack(pady=10) #label_judul.pack(pady=10): Menampilkan label di jendela dengan jarak vertikal (padding) sebesar 10 piksel dari elemen lainnya.

# Membuat frame untuk menampung input nilai
frame_input = tk.Frame(root) #frame_input = tk.Frame(root): Membuat frame di dalam jendela root, yang akan menampung input nilai mata pelajaran.
frame_input.pack(pady=20) #frame_input.pack(pady=20): Menampilkan frame di jendela dengan jarak vertikal (padding) sebesar 20 piksel.

# Membuat 10 input nilai mata pelajaran
entries = [] #entries = []: Membuat list kosong entries untuk menyimpan objek input nilai mata pelajaran (kolom input).
for i in range(10): #for i in range(10):: Loop sebanyak 10 kali (untuk 10 mata pelajaran).
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i+1}") #label = tk.Label(...): Membuat label untuk setiap mata pelajaran, seperti "Nilai Mata Pelajaran 1", "Nilai Mata Pelajaran 2", dan seterusnya.
    label.grid(row=i, column=0, padx=5, pady=5) #label.grid(row=i, column=0, padx=5, pady=5): Menempatkan label pada grid di baris i dan kolom 0, dengan padding horizontal dan vertikal sebesar 5 piksel.
    entry = tk.Entry(frame_input) #entry = tk.Entry(frame_input): Membuat kolom input (Entry) untuk setiap nilai mata pelajaran.
    entry.grid(row=i, column=1, padx=5, pady=5) #entry.grid(row=i, column=1, padx=5, pady=5): Menempatkan kolom input pada grid di baris i dan kolom 1, dengan padding horizontal dan vertikal sebesar 5 piksel.
    entries.append(entry) #entries.append(entry): Menambahkan kolom input ke dalam list entries.

# Button untuk menampilkan hasil prediksi
btn_prediksi = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi) #btn_prediksi = tk.Button(...): Membuat tombol dengan teks "Hasil Prediksi". Ketika tombol ini ditekan, fungsi hasil_prediksi akan dipanggil.
btn_prediksi.pack(pady=10) #btn_prediksi.pack(pady=10): Menampilkan tombol di jendela dengan jarak vertikal (padding) sebesar 10 piksel.

# Label untuk menampilkan hasil prediksi
label_hasil = tk.Label(root, text="", font=("Arial", 12)) #label_hasil = tk.Label(...): Membuat label kosong yang akan digunakan untuk menampilkan hasil prediksi setelah tombol ditekan.
label_hasil.pack(pady=10) #label_hasil.pack(pady=10): Menampilkan label di jendela dengan jarak vertikal (padding) sebesar 10 piksel.

# Menjalankan aplikasi
root.mainloop() #root.mainloop(): Memulai aplikasi dan membuat jendela GUI muncul. Fungsi mainloop() menjalankan loop utama Tkinter untuk menunggu interaksi pengguna dengan aplikasi.