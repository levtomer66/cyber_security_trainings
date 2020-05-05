fhs = open("wl.txt", 'r')
fho = open("wordlist.txt", 'r')
orig = [ w.strip() for w in fho.readlines() ]
scram = [ w.strip() for w in fhs.readlines() ]

def filter_len(length, wl):
    return [ w for w in wl if len(w) == length ]

def is_word_found(ow, sw):
    for i in sw:
        found = False
        for j in ow:
            if i == j:
                found = True
                break
        if not found:
            return False
    return ow

founded = []
for sw in scram:
    print ("Checking for %s" % sw)
    len_filtered = filter_len(len(sw), orig)
    for ow in len_filtered:
        if is_word_found(ow, sw) and is_word_found(sw, ow):
            founded.append(ow)
            print ("Match orig: %s == %s (scram)" % (ow, sw))
            break

print ",".join(founded)



# ",".join([w.strip()[::-1] for w in  fh.readlines()])