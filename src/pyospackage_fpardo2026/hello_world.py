"""
A module to learn how to make a package
so it contains a version of hello world

"""

def hello_world(language):
    """
    Return "hello world" in the specified language.

    Parameters
    ----------
    language : str
        One of: 'spanish', 'english', 'portuguese'

    Returns
    -------
    str
        Translated "hello world"

    Raises
    ------
    TypeError
        If language is not a string
    ValueError
        If language is not supported
    """

    # --- Type check ---
    if not isinstance(language, str):
        raise TypeError(f"language must be a string, got {type(language).__name__}")

    # --- Normalize input ---
    language = language.strip().lower()

    # --- Mapping (safer than chained if/elif) ---
    translations = {
        "spanish": "hola mundo",
        "english": "hello world",
        "portuguese": "oi mundo",
    }

    # --- Validate value ---
    if language not in translations:
        valid = ", ".join(translations.keys())
        raise ValueError(f"Unsupported language '{language}'. Choose from: {valid}")

    return translations[language]