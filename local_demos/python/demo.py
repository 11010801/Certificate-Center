#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys,urllib
import rsa
def certify():
    if(len(sys.argv)!=3):
        return
    pubf,privf=sys.argv[1:]
    pubf,privf=['pub.pem','priv.pem']
    pubkey,privkey=rsa.newkeys(1024)
    open(pubf,'w').write(pubkey.save_pkcs1())
    open(privf,'w').write(privkey.save_pkcs1())
    with open(pubf) as publicfile:
        p=publicfile.read()
        pubkey=rsa.PublicKey.load_pkcs1(p)
    with open(privf) as privatefile:
        p=privatefile.read()
        privkey=rsa.PrivateKey.load_pkcs1(p)
    msg="hello"
    crypto=rsa.encrypt(msg,pubkey)
    msg=rsa.decrypt(crypto,privkey)
    print(msg)
    signature=rsa.sign(msg,privkey,'SHA-1')
    rsa.verify(msg,signature,pubkey)

def main():
    certify()
if __name__=='__main__':
    main()
