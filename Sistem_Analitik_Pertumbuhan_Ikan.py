# ASSESSMENT 2
# SISTEM ANALITIK PERTUMBUHAN IKAN AKUARIUM

# 1. ACCOUNT DICTIONARY
akun = {
    "IKAN001": "12345",
    "IKAN002": "67890",
    "IKAN003": "abcde"
}

# 2. NESTED DICTIONARY - PROFILE
profil = {
    "IKAN001": {"nama": "Andi", "telepon": "081234567890"},
    "IKAN002": {"nama": "Budi", "telepon": "082345678901"},
    "IKAN003": {"nama": "Citra", "telepon": "083456789012"}
}

# 3. LIST OF DICTIONARIES - DATA PERTUMBUHAN
data_ikan = [
    {
        "pemilik": "IKAN001",
        "id": "F001",
        "spesies": "Koi",
        "umur": 12,
        "panjang": 18.5,
        "berat": 145,
        "suhu": 25.5,
        "pakan": 2
    },
    {
        "pemilik": "IKAN002",
        "id": "F002",
        "spesies": "Guppy",
        "umur": 8,
        "panjang": 5.8,
        "berat": 4.5,
        "suhu": 26,
        "pakan": 2
    },
    {
        "pemilik": "IKAN003",
        "id": "F003",
        "spesies": "Ikan Mas",
        "umur": 16,
        "panjang": 21.2,
        "berat": 210,
        "suhu": 24.8,
        "pakan": 1
    }
]

# 4. TUPLE MENU
menu = (
    "Login",
    "Registrasi",
    "Lihat Data",
    "Tambah Data",
    "Perbarui Data",
    "Profil",
    "Logout",
    "Keluar"
)

session = None


# FUNGSI MENU

def tampil_menu():
    if session:
        # SLICING
        return menu[2:]
    else:
        # SLICING
        return menu[:2] + menu[-1:]


# REGISTRASI

def registrasi():
    print("\n--- REGISTRASI ---")

    user = input("ID       : ")
    password = input("Password : ")
    nama = input("Nama     : ")
    telepon = input("Telepon  : ")

    if user in akun:
        print("ID sudah digunakan!")
        return

    akun[user] = password
    profil[user] = {
        "nama": nama,
        "telepon": telepon
    }

    print("Registrasi berhasil!")


# LOGIN

def login():
    global session

    print("\n--- LOGIN ---")

    user = input("ID       : ")
    password = input("Password : ")

    if user in akun and akun[user] == password:
        session = user
        print("Login berhasil!")
    else:
        print("ID atau password salah.")


# SESSION LOCK

def cek_login():
    if session is None:
        raise PermissionError(
            "Silakan login terlebih dahulu!"
        )


# LIHAT DATA PERTUMBUHAN


def lihat_data():
    cek_login()

    print("\n--- DATA PERTUMBUHAN ---")

    ditemukan = False

    for ikan in data_ikan:
        if ikan["pemilik"] == session:

            ditemukan = True

            print(
                f"\nID       : {ikan['id']}"
                f"\nSpesies  : {ikan['spesies']}"
                f"\nUmur     : {ikan['umur']} minggu"
                f"\nPanjang  : {ikan['panjang']} cm"
                f"\nBerat    : {ikan['berat']} gram"
                f"\nSuhu     : {ikan['suhu']} C"
                f"\nPakan    : {ikan['pakan']} kali/hari"
            )

    if not ditemukan:
        print("Belum ada data ikan.")


# TAMBAH DATA PERTUMBUHAN

def tambah_data():
    cek_login()

    print("\n--- TAMBAH DATA IKAN ---")

    ikan = {
        "pemilik": session,
        "id": input("ID ikan    : "),
        "spesies": input("Spesies     : "),
        "umur": angka("Umur (minggu): ", int),
        "panjang": angka("Panjang (cm): ", float),
        "berat": angka("Berat (gram): ", float),
        "suhu": angka("Suhu air    : ", float),
        "pakan": angka("Pakan/hari  : ", int)
    }

    # Cek ID ikan agar tidak duplikat
    for data in data_ikan:
        if data["pemilik"] == session and data["id"] == ikan["id"]:
            print("ID ikan sudah digunakan!")
            return

    data_ikan.append(ikan)

    print("Data berhasil ditambahkan!")


# PERBARUI DATA

def update_data():
    cek_login()

    print("\n--- PERBARUI DATA ---")

    id_ikan = input("ID ikan: ")

    for ikan in data_ikan:

        if (
            ikan["pemilik"] == session
            and ikan["id"] == id_ikan
        ):

            ikan["panjang"] = angka(
                "Panjang baru: ",
                float
            )

            ikan["berat"] = angka(
                "Berat baru: ",
                float
            )

            ikan["suhu"] = angka(
                "Suhu baru: ",
                float
            )

            print("Data berhasil diperbarui!")
            return

    print("Data ikan tidak ditemukan.")


# PROFIL

def lihat_profil():
    cek_login()

    print("\n--- PROFIL ---")

    print("ID      :", session)
    print("Nama    :", profil[session]["nama"])
    print("Telepon :", profil[session]["telepon"])


# VALIDASI INPUT

def angka(pesan, tipe):

    while True:

        try:
            return tipe(input(pesan))

        except ValueError:
            print("Input harus berupa angka!")


# LOGOUT

def logout():
    global session

    session = None

    print("Logout berhasil.")


# PROGRAM UTAMA

while True:

    daftar_menu = tampil_menu()

    print("\n=== SISTEM ANALITIK PERTUMBUHAN IKAN ===")

    for i, item in enumerate(daftar_menu, 1):
        print(i, ".", item)

    try:
        pilihan = int(input("Pilih menu: "))

        if pilihan < 1 or pilihan > len(daftar_menu):
            raise ValueError

    except ValueError:
        print("Pilihan menu tidak valid!")
        continue

    pilihan = daftar_menu[pilihan - 1]

    try:

        if pilihan == "Login":
            login()

        elif pilihan == "Registrasi":
            registrasi()

        elif pilihan == "Lihat Data":
            lihat_data()

        elif pilihan == "Tambah Data":
            tambah_data()

        elif pilihan == "Perbarui Data":
            update_data()

        elif pilihan == "Profil":
            lihat_profil()

        elif pilihan == "Logout":
            logout()

        elif pilihan == "Keluar":
            print("Program selesai.")
            break

    except PermissionError as error:
        print(error)