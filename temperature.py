1 #!/usr/bin/env python3
  2 N = 10
  3 sum = 0
  4 count = 0
  5 print("please input 10 numbers:")
  6 while count <N:
  7     number = float(input())
  8     sum = sum +number
  9     count = count + 1
 10 average = sum / N
 11 print("N = {}, Sum = {}".format(N,sum))
 12 print("Average = {:.2f}".format(average)) 