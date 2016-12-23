# Nguyen ly ke thua, reuse method, overriding method,... giong Java

class Parent():
	def __init__(self, last_name, eye_color):
		print("Parent constructor called")
		self.last_name = last_name
		self.eye_color = eye_color
		
	def show_info(self):
		print("Last name: " + self.last_name)
		print("Eye color: " + self.eye_color)	

class Child(Parent):	# mean: Child extends Parent
	def __init__(self, last_name, eye_color, number_of_toys):
		print("Child constructor called!")
		Parent.__init__(self, last_name, eye_color)
		self.number_of_toys = number_of_toys
		
	def show_info(self):
		Parent.show_info(self)
		print("Number of toys: " + str(self.number_of_toys))	

hung = Parent("Hung", "blue")
hung.show_info()
print(hung.last_name)

thieu = Child("Thieu", "White", 10)
print(thieu.last_name)
print(thieu.number_of_toys)
thieu.show_info()
