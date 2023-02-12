# Nested function calls work much the same as in other languages where innermost functions are
# resolved first. With the return values being the argument passed to the following outer function

# The input is resolved first, following the float, then the abs function, then round
print(round(abs(float(input("Enter a whole negative number please: ")))))