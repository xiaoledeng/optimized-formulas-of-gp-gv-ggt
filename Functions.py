from math import cos,sin

def Function_cylindrical_prism_V(G,rho,r,lam,z,r0,lam0,z0,DeltaR,DeltaLam,DeltaZ):
   V = DeltaLam*DeltaR*DeltaZ*G*rho*(-DeltaLam**2*r*r0**2*(r*r0*(cos(2*lam \
      - 2*lam0) - 5) + 2*(r**2 + r0**2 + (z - z0)**2)*cos(lam - lam0)) \
      - 2*DeltaR**2*(r*(-2*r**2 + r*r0*cos(lam - lam0) - 2*r0**2 \
      - 2*(z - z0)**2)*cos(lam - lam0) + 3*r0*(r**2 + (z - z0)**2)) \
      - 2*DeltaZ**2*r0*(r**2 - 2*r*r0*cos(lam - lam0) + r0**2 \
      - 2*(z - z0)**2) + 48*r0*(r**2 - 2*r*r0*cos(lam - lam0) \
      + r0**2 + (z - z0)**2)**2)/(48*(r**2 - 2*r*r0*cos(lam - lam0) \
      + r0**2 + (z - z0)**2)**(5/2))
   return V

def Function_cylindrical_prism_Vr(G,rho,r,lam,z,r0,lam0,z0,DeltaR,DeltaLam,DeltaZ):
   Vr = DeltaLam*DeltaR*DeltaZ*G*rho*(-DeltaLam**2*r0**2*(-6*r*r0*(r**2 \
      - 2*r*r0*cos(lam - lam0) + r0**2 + (z - z0)**2)*sin(lam - lam0)**2 \
      - 3*r*(r - r0*cos(lam - lam0))*(-5*r*r0*sin(lam - lam0)**2 + (r**2 \
      - 2*r*r0*cos(lam - lam0) + r0**2 + (z - z0)**2)*cos(lam - lam0)) \
      + (r**2 - 2*r*r0*cos(lam - lam0) + r0**2 + (z - z0)**2)**2*cos(lam - lam0)) \
      + DeltaR**2*(3*r*r0*(3*r**2 - 2*r0**2 + 3*(z - z0)**2) + (-4*r**4 \
      - r**2*(5*r0**2 + 2*(z - z0)**2) + r*r0*(r**2 - r*r0*cos(lam - lam0) \
      + 4*r0**2 + 4*(z - z0)**2)*cos(lam - lam0) + 2*r0**4 - 11*r0**2*(z - z0)**2 \
      + 2*(z - z0)**4)*cos(lam - lam0)) + 3*DeltaZ**2*r0*(r \
      - r0*cos(lam - lam0))*(r**2 - 2*r*r0*cos(lam - lam0) \
      + (r0 - 2*z + 2*z0)*(r0 + 2*z - 2*z0)) - 24*r0*(r \
      - r0*cos(lam - lam0))*(r**2 - 2*r*r0*cos(lam - lam0) \
      + r0**2 + (z - z0)**2)**2)/(24*(r**2 - 2*r*r0*cos(lam - lam0) \
      + r0**2 + (z - z0)**2)**(7/2))
   return Vr

def Function_cylindrical_prism_Vlam(G,rho,r,lam,z,r0,lam0,z0,DeltaR,DeltaLam,DeltaZ):
   Vlam = DeltaLam*DeltaR*DeltaZ*G*rho*(DeltaLam**2*r0**2*(2*r**4 \
         + r**2*(-25*r0**2 + 4*(z - z0)**2) + r*r0*(r*r0*cos(2*lam - 2*lam0) \
         + 10*(r**2 + r0**2 + (z - z0)**2)*cos(lam - lam0)) + 2*(r0**2 \
         + (z - z0)**2)**2) - 2*DeltaR**2*(2*r**4 + r**2*(-11*r0**2 \
         + 4*(z - z0)**2) + r*r0*(4*r**2 - r*r0*cos(lam - lam0) \
         + 4*r0**2 + 4*(z - z0)**2)*cos(lam - lam0) + 2*r0**4 \
         - 11*r0**2*(z - z0)**2 + 2*(z - z0)**4) \
         + 6*DeltaZ**2*r0**2*(r**2 - 2*r*r0*cos(lam - lam0) \
         + (r0 - 2*z + 2*z0)*(r0 + 2*z - 2*z0)) \
         - 48*r0**2*(r**2 - 2*r*r0*cos(lam - lam0) + r0**2 \
         + (z - z0)**2)**2)*sin(lam - lam0)/(48*(r**2 - 2*r*r0*cos(lam - lam0) \
         + r0**2 + (z - z0)**2)**(7/2))

   return Vlam

