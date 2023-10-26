import requests

response = requests.post('http://127.0.0.1:5000/set-word', json={'word': 'mypyWord'})
print(response.json())  # Should print {"success": True}

