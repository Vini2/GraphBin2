import pathlib
import pytest

from click.testing import CliRunner

from graphbin2.cli import main


__author__ = "Vijini Mallawaarachchi"
__credits__ = ["Vijini Mallawaarachchi"]


DATADIR = pathlib.Path(__file__).parent / "data"

@pytest.fixture(scope="session")
def tmp_dir(tmpdir_factory):
    return tmpdir_factory.mktemp("tmp")


@pytest.fixture(autouse=True)
def workingdir(tmp_dir, monkeypatch):
    """set the working directory for all tests"""
    monkeypatch.chdir(tmp_dir)


@pytest.fixture(scope="session")
def runner():
    """exportrc works correctly."""
    return CliRunner()


def test_graphbin2_spades_run(runner, tmp_dir):
    outpath = tmp_dir
    graph = DATADIR / "Sim-5G+metaSPAdes" / "assembly_graph_with_scaffolds.gfa"
    contigs = DATADIR / "Sim-5G+metaSPAdes" / "contigs.fasta"
    paths = DATADIR / "Sim-5G+metaSPAdes" / "contigs.paths"
    binned = DATADIR / "Sim-5G+metaSPAdes" / "initial_contig_bins.csv"
    abundance = DATADIR / "Sim-5G+metaSPAdes" / "abundance.abund"
    args = f"--assembler spades --graph {graph} --contigs {contigs} --paths {paths} --binned {binned} --abundance {abundance} --output {outpath}".split()
    r = runner.invoke(main, args, catch_exceptions=False)
    assert r.exit_code == 0, r.output

def test_graphbin2_flye_run(runner, tmp_dir):
    outpath = tmp_dir
    graph = DATADIR / "1Y3B_Flye" / "assembly_graph.gfa"
    contigs = DATADIR / "1Y3B_Flye" / "assembly.fasta"
    paths = DATADIR / "1Y3B_Flye" / "assembly_info.txt"
    binned = DATADIR / "1Y3B_Flye" / "initial_binning_res.csv"
    abundance = DATADIR / "1Y3B_Flye" / "abundance.tsv"
    args = f"--assembler flye --graph {graph} --contigs {contigs} --paths {paths} --binned {binned} --abundance {abundance} --output {outpath}".split()
    r = runner.invoke(main, args, catch_exceptions=False)
    assert r.exit_code == 0, r.output

# def test_graphbin2_megahit_run(runner, tmp_dir):
#     outpath = tmp_dir
#     graph = DATADIR / "ESC_MEGAHIT" / "final.gfa"
#     contigs = DATADIR / "ESC_MEGAHIT" / "final.contigs.gfa"
#     binned = DATADIR / "ESC_MEGAHIT" / "initial_binning_res.csv"
#     abundance = DATADIR / "ESC_MEGAHIT" / "abundance.tsv"
#     args = f"--assembler megahit --graph {graph} --contigs {contigs} --binned {binned} --abundance {abundance} --output {outpath}".split()
#     r = runner.invoke(main, args, catch_exceptions=False)
#     assert r.exit_code == 0, r.output