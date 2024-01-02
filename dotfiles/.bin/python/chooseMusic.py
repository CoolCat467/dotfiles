#!/usr/bin/env python3
# Program that helps you choose music

# Programmed by CoolCat467.

"""Reads 'music.txt', lets you select songs, and saves selected back to file."""

from __future__ import annotations

import os

__title__ = "Choose Music"
__author__ = "CoolCat467"
__version__ = "0.1.0"


def load_file(filename: str) -> list[str]:
    """Return list of filename file loaded split lines."""
    try:
        with open(str(filename), encoding="utf-8") as loadfile:
            data = loadfile.read().splitlines()
            loadfile.close()
    except OSError:
        data = []
        save_file(filename, data)
    return data


def save_file(filename: str, data: list[str]) -> None:
    """Save data (list) to file with filename filename, adds newline chars."""
    with open(str(filename), mode="w", encoding="utf-8") as savefile:
        savefile.write("\n".join(map(str, data)))
        savefile.close()


def escape_terminal_characters(
    use_list: list[str],
    reverse: bool = False,
) -> list[str]:
    """Iterate through a list and replace dangerous characters with themselves with backslashes before them in all strings."""
    replace_characters = """ &()"'[]$"""
    result = []
    for title in use_list:
        for char in replace_characters:
            if reverse:
                title = title.replace("\\" + char, char)
            else:
                title = title.replace(char, "\\" + char)
        result.append(title)
    return result


def main() -> None:
    """Read music listing file, ask user if song should be played for each, save selected purge non-selected."""
    list_path = os.path.expanduser("~/.bin/dep/music.txt")
    music_list = load_file(list_path)
    prnt = escape_terminal_characters(music_list, True)
    tmp = []
    for i in range(len(music_list)):
        print("\n" + str(i + 1) + " - " + prnt[i])
        if input("Play this title? (y/N) : ").lower() == "y":
            tmp.append(i)
    save_file(list_path, [music_list[i] for i in tmp])


if __name__ == "__main__":
    main()
