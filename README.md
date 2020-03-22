# Buckler

![buckler.py](buckler.png?raw=true "buckler.py")

CLI tool allowing an easy interface with the Crossref Commons package for natbib citation generation.

```
usage: buckler.py [-h] [-p PATH] [-c] source

positional arguments:
  source                search for the reference info of the DOI or website
                        you input here

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  write reference to the given file
  -c, --confirm         do not ask for user confirmation to write to bib file
```

## TODO

1. Sort reference database with each addition.
2. Allow citation generation for websites.
3. Convert between natbib and biblatex citation format.
