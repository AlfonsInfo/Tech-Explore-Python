import datetime as dt
mahasiswa1 = {
    'nama' : 'ucup surucup',
    'nim' : '2032013921',
    'sks_lulus' : 130,
    'beasiswa' :False,
    'lahir' : dt.datetime(2001,4,10)
}
mahasiswa2 = {
    'nama' : 'Otong Surotong',
    'nim' : '202332329',
    'sks_lulus' : 140,
    'beasiswa' :True,
    'lahir' : dt.datetime(2001,4,5)
}

mahasiswa3 = {
    'nama' : 'Bambang sibambank',
    'nim' : '202332322',
    'sks_lulus' : 129,
    'beasiswa' :True,
    'lahir' : dt.datetime(2001,4,5)
}

data_mahasiswa = {
    'MAH001' : mahasiswa1,
    'MAH002' : mahasiswa2,
    'MAH003' : mahasiswa3,
}

print(f"{'KEY':<6}{'Nama':<17}{'SKS':<2} {'Beasiswa':<9}{'Lahir':<10}")
print("-"*50)
for mahasiswa in data_mahasiswa:
    KEY =mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
    print(f"{KEY:<6} {NAMA:<17} {SKS:<2} {BEASISWA:<9} {LAHIR:<10}")