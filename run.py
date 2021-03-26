import time
from randomforest import predict_potential, recommend_player

print("Potential Predictor: 1 / Recommend Player: 2")
inp_number = input("Enter Number 1/2: ")
if inp_number == "1":
	print("*********Potential Predictor for Footballers************")
	name = input("Enter your name: ")
	if name == True:
		pass
	else:
		print("please enter your name.........")	
		name = input("Enter your name: ")

	position = input("What position do you play: ")
	age = input("Whats your age: ")
	stamina = input("Input your stamina(1-100): ") 
	strength = input("Input your strength(1-100): ") 
	spassing = input("Input your Short Passing(1-100): ") 
	lpassing = input("Input your Long Passing(1-100): ") 
	speed = input("Input your Speed(1-100): ") 
	finishing = input("Input your Finishing(1-100): ")

	data = [age, stamina,strength, spassing, lpassing, speed, finishing]


	print(f"Dude {name} you are a star fuckin {position} with an overall Potential of ")
	print(predict_potential(data))
	print("*******Thankyou************") 

elif inp_number == '2':
	print("*********Recommend Footballers************")
	player = input("Input Player Name: ")
	recommend_player(player)
	print("*******Thankyou************")
else:
	print("Enter Valid Number***Restart Again")
	print("*******Thankyou************")