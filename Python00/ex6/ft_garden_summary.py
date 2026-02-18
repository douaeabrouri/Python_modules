# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_summary.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: doabrour <doabrour@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/18 13:26:23 by doabrour          #+#    #+#              #
#    Updated: 2026/02/18 13:31:00 by doabrour         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_garden_summary():
	name = str(input("Enter garden name: "))
	number_plants = int(input("Enter number of plants: "))
	print("Garden: ",name)
	print("Plants: ",number_plants)
	print("Status: Growing well!")
ft_garden_summary()