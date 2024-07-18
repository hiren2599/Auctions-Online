from django import template
from ..models import User
from django.utils import timezone

register = template.Library()

@register.filter(name='search')
def search(value, id):
    """
    Linear search of a list

    Parameters
    ----------
    value : list
        A list with key values
    id : int
        The key we are searching
    
    Returns
    ------
    boolean
        True if the key is found, False otherwise.
    """
    for v in value:
        if v.id == id:
            return True
    
    return False

@register.filter(name="time_left")
def time_left(value):
    """
    Calculates the remaining time by
    subtracting the deadline with the 
    current time and converts it to 
    string with {minutes}m {seconds}s
    format. 

    Parameters
    ----------
    value : DateTime
        The deadline
    
    Returns
    ------
    string
        Remaining time in minutes and seconds
    """
    t = value - timezone.now()
    dateString = ""
    days = t.days
    if(days>0):
        dateString = dateString + str(days) + "D "
    
    seconds = t.seconds
    hours = seconds // (60*60)
    seconds = seconds % (60*60)
    if(hours>0 or len(dateString) != 0):
        dateString = dateString + str(hours) + "h "

    mintues = seconds // 60
    seconds = seconds % 60
    if(mintues>0 or len(dateString) != 0):
        dateString = dateString + str(mintues) + "m "
    if(seconds>0 or len(dateString) != 0):
        dateString = dateString + str(seconds) + "s "

    return dateString