"""
Вам дана в архиве файловая структура, состоящая из директорий и файлов.
Вам необходимо распаковать этот архив, и затем найти в данной в файловой
структуре все директории, в которых есть хотя бы один файл с расширением ".py". 

Ответом на данную задачу будет являться файл со списком таких директорий,
отсортированных в лексикографическом порядке.
"""
import os
from shutil import unpack_archive
result = []
unpack_archive('main.zip')
for curdir, lsdir, lsfile in os.walk('main'):
	for i in lsfile:
		if i.endswith('.py'):
			result.append(curdir)
			break
			
f = open('result.txt', 'w')
f.write('\n'.join(sorted(result)))
f.close()