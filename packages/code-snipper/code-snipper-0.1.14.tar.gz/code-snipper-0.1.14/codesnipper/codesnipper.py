import re
from dataclasses import dataclass
from typing import Any, List, Union

from pydantic import validate_call


@dataclass
class Code:
    """
    Dataclass representing code object with attribute `language` and `code`

    Attributes:
        code: The code text
        language: the programming language. The programming language is guessed
        based on the text after first triple backticks.
    """

    code: Union[str, None]
    language: Union[str, None]


class CodeSnipper:
    @validate_call
    def __init__(self, text: Union[str, None] = None, file_path: Union[str, None] = None):
        """Reads for code snippets within a text. A section is considered a code snippet if
        it's text is enclosed in triple backticks.

        Args:
            text: text to check code in
            file_path: filepath from where to read the text

        Raises:
            ValueError: If both `text` and `file_path` are provided
            ValueError: If none of `text` and `file_path` are provided
        """
        self.text = text
        self.file_path = file_path

        if self.text is None:
            if self.file_path is not None:
                with open(self.file_path) as file:
                    self.text = file.read()
            else:
                raise ValueError("both `text` and `file_path` cannot be `None`. At least one is required")
        else:
            if self.file_path is not None:
                raise ValueError("both text and file_path are provided. Only one is required")

    def _code_sections(self, pattern: str = "(?<=```)(.*?)(?=```)") -> List[Any]:
        matches = re.findall(pattern, self.text, flags=re.S)  # type: ignore
        codes = []
        for i in range(0, len(matches), 2):
            codes.append(matches[i])
        return codes

    def _parse_code_sections(self, matches: List[Any]) -> List[Code]:
        codes = []
        for match in matches:
            if match:
                language = re.search(r"^ *\w*?\n", match, re.S)
                if language is not None:
                    language = language.group(0).strip()
                    code = re.sub(language, "", match, 1).strip()
                else:
                    code = match.strip()
                if not language:
                    language = None
                c = Code(code=code, language=language)
                codes.append(c)
        return codes

    def codes(self) -> List[Code]:
        sections = self._parse_code_sections(self._code_sections())
        return sections
