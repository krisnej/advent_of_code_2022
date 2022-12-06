def get_packet_marker():
    with open("input.txt") as f:
        content = f.read()
    r = len(content)
    for i in range(4, r + 1):
        snippet = content[i - 4 : i]
        sorted_snippet_str = "".join(sorted(snippet))
        sorted_set_str = "".join(sorted(set(snippet)))
        if sorted_snippet_str == sorted_set_str:
            return i


def get_message_marker():
    with open("input.txt") as f:
        content = f.read()
    r = len(content)
    for i in range(14, r + 1):
        snippet = content[i - 14 : i]
        sorted_snippet_str = "".join(sorted(snippet))
        sorted_set_str = "".join(sorted(set(snippet)))
        if sorted_snippet_str == sorted_set_str:
            return i


if __name__ == "__main__":
    print(get_packet_marker())
    print(get_message_marker())
