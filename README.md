(work in progress)

# Rygor

NOTE: This is an experimental program. You've been warned.

This prototype has two modes, one straightfoward and one experimental

## Submitting clean paper names to The Retraction Watch Database

This mode takes a list of paper names from a txt file and submits them to the RWDB. It produces a fle `rygor.log` that shows the results of the query and if the paper was flagged as potential match for a retraction

```
python3 Rygor.py --input ExampleData/exampleCleanCitations.txt
```

## Submitting a medArxiv URL
This mode uses Beautiful Soup to get the citations from a medArxiv page (provided citations are present) and submits those as the query to RWDB. This involves parsing unstructured text, make sure to note the query string if you use this.
```
python3 Rygor.py --medRxiv https://www.medrxiv.org/content/10.1101/2021.01.02.20248998v1.full
```