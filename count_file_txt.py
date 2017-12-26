

def count_csv_chars(filename):
    with open(filename, 'r') as f:
        fstring = f.read()

    letters = 0
    sp_usc  = 0
    numbers = 0
    commas  = 0
    nlines  = 0
    other   = 0
    all     = 0

    for i in list(fstring):
        print "%r" % i
        all += 1
        if   i.isdigit(): numbers += 1
        elif i == ',':    commas  += 1
        elif i == '\n':   nlines  += 1
        elif i.isalpha(): letters += 1
        elif i == '_' or ' ': sp_usc += 1
        else:             other   += 1
    
    print "all = %d\n\nNumbers  = %d\nLetters  = %d\nCommas   "\
        "= %d\nNewlines = %d\nOther    = %d\n" \
        "Sp _     = %d\n"\
        % (all,numbers,letters,commas,nlines,other, sp_usc)

if __name__ == '__main__':
    filename = "lst.csv"
    count_csv_chars(filename)
    
'''
lst.csv

Numbers  = 35
Letters  = 47
Commas   = 24
Newlines = 8
Other    = 114
'''