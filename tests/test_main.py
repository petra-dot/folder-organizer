import os
import shutil
from organizer.main import organize_folder

def test_organizer(tmp_path):
    test_dir = tmp_path / "test"
    test_dir.mkdir()

    # Create dummy files
    (test_dir / "sample.jpg").write_text("fake image")
    (test_dir / "doc.pdf").write_text("fake pdf")

    organize_folder(test_dir)

    assert (test_dir / "Images" / "sample.jpg").exists()
    assert (test_dir / "Documents" / "doc.pdf").exists()
