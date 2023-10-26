import logging
import os
from enum import Enum
from typing import List, Dict, Optional, Union
from urllib import request

import aiohttp
import yaml
from pydantic import BaseModel, PositiveInt, ValidationError, Field

logger = logging.getLogger()


DEFAULT_CONFIG_PATHS = [
    os.path.expanduser(os.path.join("~", ".config", "mediasorter.yml")),
    os.path.join("etc", "mediasorter", "mediasorter.yml")
]


class MediaType(Enum):
    TV_SHOW = "tv"
    MOVIE = "movie"
    AUTO = "auto"


class Action(Enum):
    MOVE = "move"
    HARDLINK = "hardlink"
    SYMLINK = "symlink"
    COPY = "copy"


class MetadataProviderApi(BaseModel):
    name: str
    key: Optional[str]
    url: Optional[str]
    path: Optional[str]


class OperationOptions(BaseModel):
    user: str = "root"
    group: str = "media"
    chown: bool = False
    dir_mode: str = '0o644'
    file_mode: Optional[str]
    overwrite: bool = False
    infofile: bool = False
    shasum: bool = False


class ScanConfig(BaseModel):
    """
    Specify an "input/output" combo for different directories
    """
    src_path: str  # source path (duh...)
    media_type: MediaType = MediaType.AUTO  # force only a specific media type
    action: Action = Action.COPY  # select action type
    tv_shows_output: Optional[str]  # where to put recognized TV shows
    movies_output: Optional[str]  # where to put recognized movies
    options: OperationOptions = OperationOptions()  # options for the sorting operation itself


class BaseParams(BaseModel):
    min_split_length: PositiveInt = 3
    suffix_the: bool = False
    search_overrides: Dict[str, str] = {}
    name_overrides: Dict[str, str] = {}
    file_format: str


class MovieParams(BaseParams):
    subdir: bool = True  # sort all files related to a single movie to a common subdir
    file_format: str = "{title} ({year})"
    dir_format: str = file_format
    allow_metadata_tagging: bool = False


class TvShowParams(BaseParams):
    dir_format: str = "{series_title}/Season {season_id}"
    file_format: str = '{series_title} - S{season_id:02d}E{episode_id:02d} - {episode_title}'


class Parameters(BaseModel):
    valid_extensions: List[str] = [".avi", ".mkv", ".mp4"]
    split_characters: List[str] = [" ", ".", "_"]

    tv: TvShowParams = TvShowParams()
    movie: MovieParams = MovieParams()


class Logging(BaseModel):
    logfile: str
    loglevel: str


class MediaSorterConfig(BaseModel):
    # Configure different metadata provider APIs (API keys, override URLs,...).
    # Must correspond to an existing key in the MetadataProvider enum.
    api: List[MetadataProviderApi] = []

    # Configure multiple directories to be scanned
    # without the need to specify using command line interface.
    scan_sources: Optional[List[ScanConfig]] = None

    parameters: Parameters = Parameters()

    metainfo_map: Dict[str, str] = {}

    loging: Optional[Logging]

    maximum_concurrent_requests: int = Field(gt=0, default=100)


class SearchOverrides(BaseModel):
    movies: dict[str, str]
    shows: dict[str, str]


def read_search_overrides() -> SearchOverrides:
    url = 'https://raw.githubusercontent.com/xyzjonas/mediasorter/rewrite/mediasorter.search.overrides.yml'
    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            text = response.read().decode("utf-8").lower()
            data = yaml.load(text, yaml.SafeLoader)

            return SearchOverrides(**data)
    except Exception as e:
        logger.error(f'Can\'t read public search overrides file: {e}')
    return SearchOverrides(movies={}, shows={})


def read_config(config_file: str) -> MediaSorterConfig:

    with open(config_file, 'r') as cfgfile:
        o_config = yaml.load(cfgfile, Loader=yaml.SafeLoader)

    return MediaSorterConfig(**o_config['mediasorter'])


class ConfigInstance:

    __instance: MediaSorterConfig = None

    @property
    def file(self) -> MediaSorterConfig:
        if not self.is_loaded:
            raise RuntimeError('Configuration not initialized')

        return self.__instance

    @property
    def is_loaded(self) -> bool:
        return self.__instance is not None

    def load(self, custom_path: str = None):
        for cfg_path in (DEFAULT_CONFIG_PATHS if not custom_path else [custom_path]):
            try:
                logger.info(f'reading configuration file: {cfg_path}')
                self.__instance = read_config(cfg_path)
                break
            except FileNotFoundError:
                logger.warning(f"Can't load configuration '{cfg_path}', file not found")
            except (KeyError, ValidationError) as e:
                logger.warning(f"Can't load configuration '{cfg_path}', invalid config keys.")
            except Exception as e:
                logger.warning(f"Can't load configuration from '{cfg_path}', unexpected error {e} ")
        else:
            raise RuntimeError('Configuration not loaded!')


config: ConfigInstance = ConfigInstance()
