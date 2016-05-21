#Information about our Script

import rhinoscriptsyntax as rs
import math
import random

class Particle:
    #Constructor
    def __init__(self, _startPoint):
        self.location = _startPoint
        self.x = random.uniform(-2,2)
        self.y = random.uniform(-2,2)
        self.z = random.uniform(10,20)
        self.velocity = rs.VectorCreate([self.x,self.y,self.z],[0,0,0])
        self.acceleration = rs.VectorCreate([0,0,0],[0,0,0])
    def run(self):
        self.update()
        self.display()
    def update(self):
        self.velocity = rs.VectorAdd(self.velocity, self.acceleration)
        self.location = rs.VectorAdd(self.location, self.velocity)
    def display(self):
        rs.AddSphere(self.location,5)
    def applyForce(self, _force):
        self.acceleration = rs.VectorAdd(self.acceleration, _force)

class ParticleSystem:
    def __init__(self, _location):
        self.particles = []
        self.origin = rs.VectorCreate(_location,[0,0,0])
    def addParticle(self):
        self.particles.append(Particle(self.origin))
    def applyForce(self, _force):
        for p in self.particles:
            p.applyForce(_force)
    def run(self):
        for p in self.particles:
            p.run()

gravity = rs.VectorCreate([0,0,-0.5],[0,0,0])
wind = rs.VectorCreate([0.5,1.0,0.0],[0,0,0])

origin1 = rs.GetPoint("Please specify origin 1")
origin2 = rs.GetPoint("Please specify origin 2")

ps1 = ParticleSystem(origin1)
ps2 = ParticleSystem(origin2)

for i in range(100):
    ps1.applyForce(wind)
    ps1.applyForce(gravity)
    ps2.applyForce(wind)
    ps2.applyForce(gravity)
    ps1.addParticle()
    ps2.addParticle()
    ps1.run()
    ps2.run()