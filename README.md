# Lorentz_and_Galilean_Transformation
A small python implementation for 1D Lorentz and Galilean transformations for Physics Project on Einstein's theory of Special Relativity

## Purpose
This program, very simply, was designed to facilitate the creation of visual aids depicting how speeds are perceived from different inertial observers in Space-time diagrams.
By using some very simple matplotlib figures, the user can easily depict particle's trajectory in a certain reference frame. I'll show it using some concrete examples below:

## Example: Two Cars - Galilei Transformation

Imagining a red car and blue car would be depicted as such in a space-time diagram, imagining 1D movement.

![Blue Car, Red Car driving away](/Plots/1.png)

Using a Galilei-transformation, we can enter the red car's perspective

![Blue Car, Red Car driving away](/Plots/2.png)

And that's how far the story goes in classical mechanics. A car going 60km/h would view the car going 70km/h as going 10km/h from its perspective.
But for depicting it at near light-speed, Lorentz transformations are instead required to allow for the invariance of the speed of light, otherwise, this would happen

![Blue Car, Red Car driving away](/Plots/3.png)

<b> -> Applying Galilei transformation </b>

![Blue Car, Red Car driving away](/Plots/4.png)

And then the speed of light would not be constant.

## Example: Two Cars - Lorentz Transformation

Applying a Lorentz transformation would instead provide the following result:

<b> -> Lorentz Transformation </b>

![Blue Car, Red Car driving away](/Plots/5.png)

This program just allows for easy depiction of such 1D space-time diagrams.
With a bit more work, it can also be used to show why the famous twins-paradox feels so wrong.

![Twin Paradox Diagram](/Plots/6.png)
