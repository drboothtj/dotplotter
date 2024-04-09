# dotplotter
build dotplots from blastn results

## Description
`dotplotter` can take blast results, either as standard input or from a .tsv file and plots a standard dot plot. It can also highlight regions based on provided arguments (single region) or from a file (single or multiple regions) see below. Dot plots are a classic way to visualise DNA similarity and can be used for whole chromosomes or small regions.

## Installation
The easiest way to install dotplotter is though the python package index.

`pip install dotplotter`

This will fetch and install the latest version from: LINK

You can also install by cloning this repository.

`dotplotter` only requires `matplotlib` and this should be installed automatically.

## Usage
### Basic Usage
You can use `dotplotter` in two ways: using stdin, or reading a .tsv file.

Example data can be found in this repository `./example_data`.

**Important:** Regardless of method, make sure your results are in blast outfmt 6. This is specified in the search with `-outfmt 6`

#### stdin method
You can pipe your `blastn` results straight into `dotplotter`:

`blastn -query streptomyces_coelicolor.fna -subject streptomyces_albus.fna -outfmt 6 | dotplotter`

#### .tsv method
You can also read your results in from a previously generated .tsv file (e.g. `blastn -query streptomyces_coelicolor.fna -subject streptomyces_albus.fna -outfmt 6 > blastn.tsv`)

`dotplotter -i blastn.tsv`

### Highlighting
You can also highlight regions of interest.

**Important:** Highlighted regions are based on the query sequence ONLY.

#### Single Region Highlighting
The easiest way to highlight a single region is to use the in-built parameters: `-hs`/`highlight-start` and `-he`/`--highlight-end`. For example:

´´

#### Multiple Region Highlighting
To highlight multiple regions, you can provide a .csv file containing the required information. Each line should contain the start position, end position and the hex value (or colour name).
See `.example_data/highlight.csv` for an example. You can specify this file with `-hf`/`--highligh-file`.

`dotplotter -i blastn.tsv -hf highlight.csv`

### Further Usage
For more usage information, use the help command:

`dotplotter -h`

## Citation
Coming soon...

## Patch Notes
### Verion 1
- 1.0.0
  - initial release
