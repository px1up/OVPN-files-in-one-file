import os

#Переменные теги
ca_tag_open = ("<ca>\n")
ca_tag_close = ("</ca>\n")

crt_tag_open = ("<cert>\n")
crt_tag_close = ("</cert>\n")

key_tag_open = ("<key>\n")
key_tag_close = ("</key>\n")

ta_tag_open = ("<tls-auth>\n")
ta_tag_close = ("</tls-auth>\n")

os.rename('ta.key','ta')

#Поучаем файл с расширением *.key
for file in os.listdir():
    if file.endswith(".key"):
        key = (os.path.join(file))

#Поучаем файл с расширением *.crt
for file in os.listdir():
    if file.endswith(".crt"):
        crt = (os.path.join(file))
        
fileName=crt
with open(fileName,'r+') as f:
  contents=f.read()
  contents=contents[contents.find("-----BEGIN"):]
  f.seek(0)
  f.write(contents)
  f.truncate()
  
  fileName=key
with open(fileName,'r+') as f:
  contents=f.read()
  contents=contents[contents.find("-----BEGIN"):]
  f.seek(0)
  f.write(contents)
  f.truncate()   

#Открываем файл конфига *.ovpn
with open("template") as file:
    config = file.read()

#Открываем файл ca
with open("ca.crt") as file:
    ca = file.read()

#Открываем файл ta
with open("ta") as file:
    ta = file.read()

#Открываем файл *.crt
with open(crt) as file:
    user_crt = file.read()

#Открываем файл конфига *key
with open(key) as file:
     user_key = file.read()
 
#Создаем файл *.ovpn на основе config.ovpn
with open("client.ovpn", "w") as file:
    file.write(config)
with open("client.ovpn", "a") as file:
    file.write("\n") 

#Записываем ca
with open("client.ovpn", "a") as file:
    file.write(ca_tag_open)
with open("client.ovpn", "a") as file:
    file.write(ca)   
with open("client.ovpn", "a") as file:
    file.write(ca_tag_close)

#Записываем user_crt 
with open("client.ovpn", "a") as file:
    file.write(crt_tag_open)
with open("client.ovpn", "a") as file:
    file.write(user_crt)
with open("client.ovpn", "a") as file:
    file.write(crt_tag_close)   

#Записываем user_key 
with open("client.ovpn", "a") as file:
    file.write(key_tag_open)
with open("client.ovpn", "a") as file:
    file.write(user_key)
with open("client.ovpn", "a") as file:
    file.write(key_tag_close)
    
#Записываем ta
with open("client.ovpn", "a") as file:
    file.write(ta_tag_open)
with open("client.ovpn", "a") as file:
    file.write(ta)   
with open("client.ovpn", "a") as file:
    file.write(ta_tag_close)

os.rename('ta','ta.key')



    
print("Готово")