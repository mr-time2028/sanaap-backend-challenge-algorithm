def has_four_consecutive_ones_circular(binary: str) -> bool:
    if len(binary) != 7:
        raise ValueError("Input must contain exactly 7 bits.")

    if any(bit not in "01" for bit in binary):
        raise ValueError("Input must contain only 0 and 1.")

    circular_binary = binary + binary[:3]

    return "1111" in circular_binary
