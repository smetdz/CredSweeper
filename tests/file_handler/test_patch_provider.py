from unittest.mock import Mock, patch
from tests import SAMPLES_DIR
        file_path = SAMPLES_DIR / "password.patch"
        patch_provider = PatchProvider([str(file_path)], "added")
    def test_load_patch_data_utf16_n(self) -> None:
        file_path = SAMPLES_DIR / "password_utf16.patch"
        patch_provider = PatchProvider([str(file_path)], "added")
        with patch('logging.Logger.info') as mocked_logger:
            raw_patches = patch_provider.load_patch_data()
            warning_message = f"UnicodeError: Can't read content from \"{file_path}\" as utf8."
            mocked_logger.assert_called_with(warning_message)
    def test_load_patch_data_western_n(self) -> None:
        file_path = SAMPLES_DIR / "password_western.patch"
        patch_provider = PatchProvider([str(file_path)], "added")
        with patch('logging.Logger.info') as mocked_logger:
            raw_patches = patch_provider.load_patch_data()
            warning_message = f"UnicodeError: Can't read content from \"{file_path}\" as utf16."
            mocked_logger.assert_called_with(warning_message)
        file_path = SAMPLES_DIR / "iso_ir_111.patch"
        patch_provider = PatchProvider([str(file_path)], "added")
        with patch('logging.Logger.info') as mocked_logger:
            raw_patches = patch_provider.load_patch_data()
            warning_message = f"UnicodeError: Can't read content from \"{file_path}\" as utf16."
            mocked_logger.assert_called_with(warning_message)