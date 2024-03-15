# Bertrand's Paradox Visualization

This Python script visualizes three different methods of generating random chords on a circle, as described in Bertrand's Paradox. The script plots the chords and their midpoints for each method and calculates the probability of the chord being longer than the side length of an equilateral triangle inscribed in the circle.

## Requirements

- Python 3.x
- NumPy
- Matplotlib

## Usage

1. Extract the contents of the `bertrand_paradox.zip` file to a directory of your choice.
2. Navigate to the extracted directory using the terminal or command prompt.
3. Run the script:
4. The script will prompt you to enter a sample number (1, 2, or 3) corresponding to the method you want to visualize:
  Enter the sample number (1, 2, or 3):
5. Enter the desired sample number (1, 2, or 3) and press Enter.
6. The script will generate a plot for the selected method, displaying the chords and their midpoints on separate axes.
7. The probability of the chord being longer than the side length of an equilateral triangle inscribed in the circle will be printed in the console.
8. The plot will be saved as a PNG file (bertrand{sample_number}.png) in the same directory.
## Methods
Method 1: Pairs of (uniformly-distributed) random points on the unit circle are selected and joined as chords.
Method 2: First, a random radius of the circle is selected, and then a point is chosen at random (uniformly-distributed) on this radius to be the midpoint of the chord.
Method 3: A point is selected at random (uniformly distributed) within the circle, and this point is considered the midpoint of the chord.
