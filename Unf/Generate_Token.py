import requests
from requests import get, post, session
import random
import json, sys, os, re

class Kyu:
	def __init__(self):
		self.username = input('Ur Username => ')
		self.password = input('Ur Password => ')
	def nani(self):
		s = requests.Session()
		urlgenerate = ("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email={}&locale=en_US&password={}&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6" .format(self.username, self.password))
		reks1 = s.get(urlgenerate).text
		zz=json.loads(reks1)
		try:
			yyy=(zz['access_token'])
			print (yyy)
		except KeyError:
			print ("gagal ngambil akses token")

if __name__ == "__main__":
	KyuRazz = Kyu()
	KyuRazz.nani()
