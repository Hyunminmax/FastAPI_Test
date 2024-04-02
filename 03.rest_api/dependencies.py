from database import SessionLocal


# 동기용 의존성(세션 관리)
def get_db():
    db = SessionLocal()
    # yield 제너레이터: 연결 된 상태를 유지시켜주는 용도
    # db가 yield를 만나면 멈추고 대기.
    try:
        yield db
    finally:
        db.close()

# 비동기용 의존성(세션 관리)
from database import AsyncSessionLocal
async def get_async_db():
    db = SessionLocal()
    # yield 제너레이터: 연결 된 상태를 유지시켜주는 용도
    # db가 yield를 만나면 멈추고 대기.
    async with AsyncSessionLocal() as session:
        yield session

