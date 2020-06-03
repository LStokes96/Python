import pytest
from Code import cigar_party

def test_party():
    assert cigar_party.cigar_party(20,False) == False