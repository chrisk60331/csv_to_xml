import logging

from src.csv_to_xml import parse_csv

CSV_FILE = 'BrandsJobs.csv'
XML_FILE = 'BrandsJobs.xml'


def test_parse_csv():
    # given.
    with open(XML_FILE, 'r') as xml_file:
        expected = xml_file.read()
        logging.debug("parsed row" + str(expected))

    # when.
    actual = parse_csv(CSV_FILE)

    # then.
    assert actual == expected
