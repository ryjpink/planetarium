from math import sin, cos, pi

from panda3d.core import TextNode, NodePath, PandaNode

class CelestialBody:
    def __init__(self,
                 loader,
                 name,
                 radius=1,
                 color=(1, 1, 1),
                 parent=None,
                 distanceToParent=0,
                 periodInEarthYears=1.0,
                 axisTiltAngleDegrees=0,
                 selfRevolutionPeriodInYears=None,
                 hideLabel = False,
                 textureFile=None):

        self.rootNode = PandaNode(f"Root for {name}")
        self.rootNodePath = NodePath(self.rootNode)
        self.axisTiltNodePath = NodePath(self.rootNodePath)
        self.axisTiltNodePath.setHpr(0, axisTiltAngleDegrees, 0)
        self.sphere = loader.loadModel("models/planet_sphere.egg")
        self.sphere.setColor(*color)
        self.sphere.setPos(0, 0, 0)
        self.sphere.setScale(radius, radius, radius)
        self.sphere.reparentTo(self.axisTiltNodePath)

        if not hideLabel:
            self.textNode = TextNode(f"Label text for {name}")
            self.textNode.setText(name)
            self.textNode.setTextColor(1, 1, 1, 1)
            self.textNode.setTextScale(0.4)
            self.textNode.setAlign(TextNode.A_center)
            self.textNodePath = NodePath(self.textNode)
            self.textNodePath.reparentTo(self.rootNodePath)
            self.textNodePath.setPos(0, 0, 0.5 + radius * 1.2)
            self.textNodePath.setBillboardPointEye()

        if not textureFile is None:
            self.texture = loader.loadTexture(textureFile)
            self.sphere.setTexture(self.texture, 1)

        self.parent = parent
        if not self.parent is None:
            self.rootNodePath.reparentTo(self.parent.rootNodePath)
        self.distanceToParent = distanceToParent
        self.periodInEarthYears = periodInEarthYears
        self.selfRevolutionPeriodInYears = selfRevolutionPeriodInYears

    def reparentTo(self, parent):
        self.rootNodePath.reparentTo(parent)

    def animate(self, timeInYears):
        if self.selfRevolutionPeriodInYears:
            angle = timeInYears / self.selfRevolutionPeriodInYears * (2 * pi)
            self.sphere.setHpr(angle, 0, 0)
        if self.parent is None:
            return
        angle = timeInYears / self.periodInEarthYears * (2 * pi)
        x = sin(angle) * self.distanceToParent
        y = cos(angle) * self.distanceToParent
        self.rootNodePath.setPos(x, y, 0)