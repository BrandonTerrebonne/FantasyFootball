
# coding: utf-8

# In[1]:

import time
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from urlparse import urljoin
import urllib2

# plotting preferences
get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('bmh')
plt.rcParams['figure.figsize'] = (15.0, 6.0)
plt.rcParams['axes.formatter.useoffset'] = False

# turn warnings off
import warnings
warnings.filterwarnings('ignore')

# format notebook output
from IPython.display import HTML, Javascript, display
# display(Javascript("IPython.OutputArea.prototype._should_scroll=function(){return false;};"))
pd.set_option('display.max_columns', 1000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)


# In[2]:

#Define URL for scraping
url = r'http://www.nfl.com/stats/categorystats?tabSeq=1&season=2015&seasonType=REG&d-447263-p=1&statisticPositionCategory=QUARTERBACK'

page = urllib2.urlopen(url).read()
soup = bs(page)

#Define empty list for each stat
rk = []
player = []
team = []
pos = []
comp = []
att = []
pct = []
att_per_g = []
yds = []
avg = []
yds_per_g = []
td = []
intercept = []
first_down = []
first_down_percent = []
lng = []
twenty_plus = []
forty_plus = []
sck = []
rate = []

#Scrubbing stats containing hrefs
start = "\">"
end = "</a>"

def scrubbing_html(x):
    try:
        x = x.astype(str)
    except:
        x = x
    new_column = []
    for record in x:
        y = str(record)
        t = y[y.rfind(start)+2:y.find(end)]
        t = str(t)
        new_column.append(t)
    return new_column

#string.strip() - not sure I acutally need this
def string_strip(c):
    try:
        c = c.string.strip()
    except AttributeError:
        c = c
    return c

#Where the mother f****in magic happens
def meta_shit(category, col_num):
    for row in soup.find_all('tr')[1:]:
        col = row.find_all('td')
        y = col[col_num]
        x = string_strip(y)
        category.append(x)
        
meta_shit(rk,0)
meta_shit(player,1)
meta_shit(team,2)
meta_shit(pos,3)
meta_shit(comp,4)
meta_shit(att,5)
meta_shit(pct,6)
meta_shit(att_per_g,7)
meta_shit(yds,8)
meta_shit(avg,9)
meta_shit(yds_per_g,10)
meta_shit(td,11)
meta_shit(intercept,12)
meta_shit(first_down,13)
meta_shit(first_down_percent,14)
meta_shit(lng,15)
meta_shit(twenty_plus,16)
meta_shit(forty_plus,17)
meta_shit(sck,18)
meta_shit(rate,19)

columns = {'rk':rk,'player':player,'team':team,'pos':pos,'comp':comp,'att':att,'pct':pct,'att_per_g': att_per_g,'yds':yds,'avg':avg,'yds_per_g':yds_per_g,'td':td,
             'intercept':intercept,'first_down':first_down,'first_down_percent':first_down_percent,'lng':lng,'twenty_plus':twenty_plus,'forty_plus':forty_plus,'sck':sck,'rate':rate}
           
df = pd.DataFrame(columns)
df['player'] = scrubbing_html(df['player'])
df['team'] = scrubbing_html(df['team'])
print df.shape
df.head()


# In[181]:

### Testing from here down
#Define empty list for each stat
rk = []
player = []
team = []
pos = []
comp = []
att = []
pct = []
att_per_g = []
yds = []
avg = []
yds_per_g = []
td = []
intercept = []
first_down = []
first_down_percent = []
lng = []
twenty_plus = []
forty_plus = []
sck = []
rate = []

#Scrubbing stats containing hrefs
start = "\">"
end = "</a>"

def scrubbing_html(x):
    try:
        x = x.astype(str)
    except:
        x = x
    new_column = []
    for record in x:
        y = str(record)
        t = y[y.rfind(start)+2:y.find(end)]
        t = str(t)
        new_column.append(t)
    return new_column

#string.strip() - not sure I acutally need this
def string_strip(c):
    try:
        c = c.string.strip()
    except AttributeError:
        c = c
    return c

#Where the mother f****in magic happens
def meta_shit(category, col_num):
    for row in soup.find_all('tr')[1:]:
        col = row.find_all('td')
        y = col[col_num]
        x = string_strip(y)
        category.append(x)


# In[ ]:

base_url = 'http://www.nfl.com/'
next_page = 'http://www.nfl.com/stats/categorystats?archive=false&conference=null&statisticPositionCategory=QUARTERBACK&season=2015&seasonType=REG&experience=&tabSeq=1&qualified=false&Submit=Go'

next_page 

while True:
    soup = bs(requests.get(next_page).content)
    
    for row in soup.find_all('tr')[1:]:
        col = row.find_all('td')
        y = col[col_num]
    
    try:
        next_page = urljoin(base_url, soup.select('span.linkNavigation a')[1].get('href'))
    except IndexError:
        break  # exiting the loop if "Next" link not found
        
columns_2 = {'rk':rk,'player':player,'team':team,'pos':pos,'comp':comp,'att':att,'pct':pct,'att_per_g': att_per_g,'yds':yds,'avg':avg,'yds_per_g':yds_per_g,'td':td,
             'intercept':intercept,'first_down':first_down,'first_down_percent':first_down_percent,'lng':lng,'twenty_plus':twenty_plus,'forty_plus':forty_plus,'sck':sck,'rate':rate}
           
df2 = pd.DataFrame(columns_2)
df2['player'] = scrubbing_html(df['player'])
df2['team'] = scrubbing_html(df['team'])
print df2.shape
df2.head()


# In[51]:

