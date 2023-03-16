# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ialvarez <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/16 19:39:57 by ialvarez          #+#    #+#              #
#    Updated: 2023/03/16 19:53:08 by ialvarez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

for key, value in kata.items():
    print("{} was created by {}".format(key, value))
