target = test
deps = LeetCodeTest.h
obj = 344_ReverseString.o LeetCodeTest.o

cc = g++
CFLAG = -std=c++11

$(target): $(obj)
	$(cc) $(CFLAG) -o $(target) $(obj)

%.o: %.cpp $(deps)
	$(cc) $(CFLAG) -c $< -o $@

.PHONY:clean
clean:
	rm -rf $(obj) $(target) *.o
