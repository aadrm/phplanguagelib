import csv

# variable sect is used to check for changes of section in the csv file to print a commented header in the php file
sect = ''


# this variables are used for refering to the language headers of the csv file, they have to be the same.
lang1 = 'en'
lang2 = 'gr'
lang3 = 'ru'
lang4 = 'cn'
spacenum = 32 # for a better visual representation.


with open('lib.csv', 'r') as rf:
    reader = csv.DictReader(rf)
    next(reader)
    with open('lang.php', 'w') as wf: 
        
        # php opening tag
        wf.write('<?php\n\n')

        for line in reader:
            if sect != line['section']:
                sect = line['section']
                wf.write('\n\n\n//====================== ' + sect + ' ===========================\n')
        
            wf.write('\n$' + line['varname'] + ' = array('+ (spacenum - 10 - len(line['varname']))*' '+ '"' + line[lang1] + '",\n' )
            wf.write(spacenum*' ' + '"' + line[lang2] + '",\n')
            wf.write(spacenum*' ' + '"' + line[lang3] + '",\n')
            wf.write(spacenum*' ' + '"' + line[lang4] + '");\n')

        # php closing tag
        wf.write('\n?>')
            
