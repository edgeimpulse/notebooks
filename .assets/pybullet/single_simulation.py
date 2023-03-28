import pybullet as p
import pybullet_data
import time
import random
import numpy as np


# Set up PyBullet physics simulation (change from p.GUI to p.DIRECT for headless simulation)
physicsClient = p.connect(p.GUI)
p.setTimeStep(1/480)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)

# Load object URDF file
obj_file = "../.assets/pybullet/thingy53/thingy53.urdf"
obj_id = p.loadURDF(obj_file, flags=p.URDF_USE_INERTIA_FROM_FILE)

# Add a solid plane for the object to collide with
plane_id = p.loadURDF("plane.urdf")

# p.changeDynamics(plane_id, -1, linearDamping=0.1, angularDamping=0.2)
# p.changeDynamics(obj_id, -1, linearDamping=0.1, angularDamping=0.2)
# p.changeDynamics(obj_id, -1, restitution=0.6)
# p.changeDynamics(plane_id, -1, restitution=0.3) 
p.changeDynamics(plane_id, -1, linearDamping=0.01, angularDamping=0.02)
p.changeDynamics(obj_id, -1, linearDamping=0.1, angularDamping=0.02)
p.changeDynamics(obj_id, -1, lateralFriction=0.001, rollingFriction=0.001, spinningFriction=0.001)
# p.changeDynamics(plane_id, -1, lateralFriction=0.001, rollingFriction=0.001, spinningFriction=0.001)
p.changeDynamics(obj_id, -1, restitution=0.3)
p.changeDynamics(plane_id, -1, restitution=0.4)
sample_freq = 1000  # Sample frequency in Hz

# Define function to simulate dropping object from a given height
def simulate_drop(height, sims_per_height):
    for i in range(sims_per_height):
        # Set initial position and orientation of object
        x = 0
        y = 0
        z = height
        orientation = p.getQuaternionFromEuler((0,0,0))
        orientation = p.getQuaternionFromEuler((random.uniform(0, 2 * np.pi), random.uniform(0, 2 * np.pi), random.uniform(0, 2 * np.pi)))

        p.resetBasePositionAndOrientation(obj_id, [x, y, z], orientation)
        
        # Simulate until object is settled
        settled = False
        settle_steps = 150
        while settle_steps > 0:
            p.stepSimulation()
            linear_vel, angular_vel = p.getBaseVelocity(obj_id)
            pos, orn = p.getBasePositionAndOrientation(obj_id)
            if pos[2] < 0.01:
                settle_steps -= 1
            time.sleep(1/4800)


# Simulate dropping object from range of heights
for height in np.linspace(1, 1.5, num=3):
    sims_per_height = 1
    simulate_drop(height, sims_per_height)

# Disconnect from PyBullet physics simulation
p.disconnect()
