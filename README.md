<p align="center">
  <img src="https://raw.githubusercontent.com/metagentools/GraphBin2/master/docs/images/GraphBin2_Logo_light.png#gh-light-mode-only" width="450" title="GraphBin2 Logo" alt="GraphBin2 Logo">
  <img src="https://raw.githubusercontent.com/metagentools/GraphBin2/master/docs/images/GraphBin2_Logo_dark.png#gh-dark-mode-only" width="450" title="GraphBin2 Logo" alt="GraphBin2 Logo">
</p>

# GraphBin2: Refined and Overlapped Binning of Metagenomic Contigs Using Assembly Graphs

[![DOI](https://img.shields.io/badge/DOI-10.4230/LIPIcs.WABI.2020.8-informational)](https://doi.org/10.4230/LIPIcs.WABI.2020.8)
[![DOI](https://img.shields.io/badge/DOI-10.1186/s13015--021--00185--6-yellow)](https://doi.org/10.1186/s13015-021-00185-6)
[![DOI](https://zenodo.org/badge/262936904.svg)](https://zenodo.org/badge/latestdoi/262936904)
![GitHub](https://img.shields.io/github/license/Vini2/GraphBin2)
[![PyPI version](https://badge.fury.io/py/graphbin2.svg)](https://badge.fury.io/py/graphbin2)
[![Downloads](https://static.pepy.tech/badge/graphbin2)](https://pepy.tech/project/graphbin2)
[![CI](https://github.com/metagentools/GraphBin2/actions/workflows/testing.yml/badge.svg)](https://github.com/metagentools/GraphBin2/actions/workflows/testing.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![CodeQL](https://github.com/metagentools/GraphBin2/actions/workflows/codeql.yml/badge.svg)](https://github.com/metagentools/GraphBin2/actions/workflows/codeql.yml)
[![Documentation Status](https://readthedocs.org/projects/graphbin2/badge/?version=latest)](https://graphbin2.readthedocs.io/en/latest/?badge=latest)


GraphBin2 is an extension of [GraphBin](https://github.com/Vini2/GraphBin) which refines the binning results obtained from existing tools and, more importantly, is able to assign contigs to multiple bins. GraphBin2 uses the connectivity and coverage information from assembly graphs to adjust existing binning results on contigs and to infer contigs shared by multiple species.

**Note:** Due to recent requests from the community, we have added support for long-read assemblies produced from Flye. Please note that GraphBin2 has not been tested extensively on long-read assemblies. We originally developed GraphBin2 for short-read assemblies. Long-read assemblies might have sparsely connected graphs which can make the label propagation process less effective and may not result in improvements.

**NEW:** GraphBin2 is now available on PyPI at [https://pypi.org/project/graphbin2/](https://pypi.org/project/graphbin2/).

## Getting Started

### Downloading GraphBin2
You can download the latest release of GraphBin2 from [Releases](https://github.com/Vini2/GraphBin2/releases) or clone the GraphBin2 repository to your machine.

```bash
git clone https://github.com/Vini2/GraphBin2.git
```

If you have downloaded a release, you will have to extract the files using the following command.

```bash
unzip [file_name].zip
```

Now go in to the GraphBin2 folder using the command

```bash
cd GraphBin2/
```

### Setting up the environment

We recommend that you use [Conda](https://docs.conda.io/en/latest/) to run GraphBin2. You can download [Anaconda](https://www.anaconda.com/distribution/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) which contains Conda.

Once you have installed Conda, make sure you are in the GraphBin2 folder. Now run the following commands to create a Conda environment and activate it to run GraphBin2.

```bash
conda env create -f environment.yml
conda activate graphbin2
```

Now install GraphBin2 using the following command.

```bash
flit install
```

### Test the setup

After installing, run the following command to ensure that GraphBin2 is working.

```bash
graphbin2 -h
```

Now you are ready to run GraphBin2.


## Citation

GraphBin2 was accepted for publication at the 20th International Workshop on Algorithms in Bioinformatics ([WABI 2020](http://algo2020.di.unipi.it/WABI2020/)) and is published in [Leibniz International Proceedings in Informatics (LIPIcs)](https://www.dagstuhl.de/dagpub/978-3-95977-161-0) DOI: [10.4230/LIPIcs.WABI.2020.8](https://doi.org/10.4230/LIPIcs.WABI.2020.8). 

An extended journal article of GraphBin2 has been published in BMC Algorithms for Molecular Biology at DOI: [10.1186/s13015-021-00185-6](https://doi.org/10.1186/s13015-021-00185-6).

If you use GraphBin2 in your work, please cite the following publications.

```bibtex
@InProceedings{mallawaarachchi_et_al:LIPIcs:2020:12797,
  author =	{Vijini G. Mallawaarachchi and Anuradha S. Wickramarachchi and Yu Lin},
  title =	{{GraphBin2: Refined and Overlapped Binning of Metagenomic Contigs Using Assembly Graphs}},
  booktitle =	{20th International Workshop on Algorithms in Bioinformatics (WABI 2020)},
  pages =	{8:1--8:21},
  series =	{Leibniz International Proceedings in Informatics (LIPIcs)},
  ISBN =	{978-3-95977-161-0},
  ISSN =	{1868-8969},
  year =	{2020},
  volume =	{172},
  editor =	{Carl Kingsford and Nadia Pisanti},
  publisher =	{Schloss Dagstuhl--Leibniz-Zentrum f{\"u}r Informatik},
  address =	{Dagstuhl, Germany},
  URL =		{https://drops.dagstuhl.de/opus/volltexte/2020/12797},
  URN =		{urn:nbn:de:0030-drops-127974},
  doi =		{10.4230/LIPIcs.WABI.2020.8},
  annote =	{Keywords: Metagenomics binning, contigs, assembly graphs, overlapped binning}
}

@Article{Mallawaarachchi2021,
  author={Mallawaarachchi, Vijini G. and Wickramarachchi, Anuradha S. and Lin, Yu},
  title={Improving metagenomic binning results with overlapped bins using assembly graphs},
  journal={Algorithms for Molecular Biology},
  year={2021},
  month={May},
  day={04},
  volume={16},
  number={1},
  pages={3},
  abstract={Metagenomic sequencing allows us to study the structure, diversity and ecology in microbial communities without the necessity of obtaining pure cultures. In many metagenomics studies, the reads obtained from metagenomics sequencing are first assembled into longer contigs and these contigs are then binned into clusters of contigs where contigs in a cluster are expected to come from the same species. As different species may share common sequences in their genomes, one assembled contig may belong to multiple species. However, existing tools for binning contigs only support non-overlapped binning, i.e., each contig is assigned to at most one bin (species).},
  issn={1748-7188},
  doi={10.1186/s13015-021-00185-6},
  url={https://doi.org/10.1186/s13015-021-00185-6}
}
```

## Funding

GraphBin2 is funded by an [Essential Open Source Software for Science Grant](https://chanzuckerberg.com/eoss/proposals/cogent3-python-apis-for-iq-tree-and-graphbin-via-a-plug-in-architecture/) from the Chan Zuckerberg Initiative.

<p align="left">
  <img src="https://chanzuckerberg.com/wp-content/themes/czi/img/logo.svg" width="300">
</p>
