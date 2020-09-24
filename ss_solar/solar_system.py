"""http://stjarnhimlen.se/comp/tutorial.html"""

"""computes planets position by using orbital elements, only gives data of the specified date"""

"""kerem yazici"""

import math
import datetime

def rev(x):
    if x >= 360 or x < 0:
        return x%360
    elif x >= 0:
        return x
def sin(x):
    return math.sin(math.radians(x))
def cos(x):
    return math.cos(math.radians(x))
def tan(x):
    return math.tan(math.radians(x))

pi = math.pi

#---time
y = (datetime.datetime.today()).year
m = (datetime.datetime.today()).month
D = (datetime.datetime.today()).day

d = 367*y - 7 * ( y + (m+9)/12 ) / 4 - 3 * ( ( y + (m-9)/7 ) / 100 + 1 ) / 4 + 275*m/9 + D - 730515

class Planet:

    def __init__(self, name, N, i, w, a, e, M, long_cor, lat_cor):
        self.name = name
        self.N = N
        self.i = i
        self.w = w
        self.a = a
        self.e = e
        self.M = M
        def E():
            E0 = M + (180/pi) * e * sin(M) * (1 + e * cos(M))
            E1 = E0 - (E0 - (180/pi) * e * sin(E0) - M) / (1 - e * cos(E0))
            if E0-E1 < 0.005 or E1-E0 < 0.005:
                return E1
            else:
                while E0-E1 > 0.005 or E1-E0 > 0.005:
                    E1 = E0 - (E0 - (180/pi) * e * sin(E0) - M) / (1 - e * cos(E0))
                    E0 = E1
                return E1
        self.E=E()
        self.long_cor = long_cor
        self.lat_cor = lat_cor
    #def rect_coords(self):
        self.x = self.a * (cos(self.E) - self.e)
        self.y = self.a * math.sqrt(1 - self.e*self.e) * sin(self.E)

    #def dist_true_anomaly(self):
        self.r = math.sqrt( self.x*self.x + self.y*self.y )  #Earth radii or AU
        self.v = rev(math.degrees(math.atan2( self.y, self.x ))) #deg

    #def ecliptic_rect_coords(self):
        self.xeclip = self.r * ( cos(self.N) * cos(self.v+self.w) - sin(self.N) * sin(self.v+self.w) * cos(self.i) )
        self.yeclip = self.r * ( sin(self.N) * cos(self.v+self.w) + cos(self.N) * sin(self.v+self.w) * cos(self.i) )
        self.zeclip = self.r * sin(self.v+self.w) * sin(self.i)

    #def ecliptic_lat_lon_dist(self):
        self.long =  rev(math.degrees(math.atan2( self.yeclip, self.xeclip ))) + self.long_cor
        self.lat  =  math.degrees(math.atan2( self.zeclip, math.sqrt( self.xeclip*self.xeclip + self.yeclip*self.yeclip))) + self.lat_cor
        self.r    =  math.sqrt( self.xeclip*self.xeclip + self.yeclip*self.yeclip + self.zeclip*self.zeclip )


class Earth:

    def __init__(self, name, w, a, e, M ):
        self.name = name
        self.w = w
        self.a = a
        self.e = e
        self.M = M

        self.oblecl = rev(23.4393 - 3.563E-7 * d)     #as degrees

        self.E = M + (180/pi) * e * sin(M) * (1 + e * cos(M)) #result as deg    #because M in degree, use custom deg_sin

        self.L = rev(w + M)

        #rectangular coordinates in the plane of the ecliptic, where the X axis points towards the perihelion
        self.x = cos(self.E) - self.e
        self.y = sin(self.E) * math.sqrt(1 - self.e*self.e)

        #conv to distance and true Anomaly
        self.r = math.sqrt(self.x*self.x + self.y*self.y)
        self.v = rev(math.degrees(math.atan2( self.y, self.x ))) #deg

        self.lon = rev(self.v + self.w) #deg

        #sun's ecliptic rectangular coordinates
        self.x = self.r * cos(self.lon)
        self.y = self.r * sin(self.lon)
        self.z = 0.0

        #equatorial rectangular coordinates
        self.xequat = self.x
        self.yequat = self.y * cos(self.oblecl) - 0.0 * sin(self.oblecl)
        self.zequat = self.y * sin(self.oblecl) + 0.0 * cos(self.oblecl)

        self.r    =  math.sqrt( self.xequat*self.xequat + self.yequat*self.yequat + self.zequat*self.zequat )
        self.RA   =  math.degrees(math.atan2( self.yequat, self.xequat ))      #deg
        self.Decl =  math.degrees(math.atan2( self.zequat, math.sqrt( self.xequat*self.xequat + self.yequat*self.yequat) ))   #deg

