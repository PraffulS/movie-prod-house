class A(object):
    def __init__(self):
        #super(A,self).__init__()
       # self.a=a
        print("self.a")
        super(A,self).__init__()
class B(object):
    def __init__(self):
        #self.b=b 
        print("self.b")
        super(B,self).__init__()
class C(object):
    def __init__(self):
       # self.c=c
        print("self.c")
        super(C,self).__init__()
class D(A,B,C):
    def __init__(self):
        super(D,self).__init__()
       # A.__init__(self)
       # B.__init__(self)
        #C.__init__(self)
       # self.d = d
        print("self.d")
