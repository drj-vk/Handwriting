__author__ = 'diederik'

import compareSegments

#SC columns generated by jasper
sc_columns = [32, 53, 61, 87, 101, 120, 137, 170, 185, 196, 209, 220, 239]

#WordSXML
wordsXML = [[4, 57, 'm'], [57, 81, 'e'], [81, 102, 'm'], [102, 140, 'o'], [140, 169, 'r'], [169, 196, 'i'], [196, 208, 'a']]

comparator = compareSegments.Comparator()
print comparator.compare(sc_columns,wordsXML)
