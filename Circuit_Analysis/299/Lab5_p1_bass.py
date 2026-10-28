import math

R1 = 4000
R2 = 10000
alpha0 = 0
alpha1 = 1
C1 = 0.000000047
C2 = 0.0000000033
Ct = C1 + C2


omega_n0 = (R1 + alpha0*R2)/(R1*R2*Ct) 
omega_d0 = (R1 + (1-alpha0)*R2)/(R1*R2*Ct)
omega_n1 = (R1 + alpha1*R2)/(R1*R2*Ct) 
omega_d1 = (R1 + (1-alpha1)*R2)/(R1*R2*Ct)

#alpha = 0
H1 = omega_n0/omega_d0    
H2 = omega_d0/omega_n0    

#alpha = 0
H3 = omega_n1/omega_d1
H4 = omega_d1/omega_n1

result1 = 20*math.log(H1, 10)
result2 = 20*math.log(H2, 10)


print(f"Omega N: {omega_n0}")
print(f"Omega D: {omega_d0}\n")
print(f"H(jomega), alpha = 0: {H1}")
print(f"H(jomega), alpha = 1: {H2}\n")
print(f"H(jomega)|dB, alpha = 0: {result1}")
print(f"H(jomega)|dB, alpha = 1: {result2}")

