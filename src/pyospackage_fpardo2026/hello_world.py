"""
A module to learn how to make a package
so it contains a version of hello world

"""

def hello_world(language):
    """
    Prints "hello world" in the language specified.
    Options are spanish, english, portuguese.

    Parameters
    ----------
    language: string
        spanish, english, portuguese
    

    Returns
    -------
    str
        string "hello wold" in language specified by user

    Examples
    --------
    >>> hello_world(english)
    hello world
    >>> add_numbers(spanish)
    hola mundo
    """

    hello=""
    
    if language == "spanish":
        hello="hola mundo"
    elif language== "english":
        hello="hello world"
    elif language == "portuguese":
        hello="oi mundo"
    else:
        hello="I do not understand, try another language"
    
    print(hello)
    return hello