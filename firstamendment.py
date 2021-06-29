"""
Project: First Amendment
Author: Bombay20
Date Created: 10/6/2021
Date Last Modified: 26/6/2021
"""
import os
def bookcheck(book):#Checks the book file to make sure what char are advalable
    ab = 0
    a = b = c = d = e = f = g = h = i = j = k = l = m = n = o = p = q = r = s = t = u = v = w = x = y = z = fullstop = space = new_line = 0
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

def bookconversion(book,new):
    aa = -1
    ab = 0
    ba = 0
    bb = 0
    ca = ""
    total_pages = ""
    line_number = ""
    char_a = ""
    a = b = c = d = e = f = g = h = i = j = k = l = m = n = o = p = q = r = s = t = u = v = w = x = y = z = fullstop = space = ""
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
                    ba += 1
                    bb += 1
                    if contents[ba:bb] == "a":
                        a += str(pages_number) + "." + str(line_number) + "." + str(char_number) + ","
                    if contents[ba:bb] == "b":
                        b += str(pages_number) + "." + str(line_number) + "." + str(char_number) + ","
                    if contents[ba:bb] == "c":
                        c += str(pages_number) + "." + str(line_number) + "." + str(char_number) + ","
                    if contents[ba:bb] == "d":
                        d += str(pages_number) + "." + str(line_number) + "." + str(char_number) + ","
                    if contents[ba:bb] == "e":
                        e += str(pages_number) + "." + str(line_number) + "." + str(char_number) + ","
                    if contents[ba:bb] == "f":
                        f += str(pages_number) + "." + str(line_number) + "." + str(char_number) + ","
                    if contents[ba:bb] == "g":
                        g += str(pages_number) + "." + str(line_number) + "." + str(char_number) + ","
                    if contents[ba:bb] == "h":
                        h += str(pages_number) + "." + str(line_number) + "." + str(char_number) + ","
                    if contents[ba:bb] == "i":
                        i += str(pages_number) + "." + str(line_number) + "." + str(char_number) + ","
                    if contents[ba:bb] == "j":
                        j += str(pages_number) + "." + str(line_number) + "." + str(char_number) + ","
                    if contents[ba:bb] == "k":
                        k += str(pages_number) + "." + str(line_number) + "." + str(char_number) + ","
                    if contents[ba:bb] == "l":
                        l += str(pages_number) + "." + str(line_number) + "." + str(char_number) + ","
                    if contents[ba:bb] == "m":
                        m += str(pages_number) + "." + str(line_number) + "." + str(char_number) + ","
                    if contents[ba:bb] == "n":
                        n += str(pages_number) + "." + str(line_number) + "." + str(char_number) + ","
                    if contents[ba:bb] == "o":
                        o += str(pages_number) + "." + str(line_number) + "." + str(char_number) + ","
                    if contents[ba:bb] == "p":
                        p += str(pages_number) + "." + str(line_number) + "." + str(char_number) + ","
                    if contents[ba:bb] == "q":
                        q += str(pages_number) + "." + str(line_number) + "." + str(char_number) + ","
                    if contents[ba:bb] == "r":
                        r += str(pages_number) + "." + str(line_number) + "." + str(char_number) + ","
                    if contents[ba:bb] == "s":
                        s += str(pages_number) + "." + str(line_number) + "." + str(char_number) + ","
                    if contents[ba:bb] == "t":
                        t += str(pages_number) + "." + str(line_number) + "." + str(char_number) + ","
                    if contents[ba:bb] == "u":
                        u += str(pages_number) + "." + str(line_number) + "." + str(char_number) + ","
                    if contents[ba:bb] == "v":
                        v += str(pages_number) + "." + str(line_number) + "." + str(char_number) + ","
                    if contents[ba:bb] == "w":
                        w += str(pages_number) + "." + str(line_number) + "." + str(char_number) + ","
                    if contents[ba:bb] == "x":
                        x += str(pages_number) + "." + str(line_number) + "." + str(char_number) + ","
                    if contents[ba:bb] == "y":
                        y += str(pages_number) + "." + str(line_number) + "." + str(char_number) + ","
                    if contents[ba:bb] == "z":
                        z += str(pages_number) + "." + str(line_number) + "." + str(char_number) + ","
                    if contents[ba:bb] == ".":
                        fullstop += str(pages_number) + "." + str(line_number) + "." + str(char_number) + ","
                    if contents[ba:bb] == " ":
                        space += str(pages_number) + "." + str(line_number) + "." + str(char_number) + ","
                if contents[ba:bb] == "}":
                    aa = ba
                    ab = bb
                    break

        aa += 1
        ab += 1
    try:
        new_file = open(new, "x")
    except:
        os.remove(new)
    new_file = open(new, "a")#check list save
    new_file.write(str(a[0:len(a)-1])+'\n'+str(b[0:len(b)-1])+'\n'+str(c[0:len(c)-1])+'\n'+str(d[0:len(d)-1])+'\n'+str(e[0:len(e)-1])+'\n'+str(f[0:len(f)-1])+'\n'+str(g[0:len(g)-1])+'\n'+str(h[0:len(h)-1])+'\n'+str(i[0:len(i)-1])+'\n'+str(j[0:len(j)-1])+'\n'+str(k[0:len(k)-1])+'\n'+str(l[0:len(l)-1])+'\n'+str(m[0:len(m)-1])+'\n'+str(n[0:len(n)-1])+'\n'+str(o[0:len(o)-1])+'\n'+str(p[0:len(p)-1])+'\n'+str(q[0:len(q)-1])+'\n'+str(r[0:len(r)-1])+'\n'+str(s[0:len(s)-1])+'\n'+str(t[0:len(t)-1])+'\n'+str(u[0:len(u)-1])+'\n'+str(v[0:len(v)-1])+'\n'+str(w[0:len(w)-1])+'\n'+str(x[0:len(x)-1])+'\n'+str(y[0:len(y)-1])+'\n'+str(z[0:len(z)-1])+'\n'+str(fullstop[0:len(fullstop)-1])+'\n'+str(space[0:len(space)-1]))
    new_file.close()
    return("File Input: "+book+'\n'+"File Output: "+new)

