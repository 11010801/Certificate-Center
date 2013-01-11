#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys,urllib
from Crypto.PublicKey import RSA
from Crypto.Hash import MD5
import Crypto.Random
def certify():
    if(len(sys.argv)!=2):
        return
    privf=sys.argv[1]
    f=open(privf,'rb')
    privkey=RSA.importKey(f.read())
    f.close()
    f=urllib.urlopen('http://verify.wujianguo.org/publickey')
    pubkey=RSA.importKey(f.read())
    f.close()
    text=MD5.new(Crypto.Random.get_random_bytes(128)).digest()
#    print(text)
    info='20lsjustin89@gmail.com'+text
#    info='21git11010801@gmail.com'+text
    
    signature=privkey.sign(text,'')
    encinfo=pubkey.encrypt(info,32)
#    print(signature)
#    print(encinfo)
    para=urllib.urlencode({'info':encinfo,'text':signature})
    f=urllib.urlopen('http://verify.wujianguo.org/doverify',para)
#    print(f.read())
    s=f.read()
#    print(s)
    if MD5.new(text).digest()==privkey.decrypt(eval(s)):
        print "OK"
    else:
        print "ERROR"
    f.close()
def main():
    certify()
if __name__=='__main__':
    main()
