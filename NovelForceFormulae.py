This program serves a range scope that oscillates from zero pi to two pi.

# This program serves a range scope that oscillates from zero and two pi.
import math
import cmath

theta = math.pi/3;

m = 1;
a = -9.8;
t = 0;
F_net = (-1*(abs(m*a)));

F_net = -(m*a);
F_net = -1*(a*m*math.cos(2*theta));
F_net = -1*(-1*(m*a*math.sin((1/2)*theta)));
F_net != [0,14];
F_net = -(m*a*math.sin(0*theta));
print((str("The net force is ")) + str(float(F_net)));