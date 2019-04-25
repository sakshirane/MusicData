import urllib
from bs4 import BeautifulSoup
import pandas as pd


#extracting the data
def make_soup(url):
	thepage = urllib.request.urlopen(url)
	soupdata = BeautifulSoup(thepage, "html.parser")
	return soupdata

soup = make_soup("http://www.discjockey.org/top-100-songs-of-the-2000s/")
musicdata_list = []
for record in soup.find_all('tr'):
	musicdata = []
	for data in record.find_all('td'):
		#print(data.text)
		musicdata.append(data.text)
	musicdata_list.append(musicdata)
	

#cleaning the data

#first two rows have out-of-place values
musicdata_list = musicdata_list[2:]

#placing appropriate headers
header = ["Rank", "Song", "Artist", "Year", "Genre"]
musicdata_df = pd.DataFrame(musicdata_list, columns = header)

#CSV file
musicdata_df.to_csv("music_df.csv", header = True, index = False)
