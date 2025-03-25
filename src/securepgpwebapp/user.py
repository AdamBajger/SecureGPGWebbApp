from dataclasses import dataclass
from typing import TypeAlias
from starlette import html_encode
from abc import ABC, abstractmethod

from pathlib import Path
from src import ROOT_DIR

UUID: TypeAlias = str


DEFAULT_IMG = ROOT_DIR / "media" / "DEFAULT_IMG.png"

CSS_CLASSES_ENTRY = "entry"



class User(dataclass):
    id: UUID
    username: str
    email: str
    call_me: list[str]
    phone: str | None




def validate_for_html(text: str):
    """This method makes sure the presented text is HTML safe and the content cannot hack the internet lol"""
    pass


class HTML_renderable(ABC, dataclass):
    """This class represents an HTML renderable class that encapsulates osme form of safe HTML content"""
    @abstractmethod
    def get_html_entry(self):
        pass

class Paragraph(HTML_renderable):
    content: str

    def get_html_entry(self):
        return f"""<p>
            {validate_for_html(self.content)}
        <p>"""


    def __str__(self):
        return validate_for_html(self.content)
    
    def __repr__(self):
        return validate_for_html(self.content)

class Img(HTML_renderable):
    path_to_image: Path

    def __init__(self, path_to_image: str):
        """Checks if the path exists and """

    def get_html_entry(self):
        return f"""<img src="{self.path_to_image.as_posix}"</img""" if self.path_to_image is not None else 


class Video(HTML_renderable):
    def get_html_entry(self):
        return "<p> Video is not yet implemented for this web</p>"



class Post(HTML_renderable):
    id: UUID
    content: list[Paragraph, Img,  Video] | str

    def get_html_entry(self):
        if isinstance(self.content, str):
            return self.content
        else:
            return "".join([f'<div class="{CSS_CLASSES_ENTRY}">{entry.get_html_entry()}</div>' 
                            for entry in self.content])
        


