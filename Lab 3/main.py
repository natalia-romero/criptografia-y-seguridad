with open('rockyou.txt', encoding='iso-8859-1') as f, open('rockyou_mod.dic', 'w') as o:
    for line in f:
        l = line.strip()
        if not l or l[0].isdigit(): 
            continue
        l = l.replace(l[0], l[0].upper(), 1) + '0\n'
        o.write(l)
        