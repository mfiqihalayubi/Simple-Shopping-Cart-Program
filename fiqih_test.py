'''
================================================================================================
Graded Challenge 1

Nama  : Muhammad Fiqih Al-ayubi
Batch : HCK-17

Program ini dibuat dengan objective :
1. Membuat unittest program untuk melakukan testing pada method ShoppingCart() terutama method yang melakukan penambahan barang, penghapusan barang, 
   dan perhitungan total harga
   
================================================================================================
'''


import unittest
from fiqih_app import ShoppingCart, ChartItem

# Pembuatan kelas untuk tes
class TestShoppingCart(unittest.TestCase) :

    '''
    Pembuatan object dari kelas ShopingCart() pada metode setUp(). Metode ini juga memastikan bahwa setiap metode tes 
    mendapatkan objek baru yang belum memiliki data apapun sehingga antara hasil metode tes tidak saling mempengaruhi
    satu sama lain
    '''
    def setUp(self) :
        self.memulaitest = ShoppingCart()
    
    '''
    Tes menambah barang dengan fungsi menambahbarang(namabarang, harga). Tes ini menggunakan method assertEqual dimana jika
    nilainya sama seperti yang diinginkan maka hasilnya akan bernilai True/lolos uji. 
    
    Contoh penggunaan, pada tes ini, method menambahbarang() akan diberikan argumen berupa 'kursi' dan harga 150000. Method 
    assertEqual akan mengecek apakah ada barang bernama 'Kursi' pada index list object items sesuai dengan hasil yang diharapkan.
    Jika ada maka hasilnya akan True/lolos uji. Hal yang sama juga dilakukan ketika mengecek harga barang dan isi dari items. 
    '''
    def testMenambahBarang(self) :
        self.memulaitest.menambahbarang('kursi', 150000)
        self.assertEqual(len(self.memulaitest.items),1) # Cek apakah object items sudah terisi ketika menambahbarang() dijalankan
        self.assertEqual(self.memulaitest.items[0].namabarang, 'Kursi') # Cek apakah ada nama barang 'Kursi'
        self.assertEqual(self.memulaitest.items[0].harga, 150000) # Cek apakah 'Kursi' benar bernilai 150000
    
    '''
    Tes penghapusan barang dengan method mengurangibarang(namabarang, harga). Tes ini menggunakan method assertEqual dimana jika
    nilainya sama seperti yang diinginkan maka hasilnya akan bernilai True/lolos uji. 
    
    Contoh penggunaan, pada tes ini, method menambahbarang() akan dijalankan untuk memberikan input nama barang 'ac' 
    dengan harga 800000. Setelah itu method mengurangibarang() akan dijalankan untuk menghilangkan object yang memiliki
    atribut 'ac'. assertTrue() dijalankan jika method mengurangibarang() berhasil menghapus object yang memiliki atribut 'ac'.
    Catatan, method mengurangibarang() hanya mengembalikan nilai True/False  
    '''
    def testPenghapusanBarang(self) :
        self.memulaitest.menambahbarang('ac', 800000) # Membuat object dan menambahkan object tersebut ke dalam items
        self.assertTrue(self.memulaitest.mengurangibarang('ac')) # Tes mengurangibarang()
        self.assertFalse(self.memulaitest.mengurangibarang('ac')) # Tes mengurangibarang() untuk object yang sama
        self.assertEqual(len(self.memulaitest.items),0) # Tes apakah setelah barang dikurangi panjang elemen items == 0
    
    '''
    Tes menghitung total harga barang di dalam list. Tes ini menggunakan method assertEqual dimana jika nilainya sama seperti 
    yang diinginkan maka hasilnya akan bernilai True/lolos uji. 
    
    Contoh penggunaan, pada tes ini, method menambahbarang() akan dijalankan sebanyak 2 kali untuk membuat 2 object dengan
    atribut 'meja' dan 'lemari'. Setelah itu, method totalharga() akan dijalankan dan method assertEqual() akan mengecek apakah
    nilai totalnya sama seperti yang diharapkan (dalam pengetesan ini 600000).
    '''
    def testTotalHarga(self) :
        self.memulaitest.menambahbarang('meja', 250000) # Membuat object dengan atribut 'meja'
        self.memulaitest.menambahbarang('lemari', 350000) # Membuat object dengan atribut 'lemari'
        self.assertEqual(self.memulaitest.totalharga(),600000) # Tes apakah kedua object berharga total 600000
    

'''
Kode di bawah ini berfungsi untuk menjalankan test. Fungsi unittest.main(verbosity=2) akan menjalankan setiap test
'''
if __name__ == '__main__':
    unittest.main(verbosity=2)
