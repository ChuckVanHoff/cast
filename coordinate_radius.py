import numpy as np

# radius of Earth in miles
R = 3949.9

# rho = arc length distance along spherical surface of Earth

class CoordinateRadiusGenerator:

    def __init__(self, lat, long):
        self.lat = lat
        self.long = long
        self._coords_to_radians()
        self._create_r_init()
        self._create_rotation_matrix()

    def _coords_to_radians(self):
        self.theta = np.pi * (1/2 - self.lat/180)
        self.phi = np.pi * (1 + self.long/180)

    def _create_r_init(self):
        self.r_init = np.array([
            np.cos(self.phi)*np.sin(self.theta),
            np.sin(self.phi)*np.sin(self.theta),
            np.cos(self.theta)
        ])

    def _create_rotation_matrix(self):
        self.U = np.array([
            [
                np.cos(self.theta)*np.cos(self.phi),
                np.cos(self.theta)*np.sin(self.phi),
                -np.sin(self.theta)
            ],
            [
                -np.sin(self.phi),
                np.cos(self.phi),
                0
            ],
            [
                np.sin(self.theta)*np.cos(self.phi),
                np.sin(self.theta)*np.sin(self.phi),
                np.cos(self.theta)
            ]
        ])

    def _rotate_to_z_axis(self):
        self.r_prime = np.dot(self.U, self.r_init)

    def _rotate_back(self, vector):
        return np.dot(self.U.T, vector)

    def _r(self, gamma, rho):
        alpha = rho/R
        return self._rotate_back(
            np.array([
                np.cos(gamma)*np.sin(alpha),
                np.sin(gamma)*np.sin(alpha),
                np.cos(alpha)
            ])
        )

    def _get_theta_r(self, gamma, rho):
        z = self._r(gamma, rho)[-1]
        return np.arccos(z)

    def _get_phi_r(self, gamma, rho):
        r = self._r(gamma, rho)
        phi_raw = np.arctan2(r[1], r[0])
        return phi_raw + 2*np.pi*(phi_raw < 0)

    def _get_lat_long(self, gamma, rho):
        return (
            90 - 180/np.pi * self._get_theta_r(gamma, rho),
            180 * (self._get_phi_r(gamma, rho)/np.pi - 1)
        )

    def get_coordinates(self, gamma, rho):
        return self._get_lat_long(gamma, rho)


# Usage example
crg = CoordinateRadiusGenerator(
    lat=35.820020,
    long=-78.901990
)

for gamma in np.linspace(0, 2*np.pi, 11):
    # 10 mile radius
    print(gamma/(2*np.pi), crg.get_coordinates(gamma, 10))