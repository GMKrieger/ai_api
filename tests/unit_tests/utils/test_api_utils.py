import pytest
from utils import api_utils
from flask import Request
from unittest import mock
from werkzeug.datastructures import FileStorage
import numpy as np

class RequestMock(Request):

    def __init__(self, data):
        self.data = data

    @property
    def json(self):
        return self.data


def test_check_json_should_return_attribute():
    request = RequestMock({"test": "test"})
    data = dict()
    res = api_utils.check_json(request, data, 'test')
    assert res == "test"
    assert "test" in data


def test_check_json_should_return_empty_list():
    request = RequestMock({"test": "test"})
    data = dict()
    res = api_utils.check_json(request,data,'new_test')
    assert isinstance(res, list)
    assert "new_test" in data
    assert isinstance(data["new_test"], list)
    assert len(res) == 0


def test_check_op_should_return_op():
    acceptable_op = ["=", ">=", "<=", "CONTAINS", "!!=", ">", "<", "<>", "IS NULL", "IS NOT NULL"]

    for op in acceptable_op:
        res = api_utils.check_op(op)
        assert res == op


def test_check_op_should_raise_key_error():
    op = "rr"
    with pytest.raises(KeyError):
        res = api_utils.check_op(op)


def test_parse_type_should_parse_float():
    f = api_utils.parse_type("22.4")
    assert f == "'22.4'"


def test_parse_type_should_parse_int():
    i = api_utils.parse_type("333")
    assert i == "'333'"


def test_paser_type_should_parse_string():
    s = api_utils.parse_type("asdfg")
    assert "'ASDFG'" == s


def test_file_treatment_no_results():
    mock_file = mock.create_autospec(FileStorage)
    mock_file.filename = "test.csv"

    data = np.ones((4, 4))

    with mock.patch('utils.api_utils.np.genfromtxt', autospec=True) as mock_np:
        mock_np.return_value = data

        result, _, _ = api_utils.file_treatment(mock_file)

    assert data.all() == result.all()


def test_file_treatment_with_results():
    mock_file = mock.create_autospec(FileStorage)
    mock_file.filename = "test.csv"

    data = np.ones((4, 4))

    with mock.patch('utils.api_utils.np.genfromtxt', autospec=True) as mock_np:
        mock_np.return_value = data

        dataset, results, classes = api_utils.file_treatment(mock_file, mock_file)

    assert data.all() == dataset.all()
    assert data.all() == results.all()
    assert classes == 1
