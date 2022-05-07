from math import sin, cos, pi
from celestial_body import CelestialBody

from direct.showbase.ShowBase import ShowBase
from direct.task import Task

# Main window class for the Planetarium app
class SolarSystem(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Set the background color to black
        self.setBackgroundColor(0, 0, 0)

        # Load the sky sphere
        self.sky = self.loader.loadModel("models/planet_sphere.egg")
        self.sky_tex = self.loader.loadTexture("models/stars_8k_tex.jpg")
        self.sky.setTexture(self.sky_tex, 1)
        self.sky.setTwoSided(True)
        self.sky.reparentTo(self.render)
        self.sky.setScale(1000)
        self.sky.setHpr(0, 90, 90)

        # Load the sun
        self.sun = CelestialBody(self.loader, "Sun", radius=2.0, color=(1, 1, 1), textureFile="models/sun_1k_tex.jpg",
            selfRevolutionPeriodInYears=27/365, axisTiltAngleDegrees=7.25)
        self.sun.reparentTo(self.render)

        self.oneYearInSeconds = 60

        self.mercury = CelestialBody(
            self.loader, "Mercury", radius=0.1, color=(1, 1, 1), parent=self.sun, distanceToParent=4,
            periodInEarthYears=(88/365), textureFile="models/mercury_1k_tex.jpg",
            selfRevolutionPeriodInYears=59/365, axisTiltAngleDegrees=2.11)
        self.venus = CelestialBody(
            self.loader, "Venus", radius=0.15, color=(1, 1, 1), parent=self.sun, distanceToParent=5,
            periodInEarthYears=(225/365), textureFile="models/venus_1k_tex.jpg",
            selfRevolutionPeriodInYears=117/365, axisTiltAngleDegrees=2.6)
        self.earth = CelestialBody(
            self.loader, "Earth", radius=0.3, color=(1, 1, 1), parent=self.sun, distanceToParent=7,
            periodInEarthYears=1.0, textureFile="models/earth_1k_tex.jpg",
            selfRevolutionPeriodInYears=1/365, axisTiltAngleDegrees=23)
        self.mars = CelestialBody(
            self.loader, "Mars", radius=0.25, color=(1, 1, 1), parent=self.sun, distanceToParent=9,
            periodInEarthYears=(687/365), textureFile="models/mars_1k_tex.jpg",
            selfRevolutionPeriodInYears=1.025/365, axisTiltAngleDegrees=25)
        self.jupiter = CelestialBody(
            self.loader, "Jupiter", radius=1.0, color=(1, 1, 1), parent=self.sun, distanceToParent=25,
            periodInEarthYears=12, textureFile="models/jupiter_1k_tex.jpg",
            selfRevolutionPeriodInYears=0.35/365, axisTiltAngleDegrees=3)
        self.moon = CelestialBody(
            self.loader, "Moon", radius=0.08, color=(1, 1, 1), parent=self.earth, distanceToParent=0.7,
            periodInEarthYears=(1/12), textureFile="models/moon_1k_tex.jpg", hideLabel=True)
        self.phobos = CelestialBody(
            self.loader, "Phobos", radius=0.04, color=(0.8, 0.7, 0.5), parent=self.mars, distanceToParent=0.4,
            periodInEarthYears=(5/365), hideLabel=True)
        self.deimos = CelestialBody(
            self.loader, "Deimos", radius=0.02, color=(0.8, 0.7, 0.5), parent=self.mars, distanceToParent=0.5,
            periodInEarthYears=(20/365), hideLabel=True)

        self.bodies = [
            self.sun, self.mercury, self.venus, self.earth, self.moon,
            self.mars, self.jupiter, self.phobos, self.deimos]
        self.taskMgr.add(self.animateBodies, "Animate Celestial Bodies")
        self.taskMgr.add(self.animateCamera, "Animate Camera")

    def animateBodies(self, task):
        timeInYears = task.time / self.oneYearInSeconds
        for body in self.bodies:
            body.animate(timeInYears)
        return Task.cont

    def animateCamera(self, task):
        timeInYears = task.time / self.oneYearInSeconds
        angle = (timeInYears / -30 + 0.7) * (2 * pi)
        x = sin(angle) * 35
        y = cos(angle) * 35
        self.camera.setPos(x, y, 25)
        self.camera.lookAt(self.sun.rootNodePath.getPos())
        return Task.cont

if __name__ == '__main__':
    app = SolarSystem()
    app.run()