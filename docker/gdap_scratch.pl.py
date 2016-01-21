from urllib.request import urlopen
csv = urlopen("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_week.csv")
print(csv.read())