#!/usr/bin/env python3
# Program that helps play music

# Programmed by CoolCat467.

"""Program that helps play music.

Arguments:
---------
-reflist
Refresh Music List File with terminal text mode UNLESS -noTerm specified,
returns No Output

-length
Return length of Music List File

-getpos=<INDEX> [-printform]
Get the name of the music at index given, and
UNLESS -printform specified, returns path to music,
otherwise prints the song name nicely

-mkprog [-soundmode=<NUM>]
Makes a program to run the selected music and saves to
'tmprog.sh'

-getgood
Resets Music List File to songs present in file already AND
songs in 'goodmusic.txt'

-getbad
Resets Music List File to songs present in file already AND
songs NOT in 'goodmusic.txt'

"""
from __future__ import annotations

import os
import sys
from typing import Collection

__title__ = "Music"
__author__ = "CoolCat467"
__version__ = "1.1.0"
__ver_major__ = 1
__ver_minor__ = 1
__ver_patch__ = 0

HOME = os.path.expanduser("~")


class HandleFile:
    """Class for loading and saving files."""

    @staticmethod
    def save_file(filename: str, data: list[str]) -> None:
        """File saving."""
        with open(str(filename), mode="w", encoding="utf-8") as save_file:
            save_file.write("\n".join(data))
            save_file.close()

    @classmethod
    def load_file(cls, filename: str) -> list[str]:
        """File loading."""
        data = []
        try:
            with open(str(filename), encoding="utf-8") as load_file:
                data = load_file.read().splitlines()
                load_file.close()
        except OSError:
            cls.save_file(filename, [])
            return []
        return data


def scandir(path: str, exts: Collection[str]) -> list[str]:
    """Return files with extensions matching exts."""
    return [
        i for i in os.listdir(path) if "." in i and i.split(".")[1] in exts
    ]


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


def get_music(do_escape: bool = True) -> list[str]:
    """Return a list of files with the extensions wav and mp3.

    If do_escape is True, replace certain characters with equivalents.
    """
    # Get the filenames
    musics = sorted(scandir(HOME + "/Music", ("wav", "mp3", "m4a")))
    # If we are in terminal mode,
    if do_escape:
        # Pretty much just replace stuff with what it's supposed to be.
        musics = escape_terminal_characters(musics)
    # Return filenames
    return musics


def main() -> str | int:
    """Command Line Interface Entry Point."""
    # Get arguments to work off of
    args = list(sys.argv[1:])
    splitargs: list[str] = sum(
        [list(arg.split("=")) for arg in args if "=" in arg],
        [],
    )

    # Default to sending 'NOARGS'
    toret: str | int = "NOARGS"
    # Change directory to $HOME/.bin/dep
    mepath = os.path.abspath(__file__)
    os.chdir(HOME + "/.bin/dep/")

    # If we should refresh the music list file,
    if "-reflist" in args and toret == "NOARGS":
        # Get music names
        music_names = get_music("-noTerm" not in args)
        # Save music names to music.txt
        HandleFile.save_file("music.txt", music_names)
    # If we should return the length of the music file,
    if "-length" in args and toret == "NOARGS":
        # Load music file
        filedata = HandleFile.load_file("music.txt")
        # Return is length of file data.
        toret = len(filedata)
    # If getpos in equal arguments,
    if "-getpos" in splitargs and toret == "NOARGS":
        # Position is the index of '-getpos' plus one, for what getpos is set to.
        pos = int(splitargs[splitargs.index("-getpos") + 1]) - 1
        # Load music file
        filedata = HandleFile.load_file("music.txt")
        # If it's print form, return "Now Playing <title>"
        if "-printform" in args:
            toret = (
                "Now Playing "
                + escape_terminal_characters(filedata, True)[pos]
            )
        else:
            # Otherwise, return the path to the file.
            toret = HOME + "/Music/" + str(filedata[pos])
    # If we should make a program,
    if "-mkprog" in args and "-soundmode" in splitargs and toret == "NOARGS":
        # Sound is the soundmode position
        sound = str(splitargs[splitargs.index("-soundmode") + 1])
        # File data is the loaded music file
        filedata = HandleFile.load_file("music.txt")
        # Length is the number of music files
        leng = len(filedata)
        # File data is what the program should be.
        filedata = [
            "#!/bin/bash",
            "# -*- coding: utf-8 -*-",
            f"\n# Auto-generated by {__title__} v{__version__} by {__author__}.",
            f"# Said script can be found at {mepath}.\n",
            f'VSoundMode="{sound}"',
            "cd " + HOME,
            "touch .bin/dep/tmp.sh",
            "chmod 755 .bin/dep/tmp.sh",
            'echo "#!/bin/bash" > .bin/dep/tmp.sh',
            'echo "# -*- coding: utf-8 -*-" >> .bin/dep/tmp.sh',
            f'echo "# Auto-generated by {__title__} v{__version__} by {__author__}." >> .bin/dep/tmp.sh',
            "for n in {1.." + str(leng) + "}; do",
            "\t" + str(f'VMusicFile="$(python3 {mepath} -getpos=$n)"'),
            ##                    '\t'+str("Vtmp='"+HOME+"/Music/'$(sed $n'!d' .bin/dep/music.txt)"),
            "\t"
            + str(
                f'VCurPlaying="echo \\"$(python3 {mepath} -getpos=$n -printform)\\""',
            ),
            "\t"
            + 'VOmxRun="omxplayer -o $VSoundMode $VMusicFile >> /dev/null"',
            "\t" + "echo $VCurPlaying >> .bin/dep/tmp.sh",
            "\t" + "echo $VOmxRun >> .bin/dep/tmp.sh",
            "done",
        ]
        # tmprog.sh should be saved to program data
        HandleFile.save_file("tmprog.sh", filedata)
    # If we should get good music,
    if "-getgood" in args and toret == "NOARGS":
        # Get good music from the file
        good = HandleFile.load_file("goodmusic.txt")
        # Replace \\'s with nothing
        good = [str(piece).replace("\\", "") for piece in good]
        # file data is a refreshed list from get_music
        filedata = get_music()
        # Replace \\ with nothing for each entry in the music files.
        ftmp = [str(piece).replace("\\", "") for piece in filedata]
        # tmp is a list of music names if it exists
        tmp = [filedata[ftmp.index(piece)] for piece in good if piece in ftmp]
        # Save the "good" music in the music.txt file.
        HandleFile.save_file("music.txt", tmp)
    # If we should get bad music,
    if "-getbad" in args and toret == "NOARGS":
        # Get good music from the file
        good = HandleFile.load_file("goodmusic.txt")
        # Replace \\'s with nothing
        good = [str(piece).replace("\\", "") for piece in good]
        # filedata is a refreshed list from get_music
        filedata = get_music()
        # Replace \\ with nothing for each entry in the music files.
        ftmp = [str(piece).replace("\\", "") for piece in filedata]
        # tmp is a list of music names if it's not in the good list
        tmp = [
            filedata[ftmp.index(piece)] for piece in ftmp if piece not in good
        ]
        # Save the bad music in the music.txt file.
        HandleFile.save_file("music.txt", tmp)
    return toret


if __name__ == "__main__":
    print(main())
