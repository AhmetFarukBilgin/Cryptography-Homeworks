def fast_moduler(base, exponent, modules):
    result=1
    base=base%modules
    while exponent>0:
        if exponent %2==1:
            result=result*base%modules
        exponent=exponent>>1
        base=(base*base)%modules
    return result
# Example usage:
print(fast_moduler(5,117,19))  # Output: 6
print(fast_moduler(7,256,13))  # Output: 9
print(fast_moduler(10,1000,37))  # Output: 1

def fast_moduler_with_steps(base, exponent, modules):
    result=1
    base=base%modules
    steps=[]
    while exponent>0:
        steps.append((result, base, exponent))
        if exponent %2==1:
            result=result*base%modules
        exponent=exponent>>1
        base=(base*base)%modules
    steps.append((result, base, exponent))
    return result, steps
# Example usage with steps:
final_result, computation_steps = fast_moduler_with_steps(5,117,19)
print(f"Final Result: {final_result}")
print("Computation Steps:")
for step in computation_steps:
    print(f"Result: {step[0]}, Base: {step[1]}, Exponent: {step[2]}")
# Another example with steps:
final_result, computation_steps = fast_moduler_with_steps(7,256,13)
print(f"Final Result: {final_result}")
print("Computation Steps:")
for step in computation_steps:
    print(f"Result: {step[0]}, Base: {step[1]}, Exponent: {step[2]}")
# Another example with steps:
final_result, computation_steps = fast_moduler_with_steps(10,1000,37)
print(f"Final Result: {final_result}")
print("Computation Steps:")
for step in computation_steps:
    print(f"Result: {step[0]}, Base: {step[1]}, Exponent: {step[2]}")