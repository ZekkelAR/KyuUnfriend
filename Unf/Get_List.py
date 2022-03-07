import requests
from requests import get, post, session
import random
import json, sys, os, re


class de():
	def __init__(self):
		self.agen = [

	   #Chrome
	    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
	    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
	    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
	    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
	    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
	    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
	    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
	    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
	    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
	    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
	    #Firefox
	    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
	    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
	    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
	    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
	    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
	    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
	    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
	    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
	    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
	    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
	    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
	    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
	    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)',
	]
		self.proxi = [
	'http://78.160.160.70',
	'http://95.239.10.204',
	'http://205.202.42.230',
	'http://186.148.168.91',
	'http://113.252.222.73',
	'http://203.107.135.125',
	'http://80.48.119.28',
	'http://159.203.20.110',
	'http://178.128.153.253',
	'http://104.248.123.136',
	'http://157.230.149.54'

	   
	]
	def jam(self):
		self.username = input("[*] Username > ")
		self.password = input("[*] Password > ")
		asede = random.choice(self.proxi)
		reks1 = {'http':asede}
		mueheh = random.choice(self.agen)
		kwon = {'User-Agent':mueheh}
		s = requests.Session()
		self.linklogin = ('https://free.facebook.com/login/?ref=dbl&fl&refid=8')
		self.data1 = {'email':self.username,
 			 	 	  'pass' :self.password
			     	 }
		mulailogin = s.post(self.linklogin, data=self.data1, headers=kwon, proxies=reks1)
		atahiat = re.findall(r'<title>(.*?)</title>',mulailogin.text)
		print (atahiat)
		if "Facebook" in atahiat:
			self.sukses = []
			self.reks2 = input("akses => ")
			ready = ('https://graph.facebook.com/me?fields=friends.limit(500)&access_token={}' .format(self.reks2))
			noratan = s.get(ready).text
			msi = json.loads(noratan)
			self.tung = open('listID2.txt', 'w')
			for i in msi['friends']['data']:
				a = i['name']
				b = i['id']
				try:
					self.tung.write(i['id']+'|'+i['name']+'\n')
				except KeyError:
					continue
		elif " Gunakan Facebook secara Gratis di Telkomsel":
			self.sukses = []
			self.reks2 = input("akses => ")
			ready = ('https://graph.facebook.com/me?fields=friends.limit(500)&access_token={}' .format(self.reks2))
			noratan = s.get(ready).text
			msi = json.loads(noratan)
			self.tung = open('listID2.txt', 'w')
			for i in msi['friends']['data']:
				a = i['name']
				b = i['id']
				try:
					self.tung.write(i['id']+'|'+i['name']+'\n')
				except KeyError:
					continue
		"""def kontol(self):
		self.open = open('listID2.txt', 'r').readlines()
		for ya in self.open:
			b = ya.strip()
			unfriend = ('https://free.facebook.com/removefriend.php?friend_id={}&unref=profile_gear&ref=dbl' .format (b))
			oo = s.get(unfriend).text
			self.bacd = re.findall(r'value="(.*?)"', oo)
			self.param = {'fb_dtsg':self.bacd[4],
		                  'jazoest':self.bacd[5],
		                  'friend_id':self.bacd[6],
		                  'unref':'None',
		                  'confirm':'Konfirmasi'}

			self.kondom = s.post('https://free.facebook.com/a/removefriend.php', data=self.param, headers=kwon, proxies=reks1)
			self.anjing = (self.kondom).text
			if 'Anda tidak lagi berteman dengan' in self.anjing:
				print ('INFO): Unfriend Success!|{}'.format(b))
			else:
				print ('(GAGAL): {}'.format(b))"""

if __name__ == "__main__":
	konde = de()
	konde.jam()
