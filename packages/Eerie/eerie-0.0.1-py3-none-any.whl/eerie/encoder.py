"""
encode query strings.
"""

import collections.abc
import dataclasses
import typing
import urllib.parse

SafeCharacters: typing.TypeAlias = str | collections.abc.Iterable[int]


class QuoteFunction(typing.Protocol):
    """
    A :func:`urllib.parse.quote`-like function.
    """

    # pylint: disable=too-few-public-methods

    @typing.overload
    def __call__(
        self,
        string: str,
        safe: SafeCharacters,
        encoding: str | None = None,
        errors: str | None = None,
    ) -> str:
        """
        Quote a character string.

        :param string: a string to quote.
        :param safe: a string of characters considered safe.
        :param encoding: an encoding to use.
        :param errors: an error handling scheme.

        :returns: the quoted string.
        """

    @typing.overload
    def __call__(self, string: bytes | bytearray, safe: SafeCharacters) -> str:
        """
        Quote a byte string.

        :param string: a string to quote.
        :param safe: a string of characters considered safe.

        :returns: the quoted string.
        """

    def __call__(
        self,
        string: str | bytes | bytearray,
        safe: SafeCharacters,
        encoding: str | None = None,
        errors: str | None = None,
    ) -> str:
        """
        Quote a string.

        :param string: a string to quote.
        :param safe: a string of characters considered safe.
        :param encoding: an encoding to use.
        :param errors: an error handling scheme.

        :returns: the quoted string.
        """


def _encode_key(
    result: list[str],
    key: str,
    value: typing.Any,
    escape: collections.abc.Callable[[typing.Any], str],
    indexed: bool,
) -> None:
    if dataclasses.is_dataclass(value):
        for k, val in dataclasses.asdict(value).items():
            _encode_key(result, f"{key}[{k}]", val, escape, indexed)

    elif hasattr(value, "items"):
        for k, val in value.items():
            _encode_key(result, f"{key}[{k}]", val, escape, indexed)

    elif hasattr(value, "__iter__") and not isinstance(value, (bytes, str)):
        for i, val in enumerate(value):
            new_key = f"{key}[{i}]" if indexed else f"{key}[]"

            _encode_key(result, new_key, val, escape, indexed)

    elif value is None:
        result.append(escape(key))

    else:
        result.append(f"{escape(key)}={escape(value)}")


def encode(
    value: dict[typing.Any, typing.Any],
    *,
    indexed: bool = False,
    safe: SafeCharacters = "",
    encoding: str | None = None,
    errors: str | None = None,
    separator: str = "&",
    quote_via: QuoteFunction = urllib.parse.quote,
) -> str:
    """
    Build a query string from a dictionary.

    :param value: a dictionary to build a query string from.
    :param indexed: whether to use indexes as keys for lists..
    :param safe: a string of characters considered safe.
    :param encoding: an encoding to use.
    :param errors: an error handling scheme.
    :param separator: a separator to use between key-value pairs.
    :param quote_via: a function to use for quoting.

    :returns: the query string.
    """
    result: list[str] = []

    def _escape(value: typing.Any) -> str:
        if isinstance(value, bool):
            value = str(int(value))

        if not isinstance(value, (bytes, bytearray, str)):
            value = str(value)

        if isinstance(value, (bytes, bytearray)):
            return quote_via(value, safe)

        return quote_via(value, safe, encoding, errors)

    for k, val in value.items():
        _encode_key(result, k, val, _escape, indexed)

    return separator.join(result)
