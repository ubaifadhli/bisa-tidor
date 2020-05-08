from cryptography.fernet import Fernet

class AuthStorage:
	def storeAuth(self, email, password, authgroup, keyname):
		raw_auth = email+','+password
		#encryptor
		f = Fernet(self.getKey(keyname))
		encrypted = f.encrypt(raw_auth.encode())
		#write to file
		file = open('Auths/'+authgroup+'.auth', 'ab')
		file.write(encrypted+'\r\n'.encode('ascii'))
		file.close()

	def generateKey(self, keyname):
		key = Fernet.generate_key()
		file = open('Keys/'+keyname+'.key', 'wb')
		file.write(key)
		file.close()

	def getKey(self, keyname):
		file = open('Keys/'+keyname+'.key', 'rb')
		key = file.read()
		file.close()
		return key

	def getAuth(self, authgroup, keyname, th):
		file = open('Auths/'+authgroup+'.auth', 'rb')
		encrypted = file.readlines()[th]
		file.close()
		f = Fernet(self.getKey(keyname))
		decrypted = f.decrypt(encrypted)
		#data = decrypted.split(',',1)
		return decrypted

		