import pytest
from . import HelferWichtel

class TestWichtel():
    Helfer = HelferWichtel()

    def test_getPuzzleInput_Error(self):
        with pytest.raises(Exception) as e_info:
            self.Helfer.getPuzzleInput('')

    def test_getPuzzleInput_Correct(self):
        self.Helfer.getPuzzleInput('02')

