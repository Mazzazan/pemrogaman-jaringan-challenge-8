from ftplib import FTP
f = FTP()
f.connect('localhost', 2121)

f.login(user='hassan', passwd='123')
fd = open('text.txt', 'wb')
f.retrbinary('RETR text.txt', fd.write, 1024)
fd.close()
f.quit()