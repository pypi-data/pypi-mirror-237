import time

from inspect import iscoroutinefunction
from threading import BoundedSemaphore
from collections.abc import Collection
from typing import Callable, Any

from tqdm import tqdm

from eai_commons.utils.func import get_compact_function_name
from eai_commons.utils.time import current_timestamp, to_date_string, DATE_TIME_PATTERN
from eai_commons.logging import logger


def _section_run(
    function_call,
    iterator,
    origin_func_name: str,
    batch_size: int,
    time_window_sec: float = 0,
    next_batch_sec: float = 0,
) -> Collection | None:
    if not isinstance(iterator, Collection) or isinstance(iterator, str):
        return function_call(iterator)

    total_rows = len(iterator)
    at_least_rows = len(iterator)
    executed = 0
    if total_rows <= batch_size:
        return function_call(iterator)

    results = []
    func_result_type = None

    for offset in tqdm(
        range(0, total_rows, batch_size), total=total_rows // batch_size + 1
    ):
        batch_id = offset // batch_size
        sub_iterator = iterator[offset : offset + batch_size]
        begin = current_timestamp()

        sub_results = function_call(sub_iterator)
        if sub_results:
            func_result_type = func_result_type or type(sub_results)
            results.extend(sub_results)

        sub_executed = len(sub_iterator)
        executed += sub_executed
        at_least_rows -= sub_executed
        logger.info(
            f"func=[{origin_func_name}], batch id: {batch_id}, "
            f"sub tasks: {sub_executed}, "
            f"executed tasks: {executed}, "
            f"at least tasks: {at_least_rows}. "
        )

        # 最后一批，不用休眠
        if len(sub_iterator) < batch_size:
            continue
        # 限速
        elapsed = current_timestamp() - begin
        sleep = time_window_sec * 1000 - elapsed
        if sleep > 0:
            logger.info(
                f"func=[{origin_func_name}], request limit, sleep {sleep}ms before next batch."
            )
            time.sleep(sleep / 1000)
        if next_batch_sec > 0:
            logger.info(
                f"func=[{origin_func_name}], sleep {next_batch_sec * 1000}ms to next batch."
            )
            time.sleep(next_batch_sec)

    if func_result_type:
        return func_result_type(results)
    return None


def section_run(batch_size: int, time_window_sec: float = 0, next_batch_sec: float = 0):
    """
    把一连串的任务分片执行。
    :param batch_size: 分片执行数
    :param time_window_sec: 每个分片的时间窗口
    :param next_batch_sec: 执行下一分片前的休息时间
    """

    def decorator(func):
        if iscoroutinefunction(func):
            raise ValueError(
                "section_run support blocking function. don't use in async function!"
            )

        def wrapper(*args, **kwargs):
            if not args:
                return func(*args, **kwargs)
            iterator, class_inner_method = args[0], False
            if not isinstance(iterator, Collection) or isinstance(iterator, str):
                if len(args) > 1:
                    iterator, class_inner_method = args[1], True
                    if not isinstance(iterator, Collection) or isinstance(
                        iterator, str
                    ):
                        return func(*args, **kwargs)
                else:
                    return func(*args, **kwargs)

            if class_inner_method:
                function_call: Callable[[Any], Any] = lambda sub_iter: func(
                    args[0], sub_iter, *args[2:], **kwargs
                )
            else:
                function_call: Callable[[Any], Any] = lambda sub_iter: func(
                    sub_iter, *args[1:], **kwargs
                )

            origin_function_name = get_compact_function_name(func)
            begin = current_timestamp()
            logger.info(f"func=[{origin_function_name}], section_run start. ")
            results = _section_run(
                function_call,
                iterator,
                origin_function_name,
                batch_size,
                time_window_sec,
                next_batch_sec,
            )
            end = current_timestamp()
            logger.info(
                f"func=[{origin_function_name}], section_run end. time spend: {end - begin}ms, "
                f"start at: [{to_date_string(begin, DATE_TIME_PATTERN)}]"
            )
            return results

        return wrapper

    return decorator


class RateControl:
    """
    控制执行速率
    rate_max：允许的最大执行数
    timeout_sec：获取执行许可的最大等待时间
    """

    def __init__(self, rate_max: int, timeout_sec: int) -> None:
        self.rate_max = rate_max
        self.timeout_sec = timeout_sec
        self.semaphore = BoundedSemaphore(rate_max)

    def control(self, func, *args, **kwargs):
        lock_ = self.semaphore.acquire(timeout=self.timeout_sec)
        if lock_:
            try:
                return func(*args, **kwargs)
            finally:
                self.semaphore.release()

    async def async_control(self, func, *args, **kwargs):
        lock_ = self.semaphore.acquire(timeout=self.timeout_sec)
        if lock_:
            try:
                return await func(*args, **kwargs)
            finally:
                self.semaphore.release()
