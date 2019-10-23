cc = g++
target = test

deps = LeetCodeTest.h
obj = 344_ReverseString.o LeetCodeTest.o

CFLAG=-std=c++11

$(target): $(obj)
	$(cc) $(CFLAG) -o $(target) $(obj)

%.o: %.cpp $(deps)
	$(cc) $(CFLAG) -c $< -o $@
