# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: doabrour <doabrour@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/18 12:12:19 by doabrour          #+#    #+#              #
#    Updated: 2026/02/18 12:37:52 by doabrour         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_plant_age():
	age = int(input("Enter plant age in days: "))
	if (age > 60):
		print("Plant is ready to harvest!")
	else:
		print("Plant needs more time to grow.")
ft_plant_age()