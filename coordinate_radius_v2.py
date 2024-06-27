import numpy as np

# radius of Earth in miles
R = 3949.9

# rho = arc length distance along spherical surface of Earth

class CoordinateRadiusGenerator:

    def __init__(self, lat, long):
        self.lat = lat
        self.long = long
        self._coords_to_radians()

    def _coords_to_radians(self):
        """Convert latitude and longitude to radians."""
        # self.theta = np.pi * (1/2 - self.lat/180)
        self.theta = np.pi * (self.lat/180 - 1/2)
        # self.phi = np.pi * (1 + self.long/180)
        self.phi = np.pi * (self.long/180 - 1)

    def _get_rotation_matrix(self):
        """Matrix to rotate rhat_prime back to original basis."""
        theta = self.theta
        phi = self.phi
        return np.array([
        [
            np.cos(theta)*np.cos(phi),
            -np.sin(phi),
            np.sin(theta)*np.cos(phi)
        ],
        [
            np.cos(theta)*np.sin(phi),
            np.cos(phi),
            np.sin(theta)*np.sin(phi)
        ],
        [
            -np.sin(theta),
            0,
            np.cos(theta)
        ]
    ])

    def _get_rhat_prime(self, gamma):
        """Unit vector at the appropriate angle to z-axis in
        the transformed basis.

        Args:
            gamma (float): Azimuthal angle around target location.

        Returns:
            np.array: Unit vector in transformed basis
                for a location at R*gamma away from target
                location.

        """
        alpha = self.alpha
        return np.array([
            np.cos(gamma)*np.sin(alpha),
            np.sin(gamma)*np.sin(alpha),
            np.cos(alpha)
        ])

    def _get_rhat(self, gamma):
        """Rotates vectors back to original basis."""
        return np.dot(
            self._get_rotation_matrix(),
            self._get_rhat_prime(gamma)
        )

    def _get_theta_r(self, gamma):
        """Gives latitude of calculated vector in radians."""
        return np.arccos(self._get_rhat(gamma)[-1])


    def _get_phi_r(self, gamma):
        """Gives longitude of calculated vector in radians."""
        r = self._get_rhat(gamma)
        return np.sign(r[1]) * np.arccos(r[0] / np.linalg.norm(r[:2]))

    def _get_lat_long(self, gamma):
        """Convert calculated angles from radians to latitude/longitude."""
        return (
            90 - 180/np.pi * self._get_theta_r(gamma),
            # 180 * self._get_phi_r(gamma)/(np.pi - 1)
            (180/np.pi) * self._get_phi_r(gamma)
        )

    def get_coordinates(self, gamma, rho):
        """Find coordinates of single point.

            Args:
                gamma (float): azimuthal angle about target location.
                rho (float): geodesic distance from target location.

            Returns:
                tuple: (latitude, longitude)

        """
        # Convert geodesic distance to polar angle
        # from target location.
        self.alpha = rho/R
        return self._get_lat_long(gamma)

    def get_coordinate_ring(self, rho, npts):
        """Get coordinates of several points.

            Args:
                rho (float): geodesic distance from target location.
                npts (int): number of points desired, evenly spaced.

            Returns:
                np.array whose entries are [latitude, longitude]

        """
        return np.array([
            self.get_coordinates(gamma, rho)
            for gamma in np.linspace(0, 2*np.pi, npts)
        ])


if __name__ == "__main__":
    # Usage example
    crg = CoordinateRadiusGenerator(
        lat=90,
        # lat=35.820020,
        long=0
        # long=-78.901990
    )

    # miles
    rho = 10
    npts = 11
    for gamma in np.linspace(0, 2*np.pi, npts):
        # 10 mile radius
        print(gamma/(2*np.pi), crg.get_coordinates(gamma, rho))


    # These should agree with the above
    print(crg.get_coordinate_ring(rho, npts))