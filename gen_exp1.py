it = (len(x) for x in open('/tmp/my_file.txt'))
roots = ((x, x**0.5) for x in it)

print(next(roots))
print(next(roots))
print(next(roots))