url = r'http://www.nfl.com/stats/categorystats?tabSeq=1&season=' + str(season) + r'&seasonType=REG&experience=&Submit=Go&archive=false&conference=null&d-447263-p=' + str(pg) + r'&statisticPositionCategory=' + position + r'&qualified=true'

if "nflasdf" in url:
    print "yes"
else: 
    print "no"


# In[104]:

position = 'QUARTERBACK'
pg = 1
season = 2015

url = r'http://www.nfl.com/stats/categorystats?tabSeq=1&season=' + str(season) + r'&seasonType=REG&experience=&Submit=Go&archive=false&conference=null&d-447263-p=' + str(pg) + r'&statisticPositionCategory=' + position + r'&qualified=true'
page = urllib2.urlopen(url).read()
soup = bs(page)

start = "\">"
end = "</a>"
end_nolink = "</th>"

def scrubbing_html(x, y):
    try:
        x = str(x)
    except:
        x = x
    t = x[x.rfind(start)+2:x.find(y)]
    return t

#Gets column names
col_names = []
for row in soup.find_all('th')[0:]:
    row = str(row)
    if "href" in row:
        t = scrubbing_html(row, end)
        col_names.append(t)
    else:
        r = scrubbing_html(row, end_nolink)
        col_names.append(r)
    
col_names


# In[108]:

data = {k: [] for k in col_names}
data


# In[112]:

data.keys()[0]


# In[81]:

df3 = pd.DataFrame(data = None, columns = col_names)
df3


# In[113]:

## Test 2
# #Define URL for scraping


# url = r'http://www.nfl.com/stats/categorystats?tabSeq=1&season=' + str(season) + r'&seasonType=REG&experience=&Submit=Go&archive=false&conference=null&d-447263-p=' + str(pg) + r'&statisticPositionCategory=' + position + r'&qualified=true'


# page = urllib2.urlopen(url).read()
# soup = bs(page)

#Define empty list for each stat
rk = []
player = []
team = []
pos = []
comp = []
att = []
pct = []
att_per_g = []
yds = []
avg = []
yds_per_g = []
td = []
intercept = []
first_down = []
first_down_percent = []
lng = []
twenty_plus = []
forty_plus = []
sck = []
rate = []

#Scrubbing stats containing hrefs
start = "\">"
end = "</a>"

def scrubbing_html(x):
    try:
        x = x.astype(str)
    except:
        x = x
    new_column = []
    for record in x:
        y = str(record)
        t = y[y.rfind(start)+2:y.find(end)]
        t = str(t)
        new_column.append(t)
    return new_column

#string.strip() - not sure I acutally need this
def string_strip(c):
    try:
        c = c.string.strip()
    except AttributeError:
        c = c
    return c

# #Where the mother f****in magic happens
# def meta_shit(category, col_num):
#     for row in soup.find_all('tr')[1:]:
#         col = row.find_all('td')
#         y = col[col_num]
#         x = string_strip(y)
#         category.append(x)

#Where the mother f****in magic happens
def meta_shit(category, col_num):
    position = 'QUARTERBACK'
    pg = [1, 2, 3]
    season = 2015
    for pg_number in pg:
        url = r'http://www.nfl.com/stats/categorystats?tabSeq=1&season=' + str(season) + r'&seasonType=REG&experience=&Submit=Go&archive=false&conference=null&d-447263-p=' + str(pg_number) + r'&statisticPositionCategory=' + position + r'&qualified=true'
        page = urllib2.urlopen(url).read()
        soup = bs(page)
        for row in soup.find_all('tr')[1:]:
            col = row.find_all('td')
            y = col[col_num]
            x = string_strip(y)
            category.append(x)
        
meta_shit(rk,0)
meta_shit(player,1)
meta_shit(team,2)
meta_shit(pos,3)
meta_shit(comp,4)
meta_shit(att,5)
meta_shit(pct,6)
meta_shit(att_per_g,7)
meta_shit(yds,8)
meta_shit(avg,9)
meta_shit(yds_per_g,10)
meta_shit(td,11)
meta_shit(intercept,12)
meta_shit(first_down,13)
meta_shit(first_down_percent,14)
meta_shit(lng,15)
meta_shit(twenty_plus,16)
meta_shit(forty_plus,17)
meta_shit(sck,18)
meta_shit(rate,19)

columns = {'rk':rk,'player':player,'team':team,'pos':pos,'comp':comp,'att':att,'pct':pct,'att_per_g': att_per_g,'yds':yds,'avg':avg,'yds_per_g':yds_per_g,'td':td,
             'intercept':intercept,'first_down':first_down,'first_down_percent':first_down_percent,'lng':lng,'twenty_plus':twenty_plus,'forty_plus':forty_plus,'sck':sck,'rate':rate}
           
df = pd.DataFrame(columns)
df['player'] = scrubbing_html(df['player'])
df['team'] = scrubbing_html(df['team'])
print df.shape
df.head()


# In[85]:

df.to_csv(r'C:\Users\Brandon\Desktop\misc.csv')


# In[98]:

r = requests.get('http://www.nfl.com/stats/categorystats?tabSeq=1&season=2014&seasonType=REG&experience=&Submit=Go&archive=true&d-447263-p=3&conference=null&statisticPositionCategory=QUARTERBACK&qualified=true', allow_redirects=False)
r = str(r)


# In[99]:

if r == '<Response [302]>':
    print 'yes'
else:
    print 'no'


# In[8]:

#Data frame with our league point settings
point_settings = pd.read_csv(r'C:\Users\Brandon\Desktop\fantasy_football_point_settings.csv')
print point_settings.shape
point_settings.head()

