# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: doabrour <doabrour@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/18 12:08:37 by doabrour          #+#    #+#              #
#    Updated: 2026/02/18 12:11:32 by doabrour         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_harvest_total():
	day1 = int(input("Day 1 harvest: "))
	day2 = int(input("Day 2 harvest: "))
	day3 = int(input("Day 3 harvest: "))
	print("Total harvest:",day1+day2+day3)
ft_harvest_total()