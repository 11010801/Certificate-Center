Certificate-Center
==================

基于SSH的认证中心

http://verify.wujianguo.org

post请求http://verify.wujianguo.org/doverify ，参数info,text
info:
      email_len:2个0-9的字符
      email: 从第三个字符开始的email_len个字符
      msg:一串随机字符串
      email_len+email+msg用http://verify.wujianguo.org/publickey 进行rsa加密后即为info的值
text:
      上面的msg用自己的私钥进行签名后的值

若认证成功，返回对md5(msg)用email用户的公钥加密后的信息
否则返回一串随机字符串

详见local_demos
test gfw
