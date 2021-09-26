from marshmallow import fields
from .main import Fields

class BitField(fields.Field):
    
    def __init__(self, nested: Fields, *args, **kwargs):
        self.nested = nested
        super().__init__(*args, **kwargs)
    
    def _serialize(self, value, attr, obj, **kwargs) -> str:
        if value is None:
            return ""
        return int(value)
    
    def _deserialize(self, value, attr, data, **kwargs) -> int:
        try:
            return self.nested(int(value))
        except Exception as e:
            raise e