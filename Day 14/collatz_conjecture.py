def collatz_sequence(x):
    seq = [x]
    if x < 1:
       return []
    while x > 1:
       if x % 2 == 0: # if even divided by 2.
         x = x / 2
       else: # else multiply by 3 and add 1.
         x = 3 * x + 1 
       seq.append(x)
    return seq # until last item is 1.

print(collatz_sequence(int(input("Enter number for test collatz squence: "))))
