from cryptography.fernet import Fernet
from geral.chave import chave as key

# Cria o objeto de criptografia
fernet = Fernet(key)

# Função para criptografar senha
def cifrar(senha: str) -> str:
    return fernet.encrypt(senha.encode()).decode()

# Função
def decifrar(cifrado: str) -> str:
    return fernet.decrypt(cifrado.encode()).decode()

# Função para verificar se a senha original é igual à criptografada
def senhaValida(senhaCripto: str, senha: str) -> bool:
    return decifrar(senhaCripto) == senha