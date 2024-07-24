'''
================================================================================================
Graded Challenge 1

Nama  : Muhammad Fiqih Al-ayubi
Batch : HCK-17

Program ini dibuat dengan objective :
1. User dapat berinteraksi dengan program secara continue
2. User dapat menambahkan barang kedalam list barang, menghapus barang dari list barang, melihat
   isi barang di dalam list barang, dan melihat total harga dari barang - barang yang telah di-
   
================================================================================================
'''

import string


'''
Kelas ChartItem() dibuat untuk menampung attribut objek seperti namabarang dan harga. Ketika objek kelas dibuat, maka
kelas ChartItem() akan menampung objek tersebut beserta attributnya. Dalam program ini, objek diinisialisasi di dalam
method menambahbarang() pada kelas ShoppingCart()
'''
class ChartItem () :
    '''
    Fungsi ini digunakan untuk menampung attribut dari suatu objek. Objek diinisialisasi di dalam method menambahbarang()
    pada kelas ShoppingCart()
    '''
    def __init__(self, namabarang, harga) :
        self.namabarang = namabarang
        self.harga = harga


'''
Kelas ShoppingCart() dibuat untuk menampung data attribut dari beberapa objek dan melakukan seluruh operasi yang berkaitan
dengan user termasuk interface.
'''
class ShoppingCart () :

    '''
    Fungsi ini bertujuan untuk membuat atribut yang dapat menampung data attribut dari objek ChartItem()
    '''
    def __init__(self) :
        self.items = []

    '''
    Method menambahbarang() bertujuan untuk menginsialisasi objek ChartItem() dan menampung attributnya di dalam atribut 
    self.items. Ketika user memilih menu '1. Menambah barang', objek baru yang bernama barang dari kelas ChartItem() 
    akan dibuat bersama attributnya dan menyimpan data namabarang serta harga di dalam self.items. 
    '''
    def menambahbarang(self, namabarang,harga) :
        barang = ChartItem(namabarang.capitalize(), harga) # Inisialisasi object ChartItem()
        self.items.append(barang)                          # Memasukan object ChartItem() ke dalam data list

    '''
    Method totalharga() digunakan untuk menghitung total atribut harga dari seluruh objek barang yang sudah disimpan di dalam
    attribut self.items. Method ini akan dipanggil ketika user memilih menu '4. Lihat total belanja'.
    '''
    def totalharga(self) :
        total = 0                  # Variable total akan kembali ke nilai 0 setiap kali method ini dipanggil
        for barang in self.items : # Loop untuk melakukan penjumlahan terhadap seluruh attribut harga dari barang 
            total += barang.harga
        return total


    '''
    Method mengurangibarang() digunakan untuk menghapus/mengurangi object barang berdasarkan attribut namabarang yang diinput oleh 
    user. Method ini mengambil 1 argumen namabarang yang akan diinputkan oleh user pada menu '2. Hapus barang'.
    '''
    def mengurangibarang(self, namabarang) :
        namabarang = namabarang.capitalize() # Bertujuan agar format penulisannya sama dengan attribut namabarang di self.items 
        if len(self.items) != 0 :            
            for barang in self.items :       # Loop ini digunakan untuk mencari object barang berdasarkan namabarang
                if namabarang == barang.namabarang :
                    self.items.remove(barang) # Statement untuk menghapus object barang berdasarkan atribbut namabarang
                    return True
            else :
                return False
        else : 
            return False 


    '''
    Method lihatkerangjang() digunakan untuk menampilkan seluruh barang yang telah dimasukan ke dalam self.list()
    '''
    def lihatkeranjang(self) :
        for barang in self.items :
            print(f"{self.items.index(barang) +1}. {barang.namabarang} - Rp. {barang.harga}")


    '''
    Method interface() berfungsi untuk menjalankan interface dan menjaga user agar tetap terhubung ke program
    '''
    def interface(self) :
        # Loop ini menjaga interaksi antara user dan aplikasi
        while True :
            print('\nSelamat Datang di Keranjang Belanja Toko Makmur!')
            # Loop ini digunakan untuk menjaga interaksi antara user dan menu utama
            while True :
                print('Menu:\n1. Menambah barang\n2. Hapus barang\n3. Tampilkan barang di keranjang\n4. Lihat total belanja\n5. Exit\n')
                # User akan diminta untuk memasukan angka (str) untuk masuk ke salah satu menu
                pilihmenu = input('Pilih nomor untuk memilih menu : ')
                # Conditional statement digunakan agar user tidak salah dalam melakukan input
                if pilihmenu not in ['1','2','3','4','5'] :
                    print('Tolong hanya masukan salah satu angka dari menu\n')
                    continue
                elif pilihmenu in string.ascii_letters :
                    print('Karakter huruf tidak diperbolehkan')
                    continue
                else :
                    print()
                    break
            

            # Block code untuk menambah barang
            pilihmenu = int(pilihmenu)
            if pilihmenu == 1 :
                # Loop untuk menjaga interaksi pada menu menambah barang
                while True :
                    namabarang = input('Barang apa yang ingin anda tambahkan ? : ')
                    harga = int(input('Berapa harganya : '))
                    self.menambahbarang(namabarang, harga)
                    print(f'Barang {namabarang} berhasil dimasukan ke keranjang\n')
                    # Loop ini memberikan user opsi untuk menambahkan barang lagi atau keluar menuju menu utama
                    while True :
                        pilihmenu2 = input('Tekan angka 1 jika ingin lanjut menambah barang, tekan angka 2 jika ingin kembali ke menu utama : ')
                        if pilihmenu2 == '1' :
                            break
                        elif pilihmenu2 == '2' :
                            break
                        else : 
                            print('Tolong hanya masukan angka antara 1 atau 2')
                            continue
                    if pilihmenu2 == '1' :
                        continue
                    elif pilihmenu2 == '2' :
                        break

                    
            # Block code untuk menghapus barang
            elif pilihmenu == 2 :
                namabarang = input('Barang apa yang ingin dihapus ? : ')
                trueornot = self.mengurangibarang(namabarang)
                print()
                # Conditional statement untuk mengetahui apakah barang yang ingin dihapus ada di dalam keranjang/self.items. 
                # Jika tidak, maka method mengurangibarang() akan mengembalikan nilai False
                if trueornot == False :
                    print(f'Barang yang anda ingin hapus belum terdaftar\n')
                    continue
                else :
                    print(f'Barang {namabarang.capitalize()} berhasil dihapus\n')
                    continue
            

            # Block code untuk menampilkan barang di keranjang self.items
            elif pilihmenu == 3 :
                # Conditional statement untuk mengetahui apakah barang yang dicari ada di dalam keranjang/self.items. 
                # berdasarkan panjang index elemen self.items
                if len(self.items) == 0 :
                    print("Keranjang masih kosong\n")
                else :
                    print('Berikut adalah list barangmu di keranjang :')
                    self.lihatkeranjang()
                    print()
                input('Tekan tombol apapun untuk kembali ke menu utama : ')
            

            # Blcok code untuk menampilkan total harga
            elif pilihmenu == 4 :
                totalharga = self.totalharga()
                print(f'Total belanja = Rp. {totalharga}')
                if totalharga == 0 :
                    print('Sepertinya kamu belum memiliki barang di keranjang')
                input('Tekan tombol apapun untuk kembali ke menu utama : ')


            # Block code untuk keluar dari sistem
            elif pilihmenu == 5 :
                print('Sampai juumpa lagi (;...')
                break


# Main idiom
if __name__ == "__main__" :
    keranjang = ShoppingCart()
    keranjang.interface()



  
        