 Def power(g,e)
        if(e==1):
            
            return(n)
        if(e!=1):
            return(n*power(n,e-1))
        n=int(input("enter n:"))
        e=int(input("enter value:"))
        print("result:",power(n,e))
