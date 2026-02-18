# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: doabrour <doabrour@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/18 13:07:20 by doabrour          #+#    #+#              #
#    Updated: 2026/02/18 15:19:43 by doabrour         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive(days: int, day: int = 1) -> None:
	if day > days:
		print("Harvest time!")
		return
	print(f"Day {day}")
	ft_count_harvest_recursive(days, day + 1)