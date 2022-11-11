username = "georgemiracle"
password = "Semarang123!"

def login (user_name, pass_word):
    if user_name != username and pass_word != password:
        hasil = False
    else:
         hasil = True

    return hasil

i=3
while i>=1:
    userName_ = input ("masukan username anda :")
    password_ =input("masukan password :")
    hasil = (login(userName_,password_))
    if hasil==True:
        print("login berhasil")
        break
    else:
        i-=1
        print("gagal login, sisa percobaan login adalah:",i)