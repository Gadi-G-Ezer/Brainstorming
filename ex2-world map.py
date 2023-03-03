"""
world_map:
returns a corrected list – where every country’s name begins with an uppercase letter, and the remaining letters are
lowercase, for instance: world_map([‘ISRAEL’, ‘france’, ‘engLand’]) == [‘Israel’, ‘France’, ‘England’] .
"""
world_map = lambda string_list: list(map(lambda element: element.title(), string_list))

assert world_map(['ISRAEL', 'france', 'engLand']) == ['Israel', 'France', 'England']
