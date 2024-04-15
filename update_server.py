import requests

userid = "8220709131"
name = "8220709131"
ar = 100
requests.post(url='http://192.168.101.76:5000/transaction.html', json={'id': userid, 'name': name, 'ar': ar})
