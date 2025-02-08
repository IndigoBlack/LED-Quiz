from unittest.mock import patch
from Project import questions, validate


@patch('builtins.input', return_value='A')
@patch('requests.get')
def test_questions(mock_get, mock_input):
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {
        'results': [
            {
            'question': 'mocked question',
            'correct_answer': 'mocked correct answer',
            'incorrect_answers': ['mocked incorrect answer 1', 'mocked incorrect answer 2']
            }
        ]
    }
    result = questions()
    assert result is not None
    assert isinstance(result, bool)


def test_validate_false():
    assert validate('a') == False
    assert validate('b') == False
    assert validate('c') == False
    assert validate('d') == False


def test_validate_true():
    assert validate('A') == True
    assert validate('B') == True
    assert validate('C') == True
    assert validate('D') == True
