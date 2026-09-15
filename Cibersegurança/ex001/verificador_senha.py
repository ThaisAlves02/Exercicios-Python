#-----------------------------------------------------------------
#VERIFICADOR DE FORÇA DE SENHA
#-----------------------------------------------------------------

import sys

senha = input("Digite sua senha: ")

if not senha.strip():
   print (" Campo senha está vazio! ")
   sys.exit()

regras_cumpridas = 0

if len (senha) >= 8:
    regras_cumpridas += 1
      
if any(s.isupper() for s in senha):
    regras_cumpridas += 1
  
if any(s.islower() for s in senha):
    regras_cumpridas += 1
  
if any(s.isdigit() for s in senha):
    regras_cumpridas += 1
  
if any(not s.isalnum() for s in senha):
    regras_cumpridas += 1
  
#-----------------------------------------------------------------
#CLASSIFICAÇÃO DA SENHA
#-----------------------------------------------------------------
if regras_cumpridas <= 2:
  print ("Senha fraca")
  
elif regras_cumpridas == 3 or regras_cumpridas == 4:
  print ("Senha média")

else:
  print ("senha forte")

