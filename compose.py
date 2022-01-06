def get_words_from_text(text_path):
    with open(text_path, 'r') as f:
        text = f.read()
        text = ' '.join(text.split())  # whitespaces to spaces


def main():
    """
    1:get words from text
    2:make agraph using those words
    3:get the next word for x number of words (defined by user)
    4:show the user!
    :return:
    """
    pass
