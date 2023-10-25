class DotDict(dict):

    def __getattr__(self, attr):
        if attr in self:
            return self[attr]
        else:
            return None
            # raise AttributeError(f"'DotDict' object has no attribute '{attr}'")

    def __setattr__(self, attr, value):
        self[attr] = value

    def __delattr__(self, attr):
        if attr in self:
            del self[attr]
        else:
            return None
            # raise AttributeError(f"'DotDict' object has no attribute '{attr}'")

    def to_dict(self):
        return dict(self)

    def __repr__(self):
        return str(dict(self))


class DataContainer:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str(self.data)

    def __getattr__(self, name):

        if name in self.data:
            return self.data[name]
        else:
            return None
            # raise AttributeError(f"'DataContainer' object has no attribute '{name}'")


class BaseModel:
    def __init__(self, **kwargs):
        for field_name, field_type in self.__annotations__.items():
            setattr(self, field_name, kwargs.get(field_name))
