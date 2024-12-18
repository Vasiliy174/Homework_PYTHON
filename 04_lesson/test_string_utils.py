from stringutils import StringUtils


string_utils = StringUtils()


def test_capitilize():
    """Positive"""
    assert string_utils.capitilize("skypro") == "Skypro"
    assert string_utils.capitilize("hello, world") == "Hello, world"
    assert string_utils.capitilize("123") == "123"
    assert string_utils.capitilize("привет, мир") == "Привет, мир"


def test_trim():
    """Pozitive"""
    assert string_utils.trim("  Skypro") == "Skypro"
    assert string_utils.trim("  Мир, привет!") == "Мир, привет!"
    assert string_utils.trim("  174") == "174"


def test_to_list():
    """Pozitive"""
    assert string_utils.to_list("A,B,C,D") == ["A", "B", "C", "D"]
    assert string_utils.to_list("1:2:3", ":") == ["1", "2", "3"]


def test_contains():
    """Pozitiv"""


if string_utils.contains("SkyPro", "S") is True:
    if string_utils.contains("SkyPro", "U") is False:

        def test_delete_symbol():
            """Pozitive"""
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert string_utils.delete_symbol("Sky", "k") == "Sy"
    assert string_utils.delete_symbol("Puh", "u") == "Ph"


def test_starts_with():
    """Pozitiv"""


if string_utils.starts_with("SkyPro", "S") is True:

    def test_end_with():
        """Pozitiv"""
    if string_utils.end_with("Ogr", "r") is True:
        if string_utils.end_with("Ogr", "D") is False:

            def test_is_empty():
                """Pozitiv"""
    if string_utils.is_empty("") is True:
        if string_utils.is_empty(" ") is True:
            if string_utils.is_empty("007") is False:

                def test_list_to_string():
                    """Pozitiv"""
    assert string_utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert string_utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
    assert string_utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
