# csv_to_xml

Read csv files and save them to local disk as xml

# usage
```python
import csv_to_xml
data = csv_to_xml.parse_csv('my_file.csv')
with open('result_file.xml) as xml_file:
  xml_file.write(data)```
