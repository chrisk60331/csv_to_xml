"""Parse csv and write them as xml."""
import logging
from xml.etree.ElementTree import Element, tostring

from src.identity import IdentitySequence

logging.basicConfig(level=logging.DEBUG)
FILE_ENCODING = 'UTF-8'
CSV_DELIMITER = ','


def parse_csv(csv_file):
    """Parse csv and write them as xml."""
    root = Element("root")

    index = IdentitySequence()
    headers = None
    with open(csv_file, 'r') as csv:
        for row in csv:
            row = [attrib.strip() for attrib in row.split(CSV_DELIMITER) if attrib]
            if index.count == 0 and not headers:
                headers = row
            else:
                logging.debug("parsed headers" + str(headers))
                attribs = dict(zip(headers, row))
                logging.debug("parsed row" + str(attribs))
                root.append(Element(str(index.next()), attrib=attribs))

    return tostring(root, encoding="unicode")
