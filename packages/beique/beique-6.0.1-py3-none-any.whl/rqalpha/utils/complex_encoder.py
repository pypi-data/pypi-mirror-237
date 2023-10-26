import copy
from datetime import datetime, date
import json
from pandas import DataFrame
import pandas as pd


class ComplexEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o, datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o, DataFrame):
            json_str = o.to_json(orient="index", force_ascii=False)
            print(json_str)
            jo = json.loads(json_str)
            list = []
            for key, value in jo.items():
                v = copy.deepcopy(value)
                v['date'] = key
                list.append(v)
            return list
        else:
            return json.JSONEncoder.default(self, o)