def Function_cylindrical_prism_Vz(G,rho,r,lam,z,r0,lam0,z0,DeltaR,DeltaLam,DeltaZ):
   Vz = DeltaLam*DeltaR*DeltaZ*G*rho*(z - z0)*(DeltaLam**2*r*r0**2*(r*r0*(3*cos(2*lam \
         - 2*lam0) - 7) + 2*(r**2 + r0**2 + (z - z0)**2)*cos(lam - lam0)) \
         + 2*DeltaR**2*(-r*(2*r**2 + r*r0*cos(lam - lam0) \
         - 2*(r0 - z + z0)*(r0 + z - z0))*cos(lam - lam0) \
         + r0*(3*r**2 - 2*r0**2 + 3*(z - z0)**2)) \
         + 2*DeltaZ**2*r0*(3*r**2 - 6*r*r0*cos(lam - lam0) \
         + 3*r0**2 - 2*(z - z0)**2) - 16*r0*(r**2 - 2*r*r0*cos(lam - lam0) \
         + r0**2 + (z - z0)**2)**2)/(16*(r**2 - 2*r*r0*cos(lam - lam0) \
         + r0**2 + (z - z0)**2)**(7/2))
   return Vz

def Function_cylindrical_prism_Vrr(G,rho,r,lam,z,r0,lam0,z0,DeltaR,DeltaLam,DeltaZ):
   Vrr = DeltaLam*DeltaR*DeltaZ*G*rho*(DeltaLam**2*r0**2*(-20*r*r0*(2*r \
         - 3*r0*cos(lam - lam0))*(r**2 - 2*r*r0*cos(lam - lam0) + r0**2 \
         + (z - z0)**2)*sin(lam - lam0)**2 + 5*r*(-7*r*r0*sin(lam - lam0)**2 \
         + (r**2 - 2*r*r0*cos(lam - lam0) + r0**2 + (z - z0)**2)*cos(lam \
         - lam0))*(-2*r**2 + r0**2 + r0*(4*r - 3*r0*cos(lam - lam0))*cos(lam - lam0) \
         + (z - z0)**2) + 2*(2*r*cos(lam - lam0) - 3*r0*cos(2*lam - 2*lam0))*(r**2 \
         - 2*r*r0*cos(lam - lam0) + r0**2 + (z - z0)**2)**2) \
         + 3*DeltaR**2*(r0*(-12*r**4 + 3*r**2*(7*r0**2 - 3*(z - z0)**2) \
         - 2*r0**4 + r0**2*(z - z0)**2 + 3*(z - z0)**4) \
         + (4*r**5 + r**3*(6*r0**2 - 2*(z - z0)**2) \
         - 6*r*(3*r0**4 - 6*r0**2*(z - z0)**2 + (z - z0)**4) \
         + r0*(-3*r**2*(4*r0**2 + 3*(z - z0)**2) + r*r0*(2*r**2 \
         - r*r0*cos(lam - lam0) + 6*r0**2 + 6*(z - z0)**2)*cos(lam - lam0) \
         + 6*r0**4 - 23*r0**2*(z - z0)**2 + 6*(z - z0)**4)*cos(lam - lam0))*cos(lam - lam0))\
         - 3*DeltaZ**2*r0*(4*r**4 + 3*r**2*(r0 - 3*z + 3*z0)*(r0 + 3*z - 3*z0) \
         - r0*(16*r**3 + 6*r*(r0 - 3*z + 3*z0)*(r0 + 3*z - 3*z0) \
         + r0*(-21*r**2 + 10*r*r0*cos(lam - lam0) \
         - 5*r0**2 + 30*(z - z0)**2)*cos(lam - lam0))*cos(lam - lam0) \
         - (r0**2 + (z - z0)**2)*(r0 - 2*z + 2*z0)*(r0 + 2*z - 2*z0)) \
         - 24*r0*(-2*r**2 + r0**2 + r0*(4*r - 3*r0*cos(lam - lam0))*cos(lam - lam0) \
         + (z - z0)**2)*(r**2 - 2*r*r0*cos(lam - lam0) + r0**2 \
         + (z - z0)**2)**2)/(24*(r**2 - 2*r*r0*cos(lam - lam0) \
         + r0**2 + (z - z0)**2)**(9/2))
   return Vrr

