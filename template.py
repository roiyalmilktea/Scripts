#!/bin/sh
import os


company = input('会社名')
reculte = input('人事部採用担当名')
ivent = input('行事')
text = input('感想')
address_number = input('郵便番号')
address = input('住所')


f = open('user.txt', 'w')

f.write(company)
f.write(reculte)
f.write('お世話になっております。\n広島工業大学の永井弘輝です。')


f.write('---------------------------------------------------------\n')
f.write('広島工業大学')
f.write('情報学部')
f.write('知的情報システム学科')
f.write('4年')
f.write('永井弘輝')
f.write('\n')
f.write(address_number)
f.write(address)
f.write('090-8249-4426\n')
f.write('bl19067@cc.it-hiroshima.ac.jp\n')
f.write('---------------------------------------------------------\n')

f.close()
