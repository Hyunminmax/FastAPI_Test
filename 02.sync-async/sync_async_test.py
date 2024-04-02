from fastapi import APIRouter
import time

router = APIRouter()

@router.get('/slow-sync-ping')
def slow_sync_ping():
    time.sleep(10)
    return {'msg' : 'pong'}

import asyncio
@router.get('/slow-async-ping')
async def slow_async_ping():
    await asyncio.sleep(10) # 10초를 기다린다. 다른 작업들은 진행이 된다.

    return {'msg' : 'ping'}

# 피보나치 수열 > 무거운 연산 작업
# 1 1 2 3 5 8
# CPU에 부하가 걸리는 작업 (복잡한 연산) : 동기
# I/O 비동기
def cpu_intensive_task():
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    result = fibonacci(35)
    return result

# Worst case
# CPU 부하 -> Event Loop에 부하가 걸림.
async def cpu_hard_task():
    result = await cpu_intensive_task()
    return {'msg':result}

# Good case
# CPU에 부하가 많이 걸리는 작업은 이벤트 루프에서 분리 후, 별도의 프로세스에서 실행하게 만들어준다.
from concurrent.futures import ProcessPoolExecutor
def cpu_bound_task():
    with ProcessPoolExecutor() as executor:
        result = asyncio.get_event_loop().run_in_executor(
            executor, cpu_intensive_task
        ) # context switching
    return {'result': result}
