from collections.abc import Mapping


class ReadOnlyDict(Mapping):
    def __init__(self, data: dict[str, str] | None = None):
        if data is None:
            data = {}

        self._data = data

    def __getitem__(self, key: str) -> str:
        return self._data[key]

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __repr__(self):
        classname = self.__class__.__name__
        data_repr = repr(self._data)
        return f"{classname}({data_repr})"
