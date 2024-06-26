import sys
import veritabanı_uygulama_kitaplık as baglanti

print('-'*56)
print('-'*10, 'kitaplık programımıza hoş geldiniz', '-'*10)
print('-'*56)

while True:
    print('-'*10, 'yapmak istediğiniz işlemi seçiniz', '-'*10)
    print('-'*10, '(E)klemek, (L)istelemek, (G)üncellemek, (S)ilmek, (Ç)ıkmak', '-'*10)
    islem = input()

    if islem == 'Ç' or islem == 'ç':
        baglanti.cikis()
        sys.exit()

    elif islem == 'E' or islem == 'e':
        id = int(input('kitap id si giriniz: '))
        kitap = input('kitap adını giriniz: ')
        yazar = input('kitap yazarını giriniz: ')
        okunma = input('kitap okunma durumunu giriniz: ')
        begeni = input('kitap beğeni değerini giriniz: ')
        baglanti.ekle(id, kitap, yazar, okunma, begeni)

    elif islem == 'L' or islem == 'l':
        baglanti.listele()
#
    elif islem == 'G' or islem == 'g':
        baglanti.listele()
        guncellenecek = input('güncellemek istediğiniz kitabın id sini giriniz: ')
        baglanti.guncelle(guncellenecek)
#
    elif islem == 'S' or islem == 's':
        baglanti.listele()
        silinecek = input('silmek istediğiniz kitabın id sini giriniz: ')
        baglanti.sil(silinecek)
