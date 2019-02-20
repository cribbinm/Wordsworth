class InputError(Exception):
    pass


class WordRepeatError(Exception):
    pass


## '<word> +1'
## '<word> -1'

def validate_input(input):
    """
    :param input:
    :return: bool

    - Checks if input matches valid input strings
    - Check if word has been previously submitted

    Raises:
    - InputError
    - WordRepeatError
    """
    identifiers = ['+1', '-1', 'Submission:', 'Who is left to vote?', 'Status:']

    for identifier in identifiers:
        if identifier in input:
            return True

    raise InputError('Invalid input')


def create_error_response(param):
    pass


def input_is_a_submission(input):
    pass


def submit_word_for_voting(input):
    pass


def input_is_a_vote(input):
    pass


def vote_on_word(input):
    pass


def status_request(input):
    pass


def create_status_message(input):
    pass


def remaining_voter_message(input):
    pass


def remaining_voter_request(input):
    pass


def handle_string(input):
    try:
        validate_input(input)
    except Exception as e:
        return create_error_response(e)
    if input_is_a_submission(input):
        submit_word_for_voting(input)
    elif input_is_a_vote(input):
        vote_on_word(input)
    elif status_request(input):
        return create_status_message(input)
    elif remaining_voter_request(input):
        return remaining_voter_message(input)
    return
