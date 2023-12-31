def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")

friends = [
    {"name":"Rolf Smith", "Age": 24},
    {"name":"Adam Wool", "Age": 30},
    {"name":"Anne Pun", "Age": 27}
]

def get_friend_name(friend):
    return friend["name"]


print(search(friends, "Rolf Smith", get_friend_name))