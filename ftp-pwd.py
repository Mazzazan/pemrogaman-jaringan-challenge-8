from ftplib import FTP

f = FTP()
f.connect('localhost', 2121)

print('Welcome: '+  f.getwelcome())

f.login(user='hassan', passwd="123")
print('current working directory '+ f.pwd())
# names = f.nlst()
# print('list of directory: ' + str(names))
f.retrlines('LIST')
f.quit()