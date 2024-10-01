import pytest
from project.utils.loader import load


def test_load(caplog):
    caplog.set_level(10)
    load(verbose=2)
    # Check if the default data path is in the log message
    assert "/home/dati/public-datasets-vizgen-merfish/datasets/mouse_brain_map/BrainReceptorShowcase/Slice1/Replicate1" in caplog.text