import tweepy
import json

f = open("tokens/tokens.json",'r')
token_json_dict = json.load(f)

bearer = token_json_dict["bearer"]

api_key = token_json_dict["api_key"]
api_key_secret = token_json_dict["api_key_secret"]

access_token = token_json_dict["access_token"]
access_token_secret = token_json_dict["access_token_secret"]

print("bearer:",bearer)
print("api_key:", api_key)
print("api_key_secret:", api_key_secret)
print("access_token:", access_token)
print("access_token_secret:", access_token_secret)

client = tweepy.Client(bearer_token=bearer)

#client = tweepy.Client(
#        bearer_token=bearer
#        , consumer_key= api_key
#        , consumer_secret= api_key_secret
#        , access_token= access_token
#        , access_token_secret= access_token_secret
#        )
#
account = token_json_dict["account"]
user = client.get_user(username=account)
#
#print(user.data.id)
#print(user.data['id'])
#print(user[0].id)
#print(user[0]['id'])
