import requests
id = "8220709131"
name = "8220709131"
ar = 900
requests.post(url = 'http://192.168.103.76:5000/transaction.html', json = {'id' : id, 'name' : name, 'ar' : ar})