# simple fizz buzz program.
# print 'fizz' if it divided by 3
# print 'buzz' if it divided by 5
# print 'fizzbuzz' if it divided by both 3 and 5
print(''.join(['FizzBuzz ' if not (i%3 or i%5) else 'Fizz ' if not(i%3) else 'Buzz ' if not(i%5) else str(i) + ' ' for i in range(1, int(input("Enter no for test(1-): ")))]))