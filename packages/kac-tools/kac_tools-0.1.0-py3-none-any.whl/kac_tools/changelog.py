"""Changelog class that represents the model of a provided CHANGELOG file"""
import json
from pathlib import PurePath
from collections import OrderedDict


class Section:
    """Section class representing a single changelog section."""
    def __init__(self, section_string: str):
        section_split = section_string.split("\n", 1)
        if len(section_split) == 2:
            self.title, self.content = section_split
        else:
            self.title = section_split[0]
            self.content = None

        if " - " in self.title:
            self.title, self.date = self.title.split(" - ")
        else:
            self.date = None

    def __repr__(self) -> str:
        if self.date:
            return f"{self.title} - {self.date}\n{self.content}"
        return f"{self.title}\n{self.content}"

    def to_json(self) -> str:
        """Read content section in json format

        Returns:
            json (str): String containing the content of the section in json format.
        """
        return json.dumps({"title": self.title, "date": self.date, "content": self.content})

class Changelog:
    """Changelog class representing changelog composed of multiple sections."""
    def __init__(self, path: PurePath):
        self.path = path
        self.content = self.read_content()
        self.sections = self.parse_sections()

    def __getitem__(self, title):
        if title == "latest":
            return next(x for x in self.sections.values() if x.title != "Unreleased")

        if title not in self.sections:
            return None

        return self.sections[title]

    def read_content(self) -> str:
        """Read content of file in self.path

        Returns:
            content (str): String containing the content of the changelog file.
        """
        with open(self.path, "r", encoding="utf-8") as file:
            content = file.read()
        return content

    def parse_sections(self) -> OrderedDict:
        """Parse sections from self.content

        Returns:
            section_dict (OrderedDict): Dict containing Section objects with their titles as keys.
        """
        section_dict = OrderedDict()
        section_string_list = self.content.split("\n## ")
        for section_string in section_string_list[1:]:
            section = Section(section_string)
            section_dict[section.title] = section
        return section_dict
