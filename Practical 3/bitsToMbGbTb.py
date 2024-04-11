def convertBitsToMB(bits):
    mb = bits / (8 * 1024 * 1024)
    return mb
    
def convertBitsToGB(bits):
    gb = bits / (8 * 1024 * 1024 * 1024)
    return gb
    
def convertBitsToTB(bits):
    tb = bits / (8 * 1024 * 1024 * 1024 * 1024)
    return tb

bits = float(input("Enter bits to convert: "))
if bits < 0:
    print("Enter proper value")
else:
    mb = convertBitsToMB(bits)
    gb = convertBitsToGB(bits)
    tb = convertBitsToTB(bits)
    print(f"{bits:.2f} bits is equal to {mb:.2f} MB, {gb:.2f} GB, {tb:.2f} TB")
