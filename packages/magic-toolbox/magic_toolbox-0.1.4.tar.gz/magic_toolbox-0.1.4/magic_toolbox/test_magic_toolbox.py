from magic_cmd.run_cmd import run_cmd
from pathlib import Path
def test_create_project():
    run_cmd('python magic_toolbox.py create_project foo')
    foo = Path('foo')
    assert foo.exists()
    assert foo.is_dir()
    run_cmd('rm -rf foo')
