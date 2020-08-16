# ML-plays-GTA-V
A deep learning model that can drive a car in GTA-V
The model is built using Alexnet architecture the input is screen shots of the screen and the output is the key pressed
The model is able to play the game at 10 frames per second on Intel® Core™ i7-6500U CPU @ 2.50GHz × 4 


# Collecting the data
To start building your model you will need to open the game in window mode but the window in size 800*600 then move the window to the upper left corner of the screen.

Then you will need to run the main file and start driving a car around to collect the training data. I suggest to collect about 300k record.

# Training
Now it's time to train the model. Just run training.py file and set the path to the trainig data you have just collected.

# Let the model play the game
To test the model and see it actually playing just run test.py file. Don't forget to set the path to the model. Don't forget to do the instructions in Collecting the data section before running test.py.

# Future work
The model is now capable of just driving a car around. The next step maybe to train a model to avoid obstacles.
