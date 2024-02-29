from typing import Any, Dict, Type

from lyzr_rag.readers.base import BasePydanticReader
from lyzr_rag.readers.discord_reader import DiscordReader
from lyzr_rag.readers.elasticsearch import ElasticsearchReader
from lyzr_rag.readers.google_readers.gdocs import GoogleDocsReader
from lyzr_rag.readers.google_readers.gsheets import GoogleSheetsReader
from lyzr_rag.readers.notion import NotionPageReader
from lyzr_rag.readers.slack import SlackReader
from lyzr_rag.readers.string_iterable import StringIterableReader
from lyzr_rag.readers.twitter import TwitterTweetReader
from lyzr_rag.readers.web import (
    BeautifulSoupWebReader,
    RssReader,
    SimpleWebPageReader,
    TrafilaturaWebReader,
)
from lyzr_rag.readers.wikipedia import WikipediaReader
from lyzr_rag.readers.youtube_transcript import YoutubeTranscriptReader

ALL_READERS: Dict[str, Type[BasePydanticReader]] = {
    DiscordReader.class_name(): DiscordReader,
    ElasticsearchReader.class_name(): ElasticsearchReader,
    GoogleDocsReader.class_name(): GoogleDocsReader,
    GoogleSheetsReader.class_name(): GoogleSheetsReader,
    NotionPageReader.class_name(): NotionPageReader,
    SlackReader.class_name(): SlackReader,
    StringIterableReader.class_name(): StringIterableReader,
    TwitterTweetReader.class_name(): TwitterTweetReader,
    SimpleWebPageReader.class_name(): SimpleWebPageReader,
    TrafilaturaWebReader.class_name(): TrafilaturaWebReader,
    RssReader.class_name(): RssReader,
    BeautifulSoupWebReader.class_name(): BeautifulSoupWebReader,
    WikipediaReader.class_name(): WikipediaReader,
    YoutubeTranscriptReader.class_name(): YoutubeTranscriptReader,
}


def load_reader(data: Dict[str, Any]) -> BasePydanticReader:
    if isinstance(data, BasePydanticReader):
        return data
    class_name = data.get("class_name", None)
    if class_name is None:
        raise ValueError("Must specify `class_name` in reader data.")

    if class_name not in ALL_READERS:
        raise ValueError(f"Reader class name {class_name} not found.")

    # remove static attribute
    data.pop("is_remote", None)

    return ALL_READERS[class_name].from_dict(data)