def Function_cylindrical_prism_Vrlam(G,rho,r,lam,z,r0,lam0,z0,DeltaR,DeltaLam,DeltaZ):
   Vrlam = DeltaLam*DeltaR*DeltaZ*G*rho*(-DeltaLam**2*r0**2*(r*(4*r**4 \
         + 2*r**2*(-46*r0**2 + 4*(z - z0)**2) - r*r0**3*cos(3*lam - 3*lam0) \
         + 26*r0**4 - 18*r0**2*(r0**2 + (z - z0)**2)*cos(2*lam - 2*lam0) \
         + 30*r0**2*(z - z0)**2 + 4*(z - z0)**4) \
         + r0*(28*r**4 + 3*r**2*(23*r0**2 + 4*(z - z0)**2) \
         - 16*(r0**2 + (z - z0)**2)**2)*cos(lam - lam0)) \
         + 4*DeltaR**2*(r*(2*r**4 + r**2*(-21*r0**2 + 4*(z - z0)**2) \
         + 12*r0**4 - 21*r0**2*(z - z0)**2 + 2*(z - z0)**4) \
         + r0*(6*r**4 + 15*r**2*r0**2 + r*r0*(-3*r**2 + r*r0*cos(lam - lam0) \
         - 6*r0**2 - 6*(z - z0)**2)*cos(lam - lam0) \
         - 6*r0**4 + 23*r0**2*(z - z0)**2 - 6*(z - z0)**4)*cos(lam - lam0)) \
         - 20*DeltaZ**2*r0**2*(r - r0*cos(lam - lam0))*(r**2 - 2*r*r0*cos(lam - lam0) \
         + r0**2 - 6*(z - z0)**2) + 96*r0**2*(r - r0*cos(lam - lam0))*(r**2 \
         - 2*r*r0*cos(lam - lam0) + r0**2 + (z - z0)**2)**2)*sin(lam - lam0)\
         /(32*(r**2 - 2*r*r0*cos(lam - lam0) + r0**2 + (z - z0)**2)**(9/2))
   return Vrlam

def Function_cylindrical_prism_Vrz(G,rho,r,lam,z,r0,lam0,z0,DeltaR,DeltaLam,DeltaZ):
   Vrz = DeltaLam*DeltaR*DeltaZ*G*rho*(z - z0)*(DeltaLam**2*r0**2*(\
         -10*r*r0*(r**2 - 2*r*r0*cos(lam - lam0) + r0**2 \
         + (z - z0)**2)*sin(lam - lam0)**2 \
         - 5*r*(r - r0*cos(lam - lam0))*(-7*r*r0*sin(lam - lam0)**2 \
         + (r**2 - 2*r*r0*cos(lam - lam0) + r0**2 \
         + (z - z0)**2)*cos(lam - lam0)) + (r**2 - 2*r*r0*cos(lam - lam0) \
         + r0**2 + (z - z0)**2)**2*cos(lam - lam0)) \
         + DeltaR**2*(-5*r*r0*(3*r**2 - 4*r0**2 + 3*(z - z0)**2) \
         + (8*r**4 + r**2*(-9*r0**2 + 6*(z - z0)**2) \
         + r*r0*(3*r**2 - 3*r*r0*cos(lam - lam0) + 8*r0**2 \
         - 12*(z - z0)**2)*cos(lam - lam0) - 12*r0**4 \
         + 21*r0**2*(z - z0)**2 - 2*(z - z0)**4)*cos(lam - lam0)) \
         - 5*DeltaZ**2*r0*(r - r0*cos(lam - lam0))*(3*r**2 \
         - 6*r*r0*cos(lam - lam0) + 3*r0**2 - 4*(z - z0)**2) \
         + 24*r0*(r - r0*cos(lam - lam0))*(r**2 - 2*r*r0*cos(lam - lam0) \
         + r0**2 + (z - z0)**2)**2)/(8*(r**2 - 2*r*r0*cos(lam - lam0) \
         + r0**2 + (z - z0)**2)**(9/2))
   return Vrz

