#Rudimentary simulation of Bertrand's Paradox using random number generation and the random endpoints method

# import random
# import time

# count = 0
# success = 0
# start = time.time()
# for i in range(1000000):
#     a = random.randrange(0.0, 360.0)
#     if(a < 240.0 and a > 120.0):
#         success += 1
#     count += 1
# end = time.time()
# print(success/count)
# print("Time: ", end - start, " seconds")





#A better simulation of Bertrand's Paradox using all the three sampling methods (Endpoints, Radial Point, Midpoint)

import numpy as np
import matplotlib.pyplot as plt

def generate_endpoints(radius):
    angle1 = np.random.uniform(0, 2*np.pi)
    angle2 = np.random.uniform(0, 2*np.pi)
    x1 = radius * np.cos(angle1)
    y1 = radius * np.sin(angle1)
    x2 = radius * np.cos(angle2)
    y2 = radius * np.sin(angle2)
    return (x1, y1), (x2, y2)

def generate_radial_point(radius):
    angle = np.random.uniform(0, 2*np.pi)
    rx = radius * np.cos(angle)
    ry = radius * np.sin(angle)
    mpx = np.random.uniform(0, rx)
    mpy = np.random.uniform(0, ry)
    base = np.sqrt(mpx**2 + mpy**2)
    anglecos = np.arccos(base/radius)
    x1 = radius * np.cos(angle + anglecos)
    y1 = radius * np.sin(angle + anglecos)
    x2 = radius * np.cos(angle - anglecos)
    y2 = radius * np.sin(angle - anglecos)
    return (x1, y1), (x2, y2)

def generate_midpoint(radius):
    angle = np.random.uniform(0, 2*np.pi)
    r = np.sqrt(np.random.uniform(0, radius**2))
    mpx = r * np.cos(angle)
    mpy = r * np.sin(angle)
    base = np.sqrt(mpx**2 + mpy**2)
    anglecos = np.arccos(base/radius)
    x1 = radius * np.cos(angle + anglecos)
    y1 = radius * np.sin(angle + anglecos)
    x2 = radius * np.cos(angle - anglecos)
    y2 = radius * np.sin(angle - anglecos)
    return (x1, y1), (x2, y2)

def draw_circle(radius):
    circle = plt.Circle((0, 0), radius, color='b', fill=False)
    fig, ax = plt.subplots()
    ax.set_aspect('equal', adjustable='box')
    ax.add_artist(circle)
    ax.set_xlim(-radius*1.1, radius*1.1)
    ax.set_ylim(-radius*1.1, radius*1.1)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Chords on a Circle')
    plt.grid(True)
    return fig, ax

def draw_chord(point1, point2, num_chords, col):
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    plt.plot(x_values, y_values, color=col, lw=40/num_chords)

def compare_to_equilateral_triangle(side_length, chord_length):
    if chord_length > side_length:
        return True
    else:
        return False

def main(radius, side_length, num_chords, choice, dynamic):
    fig, ax = draw_circle(radius)
    success = 0
    plt.ion()
    for i in range(num_chords):
        if choice == 1: 
            point1, point2 = generate_endpoints(radius)
        elif choice == 2:
            point1, point2 = generate_radial_point(radius)
        elif choice == 3:
            point1, point2 = generate_midpoint(radius)
        else:
            print("Invalid choice")
            return
        chord_len = np.linalg.norm(np.array(point1) - np.array(point2))
        if compare_to_equilateral_triangle(side_length, chord_len):
            success += 1
            draw_chord(point1, point2, num_chords, 'g')
        else : 
            draw_chord(point1, point2, num_chords, 'r')
        if dynamic == 2:
            plt.pause(5/num_chords)
            plt.draw()
            ax.set_title(f"Success rate: {success/(i+1):.4f}")
    plt.ioff()
    # print(' ' * 50, end='\r')
    # print ('Success rate: ', success/num_chords)
    ax.set_title(f"Success rate: {success/num_chords:.4f}")
    plt.show()

radius = 1.0
side_length = np.sqrt(3)  

start = 1
while(start == 1):
    print("Choose the sampling strategy, 1 for Endpoints, 2 for Radial Point, 3 for Midpoint")
    choice = int(input())
    print("Enter 1 for static graph (faster), 2 for dynamic graph (slower)")
    dynamic = int(input())
    print("Enter number of chords:")
    num_chords = int(input())
    main(radius, side_length, num_chords, choice, dynamic)
    print("Enter 1 to continue, 0 to exit")
    start = int(input())
