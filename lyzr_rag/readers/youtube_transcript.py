"""Simple Reader that reads transcript of youtube video."""

from typing import Any, List

from lyzr_rag.readers.base import BasePydanticReader
from lyzr_rag.schema import Document


class YoutubeTranscriptReader(BasePydanticReader):
    """Youtube Transcript reader."""

    is_remote: bool = True
    languages: tuple = ("en",)

    @classmethod
    def class_name(cls) -> str:
        return "YoutubeTranscriptReader"

    @staticmethod
    def _get_video_id(link: str) -> str:
        if "youtu.be" in link: # link is youtu.be/<video_id> variant
            route = link.split("youtu.be/")[1]
            id = route.split("?si=")[0]
            return id
        else: # link is youtube.com/watch?v=<video_id> variant 
            id = link.split("?v=")[-1]
            return id


    def load_data(self, ytlinks: List[str], **load_kwargs: Any) -> List[Document]:
        """Load data from the input links.

        Args:
            pages (List[str]): List of youtube links \
                for which transcripts are to be read.

        """
        try:
            from youtube_transcript_api import YouTubeTranscriptApi
        except ImportError:
            raise ImportError(
                "`youtube_transcript_api` package not found, \
                    please run `pip install youtube-transcript-api`"
            )

        results = []
        for link in ytlinks:
            video_id = YoutubeTranscriptReader._get_video_id(link)
            srt = YouTubeTranscriptApi.get_transcript(
                video_id, languages=self.languages
            )
            transcript = ""
            for chunk in srt:
                transcript = transcript + chunk["text"] + "\n"
            results.append(Document(text=transcript, id_=video_id))
        return results
