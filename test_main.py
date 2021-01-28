from main import add

def TestAdd():
	assert add(2,3) == 5
	assert add(1,1) == 1
	assert add(2,2) == 4
	print("Test Running")

if __name__ == '__main__':
	TestAdd()


