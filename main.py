import xml.etree.ElementTree as ET

# Create the root element
root = ET.Element("rss")

# Create a child element
item = ET.SubElement(root, "item")
title = ET.SubElement(item, "title")
title.text = "title"

# Create the XML tree
tree = ET.ElementTree(root)

# Write to the file
tree.write("feed.xml")
