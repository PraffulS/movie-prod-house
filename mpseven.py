import shelve
def get_pr_ve():
    f= open("movies_n.txt","r")
    s1 = shelve.open("actors.dat","c")
    s2 = shelve.open("directors.dat","c")
    s3 = shelve.open("budget.dat","c")
    s4 = shelve.open("reldate.dat","c")
    s5 = shelve.open("collection.dat","c")
    s6 = shelve.open("certi.dat","c")
    print("""--------------details-------------""")
    m=""
    for lines in f.readlines():
            m=lines[:len(lines)-1]
            if (int(s5[m])-int(s3[m])) > 0 :
                print("movie name    :"+m)
                print("budget        :"+str(s3[m]))
                print("release date  :"+s4[m])
                print("collection    :"+str(s5[m]))
                print("profit        :"+str(int(s5[m])-int(s3[m])))
                print("\n")
    f.close()
    s1.sync()
    s1.close()
    s2.sync()
    s2.close()
    s3.sync()
    s3.close()
    s4.sync()
    s4.close()
    s5.sync()
    s5.close()
    s6.sync()
    s6.close()


