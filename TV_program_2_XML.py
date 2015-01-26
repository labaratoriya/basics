#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
import urllib2
import codecs
import string
from datetime import datetime, date, time, timedelta
import time
import re
import cgi

import StringIO
import gzip


import libxml2
from BeautifulSoup import BeautifulSoup, SoupStrainer


# CONFIGURATION OPTIONS
fetch_prefix = "http://www.gonix.net/xmltv"

channels = [
 ['HRT 1','hrt1','http://raspored.hrt.hr/format/xmltv.xml?mreza=2&ignore=%d%d%d']
,['HRT 2','hrt2','http://raspored.hrt.hr/format/xmltv.xml?mreza=3&ignore=%d%d%d']
,['HRT 3', 'hrt3', 'http://raspored.hrt.hr/format/xmltv.xml?mreza=4&ignore=%d%d%d']
,['HRT 4', 'hrt4', 'http://raspored.hrt.hr/format/xmltv.xml?mreza=40&ignore=%d%d%d']

, ['NOVA','nova','file:./temp/nova_%d-%02d-%02d.xml']
, ['RTL','rtl','file:./temp/rtl_%d-%02d-%02d.xml']
, ['RTL2','rtl2','file:./temp/rtl2_%d-%02d-%02d.xml']
, ['Doma', 'doma','file:./temp/doma_%d-%02d-%02d.xml' ]
#,['NOVA','nova','http://mojtv.hr/xmltv/service.ashx?kanal_id=9&date={day}.{month}.{year}']
 
#,['RTL','rtl','http://www.gonix.net/xmltv/rtltv.tv.gonix.net_%d-%02d-%02d.xml']
#,['RTL2', 'rtl2', 'http://www.gonix.net/xmltv/rtl2.tv.gonix.net_%d-%02d-%02d.xml']
#,['Doma', 'doma', 'http://www.gonix.net/xmltv/novadomatv.tv.gonix.net_%d-%02d-%02d.xml'] 
]


EXCLUDE = [
 'PP'
,'Vrijeme'
,'TV kalendar'
,'Vijesti'
,'Tv prodaja'
,'TV prodaja'
,'TV vrtić:'
,'Kraj programa'
,'Astro show'
,'TEST'
,'ZABA - 90 sekundi, emisija pod pokroviteljstvom'
,'Najava programa'
,'Večeras...'
,'EP reportaža'
,'Ep reportaža'
,'e-Hrvatska'
,'Sport'
,'Vijesti iz kulture'
,'Hrvatska uživo'
,'Najava'
,'Juhuhu'
,'Juhuhu (R)'
]

EXCLUDE_STARTSWITH = [
 'Croatia Osiguranje'
,'Vrijeme'
,'TV izlog'
,'TV Izlog'
,'Generalna špica'
,"Infokanal + HRA"
,"Bez komentara"
,"HAK"
,"Kraj programa"
]

EXACT_REPLACEMENTS = [
 (u', serija za djecu', '')
 , (u', humoristična serija','')
 , (u', telenovela','')
 , (u', telenovela (kod. na sat.)','')
 , (u', serija', '')
 , (u', crtana serija','')
 , (u'(kod. na sat.)','')
 , (u', dokumentarna serija','')
 , (u', dokumentarna sapunica',', serija')
 , (u', akcijski film', ', akcija')
 , (u', akcijska serija', '')
 , (u' igrani film', '')
 , (u'igrani film', '')
 , (u', akcijska komedija', ', komedija')
 , (u', romantična komedija', ', komedija')
 , (u', informativna emisija', ', emisija')
 , (u', Informativna emisija', ', emisija')
 , (u', kriminalistički triler', ', krim. triler')
 , (u', kriminalistički', ', krim.')
 , (u', akcijski triler', ', akcijski')
 , (u', dramska serija', '')
 , (u', obrazovna emisija', ', emisija')
 , (u', dokumentarni reality', ', dok. reality')
 , (u', povijesna dramska serija', '')
 , (u', humorna drama', ', komedija')
 , (u', informativni magazin', ', info magazin')
 , (u', animirana serija', ', crtani')
 , (u', humorna dramska serija', '')
 , (u', kriminalistička serija', '')
 , (u', kriminalistička drama', 'krim. drama')
 , (u', dramska kriminalistička serija', '')
 , (u', zabavna/obrazovna emisija', ', emisija')
 , (u', obiteljski', '')
 , (u', avanturistička komedija', '')
 , (u'Prijenos sjednice Hrvatskog sabora', 'Prijenos, HR Sabor')
 , (u'Županijska panorama', u'Žup. panorama')
 , (u", emisija pod pokroviteljstvom ", u", emisija")
 , (u"Filmski maraton ", u"")
 , 
]

