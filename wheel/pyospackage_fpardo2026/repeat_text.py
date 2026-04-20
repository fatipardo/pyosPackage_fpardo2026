"""Learning to create a new module
This module repeats text by the number of times
the user inputs"""

def repeat_text(text, times):
    """
    This function will repeat certain text as many
    times as the user requests.
    
    Parameters
    ----------
    
    text : str
        the text that will be repeated
    times: int
        the number of times the text will be repeated
        
    Returns
    --------
    string
        A string containing the text input by users
        repeated as many times as user requested.
        
    Examples
    --------
    >>> repeat_text("abc",3)
    abcabcabc
    >>> repeat_text("text",2)
    texttext
    """
    return text*times 