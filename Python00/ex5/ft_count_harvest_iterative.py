# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: doabrour <doabrour@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/18 13:01:21 by doabrour          #+#    #+#              #
#    Updated: 2026/02/18 13:06:39 by doabrour         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_count_harvest_iterative():
	count = int(input("Days until harvest: "))
	i = 1
	while count >= i:
		print("Day", i)
		i += 1
	print("Harvest time!")
ft_count_harvest_iterative()