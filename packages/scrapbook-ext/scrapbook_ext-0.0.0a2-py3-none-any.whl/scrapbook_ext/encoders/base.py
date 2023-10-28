from __future__ import annotations

import abc

import scrapbook
import scrapbook.encoders

# NOTE this is supposed to be in the upstream
class BaseEncoder(abc.ABC):
    def name(self):
        ...

    def encodable(self, data):
        ...

    def encode(self, scrap: scrapbook.scraps.Scrap, **kwargs):
        ...

    def decode(self, scrap: scrapbook.scraps.Scrap, **kwargs):
        ...

# NOTE this is supposed to be in the upstream
def load(encoder: BaseEncoder):
    return scrapbook.encoders.registry.register(encoder)

__all__ = [
    BaseEncoder,
    load
]
