import os
import json
import re
import sys
import traceback
import psutil
import logging
from uuid import uuid4
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class LogChunk:
    id: str
    system_name: str
    cpu_percent: float
    exc_type: str
    exc_value: str
    exc_detail: str
    exc_traceback: List[Dict[str, str]]
    file_name: str
    func_name: str
    lineno: int
    message: str
    module: str
    name: str
    level_name: str
    levelno: int
    process: int
    process_name: str
    thread: int
    thread_name: str
    total_memory: int
    available_memory: int
    memory_percent: float
    used_memory: int
    free_memory: int
    cpu_user_time: float
    cpu_system_time: float
    cpu_idle_time: float


class LogvistaHandler(logging.Handler):
    def __init__(self, system_name: str):
        super().__init__()
        self.directory = Path.home() / ".logvista"
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        self.system_name = system_name
        filename = re.sub(r'[ \-./]', '_', self.system_name.lower())
        full_path = os.path.join(self.directory, f"{filename}.logvista")
        self.full_path = full_path

    def emit(self, record: logging.LogRecord) -> None:
        try:
            exc_type, exc_value, tb = sys.exc_info()
            exc_info_dict = {}
            if tb:
                tb_list = traceback.extract_tb(tb)
                tb_dicts = []
                for frame in tb_list:
                    tb_dicts.append({
                        "tb_filename": frame.filename,
                        "tb_lineno": frame.lineno,
                        "tb_name": frame.name,
                        "tb_line": frame.line
                    })
                exc_info_dict = {
                    "exc_type": exc_type.__name__,
                    "exc_value": str(exc_value),
                    "exc_detail": ''.join(traceback.format_exception(exc_type, exc_value, tb)).replace('\n', '\\n'),
                    "traceback": tb_dicts,
                }
            virtual_memory_info = psutil.virtual_memory()._asdict()
            cpu_times_info = psutil.cpu_times()._asdict()

            data = LogChunk(
                id=str(uuid4()),
                system_name=self.system_name,
                cpu_percent=psutil.cpu_percent(),
                exc_type=exc_info_dict["exc_type"],
                exc_value=exc_info_dict["exc_value"],
                exc_detail=exc_info_dict["exc_detail"],
                exc_traceback=exc_info_dict["traceback"],
                file_name=record.filename,
                func_name=record.funcName,
                lineno=record.lineno,
                message=record.message,
                module=record.module,
                name=record.name,
                level_name=record.levelname,
                levelno=record.levelno,
                process=record.process,
                process_name=record.processName,
                thread=record.thread,
                thread_name=record.threadName,
                total_memory=virtual_memory_info["total"],
                available_memory=virtual_memory_info["available"],
                memory_percent=virtual_memory_info["percent"],
                used_memory=virtual_memory_info["used"],
                free_memory=virtual_memory_info["free"],
                cpu_user_time=cpu_times_info["user"],
                cpu_system_time=cpu_times_info["system"],
                cpu_idle_time=cpu_times_info["idle"]
            )

            try:
                self.append_data_to_buffer(data.__dict__)
            except Exception as e:
                print("Error", e)
                pass

        except Exception as e:
            print("Error", e)
            pass

    def append_data_to_buffer(self, new_data):
        with open(self.full_path, "a") as f:
            f.write(json.dumps(new_data) + "\n")