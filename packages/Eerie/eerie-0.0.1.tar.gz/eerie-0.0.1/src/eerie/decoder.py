"""
decode query strings.
"""

import typing
import urllib.parse


class DecodeError(ValueError):
    """
    Raised when a query string cannot be decoded.
    """


class UnquoteFunction(typing.Protocol):
    """
    A :func:`urllib.parse.unquote`-like function.
    """

    # pylint: disable=too-few-public-methods

    def __call__(
        self,
        string: str,
        encoding: str,
        errors: str,
    ) -> str:
        """
        Unquote a character string.

        :param string: a string to unquote.
        :param encoding: an encoding to use.
        :param errors: an error handling scheme.

        :returns: the unquoted string.
        """


def _decode_key(
    result: dict[str, typing.Any],
    key: str,
    value: str | None,
    seen: set[str],
) -> None:
    # pylint: disable=too-complex
    current: typing.Any = result
    k: str | None

    if (i := key.find("[")) != -1:
        k = key[:i]
        extra = key[i:]
    else:
        k = key
        extra = ""

    def _assign(value: typing.Any) -> None:
        nonlocal current

        if k is not None:
            if not isinstance(current, dict):
                raise DecodeError(
                    "expected dict but got " f"{type(current).__name__} for key {key!r}"
                )

            current = current.setdefault(k, value)
        else:
            if not isinstance(current, list):
                raise DecodeError(
                    "expected list but got " f"{type(current).__name__} for key {key!r}"
                )

            if len(current) == 0 or (not isinstance(current[-1], list) and value == []):
                current.append(value)
                current = value
            elif key not in seen:
                current = current[-1]
            else:
                current.append(value)
                current = value

                seen.clear()

    while extra:  # pylint: disable=while-used
        if extra.startswith("[]"):
            _assign([])

            k = None
            extra = extra[2:]

            continue

        if extra.startswith("[") and (i := extra.find("]", 1)) != -1:
            _assign({})

            k = extra[1:i]
            extra = extra[i + 1 :]

            continue

        break

    if k is not None:
        if not isinstance(current, dict):
            raise DecodeError(
                "expected dict but got " f"{type(current).__name__} for key {key!r}"
            )

        current[k] = value
    else:
        if not isinstance(current, list):
            raise DecodeError(
                "expected list but got " f"{type(current).__name__} for key {key!r}"
            )

        current.append(value)
        current = current[-1]

    seen.add(key)


def decode(
    string: str,
    encoding: str = "utf-8",
    errors: str = "replace",
    separator: str = "&",
    unquote_via: UnquoteFunction = urllib.parse.unquote,
) -> dict[str, typing.Any]:
    """
    Parse a query string into a dictionary.

    :param string: a query string to parse.
    :param encoding: an encoding to use.
    :param errors: an error handling scheme.
    :param separator: a separator to use.
    :param unquote_via: a function to use to unquote strings.

    :returns: a dictionary with parsed data.
    """
    result: dict[str, typing.Any] = {}

    seen: set[str] = set()

    for item in string.split(separator):
        if not item:
            continue

        parts = item.partition("=")

        key = unquote_via(parts[0], encoding, errors)
        value = unquote_via(parts[2], encoding, errors) if parts[1] else None

        _decode_key(result, key, value, seen)

    return result
