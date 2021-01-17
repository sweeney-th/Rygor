(work in progress)

# Rygor
## Submitting clean paper names to The Retraction Watch Database
Rygor takes a list of paper names from a txt file and submits them to the RWDB. It produces a fle `rygor.log` that shows the results of the query and if the paper was flagged as potential match for a retraction. See `ExampleData/exampleCleanCitations.txt` for formatting.
### Installation
Dependencies are manged using [pipenv](https://pipenv.pypa.io/en/latest/basics/). 
```
pipenv install
```
### Usage
```
python3 Rygor.py --input ExampleData/exampleCleanCitations.txt &
```

Monitor `rygor.log` for progress.