def Function_cylindrical_prism_Vlamlam(G,rho,r,lam,z,r0,lam0,z0,DeltaR,DeltaLam,DeltaZ):
   Vlamlam = DeltaLam*DeltaR*DeltaZ*G*rho*(12*DeltaLam**2*r0**2*(35*r**2*r0**3*sin(lam \
         - lam0)**4 - 5*r*r0*(r + 5*r0*cos(lam - lam0))*(r**2 - 2*r*r0*cos(lam - lam0) \
         + r0**2 + (z - z0)**2)*sin(lam - lam0)**2 + (r*cos(lam - lam0) + 2*r0*cos(2*lam \
         - 2*lam0))*(r**2 - 2*r*r0*cos(lam - lam0) + r0**2 + (z - z0)**2)**2) \
         - DeltaR**2*(4*r0*(2 - 6*sin(lam - lam0)**2)*(r**2 - 2*r*r0*cos(lam - lam0) \
         + r0**2 + (z - z0)**2)**2 - 16*(r*cos(lam - lam0) \
         + r0*(3*sin(lam - lam0)**2 - 1))*(r**2 - 2*r*r0*cos(lam - lam0) \
         + r0**2 + (z - z0)**2)*(r**2 + 3*r*r0*cos(lam - lam0) \
         - 4*r0**2 + (z - z0)**2) - 5*(4*r*(-2*r**2 - 3*r*r0*cos(lam - lam0) \
         + 6*r0**2 - 2*(z - z0)**2)*cos(lam - lam0) \
         + 4*r0*(3*r**2 - 4*r0**2 + 3*(z - z0)**2))*(r**2 - 2*r*r0*cos(lam - lam0) \
         - 3*r0**2*sin(lam - lam0)**2 + r0**2 + (z - z0)**2)) \
         + 12*DeltaZ**2*r0*(r0*(2*r*(-2*r**2 + 2*r*r0*cos(lam - lam0) \
         - 2*r0**2 + 3*(z - z0)**2)*cos(lam - lam0) \
         - 5*r0*(r**2 - 2*r*r0*cos(lam - lam0) + r0**2 \
         - 6*(z - z0)**2)*sin(lam - lam0)**2) \
         + (r**2 + r0**2 - 4*(z - z0)**2)*(r**2 + r0**2 + (z - z0)**2)) \
         - 96*r0*(r**2 - 2*r*r0*cos(lam - lam0) + r0**2 + (z - z0)**2)**2*(r**2 \
         - 2*r*r0*cos(lam - lam0) - 3*r0**2*sin(lam - lam0)**2 + r0**2 + (z - z0)**2))\
         /(96*(r**2 - 2*r*r0*cos(lam - lam0) + r0**2 + (z - z0)**2)**(9/2))
   return Vlamlam

def Function_cylindrical_prism_Vlamz(G,rho,r,lam,z,r0,lam0,z0,DeltaR,DeltaLam,DeltaZ):
   Vlamz = DeltaLam*DeltaR*DeltaZ*G*rho*(z - z0)*(-DeltaLam**2*r0**2*(2*r**4 \
         + r**2*(-57*r0**2 + 4*(z - z0)**2) + r*r0*(9*r*r0*cos(2*lam - 2*lam0) \
         + 22*(r**2 + r0**2 + (z - z0)**2)*cos(lam - lam0)) \
         + 2*(r0**2 + (z - z0)**2)**2) + 2*DeltaR**2*(2*r**4 \
         + r**2*(-21*r0**2 + 4*(z - z0)**2) + r*r0*(12*r**2 + 3*r*r0*cos(lam - lam0) \
         - 8*r0**2 + 12*(z - z0)**2)*cos(lam - lam0) + 12*r0**4 \
         - 21*r0**2*(z - z0)**2 + 2*(z - z0)**4) \
         - 10*DeltaZ**2*r0**2*(3*r**2 - 6*r*r0*cos(lam - lam0) \
         + 3*r0**2 - 4*(z - z0)**2) + 48*r0**2*(r**2 - 2*r*r0*cos(lam - lam0) \
         + r0**2 + (z - z0)**2)**2)*sin(lam - lam0)/(16*(r**2 - 2*r*r0*cos(lam - lam0) \
         + r0**2 + (z - z0)**2)**(9/2))
   return Vlamz

