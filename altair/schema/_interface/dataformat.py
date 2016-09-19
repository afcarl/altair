# This file auto-generated by `generate_schema_interface.py`.
# Do not modify this file directly.

import traitlets as T


class DataFormat(T.Enum):
    """
    One of ['json', 'csv', 'tsv']
    """
    def __init__(self, default_value=T.Undefined, **metadata):
        super(DataFormat, self).__init__(['json', 'csv', 'tsv'],
                                    default_value=default_value,
                                    **metadata)