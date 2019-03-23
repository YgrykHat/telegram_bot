import zipfile
import os.path

zi = os.path.exists('img.zip')

if zi == True:
	z = zipfile.ZipFile('img.zip')
	z.extractall()    # Извлечь все файлы

else:
	pass