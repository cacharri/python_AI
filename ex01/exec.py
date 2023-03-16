# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ialvarez <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 17:53:03 by ialvarez          #+#    #+#              #
#    Updated: 2023/03/15 20:17:43 by ialvarez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse

def invert(string):
    return string[::-1].swapcase()

def swap_string(args):
    if not args:
        return "El programa requiere un argumento de tipo string"        
    return invert(' '.join(args))

parser = argparse.ArgumentParser(prog='INVERSOR DE LETRAS' ,description='Invertir mayúsculas y minusculas.', epilog='Juega')
parser.add_argument('string', metavar='string', type=str, nargs='+', help='Es el string que se esta procesando')

args = parser.parse_args()
print(swap_string(args.string))
