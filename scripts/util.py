import scraperwiki,lxml.etree
import re

def etree_from_file(fn):
  with open(fn) as f:
    return lxml.etree.fromstring(scraperwiki.pdftoxml(f.read()))

def spliton(exp,it):
  i=(j for j in it)
  e=re.compile(exp)
  a=i.next()
  r=[]
  rr=[]
  for j in i:
    if e.match(j):
      rr.append(r)
      r=[]
    r.append(j)
  rr.append(r)  
  return rr

def join_text(x,y):
    text=re.compile("[a-zA-Z]+")
    if len(x) and text.search(x[-1]) and text.search(y):
        x[-1]+=y
    else:
        x.append(y)
    return x

