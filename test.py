from util.CryptUtil import *


key=hash256("key")

AESGCMFileEncrypt("a.png","b.cipher",key)
AESGCMFileDecrypt("b.cipher","d.png",key)

