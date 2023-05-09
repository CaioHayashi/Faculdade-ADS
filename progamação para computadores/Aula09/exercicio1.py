import os
os.system('cls' if os.name == 'nt' else 'clear') 

email = input("Entre com seu e-mail: ")

print(f'O dominínio do seu e-mail é http://{email[email.find("@") + 1::]}')
