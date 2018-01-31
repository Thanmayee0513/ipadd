class ipadd():
    def __init__(self,oct_a,oct_b,oct_c,oct_d):
        self.a=oct_a
        self.b=oct_b
        self.c=oct_c
        self.d=oct_d

    def __str__(self):
        return(str(self.a)+"."+str(self.b)+"."+str(self.c)+"."+str(self.d))

print(ipadd(10,0,0,1))
