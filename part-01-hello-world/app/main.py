from fastapi import FastAPI, APIRouter


app = FastAPI(title="Recipe API", openapi_url="/openapi.json")

api_router = APIRouter()


@api_router.get("/", status_code=200)
async def root() -> dict:
    """
    Root GET
    """
    # emulate long-running, expensive job
    import time, sys, os, asyncio
    t0 = time.time()
    print(f" in: {time.time()}", file=sys.stderr)
    
    pid = os.fork()
    if not pid:
        # Child
        while time.time() - t0 < 10:
            pass
        print(f"exiting [pid={os.getpid()}]: {time.time()}", file=sys.stderr)
        os._exit(0)

    print(f"started  [pid={pid}]: {time.time()}", file=sys.stderr)

    while True:
        print(f"polling [pid={pid}]: {time.time()}", file=sys.stderr)
        (ret_pid, exit_status) = os.waitpid(pid, os.WNOHANG)
        if (ret_pid, exit_status) == (0, 0):
            await asyncio.sleep(1)
            continue
        # FIXME: check for successful completion
        break

    print(f"finished [pid={pid}]: {time.time()}", file=sys.stderr)

    return {"msg": "Hello, World!"}


app.include_router(api_router)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
