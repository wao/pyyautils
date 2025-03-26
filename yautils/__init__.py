from loguru import logger
from typing import Optional, Callable, Any, Awaitable, TypeVar

T = TypeVar('T')

def not_null(obj : Optional[T])->T:
    if obj is not None:
        return obj
    else:
        raise AssertionError("Should not be None")


def yassert(cond : bool, msg : Optional[str] = None )->None:
    if not cond:
        if not msg:
            msg = "Assert error"

        raise AssertionError(msg)

def catch_all_exception(func : Callable[[Any], None]):
    def wrapped_func(*argv, **argm):
        try:
            func(*argv, **argm)
        except Exception:
            logger.exception("Unexpect exception")

    return wrapped_func

async def async_catch_all_exception(obj : Awaitable[Any]):
    try:
        return await obj
    except Exception:
        logger.exception("Unexpect exception")


__all__=['not_null', 'yassert']
