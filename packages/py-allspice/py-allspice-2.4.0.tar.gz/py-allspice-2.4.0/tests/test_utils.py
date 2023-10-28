import csv
import dataclasses
import uuid

import pytest

from allspice import AllSpice
from allspice.utils.bom_generation import AttributesMapping, generate_bom_for_altium
from allspice.utils.netlist_generation import generate_netlist

test_repo = "repo_" + uuid.uuid4().hex[:8]


@pytest.fixture(scope="session")
def port(pytestconfig):
    '''Load --port command-line arg if set'''
    return pytestconfig.getoption("port")


@pytest.fixture
def instance(port):
    try:
        g = AllSpice(
            f"http://localhost:{port}",
            open(".token", "r").read().strip(),
            ratelimiting=None,
        )
        print("AllSpice Hub Version: " + g.get_version())
        print("API-Token belongs to user: " + g.get_user().username)

        return g
    except Exception:
        assert (
            False
        ), f"AllSpice Hub could not load. Is there: \
                - an Instance running at http://localhost:{port} \
                - a Token at .token \
                    ?"


def _setup_for_generation(instance, test_name):
    # TODO: we should commit a smaller set of files in this repo so we don't depend on external data
    instance.requests_post(
        "/repos/migrate",
        data={
            "clone_addr": "https://hub.allspice.io/ProductDevelopmentFirm/ArchimajorDemo.git",
            "mirror": False,
            "repo_name": "-".join([test_repo, test_name]),
            "service": "git",
        },
    )


def test_bom_generation(request, instance):
    _setup_for_generation(instance, request.node.name)
    repo = instance.get_repository(instance.get_user().username,
                                   "-".join([test_repo, request.node.name]))
    attributes_mapping = AttributesMapping(
        description=["PART DESCRIPTION"],
        designator=["Designator"],
        manufacturer=["Manufacturer", "MANUFACTURER"],
        part_number=["PART", "MANUFACTURER #"],
    )
    bom = generate_bom_for_altium(
        instance,
        repo,
        "Archimajor.PrjPcb",
        "Archimajor.PcbDoc",
        attributes_mapping,
        # We hard-code a ref so that this test is reproducible.
        ref="95719adde8107958bf40467ee092c45b6ddaba00",
    )
    assert len(bom) == 107

    bom_as_dicts = []
    # We have to do this manually because of how csv.DictWriter works.
    for item in bom:
        entry_as_dict = {}
        for (key, value) in dataclasses.asdict(item).items():
            entry_as_dict[key] = str(value) if value is not None else ""
        bom_as_dicts.append(entry_as_dict)

    with open("tests/data/archimajor_bom_expected.csv", "r") as f:
        reader = csv.DictReader(f)
        for row, expected_row in zip(reader, bom_as_dicts):
            assert row == expected_row


def test_netlist_generation(request, instance):
    _setup_for_generation(instance, request.node.name)
    repo = instance.get_repository(instance.get_user().username,
                                   "-".join([test_repo, request.node.name]))
    netlist = generate_netlist(
        instance,
        repo,
        "Archimajor.PcbDoc",
        # We hard-code a ref so that this test is reproducible.
        ref="95719adde8107958bf40467ee092c45b6ddaba00",
    )
    assert len(netlist) == 682

    nets = list(netlist.keys())

    nets.sort()

    with open("tests/data/archimajor_netlist_expected.net", "r") as f:
        for net in nets:
            assert (net + "\n") == f.readline()
            pins_on_net = netlist[net]
            pins_on_net.sort()
            assert (" " + " ".join(pins_on_net) + "\n") == f.readline()
