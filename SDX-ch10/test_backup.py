from pathlib import Path
from unittest.mock import patch
import pytest

from backup import backup

# [setup]
FILES = {"a.txt": "aaa", "b.txt": "bbb", "sub_dir/c.txt": "ccc"}

@pytest.fixture
def our_fs(fs):
    for name, contents in FILES.items():
        fs.create_file(name, contents=contents)
# [/setup]

# [test]
def test_nested_example(our_fs):
    with patch("backup.current_counter", return_value=1002):
        manifest = backup(".", "/backup")
    for filename, hash_code in manifest:
        assert Path("/backup", f"{hash_code}.bck").exists()
        assert Path("/backup", "1002.csv").exists()
    print("hello")
# [/test]
