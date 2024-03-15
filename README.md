# Bertrand's Paradox Visualization

This Python code simulates Bertrand's Paradox using three different sampling methods: Endpoints, Radial Point, and Midpoint. It generates random chords on a circle and calculates the probability of the chord length being greater than the side length of an equilateral triangle inscribed in the circle.

## Requirements

- Python 3.x
- NumPy
- Matplotlib

## Usage

1. Extract the contents of the `bertrand_paradox.zip` file to a directory of your choice.
2. Navigate to the extracted directory using the terminal or command prompt.
3. Run the script:
4. The script will prompt you to choose the sampling strategy:
   Choose the sampling strategy, 1 for Endpoints, 2 for Radial Point, 3 for Midpoint
5. Next, you'll be asked to choose the graph type: Enter 1 for static graph (faster), 2 for dynamic graph (slower)
6. Enter the number of chords you want to generate:
7. The script will generate the chords using the selected sampling method and render the graph. Green chords represent chords longer than the side length of the 
   equilateral triangle, while red chords are shorter.
8. After the graph is displayed, you'll be prompted to continue or exit: Enter 1 to continue, 0 to exit
   
## Methods
 Endpoints: This method generates random chords by selecting two random points on the circle's circumference and connecting them.

 Radial Point: This method first selects a random radius of the circle, then chooses a point at random on this radius to be the midpoint of the chord.

 Midpoint: This method selects a point at random within the circle and considers it the midpoint of the chord.
