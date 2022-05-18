"""Parse csv and write them as xml."""
import logging
from xml.etree.ElementTree import Element, tostring

logging.basicConfig(level=logging.DEBUG)
FILE_ENCODING = "UTF-8"


def parse_csv(csv_file):
    """Parse csv and write them as xml."""
    root = Element("root")

    index = 0
    with open(csv_file, 'r') as csv:
        for row in csv:
            row = [attrib.strip() for attrib in row.split(',') if attrib]
            if index == 0:
                headers = row
            else:
                attribs = dict(zip(headers, row))
                logging.debug("parsed headers" + str(headers))
                logging.debug("parsed row" + str(attribs))
                root.append(Element(str(index), attrib=attribs))
            index += 1

    return tostring(root, encoding="unicode")
