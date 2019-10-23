target = test

deps = LeetCodeTest.h
obj = 344_ReverseString.o LeetCodeTest.o

CFLAG=-std=c++11
cc = g++

$(target): $(obj)
	$(cc) $(CFLAG) -o $(target) $(obj)

%.o: %.cpp $(deps)
	$(cc) $(CFLAG) -c $< -o $@

clean:
	rm -rf $(obj) $(target)
