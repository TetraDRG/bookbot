def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_char_count(char_count):
    sorted_char_list = sorted(
        [{'character': char, 'count': count} for char, count in char_count.items() if char.isalpha()],
        key=lambda x: x['count'],
        reverse=True
    )
    return sorted_char_list
