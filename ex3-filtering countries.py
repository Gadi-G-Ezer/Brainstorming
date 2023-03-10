PREFIX = {'i', 'f'}
SUFFIX = {'D', 'M'}

"""
filtered_world_map:
function returns a corrected list – where every country’s name begins with an uppercase letter, and the remaining 
letters are lowercase, and filters irrelevant countries. name is considered to be a country name id it either  begin 
with ‘i’ or ‘f’, or end with ‘d’ or ‘m’. 
"""

filtered_world_map = lambda string_list: list(filter(lambda a_str: a_str[0] in PREFIX or a_str[0].lower() in PREFIX or
                                                                   a_str[-1] in SUFFIX or a_str[-1].upper() in SUFFIX,
                                                     map(lambda a_string: a_string.title(), string_list)))

assert filtered_world_map(['ISRAEL', 'france', 'engLand', 'Brazil']) == ['Israel', 'France', 'England']