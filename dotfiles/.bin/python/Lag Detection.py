#!/usr/bin/env python3

"""Detect when system is slowing down."""

import sys
import time


def detect_lags(threshold: float) -> None:
    """Print when time.sleep elapsed exceeds threshold."""
    while True:
        prev = time.time()
        time.sleep(1)
        now = time.time()
        if (now - prev) > threshold:
            print(f"{lag[round(((now - prev) * 2) - 1)]} Lag")


lag = ["Small", "Medium", "Large", "Mega", "Super", "MAG"]


def main() -> None:
    """Command Line Entry Point."""
    scan = float(sys.argv[1]) if len(sys.argv) > 1 else 1.00112
    print("Starting Clock")
    try:
        detect_lags(scan)
    except KeyboardInterrupt:
        pass
    finally:
        sys.exit(0)


if __name__ == "__main__":
    main()
else:
    print(__name__)