def bookencryption(text,char,fileoutput):#*args,text,char,save,fileoutput
    a_count = b_count = c_count = d_count = e_count = f_count = g_count = h_count = i_count = j_count = k_count = l_count = m_count = n_count = o_count = p_count = q_count = r_count = s_count = t_count = u_count = v_count = w_count = x_count = y_count = z_count = fullstop_count = space_count = -1
    encrypted = encrypted_new = ""
    text = open(text, "rt").read()
    file_char = open(char, "rt")
    new = file_char.readlines()
    a = new[0]
    a = a[0:len(a)-1]
    if len(a) > 0:
        a = a.split(",")
    b = new[1]
    b = b[0:len(b)-1]
    if len(b) > 0:
        b = b.split(",")
    c = new[2]
    c = c[0:len(c)-1]
    if len(c) > 0:
        c = c.split(",")
    d = new[3]
    d = d[0:len(d)-1]
    if len(d) > 0:
        d = d.split(",")
    e = new[4]
    e = e[0:len(e)-1]
    if len(e) > 0:
        e = e.split(",")
    f = new[5]
    f = f[0:len(f)-1]
    if len(f) > 0:
        f = f.split(",")
    g = new[6]
    g = g[0:len(g)-1]
    if len(g) > 0:
        g = g.split(",")
    h = new[7]
    h = h[0:len(h)-1]
    if len(h) > 0:
        h = h.split(",")
    i = new[8]
    i = i[0:len(i)-1]
    if len(i) > 0:
        i = i.split(",")
    j = new[9]
    j = j[0:len(j)-1]
    if len(j) > 0:
        j = j.split(",")
    k = new[10]
    k = k[0:len(k)-1]
    if len(k) > 0:
        k = k.split(",")
    l = new[11]
    l = l[0:len(l)-1]
    if len(l) > 0:
        l = l.split(",")
    m = new[12]
    m = m[0:len(m)-1]
    if len(m) > 0:
        m = m.split(",")
    n = new[13]
    n = n[0:len(n)-1]
    if len(n) > 0:
        n = n.split(",")
    o = new[14]
    o = o[0:len(o)-1]
    if len(o) > 0:
        o = o.split(",")
    p = new[15]
    p = p[0:len(p)-1]
    if len(p) > 0:
        p = p.split(",")
    q = new[16]
    q = q[0:len(q)-1]
    if len(q) > 0:
        q = q.split(",")
    r = new[17]
    r = r[0:len(r)-1]
    if len(r) > 0:
        r = r.split(",")
    s = new[18]
    s = s[0:len(s)-1]
    if len(s) > 0:
        s = s.split(",")
    t = new[19]
    t = t[0:len(t)-1]
    if len(t) > 0:
        t = t.split(",")
    u = new[20]
    u = u[0:len(u)-1]
    if len(u) > 0:
        u = u.split(",")
    v = new[21]
    v = v[0:len(v)-1]
    if len(v) > 0:
        v = v.split(",")
    w = new[22]
    w = w[0:len(w)-1]
    if len(w) > 0:
        w = w.split(",")
    x = new[23]
    x = x[0:len(x)-1]
    if len(x) > 0:
        x = x.split(",")
    y = new[24]
    y = y[0:len(y)-1]
    if len(y) > 0:
        y = y.split(",")
    z = new[25]
    z = z[0:len(z)-1]
    if len(z) > 0:
        z = z.split(",")
    fullstop = new[26]
    fullstop = fullstop[0:len(fullstop)-1]
    if len(fullstop) > 0:
        fullstop = fullstop.split(",")
    space = new[27]
    space = space[0:len(space)-1]
    if len(space) > 0:
        space = space.split(",")
    aa = -1
    ab = 0
    while True:
        aa += 1
        ab += 1
        if text[aa:ab] == "a" and len(a) > 0:
            a_count += 1
            if a_count > len(a):
                a_count = 0
            encrypted_new = str(a[a_count: a_count+1])
            encrypted_new = encrypted_new[2:len(encrypted_new)-2]
            encrypted_new = "0."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "b" and len(b) > 0:
            b_count += 1
            if b_count > len(b):
                b_count = 0
            encrypted_new = str(b[b_count: b_count+1])
            encrypted_new = encrypted_new[2:len(encrypted_new)-2]
            encrypted_new = "0."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "c" and len(c) > 0:
            c_count += 1
            if c_count > len(c):
                c_count = 0
            encrypted_new = str(c[c_count:c_count+1])
            encrypted_new = encrypted_new[2:len(encrypted_new)-2]
            encrypted_new = "0."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "d" and len(d) > 0:
            d_count += 1
            if d_count > len(d):
                d_count = 0
            encrypted_new = str(d[d_count:d_count+1])
            encrypted_new = encrypted_new[2:len(encrypted_new)-2]
            encrypted_new = "0."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "e" and len(e) > 0:
            e_count += 1
            if e_count > len(e):
                e_count = 0
            encrypted_new = str(e[e_count:e_count+1])
            encrypted_new = encrypted_new[2:len(encrypted_new)-2]
            encrypted_new = "0."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "f" and len(f) > 0:
            f_count += 1
            if f_count > len(f):
                f_count = 0
            encrypted_new = str(f[f_count:f_count+1])
            encrypted_new = encrypted_new[2:len(encrypted_new)-2]
            encrypted_new = "0."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "g" and len(g) > 0:
            g_count += 1
            if g_count > len(g):
                g_count = 0
            encrypted_new = str(g[g_count:g_count+1])
            encrypted_new = encrypted_new[2:len(encrypted_new)-2]
            encrypted_new = "0."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "h" and len(h) > 0:
            h_count += 1
            if h_count > len(h):
                h_count = 0
            encrypted_new = str(h[h_count:h_count+1])
            encrypted_new = encrypted_new[2:len(encrypted_new)-2]
            encrypted_new = "0."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "i" and len(i) > 0:
            i_count += 1
            if i_count > len(i):
                i_count = 0
            encrypted_new = str(i[i_count:i_count+1])
            encrypted_new = encrypted_new[2:len(encrypted_new)-2]
            encrypted_new = "0."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "j" and len(j) > 0:
            j_count += 1
            if j_count > len(j):
                j_count = 0
            encrypted_new = str(j[j_count:j_count+1])
            encrypted_new = encrypted_new[2:len(encrypted_new)-2]
            encrypted_new = "0."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "k" and len(k) > 0:
            k_count += 1
            if k_count > len(k):
                k_count = 0
            encrypted_new = str(k[k_count:k_count+1])
            encrypted_new = encrypted_new[2:len(encrypted_new)-2]
            encrypted_new = "0."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "l" and len(l) > 0:
            l_count += 1
            if l_count > len(l):
                l_count = 0
            encrypted_new = str(l[l_count:l_count+1])
            encrypted_new = encrypted_new[2:len(encrypted_new)-2]
            encrypted_new = "0."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "m" and len(m) > 0:
            m_count += 1
            if m_count > len(m):
                m_count = 0
            encrypted_new = str(m[m_count:m_count+1])
            encrypted_new = encrypted_new[2:len(encrypted_new)-2]
            encrypted_new = "0."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "n" and len(n) > 0:
            n_count += 1
            if n_count > len(n):
                n_count = 0
            encrypted_new = str(n[n_count:n_count+1])
            encrypted_new = encrypted_new[2:len(encrypted_new)-2]
            encrypted_new = "0."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "o" and len(o) > 0:
            o_count += 1
            if o_count > len(o):
                o_count = 0
            encrypted_new = str(o[o_count:o_count+1])
            encrypted_new = encrypted_new[2:len(encrypted_new)-2]
            encrypted_new = "0."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "p" and len(p) > 0:
            p_count += 1
            if p_count > len(p):
                p_count = 0
            encrypted_new = str(p[p_count:p_count+1])
            encrypted_new = encrypted_new[2:len(encrypted_new)-2]
            encrypted_new = "0."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "q" and len(q) > 0:
            q_count += 1
            if q_count > len(q):
                q_count = 0
            encrypted_new = str(q[q_count:q_count+1])
            encrypted_new = encrypted_new[2:len(encrypted_new)-2]
            encrypted_new = "0."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "r" and len(r) > 0:
            r_count += 1
            if r_count > len(r):
                r_count = 0
            encrypted_new = str(r[r_count:r_count+1])
            encrypted_new = encrypted_new[2:len(encrypted_new)-2]
            encrypted_new = "0."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "s" and len(s) > 0:
            s_count += 1
            if s_count > len(s):
                s_count = 0
            encrypted_new = str(s[s_count:s_count+1])
            encrypted_new = encrypted_new[2:len(encrypted_new)-2]
            encrypted_new = "0."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "t" and len(t) > 0:
            t_count += 1
            if t_count > len(t):
                t_count = 0
            encrypted_new = str(t[t_count:t_count+1])
            encrypted_new = encrypted_new[2:len(encrypted_new)-2]
            encrypted_new = "0."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "u" and len(u) > 0:
            u_count += 1
            if u_count > len(u):
                u_count = 0
            encrypted_new = str(u[u_count:u_count+1])
            encrypted_new = encrypted_new[2:len(encrypted_new)-2]
            encrypted_new = "0."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "v" and len(v) > 0:
            v_count += 1
            if v_count > len(v):
                v_count = 0
            encrypted_new = str(v[v_count:v_count+1])
            encrypted_new = encrypted_new[2:len(encrypted_new)-2]
            encrypted_new = "0."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "w" and len(w) > 0:
            w_count += 1
            if w_count > len(w):
                w_count = 0
            encrypted_new = str(w[w_count:w_count+1])
            encrypted_new = encrypted_new[2:len(encrypted_new)-2]
            encrypted_new = "0."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "x" and len(x) > 0:
            x_count += 1
            if x_count > len(x):
                x_count = 0
            encrypted_new = str(x[x_count:x_count+1])
            encrypted_new = encrypted_new[2:len(encrypted_new)-2]
            encrypted_new = "0."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "y" and len(y) > 0:
            y_count += 1
            if y_count > len(y):
                y_count = 0
            encrypted_new = str(y[y_count:y_count+1])
            encrypted_new = encrypted_new[2:len(encrypted_new)-2]
            encrypted_new = "0."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "z" and len(z) > 0:
            z_count += 1
            if z_count > len(z):
                z_count = 0
            encrypted_new = str(z[z_count:z_count+1])
            encrypted_new = encrypted_new[2:len(encrypted_new)-2]
            encrypted_new = "0."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "A" and len(a) > 0:
            a_count += 1
            if a_count > len(a):
                a_count = 0
            encrypted_new = str(a[a_count: a_count + 1])
            encrypted_new = encrypted_new[2:len(encrypted_new) - 2]
            encrypted_new = "1."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "B" and len(b) > 0:
            b_count += 1
            if b_count > len(b):
                b_count = 0
            encrypted_new = str(b[b_count: b_count + 1])
            encrypted_new = encrypted_new[2:len(encrypted_new) - 2]
            encrypted_new = "1."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "C" and len(c) > 0:
            c_count += 1
            if c_count > len(c):
                c_count = 0
            encrypted_new = str(c[c_count:c_count + 1])
            encrypted_new = encrypted_new[2:len(encrypted_new) - 2]
            encrypted_new = "1."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "D" and len(d) > 0:
            d_count += 1
            if d_count > len(d):
                d_count = 0
            encrypted_new = str(d[d_count:d_count + 1])
            encrypted_new = encrypted_new[2:len(encrypted_new) - 2]
            encrypted_new = "1."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "E" and len(e) > 0:
            e_count += 1
            if e_count > len(e):
                e_count = 0
            encrypted_new = str(e[e_count:e_count + 1])
            encrypted_new = encrypted_new[2:len(encrypted_new) - 2]
            encrypted_new = "1."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "F" and len(f) > 0:
            f_count += 1
            if f_count > len(f):
                f_count = 0
            encrypted_new = str(f[f_count:f_count + 1])
            encrypted_new = encrypted_new[2:len(encrypted_new) - 2]
            encrypted_new = "1."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "G" and len(g) > 0:
            g_count += 1
            if g_count > len(g):
                g_count = 0
            encrypted_new = str(g[g_count:g_count + 1])
            encrypted_new = encrypted_new[2:len(encrypted_new) - 2]
            encrypted_new = "1."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "H" and len(h) > 0:
            h_count += 1
            if h_count > len(h):
                h_count = 0
            encrypted_new = str(h[h_count:h_count + 1])
            encrypted_new = encrypted_new[2:len(encrypted_new) - 2]
            encrypted_new = "1."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "I" and len(i) > 0:
            i_count += 1
            if i_count > len(i):
                i_count = 0
            encrypted_new = str(i[i_count:i_count + 1])
            encrypted_new = encrypted_new[2:len(encrypted_new) - 2]
            encrypted_new = "1."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "J" and len(j) > 0:
            j_count += 1
            if j_count > len(j):
                j_count = 0
            encrypted_new = str(j[j_count:j_count + 1])
            encrypted_new = encrypted_new[2:len(encrypted_new) - 2]
            encrypted_new = "1."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "K" and len(k) > 0:
            k_count += 1
            if k_count > len(k):
                k_count = 0
            encrypted_new = str(k[k_count:k_count + 1])
            encrypted_new = encrypted_new[2:len(encrypted_new) - 2]
            encrypted_new = "1."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "L" and len(l) > 0:
            l_count += 1
            if l_count > len(l):
                l_count = 0
            encrypted_new = str(l[l_count:l_count + 1])
            encrypted_new = encrypted_new[2:len(encrypted_new) - 2]
            encrypted_new = "1."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "M" and len(m) > 0:
            m_count += 1
            if m_count > len(m):
                m_count = 0
            encrypted_new = str(m[m_count:m_count + 1])
            encrypted_new = encrypted_new[2:len(encrypted_new) - 2]
            encrypted_new = "1."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "N" and len(n) > 0:
            n_count += 1
            if n_count > len(n):
                n_count = 0
            encrypted_new = str(n[n_count:n_count + 1])
            encrypted_new = encrypted_new[2:len(encrypted_new) - 2]
            encrypted_new = "1."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "O" and len(o) > 0:
            o_count += 1
            if o_count > len(o):
                o_count = 0
            encrypted_new = str(o[o_count:o_count + 1])
            encrypted_new = encrypted_new[2:len(encrypted_new) - 2]
            encrypted_new = "1."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "P" and len(p) > 0:
            p_count += 1
            if p_count > len(p):
                p_count = 0
            encrypted_new = str(p[p_count:p_count + 1])
            encrypted_new = encrypted_new[2:len(encrypted_new) - 2]
            encrypted_new = "1."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "Q" and len(q) > 0:
            q_count += 1
            if q_count > len(q):
                q_count = 0
            encrypted_new = str(q[q_count:q_count + 1])
            encrypted_new = encrypted_new[2:len(encrypted_new) - 2]
            encrypted_new = "1."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "R" and len(r) > 0:
            r_count += 1
            if r_count > len(r):
                r_count = 0
            encrypted_new = str(r[r_count:r_count + 1])
            encrypted_new = encrypted_new[2:len(encrypted_new) - 2]
            encrypted_new = "1."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "S" and len(s) > 0:
            s_count += 1
            if s_count > len(s):
                s_count = 0
            encrypted_new = str(s[s_count:s_count + 1])
            encrypted_new = encrypted_new[2:len(encrypted_new) - 2]
            encrypted_new = "1."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "T" and len(t) > 0:
            t_count += 1
            if t_count > len(t):
                t_count = 0
            encrypted_new = str(t[t_count:t_count + 1])
            encrypted_new = encrypted_new[2:len(encrypted_new) - 2]
            encrypted_new = "1."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "U" and len(u) > 0:
            u_count += 1
            if u_count > len(u):
                u_count = 0
            encrypted_new = str(u[u_count:u_count + 1])
            encrypted_new = encrypted_new[2:len(encrypted_new) - 2]
            encrypted_new = "1."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "V" and len(v) > 0:
            v_count += 1
            if v_count > len(v):
                v_count = 0
            encrypted_new = str(v[v_count:v_count + 1])
            encrypted_new = encrypted_new[2:len(encrypted_new) - 2]
            encrypted_new = "1."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "W" and len(w) > 0:
            w_count += 1
            if w_count > len(w):
                w_count = 0
            encrypted_new = str(w[w_count:w_count + 1])
            encrypted_new = encrypted_new[2:len(encrypted_new) - 2]
            encrypted_new = "1."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "X" and len(x) > 0:
            x_count += 1
            if x_count > len(x):
                x_count = 0
            encrypted_new = str(x[x_count:x_count + 1])
            encrypted_new = encrypted_new[2:len(encrypted_new) - 2]
            encrypted_new = "1."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "Y" and len(y) > 0:
            y_count += 1
            if y_count > len(y):
                y_count = 0
            encrypted_new = str(y[y_count:y_count + 1])
            encrypted_new = encrypted_new[2:len(encrypted_new) - 2]
            encrypted_new = "1."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "Z" and len(z) > 0:
            z_count += 1
            if z_count > len(z):
                z_count = 0
            encrypted_new = str(z[z_count:z_count + 1])
            encrypted_new = encrypted_new[2:len(encrypted_new) - 2]
            encrypted_new = "1."+encrypted_new
            encrypted += encrypted_new + ","
        if text[aa:ab] == "." and len(fullstop) > 0:
            fullstop_count += 1
            if fullstop_count > len(fullstop):
                fullstop_count = 0
            encrypted_new = str(fullstop[fullstop_count:fullstop_count+1])
            encrypted_new = encrypted_new[2:len(encrypted_new)-2]
            encrypted += encrypted_new + ","
        if text[aa:ab] == " " and len(space) > 0:
            space_count += 1
            if space_count > len(space):
                space_count = 0
            encrypted_new = str(space[space_count:space_count+1])
            encrypted_new = encrypted_new[2:len(encrypted_new)-2]
            encrypted += encrypted_new + ","
        if text[aa:ab] == '\n':
            encrypted += '\n'
        if ab > len(text):
            encrypted = encrypted[0:len(encrypted)-1]
            file_name = str(fileoutput)
            try:
                new_file = open(file_name+".encrypt", "x")
            except:
                os.remove(file_name+".encrypt")
            new_file = open(file_name+".encrypt", "a")#check list save
            new_file.write(encrypted)
            new_file.close()
            return("Encrypted:\n"+encrypted)

