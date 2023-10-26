import sys

import pytest
from termcolor import colored

from imppkg.harmony import main


@pytest.mark.parametrize(
    "inputs, expected", [(["1", "4", "4"], 2.0), (["hello", "world"], 0.0)]
)
def test_harmony(inputs, expected, monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["harmony"] + inputs)

    main()

    assert capsys.readouterr().out.strip() == colored(
        expected, "red", "on_cyan", attrs=["bold"]
    )
