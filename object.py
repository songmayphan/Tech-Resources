class User:
	def log(self):
		print(self)



class Teacher(User):
	def __init__ (self, name, mem_type):
		#constructor
		self.name = name
		self.mem_type = mem_type 

	def log(self):
		print ("I am a teacher")

class Customer(User):  #class Customer inherit from class USER
	def __init__ (self, name, mem_type):
		#constructor
		self.name = name
		self.mem_type = mem_type 

	@property
	def name (self):
		return self._name 
	
	# private, not accesible outsire the class, includes any method begins with underscore

	@name.setter
	def name(self,name):
		self._name = name 


	@name.deleter
	def name(self):
		del self._name

	def upgrade(self, new_mem_type):
		self.mem_type = new_mem_type

	def __str__(self):
		
		return self.name + ", " + self.mem_type
	def print_all(customers):
		for customer in customers:
			print(customer)

	def __eq__(self, other):
		#check if two customers are euqla

		if self.mem_type == other.mem_type:
			return True
		return False


	__hash__ = None 
	#overide representationto print all the customers in a nice list
	__repr__ = __str__




customers = [Customer("May", "Gold"), Customer("Attican", "Bronze")]
teacher = Teacher("Dr. Pepper", "Gold")

customers[0].upgrade("Diamond")
customers[1].upgrade("Diamond")

Customer.print_all(customers)
# constructors can be overrided 

if customers[0] == customers[1]:
	print("Both customer have the same membership type of ", customers[0].mem_type)

else: 
	print("They don't have the same memtype")



#USERS: 

users  = [Customer("May", "Gold"), Customer("Attican", "Bronze"), Teacher("Dr. Pepper", "Gold") ]
for user in users: 
	user.log()


#del customer[0].name  > delete customer name attribute
# self is put into anyt method that works with individual customers

#params are defined
#arguments are specific values > invocation

#add attribute on the fly 

# customers[1].verified = True
# print(customers[1].verified)
