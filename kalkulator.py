import os

class kalkulator:
	'Kelas kalkulator operasi matematika'
	'''Support :
		1. Tambah (+)
		2. Kurang (-)
		3. Kali(×)
		4. Bagi(:)
		'''
	
	def __init__(self,angka1,angka2):
		self.angka1 = angka1
		self.angka2 = angka2

	def pertambahan(self):
		hasil = self.angka1 + self.angka2
		print('Hasil dari',self.angka1,'+',self.angka2,'=',hasil)
		
	def pengurangan(self):
		hasil = self.angka1 - self.angka2
		print('Hasil dari',self.angka1,'-',self.angka2,'=',hasil)

	def perkalian(self):
		hasil = self.angka1 * self.angka2
		print('Hasil dari',self.angka1,'×',self.angka2,'=',hasil)
		
	def pembagian(self):
		hasil = self.angka1 / self.angka2
		print('Hasil dari',self.angka1,':',self.angka2,'=',hasil)

banner = 'OPERASI MATEMATIKA'				
print(banner.center(60))
print('='*60)
print('1. Operasi Pertambahan')
print('2. Operasi Pengurangan')
print('3. Operasi Perkalian')
print('4. Operasi Pembagian')
choose = int(input('Choose : '))
os.system('clear')

if choose == 1:
	print('=====•PERTAMBAHAN•=====')
	objek = kalkulator(int(input('Operand 1 :')),int(input('Operand 2 :')))
	hasil = objek.pertambahan()
if choose == 2:
	print('=====•PERKURANGAN•=====')
	objek = kalkulator(int(input('Operand 1 :')),int(input('Operand 2 :')))
	hasil = objek.pengurangan()
if choose == 3:
	print('=====•PERKALIAN•=====')
	objek = kalkulator(int(input('Operand 1 :')),int(input('Operand 2 :')))
	hasil = objek.perkalian()
if choose == 4:
	print('=====•PEMBAGIAN•=====')
	objek = kalkulator(int(input('Operand 1 :')),int(input('Operand 2 :')))
	hasil = objek.pembagian()