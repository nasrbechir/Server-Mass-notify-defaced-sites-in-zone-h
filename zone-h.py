import time
import re , urllib2 , sys , os, urllib
 
 
print(logo)
def unique(seq):
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]
 
def get_all(s):
    lista = []
    page = 1
    while page <= 101:
        try:
            bing = "http://www.bing.com/search?q=ip%3A" + s + "+&count=50&first=" + str(page)
            openbing = urllib2.urlopen(bing)
            readbing = openbing.read()
            findwebs = re.findall('<h2><a href="(.*?)"', readbing)
            for i in range(len(findwebs)):
                allnoclean = findwebs[i]
                findall1 = re.findall('http://(.*?)/', allnoclean)
                for idx, item in enumerate(findall1):
                    if 'www' not in item:
                        findall1[idx] = 'http://www.' + item + '/'
                    else:
                        findall1[idx] = 'http://' + item + '/'
                lista.extend(findall1)
 
            page += 50
        except urllib2.URLError:
            pass
 
    final = unique(lista)
    return final
def zoneNotify(url):
    try:
        if("http://" not in url):
            url = "http://"+str(url)
       
        notifier = "http://zone-h.com/notify/single"
        post_data = {
            "defacer" : ok,
            "domain1" : url,
            "hackmode" : "1",
            "reason" : "1"
        }
        post_data = urllib.urlencode(post_data)
        opener = urllib2.Request(notifier, post_data)
        data = urllib2.urlopen(opener).read()
    except:
        pass
 
 
 
bechir = raw_input('Enter IP >>> ')
sites = get_all(str(bechir))
ok = raw_input('Name of your zone h :')
for site in sites :
  zoneNotify(site)
 
 
                               
print '/Done'                  
 
 
with open("zone.txt", "a") as f:
                                f.write('http://www.zone-h.org/archive/ip='+bechir+"\n")                           
                                f.close()
