import requests 
from requests import get, post, session
import random
import re, json, sys, os
import time

R = '\033[31m'   # Red
N = '\033[1;37m' # White
G = '\033[32m'   # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' # Blue
C = '\033[36m' # cyan

def banner():
	print ("""
 __ __  ____   _____  ____   ____    ___  ____   ___   
|  T  T|    \ |     ||    \ l    j  /  _]|    \ |   \  
|  |  ||  _  Y|   __j|  D  ) |  T  /  [_ |  _  Y|    \ 
|  |  ||  |  ||  l_  |    /  |  | Y    _]|  |  ||  D  Y
|  :  ||  |  ||   _] |    \  |  | |   [_ |  |  ||     |
l     ||  |  ||  T   |  .  Y j  l |     T|  |  ||     |
 \__,_jl__j__jl__j   l__j\_j|____jl_____jl__j__jl_____j

Coded By  : KyuRazz
version   : 1.0
thanks to : Ago Oeng ~ Aalex ~ Dani ~ Faisal
""")

class KyuRazz:
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
	
	def Unf(self):
		self.agent = random.choice(self.agen)
		go = {'User-Agent':self.agent}
		self.proxiz = random.choice(self.proxi)
		go2 = {'http':self.proxiz}
		s = requests.Session()
		self.linklogin = ('https://free.facebook.com/login/?ref=dbl&fl&refid=8')
		self.username = ('anggiamanda986@gmail.com')
		self.password = ('zekkel1234')
		self.data1 = {'email':self.username,
 			 	 	  'pass' :self.password
			     	 }
		mulailogin = s.post(self.linklogin, data=self.data1)
		atahiat = re.findall(r'<title>(.*?)</title>',mulailogin.text)
		print (mulailogin)
		print (atahiat)
		self.open = open('listID2.txt', 'r').readlines()
		for ya in self.open:
			b = ya.strip()
			kint = b.split("|")
			ming = (kint[0])
			meng = (kint[1])
			unfriend = ('https://free.facebook.com/removefriend.php?friend_id={}&unref=profile_gear&ref=dbl' .format (ming))
			oo = s.get(unfriend).text
			self.bacd = re.findall(r'value="(.*?)"', oo)
			self.param = {'fb_dtsg':self.bacd[4],
		                  'jazoest':self.bacd[5],
		                  'friend_id':self.bacd[6],
		                  'unref':'None',
		                  'confirm':'Konfirmasi'}

			self.kara = s.post('https://free.facebook.com/a/removefriend.php', data=self.param)
			self.kere = (self.kara).text
			if 'Anda tidak lagi berteman dengan' in self.kere:
				print ('\033[31m[\033[32mSUCCESS\033[31m]\033[32m{}'.format(meng))
				time.sleep(1)
			else:
				print ('\033[31m(GAGAL): {}'.format(meng))
				time.sleep(1)

if __name__ == "__main__":
	os.system('clear')
	banner()
	Kyu = KyuRazz()
	Kyu.Unf()	