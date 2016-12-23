
arr = [100, 34, -35, 56, 29, 90, 342, 532]

def find_max(array):
	max_item = max(array)
	return max_item

def find_min(array):
	min_item = min(array)
	return min_item

def get_sum(array):
	return sum(array)

def convert_to_hex(array):
	new_list = []
	for i in range(0, len(array)):
		new_list.insert(i, hex(array[i]))
	return new_list

def pow_array(array):
	new_list = []
	for i in range(0, len(array)):
		new_list.insert(i, pow(array[i], 2))
	return new_list
	
def compare_to_number(array, number):
	new_list = []
	for i in range(0, len(array)):
		new_list.insert(i, cmp(array[i], number))
	return new_list		
			

print("Max element is: ", find_max(arr))
print("Min element is: ", find_min(arr))
print("Sum of all element is: ",  get_sum(arr))
print("Hex value of each element is: ", convert_to_hex(arr))
print("Power 2 of each element is: ", pow_array(arr))
print("Compare each element with 90: ", compare_to_number(arr, 90))
