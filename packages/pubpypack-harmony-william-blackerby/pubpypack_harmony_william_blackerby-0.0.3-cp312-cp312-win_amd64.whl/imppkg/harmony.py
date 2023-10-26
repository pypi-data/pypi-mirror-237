import sys
from imppkg.harmonic_mean import harmonic_mean
from termcolor import colored


def _parse_nums(inputs: list[str]) -> list[float]:
    try:
        measurements = [float(m) for m in inputs]
    except ValueError:
        measurements = []

    return measurements


def _calculate_results(nums: list[float]) -> float:
    result = 0.0

    try:
        result = harmonic_mean(nums)
    except ZeroDivisionError:
        pass

    return result


def _format_output(result: float) -> str:
    return colored(str(result), "red", "on_cyan", attrs=["bold"])


def main():
    measurements = _parse_nums(sys.argv[1:])
    result = _calculate_results(measurements)

    print(_format_output(result))
