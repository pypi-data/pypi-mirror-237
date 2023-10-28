from __future__ import annotations

import base64
import pickle
import functools

import scrapbook

import scrapbook.encoders
import scrapbook.scraps

from . import base
from .. import utils


class PickleEncoder(base.BaseEncoder):
    ENCODER_NAME = 'pickle'

    def name(self):
        return self.ENCODER_NAME

    def encodable(self, data):
        # TODO
        return True

    def encode(self, scrap: scrapbook.scraps.Scrap, **kwargs):
        _impl = utils.func.pipeline(
            functools.partial(pickle.dumps, **kwargs),
            # NOTE .decode() makes sure its a UTF-8 string instead of bytes
            lambda x: base64.b64encode(x).decode()
        )
        return scrap._replace(
            data=_impl(scrap.data)
        )

    def decode(self, scrap: scrapbook.scraps.Scrap, **kwargs):
        _impl = utils.func.pipeline(
            base64.b64decode,
            functools.partial(pickle.loads, **kwargs)
        )
        return scrap._replace(data=_impl(scrap.data))

def load():
    return base.load(PickleEncoder())

__all__= [
    PickleEncoder,
    load
]
