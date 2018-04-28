#### 基础python语法
- 运算符重载方法一览表：(http://www.cnblogs.com/hotbaby/p/4913363.html)

- method	overload	call
- __init__	构造函数	对象创建: X = Class(args)
- __del__	析构函数	X对象收回
- __add__	云算法+	如果没有_iadd_， X+Y， X+=Y
- __or__	运算符|	如果没有_ior_，X|Y, X|=Y
- _repr__, __str__	打印，转换	print(X)，repr(X)，str(X)
- __call__	函数调用	X(*args, **kwargs)
- __getattr__	点号运算	X.undefined
- __setattr__	属性赋值语句	X.any=value
- __delattr__	属性删除	del X.any
- __getattribute__	属性获取	X.any
- __getitem__	索引运算	X[key]，X[i:j]
- __setitem__	索引赋值语句	X[key]，X[i:j]=sequence
- __delitem__	索引和分片删除	del X[key]，del X[i:j]
- __len__	长度	len(X)，如果没有__bool__，真值测试
- __bool__	布尔测试	bool(X)
- __lt__, __gt__,
- __le__, __ge__,
>__eq__, __ne__	特定的比较	X<Y，X>Y，X<=Y，X>=Y，
X==Y，X!=Y
注释：（lt: less than, gt: greater than,
  le: less equal, ge: greater equal,
  eq: equal, ne: not equal
）
- __radd__	右侧加法	other+X
- __iadd__	实地（增强的）加法	X+=Y(or else __add__)
- __iter__, __next__	迭代环境	I=iter(X), next()
- __contains__	成员关系测试	item in X(任何可迭代)
- __index__	整数值	hex(X), bin(X),  oct(X)
- __enter__, __exit__	环境管理器	with obj as var:
- __get__, __set__,
- __delete__	描述符属性	X.attr, X.attr=value, del X.attr
- __new__	创建	在__init__之前创建对象

- stevedore使用方式
>stevedore是用来实现动态加载代码的开源模块
https://blog.csdn.net/gqtcgq/article/details/49620279
----
demo usage
- python rpc-server.py --config-file rpc.conf
- python rpc-client.py --config-file rpc.conf
