import math


# Process parameters
Kn = 256e-6/2
Kp = 58e-6/2
Vtn = [0.53, 0.56]
Vtp = [0.67, 0.73]

# Design parameters
CL = 3.43e-12
Vdd = 1.8
GB = 5e6
SR = 1/1e-6
PM = 60
ICMR = [1.3]

# 1
Cc = math.ceil(0.22*CL*1e12)*1e-12

# 2
I5 = SR*Cc
I1 = I5/2
I2 = I1

# 3
S3 = math.ceil(I5/(Kp*(Vdd - max(ICMR) - max(Vtp) + min(Vtn))**2))
S4 = S3

# 5
gm1 = GB*2*math.pi*Cc
S1 = math.ceil(gm1**2/(Kn*I5))
S2 = S1

# 6
Vds5 = min(ICMR) - math.sqrt(I5/(Kn*S1)) - max(Vtn)
S5 = math.ceil(2*I5/(Kn*Vds5**2))

# 7
# para margen de fase 60, es gm6>10*gm1
gm6 = 10 * gm1
gm4 = math.sqrt(I5 * Kp * S4)
S6 = math.ceil(S4 * gm6/gm4)

# 8
I6 = gm6**2/(2*Kp*S6)

# 9
S7 = math.ceil(S5 * I6/I5)

print(f"Cc: {Cc}")
print(f"S1: {S1}")
print(f"S2: {S2}")
print(f"S3: {S3}")
print(f"S4: {S4}")
print(f"S5: {S5}")
print(f"S6: {S6}")
print(f"S7: {S7}")