#---planets' orbital elements
Mercury = Planet( 'Mercury', rev(48.3313 + 3.24587E-5 * d),             #N  (Long of asc. node)         //deg
                             rev(7.0047 + 5.00E-8 * d),                 #i  (Inclination)               //deg
                             rev(29.1241 + 1.01444E-5 * d),             #w  (Argument of perihelion)    //deg
                             0.387098,                                  #a  (Semi-major axis)
                             0.205635 + 5.59E-10 * d,                   #e  (Eccentricity)
                             rev(168.6562 + 4.0923344368 * d), 0, 0 )   #M  (Mean anonaly)              //deg
##
Venus = Planet( 'Venus', rev(76.6799 + 2.46590E-5   * d),
                         rev(3.3946 + 2.75E-8      * d),
                         rev(54.8910 + 1.38374E-5   * d),
                         0.723330,
                         0.006773     - 1.302E-9         * d,
                         rev(48.0052 + 1.6021302244 * d), 0, 0 )
##
Mars = Planet( 'Mars',   rev(49.5574 + 2.11081E-5  * d),
                         rev(1.8497 - 1.78E-8 * d),
                         rev(286.5016 + 2.92961E-5 * d),
                         1.523688,
                         0.093405 + 2.516E-9 * d,
                         rev(18.6021 + 0.5240207766 * d), 0, 0 )

#--
Mj = rev(19.8950 + 0.0830853001 * d)
Ms = rev(316.9670 + 0.0334442282 * d)
Mu = rev(142.5905 + 0.011725806 * d)

Jupiter = Planet( 'Jupiter', rev(100.4542 + 2.76854E-5 * d),
                           rev(1.3030 - 1.557E-7 * d),
                           rev(273.8777 + 1.64505E-5 * d),
                           5.20256,
                           0.048498 + 4.469E-9 * d,
                           rev(19.8950 + 0.0830853001 * d),

                           ( -0.332 * sin(2*Mj - 5*Ms - 67.6)
                               -0.056 * sin(2*Mj - 2*Ms + 21)
                               +0.042 * sin(3*Mj - 5*Ms + 21)
                               -0.036 * sin(Mj - 2*Ms)
                               +0.022 * cos(Mj - Ms)
                               +0.023 * sin(2*Mj - 3*Ms + 52)
                               -0.016 * sin(Mj - 5*Ms - 69) ), 0 )
##
Saturn = Planet( 'Saturn', rev(113.6634 + 2.38980E-5 * d),
                           rev(2.4886 - 1.081E-7 * d),
                           rev(339.3939 + 2.97661E-5 * d),
                           9.55475,
                           0.055546 - 9.499E-9 * d,
                           rev(316.9670 + 0.0334442282 * d),

                           (+0.812 * sin(2*Mj - 5*Ms - 67.6)    #longitude correction
                            -0.229 * cos(2*Mj - 4*Ms - 2)
                            +0.119 * sin(Mj - 2*Ms - 3)
                            +0.046 * sin(2*Mj - 6*Ms - 69)
                            +0.014 * sin(Mj - 3*Ms + 32)),

                            (-0.020 * cos(2*Mj - 4*Ms - 2)+0.018 * sin(2*Mj - 6*Ms - 49)) ) #latitude correction
##
Uranus = Planet( 'Uranus', rev(74.0005 + 1.3978E-5 * d),
                    rev(0.7733 + 1.9E-8 * d),
                    rev(96.6612 + 3.0565E-5 * d),
                    19.18171 - 1.55E-8 * d,
                    0.047318 + 7.45E-9  * d,
                    rev(142.5905 + 0.011725806 * d),

                    (+0.040 * sin(Ms - 2*Mu + 6)
                        +0.035 * sin(Ms - 3*Mu + 33)
                        -0.015 * sin(Mj - Mu + 20)), 0)
##
Neptune = Planet( 'Neptune', rev(131.7806 + 3.0173E-5 * d),
                             rev(1.7700 - 2.55E-7 * d),
                             rev(272.8461 - 6.027E-6 * d),
                             30.05826 + 3.313E-8 * d,
                             0.008606 + 2.15E-9 * d,
                             rev(260.2471 + 0.005995147 * d), 0, 0 )
##
Earth = Earth( 'Earth', rev(282.9404 + 4.70935E-5 * d),
                        1.000000,
                        0.016709 - 1.151E-9 * d,
                        rev(356.0470 + 0.985600258 * d) )

#########################
