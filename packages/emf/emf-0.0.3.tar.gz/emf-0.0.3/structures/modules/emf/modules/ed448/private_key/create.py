

'''
	#
	#	write private key to path
	#
	import emf.modules.ed448.private_key.creator as ed448_private_key_creator
	private_key = ed448_private_key_creator.create (seed, format, path)
	if (private_key ["success"] == "yes"):
		private_key_class = private_key ["class"]
		private_key_string = private_key ["string"]
		
'''

'''
	import emf.modules.ed448.private_key.creator as ed448_private_key_creator
	private_key = ed448_private_key_creator.create (seed, format)
	if (private_key ["success"] == "yes"):
		private_key_class = private_key ["class"]
		private_key_string = private_key ["string"]
'''



'''
	SEED:
		4986888b11358bf3d541b41eea5daece1c6eff64130a45fc8b9ca48f3e0e02463c99c5aedc8a847686d669b7d547c18fe448fc5111ca88f4e8
		5986888b11358bf3d541b41eea5daece1c6eff64130a45fc8b9ca48f3e0e02463c99c5aedc8a847686d669b7d547c18fe448fc5111ca88f4e8
		
		4986888B11358BF3D541B41EEA5DAECE1C6EFF64130A45FC8B9CA48F3E0E02463C99C5AEDC8A847686D669B7D547C18FE448FC5111CA88F4E8
		
	FORMAT:
		DER
		PEM
'''
from Crypto.PublicKey.ECC 	import EccKey
import os.path

def WRITE (PATH, PRIVATE_KEY_STRING):
	if (os.path.exists (PATH)):
		return [ False, "PUBLIC KEY ALREADY EXISTS." ];
	
	f = open (PATH, 'wb')
	f.write (PRIVATE_KEY_STRING)
	f.close ()
	
	return [ True, "" ];


def create (
	SEED, 
	FORMAT, 
	
	path = ""
):	
	try:
		assert (len (SEED) == 114)
	except Exception:
		#
		#	WORD LIST: https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki
		#
		#		EACH WORD IS:
		#			2 ** 11 = 2048 BITS
		#			11 BOOLEAN UNITS
		#
	
		#
		#	SEED BOOLEAN UNITS:
		#		57 BYTES = (2 ** 8) * 57
		#		8 * 57 = 456
		#
		
		#
		#	11 BOOLEAN UNIT WORDS NECESSARY:
		#		456 / 11 -> 41.45 -> 42 WORDS
		#
	
		#
		#	1 BYTE = 2 ** 8 = 256 BITS
		#	2 BYTES = 
		#
		print ("Seed must be 57 bytes")
		return {
			"success": "no",
			"alarm": "Seed must be 57 bytes" 
		}

	SEED_BYTES = bytes.fromhex (SEED)
	private_key_class = EccKey (
		curve 	= "Ed448", 
		seed 	= SEED_BYTES
	)
	private_key_string = private_key_class.export_key (format = FORMAT)	
	if (len (path) >= 1):
		[ WRITTEN, NOTE ] = WRITE (path, private_key_string)
		if (WRITTEN == False):
			return {
				"success": "no",
				"alarm": NOTE 
			}
	
	return {
		"success": "yes",
		"alarm": "",
		
		"class": private_key_class, 
		"string": private_key_string
	}