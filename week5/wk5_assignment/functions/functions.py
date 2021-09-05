def up_low(s):      
    u = sum(1 for i in s if i.isupper())
    l = sum(1 for i in s if i.islower())
    print( "Upper case characters : %s, Lower case characters : %s" % (u,l))

up_low("Hello Ben")