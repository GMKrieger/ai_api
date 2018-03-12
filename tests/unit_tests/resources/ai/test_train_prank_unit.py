from resources.ai import train_prank
import numpy as np
from unittest import mock


def test_creation_and_training_should_return_ok():
    data = np.ones((4,4))
    result = np.zeros(4)

    with mock.patch('resources.ai.train_prank.api_utils.file_treatment', autospec=True) as mock_treatment:
        mock_treatment.return_value = (data, result, 1)

        id = train_prank.creation_and_training(0, 0)

    assert id
