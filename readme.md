# PDF Merger

A python script to merge multi PDF files into one.

## Install required package

This script use `os`, `datetime` and `pypdf`. To install `pypdf`, use the below command:

```bash
pip3 install pypdf
```

## How to use

1. Put all your PDFs in the folder named `sources`.

2. Run `merger.py` in the main directory.

```bash
python3 merger.py
```

If you want to use custom meta data, enter `Y` on this step:
```bash
Use custom meta data? (Y/N)
```
Please note that only `Y` is "yes", everythings else will be "no".

3. Have fun!
