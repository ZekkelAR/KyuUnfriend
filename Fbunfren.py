import os, sys


def KyuRazz():
	print ("""
		> Family Attack Cyber <
/  ___|         (_)                       
\ `--.  ___ _ __ _ ______ ___      ____ _ 
 `--. \/ _ \ '__| |_  / _` \ \ /\ / / _` |
/\__/ /  __/ |  | |/ / (_| |\ V  V / (_| |
\____/ \___|_|  |_/___\__,_| \_/\_/ \__,_|--|
                                            |            
           Auto Unfriend Faceb00k |---------|  
Ago Oeng - Aalex - Faisal - Fa Haxor - tempik 
           """)
def Unfren():
	print ("""
[1] Get Token
[2] Get List Your Friendlist 
[2] Unfriend
""")

def tempik():
	r = input('Input Ur Number > ') 
	if r == '1':
		os.system("cd Unf && python Generate_Token.py")
	elif r == '2':
		os.system('cd Unf && python Get_List.py')
	elif r == '3':
		os.system('cd Unf && python unfriend.py')

	else:
		os.system('exit') 

if __name__ == "__main__":
	os.system('clear')
	KyuRazz()
	Unfren()
	tempik()