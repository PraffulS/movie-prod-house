import mptwo
import mpthree
import mpfour
import mpfive
import mpsix
import mpseven

ch=1;
while ch!=7 :
    print(""" --------------------------------WELCOME----------------------------

    ---------------------- Select one option ----------------------

               1. Enter movie details
               2. Get movie details by movie's name
               3. Get movie details by actor's name
               4. Get movie details by director's name
               5. Get movie's business details
               6. Get profitable ventures of production house
               
    ----------------------------------------------------------------
               """)
    ch = int(input("""              Enter your choice        """))
    if ch == 0 or ch>7 :
        print("          please enter proper choice     ")
    elif ch==1 :
        #c=1
        #while c!=0 :
        mptwo.enter_details()
        #c = input("1/0")
    elif ch==2:
        c = input("enter movie name   : ")
        mpthree.get_d_m(c)
    elif ch==3:
        c = input("enter actor name   : ")
        mpfour.get_d_a(c)
    elif ch==4:
        c = input("enter director name   : ")
        mpfive.get_d_d(c)
    elif ch==5:
        c = input("enter movie name   : ")
        mpsix.get_mo_de(c)
    elif ch==6:
        mpseven.get_pr_ve()
print("exiting......")

    
