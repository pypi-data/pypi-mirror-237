'''Grab all printable characters for Codepage ranges
from the unicode ftp site'''

import os
from ftplib import FTP
from io import StringIO, BytesIO
import unicodedata
import pickle


folder = os.path.dirname(__file__)
fileName = 'data.txt'
dataFilePath = os.path.join(folder, fileName)
host = 'unicode.org'

mappingSource = {'cp1250'    : ('/Public/MAPPINGS/VENDORS/MICSFT/WINDOWS', 'CP1250.TXT'),
                 'cp1251'    : ('/Public/MAPPINGS/VENDORS/MICSFT/WINDOWS', 'CP1251.TXT'),
                 'cp1252'    : ('/Public/MAPPINGS/VENDORS/MICSFT/WINDOWS', 'CP1252.TXT'),
                 'cp1253'    : ('/Public/MAPPINGS/VENDORS/MICSFT/WINDOWS', 'CP1253.TXT'),
                 'cp1254'    : ('/Public/MAPPINGS/VENDORS/MICSFT/WINDOWS', 'CP1254.TXT'),
                 'cp1255'    : ('/Public/MAPPINGS/VENDORS/MICSFT/WINDOWS', 'CP1255.TXT'),
                 'cp1256'    : ('/Public/MAPPINGS/VENDORS/MICSFT/WINDOWS', 'CP1256.TXT'),
                 'cp1257'    : ('/Public/MAPPINGS/VENDORS/MICSFT/WINDOWS', 'CP1257.TXT'),
                 'cp1258'    : ('/Public/MAPPINGS/VENDORS/MICSFT/WINDOWS', 'CP1258.TXT'),
                 'cp874'     : ('/Public/MAPPINGS/VENDORS/MICSFT/WINDOWS', 'CP874.TXT'),
                 'cp932'     : ('/Public/MAPPINGS/VENDORS/MICSFT/WINDOWS', 'CP932.TXT'),
                 'cp936'     : ('/Public/MAPPINGS/VENDORS/MICSFT/WINDOWS', 'CP936.TXT'),
                 'cp949'     : ('/Public/MAPPINGS/VENDORS/MICSFT/WINDOWS', 'CP949.TXT'),
                 'cp950'     : ('/Public/MAPPINGS/VENDORS/MICSFT/WINDOWS', 'CP950.TXT'),
                 'cp437'     : ('/Public/MAPPINGS/VENDORS/MICSFT/PC', 'CP437.TXT'),
                 'cp737'     : ('/Public/MAPPINGS/VENDORS/MICSFT/PC', 'CP737.TXT'),
                 'cp775'     : ('/Public/MAPPINGS/VENDORS/MICSFT/PC', 'CP775.TXT'),
                 'cp850'     : ('/Public/MAPPINGS/VENDORS/MICSFT/PC', 'CP850.TXT'),
                 'cp852'     : ('/Public/MAPPINGS/VENDORS/MICSFT/PC', 'CP852.TXT'),
                 'cp855'     : ('/Public/MAPPINGS/VENDORS/MICSFT/PC', 'CP855.TXT'),
                 'cp857'     : ('/Public/MAPPINGS/VENDORS/MICSFT/PC', 'CP857.TXT'),
                 'cp860'     : ('/Public/MAPPINGS/VENDORS/MICSFT/PC', 'CP860.TXT'),
                 'cp861'     : ('/Public/MAPPINGS/VENDORS/MICSFT/PC', 'CP861.TXT'),
                 'cp862'     : ('/Public/MAPPINGS/VENDORS/MICSFT/PC', 'CP862.TXT'),
                 'cp863'     : ('/Public/MAPPINGS/VENDORS/MICSFT/PC', 'CP863.TXT'),
                 'cp864'     : ('/Public/MAPPINGS/VENDORS/MICSFT/PC', 'CP864.TXT'),
                 'cp865'     : ('/Public/MAPPINGS/VENDORS/MICSFT/PC', 'CP865.TXT'),
                 'cp866'     : ('/Public/MAPPINGS/VENDORS/MICSFT/PC', 'CP866.TXT'),
                 'cp869'     : ('/Public/MAPPINGS/VENDORS/MICSFT/PC', 'CP869.TXT'),
                 'ISO 8859-6': ('/Public/MAPPINGS/ISO8859', '8859-6.TXT'),
                 'mac-Roman' : ('/Public/MAPPINGS/VENDORS/APPLE', 'ROMAN.TXT'),
                 'cp1361'    : ('/Public/MAPPINGS/OBSOLETE/EASTASIA/KSC', 'JOHAB.TXT'),
	}
	

def getCharacters(data):
	characters = set()
	for line in data:
		line = line.strip()
		if line and not line.startswith(b'#'):
			parts = line.split(b'\t')
			if len(parts) >= 2 and parts[1].startswith(b'0x'):
				try:
					codePoint = int(parts[1], 16)
				except:
					print(line)
					break
				cat = unicodedata.category(chr(codePoint))
				if not cat.startswith('C'):
					characters.add(codePoint)
	return frozenset(characters)
	
def main():
	from otSpec.cpg import dataFilePath
	ftp = FTP(host)
	ftp.login()
	mapping = {}
	for name, location in mappingSource.items():
		folder, fileName = location
		print(folder, fileName)
		ftp.cwd(folder)
		data = BytesIO()
		ftp.retrbinary('RETR %s' % fileName, data.write)
		data.seek(0)
		mapping[name] = getCharacters(data)
	ftp.quit()
	# fix Code Page 708 MS-DOS Arabic ASMO problem
	ASMO708 = set(mapping['ISO 8859-6'])
	ASMO708 |= set((0x2502, 0x2524, 0x2561, 0x2562, 0x2556, 0x2555, 0x2563, 0x2551, 0x2557, 0x255D))
	mapping['ISO 8859-6'] = frozenset(ASMO708)
	with open(dataFilePath, 'wb') as dataFile:
		pickle.dump(mapping, dataFile)
#	dataFile.close()
	
if __name__ == '__main__':
	main()
	