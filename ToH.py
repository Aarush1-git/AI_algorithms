def ToH(n , src, aux, dest):
    if n == 1:
        print("Move disc 1 from", src, "to", dest)
        return
    ToH(n-1, src, dest, aux)
    print("Move disc", n, "from", src, "to", dest)
    ToH(n-1, aux, src, dest)

n = int(input("Enter the number of discs (n): "))
ToH(n, "A", "B", "C")
print("Total number of steps", 2**n - 1)