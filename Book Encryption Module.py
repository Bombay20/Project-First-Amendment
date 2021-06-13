"""
Project: First Amendment
Author: Mr.X
Date Created: 10/6/2021
Date Last Modified: 10/6/2021
"""
"""
import sqlite3
def create_database(databasename,tablename):
    conn = sqlite3.connect(databasename+'.db')
    c = conn.cursor()
    c.execute('CREATE TABLE (tablename)')

create_database("fun","test")
"""
def bookcheck(book):#Checks the book file to make sure what char are advalable
    ab = 0
    a = b = c = d = e = f = g = h = i = j = k = l = m = n = o = p = q = r = s = t = u = v = w = x = y = z = fullstop = space = 0
    fullstop = 0
    contents = open(book, 'rt').read().lower()
    for aa in range(len(contents)):
        ab += 1
        if contents[aa:ab] == "a":
            a += 1
        elif contents[aa:ab] == "b":
            b += 1
        elif contents[aa:ab] == "c":
            c += 1
        elif contents[aa:ab] == "d":
            d += 1
        elif contents[aa:ab] == "e":
            e += 1
        elif contents[aa:ab] == "f":
            f += 1
        elif contents[aa:ab] == "g":
            g += 1
        elif contents[aa:ab] == "h":
            h += 1
        elif contents[aa:ab] == "i":
            i += 1
        elif contents[aa:ab] == "j":
            j += 1
        elif contents[aa:ab] == "k":
            k += 1
        elif contents[aa:ab] == "l":
            l += 1
        elif contents[aa:ab] == "m":
            m += 1
        elif contents[aa:ab] == "n":
            n += 1
        elif contents[aa:ab] == "o":
            o += 1
        elif contents[aa:ab] == "p":
            p += 1
        elif contents[aa:ab] == "q":
            q += 1
        elif contents[aa:ab] == "r":
            r += 1
        elif contents[aa:ab] == "s":
            s += 1
        elif contents[aa:ab] == "t":
            t += 1
        elif contents[aa:ab] == "u":
            u += 1
        elif contents[aa:ab] == "v":
            v += 1
        elif contents[aa:ab] == "w":
            w += 1
        elif contents[aa:ab] == "x":
            x += 1
        elif contents[aa:ab] == "y":
            y += 1
        elif contents[aa:ab] == "z":
            z += 1
        elif contents[aa:ab] == ".":
            fullstop += 1
        elif contents[aa:ab] == " ":
            space += 1
    ammount = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,fullstop,space]
    printammount = ["a="+str(a),"b="+str(b),"c="+str(c),"d="+str(d),"e="+str(e),"f="+str(f),"g="+str(g),"h="+str(h),"i="+str(i),"j="+str(j),"k="+str(k),"l="+str(l),"m="+str(m),"n="+str(n),"o="+str(o),"p="+str(p),"q="+str(q),"r="+str(r),"s="+str(s),"t="+str(t),"u="+str(u),"v="+str(v),"w="+str(w),"x="+str(x),"y="+str(y),"z="+str(z),".="+str(fullstop)," ="+str(space)]
    return(printammount)

def bookconversion(book):#Coverts .book file to .char file
    aa = 0
    ab = 1
    collection = ""
    total_pages = ""
    pages_number = ""
    line_number = ""
    contents = open(book, 'rt').read().lower()
    len_contents = len(contents)
    while aa != len_contents:
        aa += 1
        ab += 1
        a = []
        if contents[aa:ab] == "[":#Checks and saves the total pages of the .book file
            while collection != True:
                aa += 1
                ab += 1
                if contents[aa:ab] != "]":
                    total_pages += str(contents[aa:ab])
                else:
                    print("total = "+total_pages)
        if contents[aa:ab] == "(":#Checks for page number
            pages_number = ""
            collection = False
            while collection != True:
                aa += 1
                ab += 1
                if contents[aa:ab] != ")":#End of page number and saves page number.
                    pages_number += str(contents[aa:ab])
                    print(pages_number)
                else:
                    while aa != len_contents:#Collects line number
                        aa += 1
                        ab += 1
                        if contents[aa:ab] != "{":
                            print(contents[aa:ab])
                            line_number += contents[aa:ab]
                        else:
                            print(line_number)
                            collection = True
                            while aa != len_contents:
                                ba = 0
                                bb = 1
                                if contents[aa:ab] != "}":
                                    if contents[aa:ab] == "a":
                                        a.append(str(pages_number)+"."+str(line_number)+"."+str(bb))
                                ba += 1
                                bb += 1
                                aa += 1
                                ab += 1
                                print(contents[aa:ab])
                                if contents[aa:ab] == "}":
                                    print(pages_number)
                                    print(line_number)
                                    print(bb)
                                    print(a)
                                    break
                            break
            break
