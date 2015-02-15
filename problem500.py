product = 1
for n in range(1, 500502):
    product = product * n;
    if (product > 500500507):
        product = product % 500500507
        
    print n, product
    
print product