def to_regex(string):
    regex = []	
    for char in string:
        if char.isalpha():
            regex.append("[")
            regex.append(char.swapcase())
            regex.append(char)
            regex.append("]")
            regex.append("+")
        elif char.isspace():
            regex.append("\s*")
        else:
            regex.append(char)
    return "".join(regex)

_REPLACEMENTS = [(re.compile(r'Nogomet.*SP.*', re.I|re.U), '')
                , (re.compile(r'\(?S\d+E\d+(/\d+)?\)?', re.I|re.U), '')
                , (re.compile(r',\s*\w+\s*[fF]+[iI]+[lL]+[mM]+', re.I|re.U), '')
                , (re.compile(r',\s*\w+\s*-\s*\w+\s*[fF]+[iI]+[lL]+[mM]+', re.I|re.U), '')
                , (re.compile(r',\s*\w+\s*-\s*\w+\s*[sS]+[eE]+[rR]+[iI]+[jJ]+[aA]+', re.I|re.U), '')                
                , (re.compile(r',\s*\w+\s*-\s*\w+\s*-\s*\w+\s*[fF]+[iI]+[lL]+[mM]+', re.I|re.U), '')                
                , (re.compile(r'\(?\d+(-\d+)?/\d+\)?', re.I|re.U), '')
                , (re.compile(r"\(?\s*([oO]+[kK]+[oO]+\s*)?\d+'(\d+\"?)?\)?", re.I|re.U), '')
                , (re.compile(r"\s*-*\s*[cC]+[iI]+[kK]+[lL]+[uU]+[sS]+.*:", re.I|re.U), ":")
                , (re.compile(r"^[cC]+[iI]+[kK]+[lL]+[uU]+[sS]+.*:", re.I|re.U), "")
                , (re.compile('^'+to_regex("Filmski maraton")+"\s*:\s*"), u"")                
]

		
REPLACEMENTS = []
for exact_pat, rep in EXACT_REPLACEMENTS:
    # permute large/small letters at start
    # any number of spaces
    # repeated letters           
    reg = re.compile(to_regex(exact_pat), re.I|re.U)
    REPLACEMENTS.append((reg, rep))
    reg = None

REPLACEMENTS.extend(_REPLACEMENTS)
print REPLACEMENTS

#,'poluvrijeme'

EXCLUDE_RE = re.compile(r'(tarot\sshow|nova\slova)')

print '!!!!!!!!!!     XMLTV TO INDESIGN PROGRAM GENERATOR     !!!!!!!!!!!!!!!!!\n'
# listing is per day
delta = timedelta(days=1)

start_date_input = raw_input('Start date (yyyy-mm-dd): ')
(year,month,day) = start_date_input.split("-")
start_date = date(int(year), int(month), int(day))

DEFAULT_FILENAME = 'tv-data.xml'
FILENAME = raw_input('Output file name (tv-data.xml): ')

if not FILENAME:
    FILENAME = DEFAULT_FILENAME

datafile = codecs.open(FILENAME, encoding='utf-8', mode='w')
datafile.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<?whitespace-handling use-tags?>\n")#<?whitespace-handling use-tags?>
#datafile.write('<Root xmlns:aid="http://ns.adobe.com/AdobeInDesign/4.0/">')
datafile.write('<Root xmlns:aid="http://ns.adobe.com/AdobeInDesign/3.0/">\n')


daynames = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday', 'Sunday']

