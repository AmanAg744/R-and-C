import xml.etree.ElementTree as ET
data = '''<person>
<name>Chuck</name>
<phone type="intl">
+1 734 303 4456
</phone>
<email hide="yes"/>
</person>'''
tree = ET.fromstring(data)     # takes the xml and gives back a tree
print(tree.find('name').text)
print(tree.find('email').get('hide'))

