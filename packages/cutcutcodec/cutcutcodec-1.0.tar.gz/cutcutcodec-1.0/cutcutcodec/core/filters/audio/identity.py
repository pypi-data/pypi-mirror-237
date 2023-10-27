#!/usr/bin/env python3

"""
** An audio filter that doing nothing. **
-----------------------------------------
"""

import typing

from cutcutcodec.core.classes.filter import Filter
from cutcutcodec.core.classes.stream import Stream



class FilterAudioIdentity(Filter):
    """
    ** Allows to convert a set of streams into a filter. **

    Examples
    --------
    >>> from cutcutcodec.core.filters.audio.identity import FilterAudioIdentity
    >>> from cutcutcodec.core.generation.audio.noise import GeneratorAudioNoise
    >>>
    >>> (s_base_audio,) = GeneratorAudioNoise(0).out_streams
    >>> identity = FilterAudioIdentity([s_base_audio])
    >>>
    >>> s_base_audio is identity.out_streams[0]
    True
    >>>
    """

    def __init__(self, in_streams: typing.Iterable[Stream]):
        """
        Parameters
        ----------
        in_streams : typing.Iterable[Stream]
            All the streams to keep intact.
            Transmitted to ``cutcutcodec.core.classes.filter.Filter``.
        """
        super().__init__(in_streams, in_streams)

    def _getstate(self) -> dict:
        return {}

    def _setstate(self, in_streams: typing.Iterable[Stream], state: dict) -> None:
        assert state == {}
        FilterAudioIdentity.__init__(self, in_streams)

    @classmethod
    def default(cls):
        return cls([])
