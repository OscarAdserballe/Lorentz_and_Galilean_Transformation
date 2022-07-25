# A small python program to depict the difference between
# classical mechanics and special relativity by creating small visual aids.
# There weren't really any available resources on the internet, so
# programming it myself was a quicker, more customisable approach

import math
from matplotlib import pyplot as plt
import numpy as np
import matplotlib
import copy

# Declaring speed of light
c = 3 * 10**8        
# Setting up the plot and customising it so it looks a bit better
fig = plt.figure()
ax = plt.axes()
plt.axhline(y=0, color="black")
# plt.axvline(x=0, label="t", color="black")
plt.ylabel("Tid i år")
plt.xlabel("k: lysår")
plt.grid(True)
plt.title("Rumtidsdiagram")
plt.ylim([0, 5])
"""plt.xlim([-5, 2.375])
plt.xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],\
    labels=["-5k", "-4k", "-3k", "-2k", "-1k", "0", "1k", "2k",\
          "3k", "4k", "5k"]) """
plt.xlim([-2, 2])
plt.xticks([-2, -1, 0, 1, 2],\
    labels=["-2k", "-1k", "0", "1k", "2k"])
plt.yticks([0, 1, 2, 3, 4, 5])


#Plotting a spacetime diagram, where time is along the second axis, and distance along the first axis
#Special relativity operates out of a framework where the speed of light is always constant.
#The Lorentz transformations to "switch" perspective only works with movement in one direction.
#Requires a rightward and leftward moving photon to visualize. Their movements are plotted as a function of the distance they've travelled:
# tc = x <=> t = x/c            (or, more generally: t=x/v)

# initialise some particle
# in hindsigt, creating a particle class would definitely have been better
# and then adding the transformations as different methods
def createParticle(starting_point, velocity, starting_t=0):
    t_values = []
    x_values = np.arange(-10, 10, 0.01)
    for i in range(len(x_values)):

        t_values.append((x_values[i]/velocity)+float(starting_t)) #t=x/v
        x_values[i] += starting_point
    return x_values, t_values, velocity

# Apply galilean transformation where x' = x-vt as in classical mechanics
def galileanTransformation(frame_of_reference_velocity, particle):
    
    for i in range(len(particle[0])):   #Loop through the x_values of the particle that will be adjusted to the frame of reference.
        particle[0][i] = particle[0][i]-frame_of_reference_velocity*particle[1][i]   #x' = x-vt
    new_particle_velocity = round((particle[0][1]-particle[0][0])/(particle[1][1]-particle[1][0]), 2)
    return particle[0], particle[1], new_particle_velocity        #new x and v, whilst t remains the same

# Apply Lorentz Transformation which applies in Special Relativity whre speeds are near c
def lorentzTransformation(frame_of_reference_velocity, particle):
    lorentzFactor = 1/(math.sqrt(1-(frame_of_reference_velocity**2)))
    
    #For the purposes of this program, c is set to 1, and therefore left out of the equations
    transformed_t = []
    transformed_x = []
    for i in range(len(particle[0])):
        transformed_x.append(lorentzFactor * (particle[0][i]-(frame_of_reference_velocity*particle[1][i])))
        transformed_t.append(lorentzFactor * (particle[1][i]-(frame_of_reference_velocity*particle[0][i])))

    if particle[2] != 1 and particle[2] !=-1:
        own_lorentzFactor = 1/(math.sqrt(1-(particle[2]**2)))
        print(own_lorentzFactor)
        if particle[2] > -0.02 and particle[2] < 0.02:
            for i in range(6):
                plt.scatter(0, i, color="blue")
        else:
            for i in range(len(transformed_t)):
                if round(transformed_t[i], 2)%own_lorentzFactor<0.01:
                    plt.scatter(transformed_x[i], transformed_t[i], color="green")
    print("Done")
            
    new_particle_velocity = round((particle[2]-frame_of_reference_velocity)/(1-(frame_of_reference_velocity*particle[2])), 2)  #Subtracting the particle's velocity from that of the frame of reference using velocity equation derived from the lorentz-transformation
    return transformed_x, transformed_t, new_particle_velocity

# takes some list of particles along with a colour key and plots them in diagram
def plotAll(some_list_of_particles, colour_key, style="solid"):
    for particle_num in range(len(list_of_particles)):
        if style == "solid":
            ax.plot(list_of_particles[particle_num][0], list_of_particles[particle_num][1], color=colour_key[particle_num], label="v="+str(list_of_particles[particle_num][2]) + "c")
        elif style == "dashed":
            ax.plot(list_of_particles[particle_num][0], list_of_particles[particle_num][1], color=colour_key[particle_num], label="v="+str(list_of_particles[particle_num][2]) + "", linestyle="dashed")


# creating whatever photons are needed for particular diagram
rightward_photon = createParticle(0, 1)
leftward_photon = createParticle(0, -1)
red_car = createParticle(0, 0.001)
blue_car = createParticle(0, 0.8)
blue_car2 = createParticle(2, -0.8, 2.5)

list_of_particles = [red_car, blue_car, blue_car2, rightward_photon, leftward_photon]
corresponding_colour_list = ["red", "blue", "blue", "orange", "orange"]

frame_of_reference_velocity = 0.00

# what type of transformation
lorentz = True
newton = False

if lorentz and not newton:
    for i in range(len(list_of_particles)):
        list_of_particles[i] = lorentzTransformation(frame_of_reference_velocity, list_of_particles[i])
    plotAll(list_of_particles, corresponding_colour_list)
elif newton and not lorentz:
    for i in range(len(list_of_particles)):
        list_of_particles[i] = galileanTransformation(frame_of_reference_velocity, list_of_particles[i])
    plotAll(list_of_particles, corresponding_colour_list)

for k in range(1, 6):
    plt.plot([0, (20-4*k)/9], [k, (20+5*k)/9], color="orange", linestyle="dashed")


plt.legend()

# saving plot
plt.savefig("Tvillingeparadoks.png", dpi=300)
plt.show()
