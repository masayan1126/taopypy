import numpy as np
from formatter.error_formatter import ErrorFormatter


def main() -> None:
    try:
        raise Exception("Exception!!")
    except Exception as e:
        obj = ErrorFormatter().format(e)
        print(f"message={obj['message']}")
        print(f"stack_trace={obj['stack_trace']}")
