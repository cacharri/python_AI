# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ialvarez <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/16 16:21:46 by ialvarez          #+#    #+#              #
#    Updated: 2023/03/16 19:38:41 by ialvarez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) > 3:
    print("AssertionError: too many arguments")
elif len(sys.argv) < 2:
    print("Usage: python operations.py <number1> <number2>\nExample:\n  python operations.py 10 3")
elif len(sys.argv) == 2:
    print("AssertionError: too few argument")
elif sys.argv[1].isdigit() == False:
    print("AssertionError: only integers")
elif sys.argv[2].isdigit() == False:
    print("AssertionError: only integers")
else:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    if len(sys.argv) == 3:
        print("Sum          ",x+y)
        print("Difference:  ",x-y)
        print("Product:     ",x*y)
        if y == 0:
            print("Quotient:     ERROR (division by zero)")
        else:
            print("Quotient:    ",x/y)
        if y == 0:
            print("Quotient:     ERROR (modulo by zero)")
        else:
            print("Remainder:   ",x%y)