"""
def total_pages(book):
    aa = 0
    ab = 1
    contents = open(book, 'rt').read().lower()
    len_contents = len(contents)
    while aa != len_contents:
        aa += 1
        ab += 1
        a = []
        if contents[aa:ab] == "[":#Checks and saves the total pages of the .book file
            while collection != True:
                aa += 1
                ab += 1
                if contents[aa:ab] != "]":
                    total_pages += str(contents[aa:ab])
                elif contents[aa:ab] == "]":
                    print("total = "+total_pages)
                    collection = True

def check_for_page_number(book):
    global pages_number
    aa = 0
    ab = 1
    contents = open(book, 'rt').read().lower()
    if contents[aa:ab] == "(":  # Checks for page number
        pages_number = ""
        collection = False
        while collection != True:
            aa += 1
            ab += 1
            if contents[aa:ab] != ")":  # End of page number and saves page number.
                pages_number += str(contents[aa:ab])
                print(pages_number)
            else:
                break

def collect_line_number(book):
    aa = 0
    ab = 1
    line_number = ""
    contents = open(book, 'rt').read().lower()
    while True:  # Collects line number
        aa += 1
        ab += 1
        if contents[aa:ab] != "{":
            print(contents[aa:ab])
            line_number += contents[aa:ab]
        else:
            print(line_number)
            break

def check_char(book):
    global pages_number
    aa = 0
    ab = 1
    a = []
    contents = open(book, 'rt').read().lower()
    len_contents = len(contents)
    while aa != len_contents:
        ba = 0
        bb = 1
        if contents[aa:ab] != "}":
            if contents[aa:ab] == "a":
                a.append(str(pages_number) + "." + str(line_number) + "." + str(bb))
        if contents[aa:ab] == "}":
            print(pages_number)
            print(line_number)
            print(bb)
            print(a)
            break
        ba += 1
        bb += 1
        aa += 1
        ab += 1
        print(contents[aa:ab])

def bookconversion2(book):#Coverts .book file to .char file
    total_pages(book)
    check_for_page_number(book)
    collect_line_number(book)
    check_char(book)
"""
def bookconversion3(book,new):
    aa = -1
    ab = 0
    ba = 0
    bb = 0
    total_pages = ""
    line_number = ""
    a = b = c = d = e = f = g = h = i = j = k = l = m = n = o = p = q = r = s = t = u = v = w = x = y = z = fullstop = space = []
    contents = open(book, 'rt').read().lower()
    len_contents = len(contents)
    while aa <= len_contents:
        if contents[aa:ab] == "[":  # Checks and saves the total pages of the .book file
            ba = aa
            bb = ab
            aa += 1
            ab += 1
            while True:
                ba += 1
                bb += 1
                if contents[ba:bb] != "]":
                    total_pages += str(contents[aa:ab])
                elif contents[ba:bb] == "]":
                    print("total = " + total_pages)
                    break
        if contents[aa:ab] == "(" and contents[aa:ab] != ")":# Checks for page number
            pages_number = ""
            ba = aa
            bb = ab
            while True:
                ba += 1
                bb += 1
                if contents[ba:bb] != ")" and contents[ba:bb] != "(":# End of page number and saves page number.
                    if contents[ba:bb] == "1" or contents[ba:bb] == "2" or contents[ba:bb] == "3" or contents[ba:bb] == "4" or contents[ba:bb] == "5" or contents[ba:bb] == "6" or contents[ba:bb] == "7" or contents[ba:bb] == "8" or contents[ba:bb] == "9" or contents[ba:bb] == "0":
                        pages_number += str(contents[ba:bb])
                elif contents[ba:bb] == ")":
                    print("Page Number = " + pages_number)
                    aa = ba
                    ab = bb
                    break
        if contents[aa:ab] == "£":
            ba = aa
            bb = ab
            line_number = ""
            while True:  # Collects line number
                ba += 1
                bb += 1
                if contents[ba:bb] != "{":
                    line_number += contents[ba:bb]
                else:
                    print("Line Number = "+line_number)
                    aa = ba
                    ab = bb
                    break
        if contents[aa:ab] == "{":
            ba = aa
            bb = ab
            char_number = -1
            while True:
                if contents[ba:bb] != "}":
                    char_number += 1
                    if contents[ba:bb] == "a":
                        a.append(str(pages_number) + "." + str(line_number) + "." + str(char_number))
                    if contents[ba:bb] == "b":
                        b.append(str(pages_number) + "." + str(line_number) + "." + str(char_number))
                    if contents[ba:bb] == "c":
                        c.append(str(pages_number) + "." + str(line_number) + "." + str(char_number))
                    if contents[ba:bb] == "d":
                        d.append(str(pages_number) + "." + str(line_number) + "." + str(char_number))
                    if contents[ba:bb] == "e":
                        e.append(str(pages_number) + "." + str(line_number) + "." + str(char_number))
                    if contents[ba:bb] == "f":
                        f.append(str(pages_number) + "." + str(line_number) + "." + str(char_number))
                    if contents[ba:bb] == "g":
                        g.append(str(pages_number) + "." + str(line_number) + "." + str(char_number))
                    if contents[ba:bb] == "h":
                        h.append(str(pages_number) + "." + str(line_number) + "." + str(char_number))
                    if contents[ba:bb] == "i":
                        i.append(str(pages_number) + "." + str(line_number) + "." + str(char_number))
                    if contents[ba:bb] == "j":
                        j.append(str(pages_number) + "." + str(line_number) + "." + str(char_number))
                    if contents[ba:bb] == "k":
                        k.append(str(pages_number) + "." + str(line_number) + "." + str(char_number))
                    if contents[ba:bb] == "l":
                        l.append(str(pages_number) + "." + str(line_number) + "." + str(char_number))
                    if contents[ba:bb] == "m":
                        m.append(str(pages_number) + "." + str(line_number) + "." + str(char_number))
                    if contents[ba:bb] == "n":
                        n.append(str(pages_number) + "." + str(line_number) + "." + str(char_number))
                    if contents[ba:bb] == "o":
                        o.append(str(pages_number) + "." + str(line_number) + "." + str(char_number))
                    if contents[ba:bb] == "p":
                        p.append(str(pages_number) + "." + str(line_number) + "." + str(char_number))
                    if contents[ba:bb] == "q":
                        q.append(str(pages_number) + "." + str(line_number) + "." + str(char_number))
                    if contents[ba:bb] == "r":
                        r.append(str(pages_number) + "." + str(line_number) + "." + str(char_number))
                    if contents[ba:bb] == "s":
                        s.append(str(pages_number) + "." + str(line_number) + "." + str(char_number))
                    if contents[ba:bb] == "t":
                        t.append(str(pages_number) + "." + str(line_number) + "." + str(char_number))
                    if contents[ba:bb] == "u":
                        u.append(str(pages_number) + "." + str(line_number) + "." + str(char_number))
                    if contents[ba:bb] == "v":
                        v.append(str(pages_number) + "." + str(line_number) + "." + str(char_number))
                    if contents[ba:bb] == "w":
                        w.append(str(pages_number) + "." + str(line_number) + "." + str(char_number))
                    if contents[ba:bb] == "x":
                        x.append(str(pages_number) + "." + str(line_number) + "." + str(char_number))
                    if contents[ba:bb] == "y":
                        y.append(str(pages_number) + "." + str(line_number) + "." + str(char_number))
                    if contents[ba:bb] == "z":
                        z.append(str(pages_number) + "." + str(line_number) + "." + str(char_number))
                    if contents[ba:bb] == ".":
                        fullstop.append(str(pages_number) + "." + str(line_number) + "." + str(char_number))
                    if contents[ba:bb] == " ":
                        space.append(str(pages_number) + "." + str(line_number) + "." + str(char_number))
                if contents[ba:bb] == "}":
                    break
                ba += 1
                bb += 1
                aa += 1
                ab += 1

        aa += 1
        ab += 1
    return(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,fullstop,space)


print(bookcheck("test.book"))
bookconversion3("test.book","test.char")