#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
import re
import codecs
from datetime import datetime, date, time, timedelta
import urllib2
import chardet

#re_date_heading = re.compile(u"(?:SUBOTA|NEDJELJA|PONEDJELJAK|UTORAK|SRIJEDA|[CČ]ETVRTAK|PETAK)\s+(\d\d?)\s*\.\s*(\d\d?)\s*\.\s*(\d\d\d\d)\s*\.?", re.I|re.U)
re_date_heading = re.compile(u"(?:SUBOTA|NEDJELJA|PONEDJELJAK|UTORAK|SRIJEDA|[CČ]ETVRTAK|PETAK|[Ss]ubota|[Nn]edjelja|[Pp]onedljeljak|[Uu]torak|[Ss]rijeda|[CČcč]etvrtak|[Pp]etak)?[,]?\s?(\d\d?)\s*\.\s*(\d\d?)\s*\.\s*(\d\d\d\d)\s*\.?\s*(?:SUBOTA|NEDJELJA|PONEDJELJAK|UTORAK|SRIJEDA|[CČ]ETVRTAK|PETAK|[Ss]ubota|[Nn]edjelja|[Pp]onedljeljak|[Uu]torak|[Ss]rijeda|[CČcč]etvrtak|[Pp]etak)?", re.I|re.U)
re_entry = re.compile(r"(\d\d?)[\:\.](\d\d?)\s+(.+)$")
re_category = re.compile(r"(film|serija)", re.I)

def process_data(data):
    inlisting = False
    listings = []
    current_day = 5
    current_file = None
    current_date = None
    current_date_string = "%s.%s.%s"
    x = 0
    data = re.split("[\n\r]+", data)
    
    for line in data:
        
        # check if there is a heading line
        heading_matched = re.match(re_date_heading, line)
        if heading_matched:
            day, month, year = int(heading_matched.group(1)), int(heading_matched.group(2)), int(heading_matched.group(3))
            print "Heading found: %d-%02d-%02d: " % (year, month, day)
            #current_date = datetime(int(year),int(month),int(date))
            fname = 'temp/%s_%02d-%02d-%02d.xml' % (FILENAME, int(year), int(month), int(day))
            datafile = codecs.open(fname, encoding='utf8', mode='w')
            datafile.write('<tv generator-info-name="nonametv">')
            inlisting = True
            heading_matched = False
            continue
        else:
            pass
    
        
        if re.match(r'^\s*$', line):
            continue
        
        # if we are inlisiting, that means we have seen a header
        if inlisting is True:
            
            # check if we have time and title
            entry_matched = re.match(re_entry, line)
            if entry_matched:
                #listings.append(entry_matched.group(1), entry_matched.group(2))
                title = unicode(entry_matched.group(3))
                hour = int(entry_matched.group(1))
                minute = int(entry_matched.group(2))
                
                datafile.write('<programme start="%04d%02d%02d%02d%02d00 +0100" stop="" channel="nova">' % (year,month,day,hour,minute))
                category = None
                
                matched_category = re.search(re_category, title)
                if matched_category:
                    catmap = {'film':'movie', 'serija':'series'}
                    
                    if matched_category.group(1) in catmap:
                        category = catmap[matched_category.group(1)]
                
                
                title = title.replace(', igrani film', '').replace(', crtana serija', '').replace(', serija', '').replace('&', '&amp;')
                datafile.write('\t<title lang="hr">%s</title>\n' % title)
                if category:
                    datafile.write('\t<category lang="en">%s</category>\n' % category)
                datafile.write('</programme>')
                datafile.write("\n")
                
                x+=1
                #print entry_matched.group(1), entry_matched.group(2)#, entry_matched.group(3)
            # if we are missing a time and title, close the file
            else:
                print 'Found %d listings.' % x
                print "wrote %s\n" % fname
                x = 0
                inlisting = False
                datafile.write('</tv>')
                datafile.close()



# character set detection. we dont know what kind of shit we will get
FILENAMES = ['rtl', 'rtl2', 'nova', 'doma']

print '!!!!!!!!!!!!!!!     XMLTV PROGRAM GENERATOR     !!!!!!!!!!!!!!!!!!!!\n'

for FILENAME in FILENAMES:
    try:
        name = '.'.join([FILENAME, 'txt'])
        f = open(name)
    except Exception:
        print 'not found: {}'.format(name)
        continue

    charset = chardet.detect(f.read())
    print 'Character set detected: %s (%s).' % (charset['encoding'], charset['confidence']*100)
    f.close()

    print 'Processing %s...\n' % f

# open the file with the detected charset
    datafile = codecs.open(name, encoding=charset['encoding'])
    data = datafile.read()
    datafile.close()


    process_data(data)

            
raw_input('Press any key to exit')