for dayi in xrange(0,7):
    day_number = start_date.weekday()
    
    print "\nAssembling day %d (%s)..." % (day_number, daynames[day_number])
    
    
    for channel in channels:
        channel_url = channel[2]
        channel_id = channel[1]
        channel_label = channel[0]
        
        time.sleep(.015)
        
        try:
            final_url = channel_url % (start_date.year, start_date.month, start_date.day)
        except TypeError:
            final_url = channel_url.format(year=start_date.year, month=start_date.month, day=start_date.day)
        
        try:
            print "Fetching %s " % final_url,
            socket = urllib2.urlopen(final_url)
            data = socket.read()
            #print "(%dk)" % (len(data)/1000)
            encoding = socket.headers.get('content-encoding')
            if encoding == 'gzip':
                fdata = StringIO.StringIO(data)
                gzipper = gzip.GzipFile(fileobj = fdata)
                data = gzipper.read()

            #charset = socket.headers.get('content-type').split('; charset=')[-1]
            #data = unicode(data, encoding= charset)

            tv = libxml2.parseDoc(data)

            programs = tv.xpathEval('//tv/programme')
        except libxml2.parserError:
            print '!!!!!!! ERROR !!!!!!!   Failed to parse file %s' % final_url
            #raw_input('Press any key to exit...')
            #sys.exit(-1)

            datafile.write('<tv-listing day="%s" channel="%s">\n' % (day_number, channel_id) )
            datafile.write('</tv-listing>\n')

            continue
            
        except urllib2.URLError, e:
            print '!!!!!!! ERROR !!!!!!!   Failed to fetch file %s' % final_url
            #print str(e)
            #print final_url

            datafile.write('<tv-listing day="%s" channel="%s">\n' % (day_number, channel_id) )
            datafile.write('</tv-listing>\n')

            #raw_input('Press any key to exit...')
            #sys.exit(-1)
            continue
        
        datafile.write('<tv-listing day="%s" channel="%s">\n' % (day_number, channel_id) )
        
        #datafile.write("<tv-header>%s</tv-header>\r" % channel_label)
        #datafile.write("<aid:br></aid:br>")
        #datafile.write('<tv-table xmlns:aid="http://ns.adobe.com/AdobeInDesign/4.0/" aid:table="table" aid:trows="%s" aid:tcols="2">' % len(programs))
        prevtitle = ''
        first = True
        for x in xrange(0, len(programs)):
            EXCLUDED = False
            program = programs[x]
            
            starttimenode = program.xpathEval('@start')[0].content
            titlenode = program.xpathEval('title')[0].content
            #print titlenode
            #check for exclusions: title match, start match, regular exp match
            if titlenode in EXCLUDE:
                EXCLUDED = True
            
            for excludestart in EXCLUDE_STARTSWITH:
                if titlenode.startswith(excludestart):
                    EXCLUDED = True
                    
            if EXCLUDE_RE.search(titlenode, re.I|re.U):
                EXCLUDED = True
            
            if EXCLUDED:
                continue

            # parse out the time and title

            starttimenode = starttimenode.replace(" +", "")
            try:
                starttime = datetime.strptime(starttimenode[0:-5], "%Y%m%d%H%M%S")
            except ValueError:
                #print starttimenode
                try:
                    starttime = datetime.strptime(starttimenode, "%Y%m%d%H%M%S")
                except ValueError:
                    starttime = datetime.strptime(starttimenode[0:-7], "%Y%m%d%H%M%S")
                #raise 
            
            if starttime.date() >= start_date + delta or starttime.date() < start_date:
                continue
                
            startime_text = "%02d:%02d" % (starttime.hour, starttime.minute)
            title_text = titlenode.decode('utf-8')
 
            #clean up
            title_text = title_text.replace('&', '&amp;')
            
            # check for replacements
            for reg, rep in REPLACEMENTS:
                if reg.search(title_text):
                        title_text = reg.sub(rep, title_text)
	        
            # find the category
            category = ''
            catnode = program.xpathEval('category')
            creditsnode = program.xpathEval('credits')
            if catnode:
                category = catnode[-1].content
                
            if not category and creditsnode:
                category = 'movie'
                
            # ones with category are a little longer, cut them more
            #if category and len(title_text) > 35:
            #    title_text = title_text[0:35]+'...'
            #elif len(title_text) > 40:
            #    title_text = title_text[0:40]+'...'
           
            # if the title is the same continue
            if title_text == prevtitle:
                continue
                
            # only print breaks if this is not the first entry
            if not first:
                datafile.write('<aid:br/>')
                
            #datafile.write(u'<tv-listing-time aid:table="cell" aid:crows="1" aid:ccols="1" aid:ccolwidth="19.812335958005235">%s</tv-listing-time>' % startime_text)
            #datafile.write(u'<tv-listing-title aid:table="cell" aid:crows="1" aid:ccols="1" aid:ccolwidth="120.85695538057746">%s</tv-listing-title>' % title_text)

            if any([(value in category.lower()) for value in ['movie', 'film', 'igrane']]):
                datafile.write("<tv-entry-film>%s&#x2005;<category-marker-film>Film</category-marker-film>&#x2002;%s</tv-entry-film>\n" % (startime_text, title_text))
            elif any([(value in category.lower()) for value in ['series', 'serija', 'serije']]):
                datafile.write("<tv-entry-series>%s&#x2005;<category-marker-series>Serija</category-marker-series>&#x2002;%s</tv-entry-series>\n" % (startime_text, title_text))
            else:
                datafile.write("<tv-entry>%s&#x2005;%s</tv-entry>\n" % (startime_text, cgi.escape(title_text)))
                
            first = False
            prevtitle = title_text

        #datafile.write('</tv-table>')
        datafile.write('</tv-listing>\n')

    start_date+= delta

datafile.write("</Root>")
datafile.close()
raw_input('\nPress any key to exit...')



