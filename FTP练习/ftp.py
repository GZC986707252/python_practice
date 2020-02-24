from ftplib import FTP

ftp = FTP('192.168.137.1')
ftp.login('test')

print(ftp.getwelcome())
print(ftp.dir())