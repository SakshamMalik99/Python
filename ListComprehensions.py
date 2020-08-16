a, b, c, n = [int(raw_input()) for _ in xrange(4)]
print [[x,y,z] for x in xrange(a + 1) for y in xrange(b + 1) for z in xrange(c + 1) if x + y + z != n]