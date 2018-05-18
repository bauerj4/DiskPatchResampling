import numpy as np

def Spherical_Plummer(r,eps):
    norm = eps**3/3.
    return r**2/norm * (1 + r**2/eps**2)**-2.5 

Spherical_Plummer_Vectorized = np.vectorize(Spherical_Plummer, excluded=['eps'])
def Sample_Plummer(num_samples, eps):
    sample = np.zeros(num_samples)
    i      = 0
    while(i < num_samples):
        r    = np.random.uniform(0,10.* eps)
        dist = Spherical_Plummer(r,eps)
        if (dist > np.random.uniform()):
            sample[i] = r
            i += 1
    return sample

#Inverse_Plummer_CDF = np.vectorize(Inverse_Plummer_CDF, excluded=['eps'])

"""

Particle class. Contains coordinates, mass, 
and position resampling algorithms

"""

class Particle(object):
    def __init__(self,coords,eps):
        self.x  = coords[1]
        self.y  = coords[2]
        self.z  = coords[3]
        self.vx = coords[4]
        self.vy = coords[5]
        self.vz = coords[6]
        self.eps= eps

    def Resample_Plummer_Positions(self, num_resample):
        cost  = np.random.uniform(-1,1,size=num_resample)
        phi   = np.random.uniform(0,2. * np.pi,size=num_resample)
        theta = np.arccos(cost)
        sint  = np.sin(theta)
        #u     = np.random.uniform(size=num_resample)
        r     = Sample_Plummer(num_resample,self.eps)
        pos   = r * np.array([sint * np.cos(phi), sint * np.sin(phi), cost])
        pos   = pos.T
        
        return pos
