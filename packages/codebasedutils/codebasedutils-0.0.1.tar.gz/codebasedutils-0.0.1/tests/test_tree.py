import pytest
from click.testing import CliRunner
from CodebasedUtils.core.main import util

@pytest.fixture
def runner():
    return CliRunner()

def test_dirprint(runner):
    result = runner.invoke(util, ['tree', '.'])
    assert result.exit_code == 0, f"Unexpected output:\n{result.output}"  # Combined the print and assert for simplicity

def test_dirprint_exclude(runner):
    result = runner.invoke(util, ['tree', '.', '--exclude', '.py'])
    assert result.exit_code == 0
    assert 'CodebasedUtils.py' not in result.output
