#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys,urllib
from Crypto.PublicKey import RSA
from Crypto.Hash import MD5
def certify():
    if(len(sys.argv)!=2):
        return
    privf=sys.argv[1]
    f=open(privf,'rb')
    privkey=RSA.importKey(f.read())
    f.close()
#    f=open(pubf,'rb')
    f=urllib.urlopen('http://verify.wujianguo.org/publickey')
    pubkey=RSA.importKey(f.read())
    f.close()
    text='wujianguo'
    hash=MD5.new(text).digest()
    signature=privkey.sign(hash,'')
    print(pubkey.verify(hash,signature))
 
def main():
    certify()
if __name__=='__main__':
    main()
