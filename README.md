# blorgh
Python static site generator (Markdown -> HTML) from a Git repo

Blorgh
======

Blorgh requires Markdown to blawg.

## Installation
```
$ git clone git@github.com:varl/blorgh.git /path/to/blorgh
$ chmod +x /path/to/blorgh.py
$ ln -s /path/to/blorgh.py ~/bin/blorgh
```

## Usage
```
$ blorgh -h
usage: blorgh.py [-h] [-o OUTPUT_DIR] [-u URL] [-d DIRECTORY]

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        output directory where the static files will be put
  -u URL, --url URL     The Git repo URL to checkout and build
  -d DIRECTORY, --directory DIRECTORY
                        The source directory to build from

```
## Tests

e.g.

```
$ python3 lib/*_test.py
```

## Caveats

No `git`? `(╯._.)╯︵ ┻━┻`

## License

Not yet.

/v.
