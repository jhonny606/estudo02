msg = 'a'
msgCodificadaASCII = ord(msg[0]) + 1
msgCodificadaTxt = chr(msgCodificadaASCII)


print(msg)
print(msgCodificadaASCII)
print(msgCodificadaTxt)

#================================

msg = 'banana'
for i in msg:
    msgCodificadaASCII = ord(i) + 1
    msgCodificadaTxt += chr(msgCodificadaASCII)


print(msg)
print(msgCodificadaASCII)
print(msgCodificadaTxt)