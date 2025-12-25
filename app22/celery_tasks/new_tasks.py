from app22.logger_core.config_logger import ConfigLogger
from fastapi.encoders import jsonable_encoder
from datetime import datetime
import asyncio
import time

from app22.celery_tasks.Class_client_https import main_weather_create_task, RespServer
from app22.celery_tasks.celery_worker import celery

from app22.new_routers.schema_new_tasks import TaskOneAdd
from app22.db_core.db_conf import SessionDB
from app22.db_core.model.model_new_tasks import TaskOne


logFC = ConfigLogger.getLogger("FileStdout", "new_tasks")


@celery.task(name="task_weather_new")
def task_weather_new(sleep_sec: int = 1, city: str = "", appid: str = ""):
    logFC.info(f"'task_weather_new' {datetime.utcnow()}: {sleep_sec} - {city}")

    result: RespServer = asyncio.run(main_weather_create_task(city, appid))

    time.sleep(sleep_sec)
    logFC.info(f"'task_weather_new' {datetime.utcnow()}: {sleep_sec} - {appid}")
    return result.dict()


@celery.task(name="task_one_add")
def task_one_add(body_dict: dict):
    logFC.info(f"'task_one_add' {datetime.utcnow()}: 'before' = {body_dict}")
    body = TaskOneAdd(**body_dict)

    new_one: TaskOne = TaskOne(title=body.title, msg=body.msg)
    with SessionDB.get_session() as db:
        db.add(new_one)
        db.commit()
        db.refresh(new_one)

    res: dict = jsonable_encoder(new_one)
    logFC.info(f"'task_one_add' {datetime.utcnow()}: 'after' = {res}")
    return res
