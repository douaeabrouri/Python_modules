# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: doabrour <doabrour@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/18 13:07:20 by doabrour          #+#    #+#              #
#    Updated: 2026/02/18 13:25:09 by doabrour         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive(days, i):
	if days < i:
		print("Harvest time!")
		return 
	print(f"Day {i}")
	ft_count_harvest_recursive(days, i + 1)
count = int(input("Days until harvest: "))
i = 1
ft_count_harvest_recursive(count, i)