import xml.etree.ElementTree as ET

def modifier_valeurs_xml(fichier_xml):
    tree = ET.parse(fichier_xml)
    root = tree.getroot()
    for zone in root.findall(".//zone"):
        zone.set("smin", "0") # Do not change
        zone.set("smax", "0") # Do not change 
        zone.set("dmin", "10") # <--- Min Zombies
        zone.set("dmax", "15") # <--- Max Zombies
    tree.write(fichier_xml)

fichier_xml = "PATH_TO_zombie_territories.xml" # Windows use "\" and Linux "/' So, be aware.  
modifier_valeurs_xml(fichier_xml)
