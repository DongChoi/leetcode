# You can't skip past the end of a string
# You can't delete past the end of a string
# Delete operations are applied forward while keeping the cursor in place


def isValid(stale, latest, otjson):
    # loop through the json object and get the operation to feed it to the correct function
    curr_count = 0
    if stale == latest and otjson == []:
        print(True)
        return True

    for ops in otjson:
        if ops["op"] == "skip":
            curr_count = skip(stale, curr_count, ops["count"])
        elif ops["op"] == "delete":
            stale = delete(stale, curr_count, ops["count"])
        elif ops["op"] == "insert":
            res = insert(stale, curr_count, ops["chars"])
            stale, curr_count = res[0], res[1]
        if curr_count == "False" or stale == False:
            print(False)
            return False
    if stale == latest:
        print(True)
        return True
    else:
        print(False)
        return False


"""changes curr_count to curr_count+count and checks if it goes past the length"""


def skip(stale, curr_count, count):
    # skips and updates count
    if (curr_count + count) > len(stale):
        return "False"
    else:
        return curr_count + count


"""deletes curr_c to delete_c + curr_c"""


def delete(stale, curr_count, delete_count):
    if curr_count + delete_count > len(stale):
        return False
    else:
        end_index = curr_count + delete_count
        modified_text = stale[:curr_count] + stale[end_index:]
    return modified_text


"""Inserts adds 0 to curr_c plus chars plus curr_c to end """


def insert(stale, curr_count, chars):
    new_stale = stale[:curr_count] + chars + stale[curr_count:]

    return [new_stale, curr_count + len(chars)]


# Dear recruitment team, for the sake of time, i just changed the string json into json but i know how to convert them via json.loads()
isValid(
    "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
    "Repl.it uses operational transformations.",
    [{"op": "skip", "count": 40}, {"op": "delete", "count": 47}],
)
# true

isValid(
    "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
    "Repl.it uses operational transformations.",
    [{"op": "skip", "count": 45}, {"op": "delete", "count": 47}],
)
# false, delete past end

isValid(
    "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
    "Repl.it uses operational transformations.",
    [
        {"op": "skip", "count": 40},
        {"op": "delete", "count": 47},
        {"op": "skip", "count": 2},
    ],
)
# false, skip past end

isValid(
    "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
    "We use operational transformations to keep everyone in a multiplayer repl in sync.",
    [
        {"op": "delete", "count": 7},
        {"op": "insert", "chars": "We"},
        {"op": "skip", "count": 4},
        {"op": "delete", "count": 1},
    ],
)
# true

isValid(
    "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
    "We can use operational transformations to keep everyone in a multiplayer repl in sync.",
    [
        {"op": "delete", "count": 7},
        {"op": "insert", "chars": "We"},
        {"op": "skip", "count": 4},
        {"op": "delete", "count": 1},
    ],
)
# false

isValid(
    "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
    "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
    [],
)
# true
