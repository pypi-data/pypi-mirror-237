import logging
from typing import Optional, List, Dict

from logvista.level import Level
from logvista.configs import StreamConfig, FileConfig, LogvistaConfig


class Configs:
    __key: str
    __logvista_config: Optional[LogvistaConfig]
    __stream_config: Optional[StreamConfig]
    __file_config: Optional[FileConfig]

    def __init__(
            self,
            key: str,
            *,
            logvista_config: Optional[LogvistaConfig] = None,
            stream_config: Optional[StreamConfig] = None,
            file_config: Optional[FileConfig] = None
        ) -> None:
        self.__key = key
        self.__logvista_config = logvista_config
        self.__stream_config = stream_config
        self.__file_config = file_config

    def __str__(self) -> str:
        return f'{self.key}-configs'

    @property
    def key(self) -> str:
        return self.__key

    @property
    def logvista_config(self) -> Optional[LogvistaConfig]:
        return self.__logvista_config

    @property
    def stream_config(self) -> Optional[StreamConfig]:
        return self.__stream_config

    @property
    def file_config(self) -> Optional[FileConfig]:
        return self.__file_config


class Observer:
    __system_name: str
    __configs_list: List[Configs]

    def __init__(
            self,
            system_name: str,
        ) -> None:
        self.__system_name = system_name
        self.__configs_list = [Configs(
                "default",
                stream_config=StreamConfig(),
                file_config=FileConfig(),
                logvista_config=LogvistaConfig()
            )]

    def __str__(self) -> str:
        return f'{self.system_name}-observer'

    def get_configs(self, configs_key: str) -> Optional[Configs]:
        for configs in self.__configs_list:
            if configs.key == configs_key:
                return configs
        return None

    def add_configs(self, configs: Configs) -> None:
        self.__configs_list.append(configs)

    def get_logger(
            self,
            logger_name: str,
            configs_key: str = "default"
        ) -> logging.Logger:
        logger = logging.getLogger(logger_name)
        logger.setLevel(Level.DEBUG.value)
        return logger

    @property
    def system_name(self) -> str:
        return self.__system_name

    @property
    def configs_list(self) -> List[Configs]:
        return self.__configs_list