def test_sequence(client_sequence: list, right_sequence: list) -> list:
    intermediate_results = list()

    for index in range(len(right_sequence)):
        if client_sequence[index] == right_sequence[index]:
            intermediate_results.append(True)
        else:
            intermediate_results.append(False)
    return intermediate_results


def is_right_result(intermediate_results: list) -> bool:
    is_right = True
    for element in intermediate_results:
        is_right ^= element
    return is_right
