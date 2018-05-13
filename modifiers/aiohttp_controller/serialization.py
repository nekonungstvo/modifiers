import datetime
import json
from enum import Enum
from functools import partial

from pydantic import BaseModel


class UniversalEncoder(json.JSONEncoder):
    ENCODER_BY_TYPE = {
        datetime.datetime: lambda o: o.isoformat(),
        Enum: lambda o: o.value,
        BaseModel: lambda o: o.dict()
    }

    def default(self, obj):
        for data_type, encoder in self.ENCODER_BY_TYPE.items():
            if isinstance(obj, data_type):
                return encoder(obj)
        return super().default(obj)


dumps = partial(json.dumps, cls=UniversalEncoder)
