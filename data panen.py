data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500,
        },
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450,
        },
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600,
        },
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550,
        },
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 400,
        },
    },
}



for lokasi, data in data_panen.items():
    print(f"{lokasi}: {data}")

print("Hasil panen jagung dari lokasi2:", data_panen['lokasi2']['hasil_panen']['jagung'])
print("Nama lokasi dari lokasi3:", data_panen['lokasi3']['nama_lokasi'])


padi_panen = {}
kedelai_panen = {}


for lokasi, data in data_panen.items():
    padi_panen[lokasi] = data['hasil_panen']['padi']
    kedelai_panen[lokasi] = data['hasil_panen']['kedelai']

print("Jumlah panen padi:", padi_panen)
print("Jumlah panen kedelai:", kedelai_panen)


for lokasi, data in data_panen.items():
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']
    if padi > 1300 or jagung > 800:
        print(f"{data['nama_lokasi']} memerlukan perhatian khusus.")
    else:
        print(f"{data['nama_lokasi']} dalam kondisi baik.")




