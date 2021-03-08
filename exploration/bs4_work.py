from bs4 import BeautifulSoup
from xml.etree import ElementTree as et

with open("..\\data\\ceesim\\NSIN_Test_Scenario_Export.xml", "rt") as ex:
    data = ex.read()
soup = BeautifulSoup(data, 'lxml')

emitters = soup.findAll("emittermode")
nsin_1 = emitters[0]

for child in nsin_1.emittermodeheader.children:
    if child == "\n" or child == "":
        continue
    print(child, "\ni\n")
    if child.name == "lastupdatedate":
        break

