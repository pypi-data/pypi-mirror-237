import pytest

from codesnipper.codesnipper import Code, CodeSnipper  # pyright: ignore

TEST_CASES = [
    # no code section, single line
    "hello world",
    # no code section, multi lines
    """
    hello world
    this test case does
    not have any code section
    """,
    # with only one code section, single line
    "```x=1```",
    # with only one code section, multi line
    """
    hell world
    ```
    x = 1
    y = list(1)
    ```
    """,
    # with only one code section, multi line, language
    """
    hell world
    ```python
    x = 1
    y = list(1)
    ```
    """,
    # with two code sections
    """
    hello world
    ```python
    x = 1
    y = dict(1,2)
    ```
    This is not a code section
    ```r
    x <- 1
    y <- 2
    ```
    Last line to end
    """,
]

EXPECTED_CODE = [
    [None],
    [None],
    ["x=1"],
    [
        """
    x = 1
    y = list(1)
    """
    ],
    [
        """
    x = 1
    y = list(1)
    """
    ],
    [
        """
    x = 1
    y = dict(1,2)
    """,
        """
    x <- 1
    y <- 2
    """,
    ],
]

EXPECTED_LANGUAGE = [[None], [None], [None], [None], ["python"], ["python", "r"]]


class TestCodeSnipper:
    @pytest.mark.parametrize(
        "test_value, expected_value",
        [(test_case, result) for test_case, result in zip(TEST_CASES, [0, 0, 1, 1, 1, 2])],
    )
    def test_code_sections(self, test_value, expected_value):
        # test the length of matches
        snipper = CodeSnipper(test_value)
        assert len(snipper._code_sections()) == expected_value

    @pytest.mark.parametrize(
        "test_value, expected_code, expected_language",
        [(val, code, lang) for val, code, lang in zip(TEST_CASES, EXPECTED_CODE, EXPECTED_LANGUAGE)],
    )
    def test_parse_code_sections(self, test_value, expected_code, expected_language):
        snipper = CodeSnipper(test_value)
        matches = snipper._code_sections()
        codes = snipper._parse_code_sections(matches=matches)
        assert isinstance(codes, list)

        if codes:
            assert isinstance(codes[0], Code)

            for c, e, lang in zip(codes, expected_code, expected_language):
                if lang is None:
                    assert c.language is None
                else:
                    assert c.language == lang.strip()
                if e is None:
                    assert c.code is None
                else:
                    assert c.code == e.strip()

    def test_both_params_provided(self):
        with pytest.raises(ValueError):
            CodeSnipper("test string", "test filepath")

    def test_none_params_provided(self):
        with pytest.raises(ValueError):
            CodeSnipper()
