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
        self.acceleration = rs.VectorCreate([0,0,-0.5],[0,0,0])
    def run(self):
        self.update()
        self.display()
    def update(self):
        self.velocity = rs.VectorAdd(self.velocity, self.acceleration)
        self.location = rs.VectorAdd(self.location, self.velocity)
    def display(self):
        rs.AddSphere(self.location,5)

#particle = Particle(rs.VectorCreate([0,0,20],[0,0,0]))

particles = []

for i in range(5):
    particle = Particle(rs.VectorCreate([0,0,20],[0,0,0]))
    particles.append(particle)

for i in range(100):
    for p in particles:
        p.run()

