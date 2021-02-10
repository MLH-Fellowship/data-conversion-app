from bs4 import BeautifulSoup

with open("NSIN_Test_Scenario_Export.xml", "rt", encoding="utf-8") as ex:
    data = ex.read()
soup = BeautifulSoup(data, 'lxml')

# Shows first generator element and its children
print(soup.generator)
