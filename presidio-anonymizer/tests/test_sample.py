import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    # replace the following line with your test
    assert sample_run_anonymizer("My name is Bond.", 11,15) == sample_run_anonymizer("My name is Bond.", 11, 15)