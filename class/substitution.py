encode = ['Q','W','E','R','T','Y','U','I','O','P', \
          'A','S','D','F','G','H','J','K','L', \
          'Z','X','C','V','B','N','M']
decode = ['K','X','V','M','C','N','O','P','H','Q', \
          'R','S','Z','Y','I','J','A','D','L', \
          'E','G','W','B','U','F','T']

message = 'TOPSECRET'
coded = []
for i in range(len(message)):
    codebook_index = ord(message[i])-ord('A')
    coded.append(encode[codebook_index])

decoded = []
for i in range(len(coded)):
    codebook_index = ord(coded[i])-ord('A')
    decoded.append(decode[codebook_index])
