def harmonic_mean(measurements: list[float]) -> float:
    return len(measurements) / sum(1 / m for m in measurements)
