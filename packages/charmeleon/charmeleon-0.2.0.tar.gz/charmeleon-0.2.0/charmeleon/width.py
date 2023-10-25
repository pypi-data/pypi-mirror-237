"""Width class for handling width of characters."""
import pathlib
import re

import charmeleon.table.alpha
import charmeleon.table.digit
import charmeleon.table.kana
import charmeleon.table.punct
from charmeleon.error import ArgError


class Width:
    """Width class for handling width of characters."""

    def __init__(self: "Width",  # noqa: PLR0913
                 digit: bool = True,
                 alpha: bool = True,
                 punct: bool = True,
                 kana: bool = True,
                 go: bool = False) -> None:
        """
        Initialize Width class.

        Args:
        ----
            digit (bool): True if digit characters are used.
            alpha (bool): True if alphabet characters are used.
            punct (bool): True if punctuation characters are used.
            kana (bool): True if kana characters are used.
            go (bool): True if golang's width functions are used.

        Raises:
        ------
            ArgError: If all of digit, alpha, punct and kana are False.
        """
        if not any({digit, alpha, punct, kana}):
            msg = "At least one of digit, alpha, punct or kana must be True."
            raise ArgError(msg)
        self.__h2f_table = {}
        self.__f2h_table = {}
        self.__hs2f_pattern = None
        if digit:
            self.__h2f_table |= str.maketrans(charmeleon.table.digit.HALF2FULL)
            self.__f2h_table |= str.maketrans(charmeleon.table.digit.FULL2HALF)
        if alpha:
            self.__h2f_table |= str.maketrans(charmeleon.table.alpha.HALF2FULL)
            self.__f2h_table |= str.maketrans(charmeleon.table.alpha.FULL2HALF)
        if punct:
            self.__h2f_table |= str.maketrans(charmeleon.table.punct.HALF2FULL)
            self.__f2h_table |= str.maketrans(charmeleon.table.punct.FULL2HALF)
        if kana:
            self.__h2f_table |= str.maketrans(charmeleon.table.kana.HALF2FULL)
            self.__f2h_table |= str.maketrans(charmeleon.table.kana.FULL2HALF)
            self.__hs2f = charmeleon.table.kana.HALFS2FULL
            self.__hs2f_pattern = re.compile(
                "|".join(map(re.escape, self.__hs2f.keys())))
        if go:
            import platform
            from ctypes import c_char_p, cdll
            system = platform.system().lower()
            machine = platform.machine().lower()
            if system not in {"linux", "darwin"}:
                msg = (f"Unsupported system: {system}."
                       "go option is supported only for Linux and Darwin.")
                raise ArgError(msg)
            if machine not in {"x86_64", "arm64"}:
                msg = (f"Unsupported machine: {machine}."
                       "go option is supported only for x86_64 and arm64.")
                raise ArgError(msg)
            machine = "amd64" if machine == "x86_64" else "arm64"
            path = pathlib.Path(__file__).parent / f"go/{system}_{machine}"
            lib = cdll.LoadLibrary(path.as_posix())
            self.__narrow = lib.Narrow
            self.__narrow.argtypes = [c_char_p]
            self.__narrow.restype = c_char_p
            self.__widen = lib.Widen
            self.__widen.argtypes = [c_char_p]
            self.__widen.restype = c_char_p
            self.__fold = lib.Fold
            self.__fold.argtypes = [c_char_p]
            self.__fold.restype = c_char_p

    def __h2f_replace(self: "Width", match: re.Match) -> str:
        """Replace function for re.sub."""
        return self.__hs2f[match.group(0)]

    def to_full(self: "Width", chars: str) -> str:
        """
        Convert half-width characters to full-width characters.

        Args:
        ----
            chars (str): Characters to be converted.

        Returns:
        -------
            str: Converted characters.

        Examples:
        --------
            >>> from charmeleon import Width
            >>> width = Width()
            >>> width.to_full("abc")
            'ａｂｃ'
        """
        if self.__hs2f_pattern:
            return (self.__hs2f_pattern.sub(self.__h2f_replace, chars)
                    .translate(self.__h2f_table))
        return chars.translate(self.__h2f_table)

    def to_half(self: "Width", chars: str) -> str:
        """
        Convert full-width characters to half-width characters.

        Args:
        ----
            chars (str): Characters to be converted.

        Returns:
        -------
            str: Converted characters.

        Examples:
        --------
            >>> from charmeleon import Width
            >>> width = Width()
            >>> width.to_half("ＡＢＣ")
            'ABC'
        """
        return chars.translate(self.__f2h_table)

    def narrow(self: "Width", chars: str) -> str:
        """
        narrow function is a proxy for golang's Narrow function.

        Narrow is a transform that maps runes to their narrow variant, if available.
        See https://pkg.go.dev/golang.org/x/text/width#Narrow.

        Args:
        ----
            chars (str): Characters to be converted.

        Returns:
        -------
            str: Converted characters.

        Examples:
        --------
            >>> from charmeleon import Width
            >>> width = Width(go=True)
            >>> width.narrow("abヲ￦○￥Ａ")
            'abｦ₩￮¥A'
        """
        return self.__narrow(chars.encode()).decode()

    def widen(self: "Width", chars: str) -> str:
        """
        widen function is a proxy for golang's Widen function.

        Widen is a transform that maps runes to their wide variant, if available.
        See https://pkg.go.dev/golang.org/x/text/width#Widen.

        Args:
        ----
            chars (str): Characters to be converted.

        Returns:
        -------
            str: Converted characters.

        Examples:
        --------
            >>> from charmeleon import Width
            >>> width = Width(go=True)
            >>> width.widen("ab¥ｦ₩￮")
            'ab¥ヲ￦○'
        """
        return self.__widen(chars.encode()).decode()

    def fold(self: "Width", chars: str) -> str:
        """
        fold function is a proxy for golang's Fold function.

        Fold is a transform that maps all runes to their canonical width.
        See https://pkg.go.dev/golang.org/x/text/width#Fold.

        Args:
        ----
            chars (str): Characters to be converted.

        Returns:
        -------
            str: Converted characters.

        Examples:
        --------
            >>> from charmeleon import Width
            >>> width = Width(go=True)
            >>> width.fold("abｦ￦￮￥Ａ")
            'abヲ₩○¥A'
        """
        return self.__fold(chars.encode()).decode()
