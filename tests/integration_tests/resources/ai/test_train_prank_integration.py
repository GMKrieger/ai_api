import requests

def test_should_return_ok_with_correct_files():
    files = {"dataset": open("files/sized_test_dataset.csv", "rb"),
             "results": open("files/sized_test_results.csv", "rb")}

    response = requests.post('http://127.0.0.1:5000/api/train/prank/', files=files)
    assert response.status_code == 200


def test_should_return_error_without_results():
    files = {"dataset": open("files/sized_test_dataset.csv", "rb")}

    response = requests.post('http://127.0.0.1:5000/api/train/prank/', files=files)
    assert response.status_code == 406
