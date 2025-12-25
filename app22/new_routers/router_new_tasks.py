from app22.logger_core.config_logger import ConfigLogger
from fastapi import APIRouter, HTTPException, Depends
from celery.result import AsyncResult
from datetime import datetime

from app22.celery_tasks.Class_client_https import RespServer
from app22.celery_tasks.new_tasks import task_weather_new, task_one_add
from app22.new_routers.schema_new_tasks import Req1BodyReq, TaskOneAdd, TaskOneQuery, Req1ParamsReq


logFC = ConfigLogger.getLogger("FileStdout", "new_routers")


new_router = APIRouter(prefix="/new_router", tags=["NEW new_routers"])


@new_router.post("/weather_new_celery", response_model=RespServer)
async def weather_new_celery(body: Req1BodyReq, params: Req1ParamsReq = Depends()):
    logFC.info(f"POST/weather_new_celery : {datetime.utcnow()} : params \n{params.dict()} \n{body.dict()}")

    task: AsyncResult = task_weather_new.delay(body.sleep_sec, params.q, params.APPID)

    task_result: dict = task.get()
    result_from_celery: RespServer = RespServer(**task_result)
    logFC.info(f"POST/weather_new_celery : {datetime.utcnow()} : res \n{result_from_celery}")

    if task_result is None:
        raise HTTPException(status_code=500, detail="Task 'task_weather_new.delay' execution failed")
    return result_from_celery


@new_router.post("/one_add", response_model=TaskOneQuery)
async def one_add(body: TaskOneAdd):
    logFC.info(f"POST/task_one_add : 'begin' {datetime.utcnow()} : body.dict() = {body.dict()}")

    task: AsyncResult = task_one_add.delay(body.dict())
    task_result: dict = task.get()

    logFC.info(f"POST/task_one_add : 'end' {datetime.utcnow()} : task_result = {task_result}")
    if task_result is None:
        raise HTTPException(status_code=500, detail="Task 'task_one_add' execution failed")
    return TaskOneQuery(**task_result)