def Function_cylindrical_prism_Vzz(G,rho,r,lam,z,r0,lam0,z0,DeltaR,DeltaLam,DeltaZ):
   Vzz = DeltaLam*DeltaR*DeltaZ*G*rho*(-6*DeltaLam**2*r*r0**2*(-4*r**2*r0**2*cos(lam \
         - lam0)**3 + 5*r*r0*(r**2 + r0**2 - 6*(z - z0)**2)*sin(lam - lam0)**2 \
         + 2*r*r0*(2*r**2 + 2*r0**2 - 3*(z - z0)**2)*cos(lam - lam0)**2 \
         - (10*r**2*r0**2*sin(lam - lam0)**2 + (r**2 + r0**2 - 4*(z - z0)**2)*(r**2 + r0**2 \
         + (z - z0)**2))*cos(lam - lam0)) - DeltaR**2*(3*r*(4*r**4 + 3*r**2*(3*r0**2 \
         - 4*(z - z0)**2) - 12*r0**4 + 72*r0**2*(z - z0)**2 \
         - 16*(z - z0)**4)*cos(lam - lam0) - 3*r0*(9*r**4 \
         - 3*r**2*r0**2 + r**2*(r*r0*cos(3*lam - 3*lam0) \
         + (3*r**2 - 5*r0**2 + 18*(z - z0)**2)*cos(2*lam - 2*lam0)) \
         - 4*r0**4 + 42*r0**2*(z - z0)**2 - 24*(z - z0)**4)) \
         + 6*DeltaZ**2*r0*(3*r**4 + 6*r**2*(r0 - 2*z + 2*z0)*(r0 + 2*z - 2*z0) \
         - 12*r*r0*(r**2 - r*r0*cos(lam - lam0) + (r0 - 2*z + 2*z0)*(r0 + 2*z \
         - 2*z0))*cos(lam - lam0) + 3*r0**4 - 24*r0**2*(z - z0)**2 + 8*(z - z0)**4) \
         - 48*r0*(r**2 - 2*r*r0*cos(lam - lam0) + r0**2 - 2*(z - z0)**2)*(r**2 \
         - 2*r*r0*cos(lam - lam0) + r0**2 + (z - z0)**2)**2)\
         /(48*(r**2 - 2*r*r0*cos(lam - lam0) + r0**2 + (z - z0)**2)**(9/2))
   return Vzz

def Function_cylindrical_shell_V(G,rho,r,z,r1,r2,z1,z2):
   V = -pi*G*rho*(-r1**2*log(-z + z1 + sqrt(r1**2 + (z - z1)**2)) \
      + r2**2*log(-z + z1 + sqrt(r2**2 + (z - z1)**2)) \
      + (z - z1)*(sqrt(r1**2 + (z - z1)**2) - sqrt(r2**2 + (z - z1)**2))) \
      + pi*G*rho*(-r1**2*log(-z + z2 + sqrt(r1**2 + (z - z2)**2)) \
      + r2**2*log(-z + z2 + sqrt(r2**2 + (z - z2)**2)) \
      + (z - z2)*(sqrt(r1**2 + (z - z2)**2) - sqrt(r2**2 + (z - z2)**2)))
   return V

def Function_cylindrical_shell_Vz(G,rho,r,z,r1,r2,z1,z2):
   Vz = 2*pi*G*rho*(-sqrt(r1**2 + (z - z1)**2) \
      + sqrt(r1**2 + (z - z2)**2) + sqrt(r2**2 + (z - z1)**2) \
      - sqrt(r2**2 + (z - z2)**2))
   return Vz

def Function_cylindrical_shell_Vrr(G,rho,r,z,r1,r2,z1,z2):
   Vrr = pi*G*rho*(z - z2)*(sqrt(r1**2 + (z - z2)**2) \
      - sqrt(r2**2 + (z - z2)**2))/(sqrt(r1**2 + (z - z2)**2)*sqrt(r2**2 + (z - z2)**2)) \
      - pi*G*rho*(z - z1)*(sqrt(r1**2 + (z - z1)**2) \
      - sqrt(r2**2 + (z - z1)**2))/(sqrt(r1**2 + (z - z1)**2)*sqrt(r2**2 + (z - z1)**2))
   return Vrr

def Function_cylindrical_shell_Vlamlam(G,rho,r,z,r1,r2,z1,z2):
   Vlamlam = pi*G*rho*(z - z2)*(sqrt(r1**2 + (z - z2)**2) \
      - sqrt(r2**2 + (z - z2)**2))/(sqrt(r1**2 + (z - z2)**2)*sqrt(r2**2 + (z - z2)**2)) \
      - pi*G*rho*(z - z1)*(sqrt(r1**2 + (z - z1)**2) \
      - sqrt(r2**2 + (z - z1)**2))/(sqrt(r1**2 + (z - z1)**2)*sqrt(r2**2 + (z - z1)**2))
   return Vlamlam

def Function_cylindrical_shell_Vzz(G,rho,r,z,r1,r2,z1,z2):
   Vzz = -2*pi*G*rho*(z - z2)*(sqrt(r1**2 + (z - z2)**2) \
      - sqrt(r2**2 + (z - z2)**2))/(sqrt(r1**2 + (z - z2)**2)*sqrt(r2**2 + (z - z2)**2)) \
      + 2*pi*G*rho*(z - z1)*(sqrt(r1**2 + (z - z1)**2) \
      - sqrt(r2**2 + (z - z1)**2))/(sqrt(r1**2 + (z - z1)**2)*sqrt(r2**2 + (z - z1)**2))
   return Vzz
