
def sort_data(sequence: list | set | str | dict) -> tuple:
    sequence = set(sequence)
    sorted_sequence = sorted(sequence)
    return tuple(sorted_sequence)