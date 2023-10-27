import ast
import os

from archive_strategy.archiver import Archiver

BASE_DIR = os.environ.get("ARCHIVE_BASE_DIR", "/backups")
ARCHIVE_DIR = os.environ.get("ARCHIVE_DIR", "/archive")
ARCHIVE_USER = os.environ.get("ARCHIVE_USER", "root")
ARCHIVE_GROUP = os.environ.get("ARCHIVE_GROUP", "root")
ARCHIVE_TEST_MODE = ast.literal_eval(os.environ.get("ARCHIVE_TEST_MODE", "False"))
ARCHIVE_DELETE = ast.literal_eval(os.environ.get("ARCHIVE_DELETE", "False"))
ARCHIVE_DEBUG = ast.literal_eval(os.environ.get("ARCHIVE_DEBUG", "True"))


def main():
    archiver = Archiver(
        archive_dir=ARCHIVE_DIR,
        base_dir=BASE_DIR,
        archive_user=ARCHIVE_USER,
        archive_group=ARCHIVE_GROUP,
        test_mode=ARCHIVE_TEST_MODE,
        delete=ARCHIVE_DELETE,
        debug=ARCHIVE_DEBUG,
    )
    archiver.show_info()
    archiver.archive()
    archiver.organise()
