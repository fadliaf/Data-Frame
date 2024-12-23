import pandas as pd
pd.set_option ('display.max_rows', None)
dataframe = pd.read_csv('data_sampah.csv')

print(dataframe)

total = 0
for index, row in dataframe.iterrows():
    jumlah_sampah = row['jumlah_produksi_sampah']
    if row['tahun'] == 2020:
        total = total + jumlah_sampah
print(f"Total produksi sampah di Jawa Barat pada tahun 2020 adalah {total}")


# total_2015 = 0
# total_2016 = 0
# total_2017 = 0
# total_2018 = 0
# total_2019 = 0
# total_2020 = 0
# total_2021 = 0

# for index, row in dataframe.iterrows():
#     tahun = row['tahun']
#     jumlah_sampah = row['jumlah_produksi_sampah']
#     if tahun == 2015:
#         total_2015 = total_2015 + jumlah_sampah
#     elif tahun == 2016:
#         total_2016 = total_2016 + jumlah_sampah
#     elif tahun == 2017:
#         total_2017 = total_2017 + jumlah_sampah
#     elif tahun == 2018:
#         total_2018 = total_2018 + jumlah_sampah
#     elif tahun == 2019:
#         total_2019 = total_2019 + jumlah_sampah
#     elif tahun == 2020:
#         total_2020 = total_2020 + jumlah_sampah
#     else:
#         total_2021 = total_2021 + jumlah_sampah
# print(f"Total produksi sampah pada tahun 2015 adalah {total_2015}")
# print(f"Total produksi sampah pada tahun 2016 adalah {total_2016}")
# print(f"Total produksi sampah pada tahun 2017 adalah {total_2017}")
# print(f"Total produksi sampah pada tahun 2018 adalah {total_2018}")
# print(f"Total produksi sampah pada tahun 2019 adalah {total_2019}")
# print(f"Total produksi sampah pada tahun 2020 adalah {total_2020}")
# print(f"Total produksi sampah pada tahun 2021 adalah {total_2021}")
