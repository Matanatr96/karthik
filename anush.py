import karthik
import sys

print ('argument list', sys.argv)
first = int(sys.argv[1])
second = str(sys.argv[2])

print(f"Hello {second}")
new_value = karthik.multiply_by2(first)
print(new_value)