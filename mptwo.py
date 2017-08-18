import shelve
def enter_details():
    m_name = input("enter movie name   :")
    a_name = input("enter actor name   :")
    d_name = input("enter director name   :")
    budget = input("enter budget       :")
    release_date = input("enter release date   :")
    collection = input("enter collection   :")
    certi = input("enter certification  :")
    s1 = shelve.open("actors.dat","c")
    s2 = shelve.open("directors.dat","c")
    s3 = shelve.open("budget.dat","c")
    s4 = shelve.open("reldate.dat","c")
    s5 = shelve.open("collection.dat","c")
    s6 = shelve.open("certi.dat","c")
    f = open("movies_n.txt","a")
    f.write(m_name+"\n")
    f.close()
    s1[m_name] = a_name
    s2[m_name] = d_name
    s3[m_name] = budget
    s4[m_name] = release_date
    s5[m_name] = collection
    s6[m_name] = certi
    print("\n")
    #c = input("do you want to enter more entries (1/0)")
    #print(s[m_name])
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

