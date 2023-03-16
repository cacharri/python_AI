# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ialvarez <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 18:53:31 by ialvarez          #+#    #+#              #
#    Updated: 2023/03/15 20:19:08 by ialvarez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) < 2:
    print("AssertionError: you need to provide one argument")
elif len(sys.argv) > 2:
        print("AssertionError: more than one argument are provided")
else:
    if sys.argv[1].isdigit() == False:
        print('AssertionError: argument is not an integer')
    elif int(sys.argv[1]) == 0:
        print('I´m Zero.')
    elif int(sys.argv[1]) % 2 == 0:
        print("I´m Even.")
    elif int(sys.argv[1]) % 2 != 0:
        print("I´m Odd.")
