import requests
from encryptdevrypt import aes_decrypt, aes_encrypt
cipher_key = bytes([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
cipher_iv = bytes([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
def sendToServer(payload):
    # payload = aes_decrypt(cipher_key, cipher_iv, encryptedPayload)
    print(payload)
    sender = payload[0:10]
    reciever = payload[10:20]
    ar = payload[20:27]
    print(sender)
    print(reciever)
    print(ar)
    requests.post(url='http://127.0.0.1:5000/transaction.html', json={'sender': sender, 'reciever': reciever, 'ar': ar})
