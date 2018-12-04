def main():
    """
    CP1404/CP5632 Practical
    check the number of words in a sentence
    """
    text = str(input("Sentence: "))
    print("text: {}".format(text))
    text_dict = {}
    text_list = text.split()
    text_list.sort()
    for text in text_list:
        if text in text_dict:
            text_dict[text] += 1
        else:
            text_dict[text] = 1
        # for text2 in text_dict:
        #     if text_list[text] == text_dict[text2]:
        #         text_dict[text2] += 1
        #     else:
        #         text_dict[text_list[text]] += 1
    for text in text_dict:
        print(text, ":", text_dict[text])

main()