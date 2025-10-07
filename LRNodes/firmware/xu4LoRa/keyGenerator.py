#!/usr/bin/env python3
# Generate LoRaWAN AppKey(s) as 32-char uppercase hex strings

import argparse
import secrets

def generate_appkey() -> str:
    # 16 bytes = 128-bit AES key used by LoRaWAN
    return secrets.token_hex(16).upper()  # 32 hex chars

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate LoRaWAN AppKey(s).")
    parser.add_argument("-n", "--num", type=int, default=1, help="number of keys to generate")
    args = parser.parse_args()

    for _ in range(args.num):
        print(generate_appkey())

