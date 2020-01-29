import asyncio


def create_or_use_loop(awaitable):
    try:
        event_loop = asyncio.get_event_loop()
    except RuntimeError:
        event_loop = None

    if event_loop and event_loop.is_running():
        event_loop.call_soon_threadsafe(event_loop.create_task, awaitable)
    else:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(awaitable)
        finally:
            loop.close()
            asyncio.set_event_loop(event_loop)
