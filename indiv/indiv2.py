# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def print_idols_group(**group):
    """
    which idol belongs to which group
    """
    if group:
        for name, group in group.items():
            print(f"{name}: {group}")
    else:
        return None


if __name__ == "__main__":
    print_idols_group(
        Nayen="Twice", Momo="Twice", Karina="Aespa",
        Tzuyu="Twice", Winter="Aespa", Bibi="None",
        Ryujin="Itzy", DPR="None", Lia="Itzy", Lisa="Blackpink"
    )

