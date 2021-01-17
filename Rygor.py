from RygorTools import RygorTools

import logging as log

import time
import argparse



# get commandl ine arguments
parser = argparse.ArgumentParser(description='Rygor')

parser.add_argument(
  "-i", "--input",
  help = "a .txt file in the format shown in /ExampleData/exampleCleanCitations",
  default = None
)

parser.add_argument(
  "-im", "--medRxiv",
  help = "EXTREMELY experimental feature to search for retractions in the citations of a medRxiv by webscraping them and using them as input",
  default = None
)

args = parser.parse_args()



# configure logger
log.basicConfig(
  filename ='rygor.log',
  filemode ='w',
  level=log.INFO,
  format ='%(name)s - %(levelname)s - %(message)s'
)



if args.input is not None:
    clean = False
    citations = [l for l in open(str(args.input), "r")]

if args.medRxiv is not None:
    clean = True
    citations = RygorTools.getCitationsFromMedrxivURL(args.medRxiv)

for i, cit in enumerate(citations):
    if i % 5 == 0:
        time.sleep(5)
    result = RygorTools.queryRWDB(cit, clean = clean)
    soup = result.soup
    tables = soup.find_all("tbody")
    dataTable = RygorTools.getResultsTable(soup)
    # TODO find a way to tidy the up
    if dataTable is not None:
        log.info(
            "Possible retraction for: " + result.paperInput + "\n" +
            "\n".join([str(i) for i in RygorTools.getResultsTableData(dataTable)])
        )
    else:
        log.info(
            "No RWDB results found for: \n\t" + result.paperInput +
            "\n\tunder query: " + result.queryString + "\n"
        )