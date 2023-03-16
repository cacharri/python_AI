# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ialvarez <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 20:21:19 by ialvarez          #+#    #+#              #
#    Updated: 2023/03/16 16:20:28 by ialvarez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def text_analyzer(text=None):
    """
    This function analyzes a given text and counts the number of upper case characters, lower case characters, punctuation marks and spaces in a given text.
    """
    if text is None:
        text = input("Please enter a text to analyze: ")
    if not isinstance(text, str):
        print("AssertionError: argument is not a string")
        return

    upper_count = 0
    lower_count = 0
    punc_count = 0
    space_count = 0

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isspace():
            space_count += 1
        elif char in [',', '.', '!', '?', ':', ';']:
            punc_count += 1

    print(f"The text contains {len(text)} character(s):")
    print(f"- {upper_count} upper letter(s)")
    print(f"- {lower_count} lower letter(s)")
    print(f"- {punc_count} punctuation mark(s)")
    print(f"- {space_count} space(s)")

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 2:
        print("AssertionError: more than one argument")
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else :
        text_analyzer()
