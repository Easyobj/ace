#!/usr/bin/env python
#coding:utf-8
import sys
import base64
reload(sys)
sys.setdefaultencoding('utf-8')
import hmac
import hashlib
ekey = 'd1ad1b6b711d363640abe9dca793adaf13a7a7cd06a90794983649c9871fc14d'

doc_list =  ['doc1','doc2','doc3','doc4','doc5','doc6']
for i in doc_list:
    to_enc = base64.b64encode('http://8.210.228.243:8080/' + i)
    enc_res = hmac.new(ekey, to_enc, hashlib.md5).hexdigest()
    print ((doc_list.index(i) + 1) + '列水印Word文档演示地址：')
    print ('http://8.210.228.243/apps/editor/openEditor?callURL='+to_enc+'&sign='+enc_res + '\n')

txt_list =  ['txt1','txt2','txt3','txt4','txt5','txt6']

for i in txt_list:
    to_enc = base64.b64encode('http://8.210.228.243:8080/' + i)
    enc_res = hmac.new(ekey, to_enc, hashlib.md5).hexdigest()
    print ((txt_list.index(i) + 1) + '列水印TXT文档演示地址：')
    print ('http://8.210.228.243/apps/editor/openEditor?callURL='+to_enc+'&sign='+enc_res + '\n')