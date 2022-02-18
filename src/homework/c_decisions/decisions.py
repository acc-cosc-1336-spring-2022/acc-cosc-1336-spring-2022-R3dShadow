
def get_options_ratio(options, total):
    ratio = options / total
    return ratio

def get_faculty_rating(ratio):
    if ratio > .9 and ratio <= 1:
        return "Excellent"
    if ratio > .8 and ratio <.9:
        return "Very Good"
    if ratio > .7 and ratio <.8:
        return "Good"
    if ratio > .6 and ratio <.7:
        return "Needs Improvement"
    if ratio > 0 and ratio <.6:
        return "Unacceptable"