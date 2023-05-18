from saq import Queue
from sqlalchemy import text

from app.configs.database import SessionFactory
from app.configs.settings import get_settings

settings = get_settings()


async def before_process(ctx):
    ctx["session"] = SessionFactory()


async def after_process(ctx):
    await ctx["session"].close()


queue = Queue.from_url(settings.get_redis_url())


async def example(ctx, **kwargs):
    session = ctx["session"]
    await session.execute(text("select 'pong';"))


settings = {
    "queue": queue,
    "functions": [example],
    "concurrency": 10,
    "before_process": before_process,
    "after_process": after_process,
}
