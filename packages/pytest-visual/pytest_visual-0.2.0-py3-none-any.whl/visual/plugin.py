from pathlib import Path
from typing import List

import pytest
from _pytest.config.argparsing import Parser
from _pytest.fixtures import FixtureRequest
from plotly.graph_objs import Figure

from visual.io import (
    Statement,
    clear_statements,
    get_storage_path,
    read_statements,
    write_statements,
)
from visual.prompter import Prompter, visual_prompter
from visual.utils import get_visualization_flags


def pytest_addoption(parser: Parser):
    parser.addoption("--visual", action="store_true", help="Run visualization tests, prompt for acceptance")
    parser.addoption("--visual-yes-all", action="store_true", help="Visualization tests are accepted without prompting")
    parser.addoption("--visual-reset-all", action="store_true", help="Don't visualize, but mark all visualization cases as unaccepted")  # fmt: skip


@pytest.fixture
def visualize(request: FixtureRequest, visual_prompter: Prompter):
    run_visualization, yes_all, reset_all = get_visualization_flags(request)
    visualizer = Visualize()
    storage_path = get_storage_path(request)

    if run_visualization:
        # Run test
        yield visualizer

        # Handle visualization
        statements = visualizer.statements
        if yes_all:
            _teardown_with_yes_all(storage_path, statements)
        else:
            _teardown_with_verification(visual_prompter, storage_path, statements)
    elif reset_all:
        _teardown_with_reset_all(storage_path)
    else:
        pytest.skip("Visualization is not enabled, add --visual option to enable")


def _teardown_with_yes_all(path: Path, statements: List[Statement]) -> None:
    write_statements(path, statements)


def _teardown_with_verification(prompter: Prompter, path: Path, statements: List[Statement]) -> None:
    prev_statements = read_statements(path)

    if statements != prev_statements:
        if prompter.prompt_user(prev_statements, statements):
            write_statements(path, statements)
        else:
            pytest.fail("Visualizations were not accepted")


def _teardown_with_reset_all(path: Path) -> None:
    clear_statements(path)
    pytest.skip("Resetting visualization case as per --visualize-reset-all")


class Visualize:
    def __init__(self):
        self.statements: List[Statement] = []

    def print(self, text) -> None:
        self.statements.append(["print", text])

    def show(self, fig: Figure) -> None:
        self.statements.append(["plot", str(fig.to_json())])
