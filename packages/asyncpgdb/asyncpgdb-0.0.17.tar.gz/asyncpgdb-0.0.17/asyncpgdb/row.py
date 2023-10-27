from typing import Callable, Type
from asyncpgdb.typing import T
from asyncpgdb.asyncpg import Record

class RowTypeError(TypeError):
    def __init__(self, row_class, row_type):
        super().__init__(
            f"asyncpgdb.row.parse_row.type_error: expected: {row_class.__name__} actual: {row_type.__name__}"
        )


def parse_row(row, row_class: Type[T]):
    result = None
    for key in ("parse_obj", "model_validate"):
        if hasattr(row_class, key):
            parser = getattr(row_class, key)
            try:
                value = parser(row)
            except Exception:
                value = None
            if value is not None:
                result = value
                break
    else:
        result = row
    


    if not isinstance(result, (row_class,Record)):
        if result is not None and ".Record" in type(result).__name__:
            result = dict(result)
        else:

            row_type = type(result)
            raise RowTypeError(row_class=row_class, row_type=row_type)

    return result


def get_row_parser(row_class: Type[T]) -> Callable[[object], T]:
    result = lambda row: parse_row(row=row, row_class=row_class)
    return result
