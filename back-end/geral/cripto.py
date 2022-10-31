from cryptography.fernet import Fernet

password = "123senhaforte123"
key = Fernet.generate_key()
 
# Instance the Fernet class with the key
fernet = Fernet("hey")
 
# then use the Fernet class instance
# to encrypt the string string must
# be encoded to byte string before encryption
encMessage = fernet.encrypt(password.encode())
 
print("original string: ", password)
print("encrypted string: ", encMessage)
 
# decrypt the encrypted string with the
# Fernet instance of the key,
# that was used for encrypting the string
# encoded byte string is returned by decrypt method,
# so decode it to string with decode methods
decMessage = fernet.decrypt(encMessage).decode()
 
print("decrypted string: ", decMessage)

class Usuario:
    nome = ''
    email = ''
    senha = ''

''''

TODO:

1) Gerar chave aleatória pro usuário
2) Criptografar a senha com a chave criada
3) Mostrar essa senha criptografada no JSON
4) Descriptografar a senha usando a chave

'''