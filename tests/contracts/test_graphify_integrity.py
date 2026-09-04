import json
from pathlib import Path


def test_graph_exists():
    graph = Path("graphify-out/graph.json")
    assert graph.exists(), "Graphify graph is missing"


def test_graph_has_relationships():
    graph = Path("graphify-out/graph.json")
    if not graph.exists():
        return

    data = json.loads(graph.read_text())

    nodes = data.get("nodes", [])
    edges = data.get("edges", [])

    assert nodes, "Graph contains no nodes"
    assert edges, "Graph contains no relationships"
