from abc import abstractmethod
from logging import Logger
from typing import Any, Callable, Coroutine, List, Optional, Type
from asyncpgdb.typing import T
from asyncpgdb.sql import query_args
from asyncpgdb.row import get_row_parser, parse_row
from asyncpgdb.asyncpg import ConnectionAsyncpg
from asyncpgdb.exception import handle_exception as __handle_exception


def __execute__(func: Callable[..., Coroutine[Any, Any, T]]):
    exception_id = f"asyncpgdb.execute.{func.__name__}.exception"

    async def inner(*args, **kwargs) -> T:
        try:
            result = await func(*args, **kwargs)
        except Exception as exception:
            result = __handle_exception(exception_id, exception)
        return result

    return inner


def __iterate__(func):
    exception_id = f"asyncpgdb.iterate.{func.__name__}.exception"

    async def inner(*args, **kwargs):
        try:
            async for obj in func(*args, **kwargs):
                yield obj
        except Exception as exception:
            __handle_exception(exception_id, exception)

    return inner


async def _execute_query(query: str, vars: Optional[dict], func):
    qa = query_args(query=query, vars=vars)
    result = await func(*qa.query_args())
    return result


@__execute__
async def fetch_var(
    query: str,
    vars: Optional[dict] = None,
    conn: ConnectionAsyncpg = None,
    row_class: Optional[Type[T]] = None,
):
    var = await _execute_query(query=query, vars=vars, func=conn.fetchval)
    if var is None:
        result = None
    elif row_class is None:
        result = var
    else:
        result = parse_row(row=var, row_class=row_class)

    return result


@__execute__
async def fetch_one(
    query: str,
    vars: Optional[dict] = None,
    conn: ConnectionAsyncpg = None,
    row_class: Type[T] = dict,
):
    row = await _execute_query(query=query, vars=vars, func=conn.fetchrow)
    result = None if row is None else parse_row(row=row, row_class=row_class)
    return result


@__execute__
async def fetch_all(
    query: str,
    vars: Optional[dict] = None,
    conn: ConnectionAsyncpg = None,
    row_class: Type[T] = dict,
):
    rows = await _execute_query(query=query, vars=vars, func=conn.fetch)
    if rows and isinstance(rows, list):
        if row_class is dict:
            result: List[dict] = list(map(row_class, rows))
        else:
            row_parser = get_row_parser(row_class=row_class)
            result: List[row_class] = list(map(row_parser, rows))
    else:
        result = []

    return result


@__iterate__
async def iter_all(
    query: str,
    vars: Optional[dict] = None,
    conn: ConnectionAsyncpg = None,
    row_class: Type[T] = dict,
):
    qa = query_args(query=query, vars=vars)
    async with conn.transaction():
        row_parser = get_row_parser(row_class=row_class)
        async for row in conn.cursor(*qa.query_args()):
            yield row_parser(row)


@__execute__
async def execute(
    query: str,
    vars: Optional[dict] = None,
    timeout: Optional[float] = None,
    conn: ConnectionAsyncpg = None,
):
    qa = query_args(query=query, vars=vars)
    result = True
    async with conn.transaction():
        result = await conn.execute(*qa.query_args(), timeout=timeout)
        if result is None:
            result = True
    return result


@__execute__
async def execute_many(
    query: str,
    vars_list: list[dict],
    timeout: Optional[float] = None,
    conn: ConnectionAsyncpg = None,
):
    result = None
    qa = query_args(command=query, vars_list=vars_list)

    async with conn.transaction():
        result = await conn.executemany(*qa.command_args(), timeout=timeout)
    if result is None:
        result = True
    return result


class ExecuteProtocol:
    @abstractmethod
    async def acquire_connection(self) -> ConnectionAsyncpg:
        pass

    @abstractmethod
    async def release(self, __conn: ConnectionAsyncpg):
        pass

    def log_info(self, *args):
        logger = getattr(self, "_logger")
        if logger is not None and isinstance(logger, Logger):
            logger.info(*args)

    async def _execute(self, method: Callable[..., Coroutine[Any, Any, T]], **kwargs):
        conn = await self.acquire_connection()
        kwargs["conn"] = conn
        result = await method(**kwargs)
        await self.release(conn)
        return result

    async def _iterate(self, method: Callable[..., Coroutine[Any, Any, T]], **kwargs):
        conn = await self.acquire_connection()
        kwargs["conn"] = conn
        async for obj in method(**kwargs):
            yield obj
        await self.release(conn)

    async def fetch_var(
        self,
        query: str,
        vars: Optional[dict] = None,
        row_class: Optional[Type[T]] = None,
    ):
        return await self._execute(
            method=fetch_var, query=query, vars=vars, row_class=row_class
        )

    async def fetch_one(
        self, query: str, vars: Optional[dict] = None, row_class: Type[T] = dict
    ):
        return await self._execute(
            method=fetch_one, query=query, vars=vars, row_class=row_class
        )

    async def fetch_all(
        self, query: str, vars: Optional[dict] = None, row_class: Type[T] = dict
    ):
        return await self._execute(
            method=fetch_all, query=query, vars=vars, row_class=row_class
        )

    async def iter_all(
        self, query: str, vars: Optional[dict] = None, row_class: Type[T] = dict
    ):
        async for obj in self._iterate(
            method=iter_all, query=query, vars=vars, row_class=row_class
        ):
            yield obj

    async def execute(
        self,
        query: str,
        vars: Optional[dict] = None,
        timeout: Optional[float] = None,
    ):
        return await self._execute(
            method=execute, query=query, vars=vars, timeout=timeout
        )

    async def execute_many(
        self,
        query: str,
        vars_list: list[dict],
        timeout: Optional[float] = None,
    ):
        result = None
        if vars_list:
            result = await self._execute(
                method=execute_many,
                query=query,
                vars_list=vars_list,
                timeout=timeout,
            )
        return result
