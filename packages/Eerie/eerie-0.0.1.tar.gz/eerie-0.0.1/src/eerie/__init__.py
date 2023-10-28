"""
eerie is a Python library for building and parsing query strings.
"""

from .decoder import DecodeError, decode, UnquoteFunction
from .encoder import encode, QuoteFunction

__all__ = (
    "decode",
    "DecodeError",
    "encode",
    "QuoteFunction",
    "UnquoteFunction",
)
