months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

def month_2nd_letter(month):
    """Should take in a month, in the range 1-12, 
    and return the character that is the second letter
    in its English name."""
    if 1 <= month <= 12:
        english_name = months[month]
        return english_name[1]
    return ""