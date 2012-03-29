import requests
from BeautifulSoup import BeautifulSoup
import re

def startloop(url, count):
    #Dictionary for User agents
    kwargs = {}
    kwargs['headers'] = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}

    for i in range(count):
        
        print "Doing Page " + str(i+1)
        
        #Calling the request library to fetch the url using the User Agent and give us the HTML Content and store it in data library
        data = requests.get(url, **kwargs).content
        soup = BeautifulSoup(data, convertEntities=BeautifulSoup.HTML_ENTITIES)

        result = soup.find('table', {'class' : 'images_table'})

        anchors = result.findAll('a')
        for anch in anchors:
            link = re.findall('imgurl=(.*\.png)', str(anch))
            img_url = link.pop()
            filename = img_url.split('/')[-1]
            print "Fetching File : " + filename
            f = open(filename, 'w')
            f.write(requests.get(img_url).content)
            f.close()
            print "Done Fetching File : " + filename
        
        BASE_URL = 'http://www.google.com'
        footer = soup.find('div', {'id' : 'foot'})
        next = footer.findAll('td', {'class' : 'b'})[-1]
        url = BASE_URL + next.find('a')['href']

        
            
        count -= 1
        
if __name__ == '__main__':
    
    #Url we'll be fecthing
    url = 'http://www.google.co.in/search?tbm=isch&hl=en&source=hp&biw=1333&bih=663&q=ext%3Apng&gbv=2&oq=ext%3Apng&aq=f&aqi=&aql=&gs_l=img.3...1401l3910l0l4123l7l7l0l2l0l0l125l591l0j5l5l0.frgbld.#q=ext:png&hl=en&safe=off&gbv=2&tbm=isch&source=lnt&tbs=isz:m&sa=X&ei=SWp0T66tIoWsrAeV5rzZDQ&ved=0CA0QpwUoAg&bav=on.2,or.r_gc.r_pw.r_qf.,cf.osb&fp=6ba8ab9a37eb1e99&biw=1333&bih=663'

    startloop(url, 10)
    print "Finished."
