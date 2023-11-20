import xml.etree.ElementTree as ET

tree = ET.parse("country_data.xml")
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)

print("-------------------")

for neighbor in root.iter("neighbor"):
    print(neighbor.attrib)

print("-------------------")

for neighbor in root.findall("neighbor"):
    print(neighbor.attrib)

print("-------------------")

for country in root.findall("country"):
    rank = country.find("rank").text
    name = country.get("name")
    print(name, rank)
