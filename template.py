#!/bin/sh
import os


company = input('��Ж�')
reculte = input('�l�����̗p�S����')
ivent = input('�s��')
text = input('���z')
address_number = input('�X�֔ԍ�')
address = input('�Z��')


f = open('user.txt', 'w')

f.write(company)
f.write(reculte)
f.write('�����b�ɂȂ��Ă���܂��B\n�L���H�Ƒ�w�̉i��O�P�ł��B')


f.write('---------------------------------------------------------\n')
f.write('�L���H�Ƒ�w')
f.write('���w��')
f.write('�m�I���V�X�e���w��')
f.write('4�N')
f.write('�i��O�P')
f.write('\n')
f.write(address_number)
f.write(address)
f.write('090-8249-4426\n')
f.write('bl19067@cc.it-hiroshima.ac.jp\n')
f.write('---------------------------------------------------------\n')

f.close()
