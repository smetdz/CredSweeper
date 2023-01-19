from unittest.mock import patch
from credsweeper.config import Config
    def test_load_patch_data_p(self, config: Config) -> None:
        raw_patches = patch_provider.load_patch_data(config)
    def test_load_patch_data_utf16_n(self, config: Config) -> None:
            raw_patches = patch_provider.load_patch_data(config)
    def test_load_patch_data_western_n(self, config: Config) -> None:
            raw_patches = patch_provider.load_patch_data(config)
    def test_load_patch_data_n(self, config: Config) -> None:
            raw_patches = patch_provider.load_patch_data(config)

    def test_oversize_n(self, config: Config) -> None:
        """Evaluate warning occurrence while load oversize diff file"""
        # use UTF-16 encoding to prevent any Windows style transformation
        file_path = SAMPLES_DIR / "password_utf16.patch"
        patch_provider = PatchProvider([str(file_path)], "added")

        config.size_limit = 0
        with patch('logging.Logger.warning') as mocked_logger:
            raw_patches = patch_provider.load_patch_data(config)
            warning_message = f"Size (512) of the file '{file_path}' is over limit (0)"
            mocked_logger.assert_called_with(warning_message)

        assert isinstance(raw_patches, list)
        assert len(raw_patches) == 0