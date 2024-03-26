import requests


token_url = ""
client_id = ""
client_secret = ""
data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }

def get_oauth_token(client_id, client_secret, token_url):
    response = requests.post(token_url, data=data)
    if response.status_code == 200:
        token_data = response.text
        return token_data.get('access_token')
    else:
        print(f"Failed to obtain token, status code: {response.status_code}")
        return None

token = get_oauth_token(client_id, client_secret, token_url)
print("Access token:", token)