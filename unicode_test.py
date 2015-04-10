# -*- coding: utf-8 -*-
import requests
urlc = [u'фывыюыва.апр', u'http://www.Alliancefrançaise.nu']

for url in urlc:
	requests.get(url)

#ru_url = u'красота.рф'
#print ru_url.encode('idna')

#print u'@'.encode('idna')
#print ru_url
#requests.get(ru_url)http://xn--80aa2arihi.xn--p1ai/
"""        if url != url.encode('idna'):
            if url.lower().startswith('http://'):
                url = url[7:]
            url = 'http://' + url.encode('idna')"""