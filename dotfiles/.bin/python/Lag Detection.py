#!/usr/bin/env python3
import sys, time

def detect_lags(threshold: float) -> None:
    while True:
        prev = time.time()
        time.sleep(1)
        now = time.time()
        if (now - prev) > threshold:
            print('%s Lag' % lag[round(((now - prev) * 2) - 1)])

lag = ['Small', 'Medium', 'Large', 'Mega', 'Super', 'MAG']

def main() -> None:
    if len(sys.argv) > 1:
        scan = float(sys.argv[1])
    else:
        scan = 1.00112
    print('Starting Clock')
    try:
        detect_lags(scan)
    except KeyboardInterrupt:
        pass
    finally:
        sys.exit(0)

if __name__ == '__main__':
    main()
else:
    print(__name__)
