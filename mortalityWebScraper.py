import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


pdf_url = 'http://www.healthdata.org/sites/default/files/files/county_profiles/US/2015/County_Report_Crowley_County_Colorado.pdf'

import urllib
import html
from bs4 import BeautifulSoup as BS

req = urllib.request.Request(pdf_url, headers={'User-Agent' : "Magic Browser"}) 
con = urllib.request.urlopen(req)
print(con.read())

html=con.read()
soup = BS(html)
print(soup.get_text())

