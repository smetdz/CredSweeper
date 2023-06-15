import pytest

from credsweeper.file_handler.analysis_target import AnalysisTarget
from credsweeper.filters import LineSpecificKeyCheck
from tests.filters.conftest import LINE_VALUE_PATTERN, DUMMY_ANALYSIS_TARGET
from tests.test_utils.dummy_line_data import get_line_data


class TestLineSpecificKeyCheck:

    @pytest.mark.parametrize("line", [
        '"AwsAccessKey": "AKIAGIREOGIAWSKEY123,',
    ])
    def test_line_specific_key_check_p(self, file_path: pytest.fixture, line: str) -> None:
        cred_candidate = get_line_data(file_path, line=line, pattern=LINE_VALUE_PATTERN)
        assert LineSpecificKeyCheck().run(cred_candidate, DUMMY_ANALYSIS_TARGET) is False

    @pytest.mark.parametrize("line", [
        '"AwsAccessKey": enc("AKIAGIREOGIAWSKEY123"),',
        '"AwsAccessKey": "AKIAGIREXAMPLEKEY123"',
    ])
    def test_line_specific_key_check_n(self, file_path: pytest.fixture, line: str) -> None:
        cred_candidate = get_line_data(file_path, line=line, pattern=LINE_VALUE_PATTERN)
        assert LineSpecificKeyCheck().run(cred_candidate, DUMMY_ANALYSIS_TARGET) is True
