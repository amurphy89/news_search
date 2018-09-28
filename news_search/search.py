import os


def search(search_type, terms):

    data = ""
    data_location = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), "data.txt")
    results = []

    with open(data_location, "r") as f:
        data = f.read()
        data = data.split("\n")

        for idx, val in enumerate(data):
            search_type = search_type.lower()
            if search_type == "or":
                if any(x in val for x in terms):
                    results.append(idx)
            elif search_type == "and":
                if all(x in val for x in terms):
                    results.append(idx)

    return results
