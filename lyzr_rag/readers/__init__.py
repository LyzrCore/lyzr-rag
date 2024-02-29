"""Data Connectors for LlamaIndex.

This module contains the data connectors for LlamaIndex. Each connector inherits
from a `BaseReader` class, connects to a data source, and loads Document objects
from that data source.

You may also choose to construct Document objects manually, for instance
in our `Insert How-To Guide <../how_to/insert.html>`_. See below for the API
definition of a Document - the bare minimum is a `text` property.

"""

from lyzr_rag.readers.bagel import BagelReader
from lyzr_rag.readers.base import ReaderConfig
from lyzr_rag.readers.chatgpt_plugin import ChatGPTRetrievalPluginReader
from lyzr_rag.readers.chroma import ChromaReader
from lyzr_rag.readers.dashvector import DashVectorReader
from lyzr_rag.readers.deeplake import DeepLakeReader
from lyzr_rag.readers.discord_reader import DiscordReader
from lyzr_rag.readers.download import download_loader
from lyzr_rag.readers.elasticsearch import ElasticsearchReader
from lyzr_rag.readers.faiss import FaissReader

# readers
from lyzr_rag.readers.file.base import SimpleDirectoryReader
from lyzr_rag.readers.file.docs_reader import PDFReader
from lyzr_rag.readers.file.html_reader import HTMLTagReader
from lyzr_rag.readers.github_readers.github_repository_reader import (
    GithubRepositoryReader,
)
from lyzr_rag.readers.google_readers.gdocs import GoogleDocsReader
from lyzr_rag.readers.json import JSONReader
from lyzr_rag.readers.make_com.wrapper import MakeWrapper
from lyzr_rag.readers.mbox import MboxReader
from lyzr_rag.readers.metal import MetalReader
from lyzr_rag.readers.milvus import MilvusReader
from lyzr_rag.readers.mongo import SimpleMongoReader
from lyzr_rag.readers.myscale import MyScaleReader
from lyzr_rag.readers.notion import NotionPageReader
from lyzr_rag.readers.obsidian import ObsidianReader
from lyzr_rag.readers.pathway import PathwayReader
from lyzr_rag.readers.pinecone import PineconeReader
from lyzr_rag.readers.psychic import PsychicReader
from lyzr_rag.readers.qdrant import QdrantReader
from lyzr_rag.readers.slack import SlackReader
from lyzr_rag.readers.steamship.file_reader import SteamshipFileReader
from lyzr_rag.readers.string_iterable import StringIterableReader
from lyzr_rag.readers.twitter import TwitterTweetReader
from lyzr_rag.readers.txtai import TxtaiReader
from lyzr_rag.readers.weaviate.reader import WeaviateReader
from lyzr_rag.readers.web import (
    BeautifulSoupWebReader,
    RssReader,
    SimpleWebPageReader,
    TrafilaturaWebReader,
)
from lyzr_rag.readers.wikipedia import WikipediaReader
from lyzr_rag.readers.youtube_transcript import YoutubeTranscriptReader
from lyzr_rag.schema import Document

__all__ = [
    "WikipediaReader",
    "YoutubeTranscriptReader",
    "SimpleDirectoryReader",
    "JSONReader",
    "SimpleMongoReader",
    "NotionPageReader",
    "GoogleDocsReader",
    "MetalReader",
    "DiscordReader",
    "SlackReader",
    "WeaviateReader",
    "PathwayReader",
    "PineconeReader",
    "PsychicReader",
    "QdrantReader",
    "MilvusReader",
    "ChromaReader",
    "DeepLakeReader",
    "FaissReader",
    "TxtaiReader",
    "MyScaleReader",
    "Document",
    "StringIterableReader",
    "SimpleWebPageReader",
    "BeautifulSoupWebReader",
    "TrafilaturaWebReader",
    "RssReader",
    "MakeWrapper",
    "TwitterTweetReader",
    "ObsidianReader",
    "GithubRepositoryReader",
    "MboxReader",
    "ElasticsearchReader",
    "SteamshipFileReader",
    "ChatGPTRetrievalPluginReader",
    "BagelReader",
    "HTMLTagReader",
    "ReaderConfig",
    "PDFReader",
    "DashVectorReader",
    "download_loader",
]