#Do Encryption capatials before the Decryption
def bookdecryption(text1,char,fileoutput):
    a_count = b_count = c_count = d_count = e_count = f_count = g_count = h_count = i_count = j_count = k_count = l_count = m_count = n_count = o_count = p_count = q_count = r_count = s_count = t_count = u_count = v_count = w_count = x_count = y_count = z_count = fullstop_count = space_count = A_count = B_count = C_count = D_count = E_count = F_count = G_count = H_count = I_count = J_count = K_count = L_count = M_count = N_count = O_count = P_count = Q_count = R_count = S_count = T_count = U_count = V_count = W_count = X_count = Y_count = Z_count = 0
    aa = -1
    ab = 0
    text = []
    file_char = open(char, "rt")
    new = file_char.readlines()
    text1 = open(text1, "rt")
    a = new[0]
    a = a[0:len(a)-1]
    if len(a) > 0:
        a = a.split(",")
    b = new[1]
    b = b[0:len(b)-1]
    if len(b) > 0:
        b = b.split(",")
    c = new[2]
    c = c[0:len(c)-1]
    if len(c) > 0:
        c = c.split(",")
    d = new[3]
    d = d[0:len(d)-1]
    if len(d) > 0:
        d = d.split(",")
    e = new[4]
    e = e[0:len(e)-1]
    if len(e) > 0:
        e = e.split(",")
    f = new[5]
    f = f[0:len(f)-1]
    if len(f) > 0:
        f = f.split(",")
    g = new[6]
    g = g[0:len(g)-1]
    if len(g) > 0:
        g = g.split(",")
    h = new[7]
    h = h[0:len(h)-1]
    if len(h) > 0:
        h = h.split(",")
    i = new[8]
    i = i[0:len(i)-1]
    if len(i) > 0:
        i = i.split(",")
    j = new[9]
    j = j[0:len(j)-1]
    if len(j) > 0:
        j = j.split(",")
    k = new[10]
    k = k[0:len(k)-1]
    if len(k) > 0:
        k = k.split(",")
    l = new[11]
    l = l[0:len(l)-1]
    if len(l) > 0:
        l = l.split(",")
    m = new[12]
    m = m[0:len(m)-1]
    if len(m) > 0:
        m = m.split(",")
    n = new[13]
    n = n[0:len(n)-1]
    if len(n) > 0:
        n = n.split(",")
    o = new[14]
    o = o[0:len(o)-1]
    if len(o) > 0:
        o = o.split(",")
    p = new[15]
    p = p[0:len(p)-1]
    if len(p) > 0:
        p = p.split(",")
    q = new[16]
    q = q[0:len(q)-1]
    if len(q) > 0:
        q = q.split(",")
    r = new[17]
    r = r[0:len(r)-1]
    if len(r) > 0:
        r = r.split(",")
    s = new[18]
    s = s[0:len(s)-1]
    if len(s) > 0:
        s = s.split(",")
    t = new[19]
    t = t[0:len(t)-1]
    if len(t) > 0:
        t = t.split(",")
    u = new[20]
    u = u[0:len(u)-1]
    if len(u) > 0:
        u = u.split(",")
    v = new[21]
    v = v[0:len(v)-1]
    if len(v) > 0:
        v = v.split(",")
    w = new[22]
    w = w[0:len(w)-1]
    if len(w) > 0:
        w = w.split(",")
    x = new[23]
    x = x[0:len(x)-1]
    if len(x) > 0:
        x = x.split(",")
    y = new[24]
    y = y[0:len(y)-1]
    if len(y) > 0:
        y = y.split(",")
    z = new[25]
    z = z[0:len(z)-1]
    if len(z) > 0:
        z = z.split(",")
    fullstop = new[26]
    fullstop = fullstop[0:len(fullstop)-1]
    if len(fullstop) > 0:
        fullstop = fullstop.split(",")
    space = new[27]
    space = space[0:len(space)-1]
    if len(space) > 0:
        space = space.split(",")
    text1 = text1.readlines()
    for nn in range(len(text1)):
        text += text1[nn].split(",")
    decryption = ""
    while True:
        aa += 1
        ab += 1
        if str(text[aa:ab]) == "['0."+str(a[a_count:a_count+1])[2:len(str(a[a_count:a_count+1]))-2]+"']":
            a_count += 1
            if a_count > len(a):
                a_count = 0
            decryption += "a"
        if str(text[aa:ab]) == "['0."+str(b[b_count:b_count+1])[2:len(str(b[b_count:b_count+1]))-2]+"']":
            b_count += 1
            if b_count > len(b):
                b_count = 0
            decryption += "b"
        if str(text[aa:ab]) == "['0."+str(c[c_count:b_count+1])[2:len(str(c[c_count:c_count+1]))-2]+"']":
            c_count += 1
            if c_count > len(c):
                c_count = 0
            decryption += "c"
        if str(text[aa:ab]) == "['0."+str(d[d_count:d_count+1])[2:len(str(d[d_count:d_count+1]))-2]+"']":
            d_count += 1
            if d_count > len(d):
                d_count = 0
            decryption += "d"
        if str(text[aa:ab]) == "['0."+str(e[e_count:e_count+1])[2:len(str(e[e_count:e_count+1]))-2]+"']":
            e_count += 1
            if e_count > len(e):
                e_count = 0
            decryption += "e"
        if str(text[aa:ab]) == "['0."+str(f[f_count:f_count+1])[2:len(str(f[f_count:f_count+1]))-2]+"']":
            f_count += 1
            if f_count > len(f):
                f_count = 0
            decryption += "f"
        if str(text[aa:ab]) == "['0."+str(g[g_count:g_count+1])[2:len(str(g[g_count:g_count+1]))-2]+"']":
            g_count += 1
            if g_count > len(g):
                g_count = 0
            decryption += "g"
        if str(text[aa:ab]) == "['0."+str(h[h_count:h_count+1])[2:len(str(h[h_count:h_count+1]))-2]+"']":
            h_count += 1
            if h_count > len(h):
                h_count = 0
            decryption += "h"
        if str(text[aa:ab]) == "['0."+str(i[i_count:i_count+1])[2:len(str(i[i_count:i_count+1]))-2]+"']":
            i_count += 1
            if i_count > len(i):
                i_count = 0
            decryption += "i"
        if str(text[aa:ab]) == "['0."+str(j[j_count:j_count+1])[2:len(str(j[j_count:j_count+1]))-2]+"']":
            j_count += 1
            if j_count > len(j):
                j_count = 0
            decryption += "j"
        if str(text[aa:ab]) == "['0."+str(k[k_count:k_count+1])[2:len(str(k[k_count:k_count+1]))-2]+"']":
            k_count += 1
            if k_count > len(k):
                k_count = 0
            decryption += "k"
        if str(text[aa:ab]) == "['0."+str(l[l_count:l_count+1])[2:len(str(l[l_count:l_count+1]))-2]+"']":
            l_count += 1
            if l_count > len(l):
                l_count = 0
            decryption += "l"
        if str(text[aa:ab]) == "['0."+str(m[m_count:m_count+1])[2:len(str(m[m_count:m_count+1]))-2]+"']":
            m_count += 1
            if m_count > len(m):
                m_count = 0
            decryption += "m"
        if str(text[aa:ab]) == "['0."+str(n[n_count:n_count+1])[2:len(str(n[n_count:n_count+1]))-2]+"']":
            n_count += 1
            if n_count > len(n):
                n_count = 0
            decryption += "n"
        if str(text[aa:ab]) == "['0."+str(o[o_count:o_count+1])[2:len(str(o[o_count:o_count+1]))-2]+"']":
            o_count += 1
            if o_count > len(o):
                o_count = 0
            decryption += "o"
        if str(text[aa:ab]) == "['0."+str(p[p_count:p_count+1])[2:len(str(p[p_count:p_count+1]))-2]+"']":
            p_count += 1
            if p_count > len(p):
                p_count = 0
            decryption += "p"
        if str(text[aa:ab]) == "['0."+str(q[q_count:q_count+1])[2:len(str(q[q_count:q_count+1]))-2]+"']":
            q_count += 1
            if q_count > len(q):
                q_count = 0
            decryption += "q"
        if str(text[aa:ab]) == "['0."+str(r[r_count:r_count+1])[2:len(str(r[r_count:r_count+1]))-2]+"']":
            r_count += 1
            if r_count > len(r):
                r_count = 0
            decryption += "r"
        if str(text[aa:ab]) == "['0."+str(s[s_count:s_count+1])[2:len(str(s[s_count:s_count+1]))-2]+"']":
            s_count += 1
            if s_count > len(b):
                s_count = 0
            decryption += "s"
        if str(text[aa:ab]) == "['0."+str(t[t_count:t_count+1])[2:len(str(t[t_count:t_count+1]))-2]+"']":
            t_count += 1
            if t_count > len(t):
                t_count = 0
            decryption += "t"
        if str(text[aa:ab]) == "['0."+str(u[u_count:u_count+1])[2:len(str(u[u_count:u_count+1]))-2]+"']":
            u_count += 1
            if u_count > len(u):
                u_count = 0
            decryption += "u"
        if str(text[aa:ab]) == "['0."+str(v[v_count:v_count+1])[2:len(str(v[v_count:v_count+1]))-2]+"']":
            v_count += 1
            if v_count > len(v):
                v_count = 0
            decryption += "v"
        if str(text[aa:ab]) == "['0."+str(w[w_count:w_count+1])[2:len(str(w[w_count:w_count+1]))-2]+"']":
            w_count += 1
            if w_count > len(w):
                w_count = 0
            decryption += "w"
        if str(text[aa:ab]) == "['0."+str(x[x_count:x_count+1])[2:len(str(x[x_count:x_count+1]))-2]+"']":
            x_count += 1
            if x_count > len(x):
                x_count = 0
            decryption += "x"
        if str(text[aa:ab]) == "['0."+str(y[y_count:y_count+1])[2:len(str(y[y_count:y_count+1]))-2]+"']":
            y_count += 1
            if y_count > len(y):
                y_count = 0
            decryption += "y"
        if str(text[aa:ab]) == "['0."+str(z[z_count:z_count+1])[2:len(str(z[z_count:z_count+1]))-2]+"']":
            z_count += 1
            if z_count > len(z):
                z_count = 0
            decryption += "z"
        if str(text[aa:ab]) == "['1."+str(a[a_count:a_count+1])[2:len(str(a[a_count:a_count+1]))-2]+"']":
            a_count += 1
            if a_count > len(a):
                a_count = 0
            decryption += "A"
        if str(text[aa:ab]) == "['1."+str(b[b_count:b_count+1])[2:len(str(b[b_count:b_count+1]))-2]+"']":
            b_count += 1
            if b_count > len(b):
                b_count = 0
            decryption += "B"
        if str(text[aa:ab]) == "['1."+str(c[c_count:c_count+1])[2:len(str(c[c_count:c_count+1]))-2]+"']":
            c_count += 1
            if c_count > len(c):
                c_count = 0
            decryption += "C"
        if str(text[aa:ab]) == "['1."+str(d[d_count:d_count+1])[2:len(str(d[d_count:d_count+1]))-2]+"']":
            d_count += 1
            if d_count > len(d):
                d_count = 0
            decryption += "D"
        if str(text[aa:ab]) == "['1."+str(e[e_count:e_count+1])[2:len(str(e[e_count:e_count+1]))-2]+"']":
            e_count += 1
            if e_count > len(e):
                e_count = 0
            decryption += "E"
        if str(text[aa:ab]) == "['1."+str(f[f_count:f_count+1])[2:len(str(f[f_count:f_count+1]))-2]+"']":
            f_count += 1
            if f_count > len(f):
                f_count = 0
            decryption += "F"
        if str(text[aa:ab]) == "['1."+str(g[g_count:g_count+1])[2:len(str(g[g_count:g_count+1]))-2]+"']":
            g_count += 1
            if g_count > len(g):
                g_count = 0
            decryption += "G"
        if str(text[aa:ab]) == "['1."+str(h[h_count:h_count+1])[2:len(str(h[h_count:h_count+1]))-2]+"']":
            h_count += 1
            if h_count > len(h):
                h_count = 0
            decryption += "H"
        if str(text[aa:ab]) == "['1."+str(i[i_count:i_count+1])[2:len(str(i[i_count:i_count+1]))-2]+"']":
            i_count += 1
            if i_count > len(i):
                i_count = 0
            decryption += "I"
        if str(text[aa:ab]) == "['1."+str(j[j_count:j_count+1])[2:len(str(j[j_count:j_count+1]))-2]+"']":
            j_count += 1
            if j_count > len(j):
                j_count = 0
            decryption += "J"
        if str(text[aa:ab]) == "['1."+str(k[k_count:k_count+1])[2:len(str(k[k_count:k_count+1]))-2]+"']":
            k_count += 1
            if k_count > len(k):
                k_count = 0
            decryption += "K"
        if str(text[aa:ab]) == "['1."+str(l[l_count:l_count+1])[2:len(str(l[l_count:l_count+1]))-2]+"']":
            l_count += 1
            if l_count > len(l):
                l_count = 0
            decryption += "L"
        if str(text[aa:ab]) == "['1."+str(m[m_count:m_count+1])[2:len(str(m[m_count:m_count+1]))-2]+"']":
            m_count += 1
            if m_count > len(m):
                m_count = 0
            decryption += "M"
        if str(text[aa:ab]) == "['1."+str(n[n_count:n_count+1])[2:len(str(n[n_count:n_count+1]))-2]+"']":
            n_count += 1
            if n_count > len(n):
                n_count = 0
            decryption += "N"
        if str(text[aa:ab]) == "['1."+str(o[o_count:o_count+1])[2:len(str(o[o_count:o_count+1]))-2]+"']":
            o_count += 1
            if o_count > len(o):
                o_count = 0
            decryption += "O"
        if str(text[aa:ab]) == "['1."+str(p[p_count:p_count+1])[2:len(str(p[p_count:p_count+1]))-2]+"']":
            p_count += 1
            if p_count > len(p):
                p_count = 0
            decryption += "P"
        if str(text[aa:ab]) == "['1."+str(q[q_count:q_count+1])[2:len(str(q[q_count:q_count+1]))-2]+"']":
            q_count += 1
            if q_count > len(q):
                q_count = 0
            decryption += "Q"
        if str(text[aa:ab]) == "['1."+str(r[r_count:r_count+1])[2:len(str(r[r_count:r_count+1]))-2]+"']":
            r_count += 1
            if r_count > len(r):
                r_count = 0
            decryption += "R"
        if str(text[aa:ab]) == "['1."+str(s[s_count:s_count+1])[2:len(str(s[s_count:s_count+1]))-2]+"']":
            s_count += 1
            if s_count > len(b):
                s_count = 0
            decryption += "S"
        if str(text[aa:ab]) == "['1."+str(t[b_count:t_count+1])[2:len(str(t[t_count:t_count+1]))-2]+"']":
            t_count += 1
            if t_count > len(t):
                t_count = 0
            decryption += "T"
        if str(text[aa:ab]) == "['1."+str(u[u_count:b_count+1])[2:len(str(u[u_count:u_count+1]))-2]+"']":
            u_count += 1
            if u_count > len(u):
                u_count = 0
            decryption += "U"
        if str(text[aa:ab]) == "['1."+str(v[v_count:v_count+1])[2:len(str(v[v_count:v_count+1]))-2]+"']":
            v_count += 1
            if v_count > len(v):
                v_count = 0
            decryption += "V"
        if str(text[aa:ab]) == "['1."+str(w[w_count:w_count+1])[2:len(str(w[w_count:w_count+1]))-2]+"']":
            w_count += 1
            if w_count > len(w):
                w_count = 0
            decryption += "W"
        if str(text[aa:ab]) == "['1."+str(x[x_count:x_count+1])[2:len(str(x[x_count:x_count+1]))-2]+"']":
            x_count += 1
            if x_count > len(x):
                x_count = 0
            decryption += "X"
        if str(text[aa:ab]) == "['1."+str(y[y_count:y_count+1])[2:len(str(y[y_count:y_count+1]))-2]+"']":
            y_count += 1
            if y_count > len(y):
                y_count = 0
            decryption += "Y"
        if str(text[aa:ab]) == "['1."+str(z[z_count:z_count+1])[2:len(str(z[z_count:z_count+1]))-2]+"']":
            z_count += 1
            if z_count > len(z):
                z_count = 0
            decryption += "Z"
        if str(text[aa:ab]) == "['"+str(fullstop[fullstop_count:fullstop_count+1])[2:len(str(fullstop[fullstop_count:fullstop_count+1]))-2]+"']":
            fullstop_count += 1
            if fullstop_count > len(fullstop):
                fullstop_count = 0
            decryption += "."
        if str(text[aa:ab]) == "['"+str(space[space_count:space_count+1])[2:len(str(space[space_count:space_count+1]))-2]+"']":
            space_count += 1
            if space_count > len(space):
                space_count = 0
            decryption += " "
        if str(text[aa:ab]) == str(['\n']):
            decryption += '\n'
        if ab > len(text):
            file_name = str(fileoutput)
            try:
                new_file = open(file_name+".decrypt", "x")
            except:
                os.remove(file_name+".decrypt")
            new_file = open(file_name+".decrypt", "a")#check list save
            new_file.write(decryption)
            new_file.close()
            return("Decryption: \n"+decryption)
