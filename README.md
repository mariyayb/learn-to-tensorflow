# Learn To Tensorflow

This repository contains mini programming challenges
aimed to gradually stretch your working skills and 
understanding of tensorflow basics.

Each challenge has a corresponding solution in the solutions folder.
If you need a hint or some starter code to give you structure there are templates in the template folder which have only the outline of the solution files.

If you are totally new to Tensorflow and don't know the difference between the graph and code, check out the subdirectory [the_basics](the_basics)


## How to use this resource
These are skills building exercises.  It is suggested that you go through all the challenges in Levels where each Level becomes increasingly more difficult.  If a Level takes you more than three hours to complete then consider repeating the Level another day before going onto the next Level.

### Level 1 - Beginner
Try to do the challenges using as much reference as you need such as the templates, searching for information on the web, and referencing the solution as needed.

### Level 2 - Template user
Same as Level 1 but do not reference the solution folder.

### Level 3 - Web researcher
Same as Level 2 but also do not refer to the template folder.

### Level 4 - Solo
Do all the challenges without any reference including searching the web.  Try substituting relu for sigmoid and compare the difference in learning rate and loss.

### Beyond Level 4 - The Graduate
If you've completed Level 4 within three hours then consider yourself graduated.  It's time to move onto more complex real life applications.

Consider visiting https://www.tensorflow.org and going through each tutorial in a similar manner, graduating yourself from Level 1 up to Level 5.  There is a unix bash script in the solutions folder **solutions/convert-solution-to-template.sh** that you could use on any code to convert it to a template, like so:
```
./solutions/convert-solution-to-template.sh < solution-file-name.py > template-file-name.py
```

## Using Virtual Environment

### The code uses Python 3.6 
( Python >3.6 is not supported by tensorflow at time of writing)

Install Python 3.6 if you don't have it already.  On a mac use 
```
brew install https://raw.githubusercontent.com/Homebrew/homebrew-core/f2a764ef944b1080be64bd88dca9a1d80130c558/Formula/python.rb
```
Create a virtual env and install the dependencies
```
virtualenv --python python3.6 ~/env/learn-to-tensorflow
source ~/env/learn-to-tensorflow/bin/activate
pip install -r requirements.txt
```
On future sessions just use
```
source ~/env/learn-to-tensorflow/bin/activate
```


## The challenges

### 00-count.py
Create a very basic tensorflow program that adds one to a variable and uses a loop to run the addition ten times.


### 01-multiply.py
Multiply two matricies together.
```
input1 = [[3. , 5.]]
input2 = [[7.],[1.]]
```
The result should be 26.


### 02-xor-1d.py
Solve the xor problem using
```
input  = [[0,0],[1,1],[1,0],[0,1]]
output = [[0],  [0],  [1],  [1]]
```
And break the problem into the following layers
- the 1x2 input layer
- 2x3 + bias hidden sigmoid layer
- 3x1 + bias sigmoid output layer
- calculate loss as the sum of the squares of y - y_
- use gradient decent (set to 1.0) to minimize loss

Run iteratively 500 times and print all the variable data.


### 03-regularization.py
Add regularization to 02-xor-1d.py

One type of regularization is to minimize the values of the transformation matricies, such as the as the average or sum of the square of m1 and the square of m2.  The regularization term will need to be scaled to work with the loss term.  A scaling factor can be found experimentally.  Try multiplying your regularization by 0.01 to begin then experiment with different values.


### 04-xor-2d.py
Solve the xor problem using
```
input  = [[0.,0.],[1.,1.],[1.,0.],[0.,1.]]
output = [[1.,0.],[1.,0.],[0.,1.],[0.,1.]]
```


### 05-feed.py
Replicate 04-xor-2d, but instead of using constants for input and output, use feeds.


### 06-save.py
Improve 05-feed.py to save the session information at the end of training and to use the saved session information if it exists instead of training.


### 07-layers.py
Tensorflow has created helper functions called *tf.layers* that package up common combinations of tensors.  Use *tf.layers* to do the induction of xor.


### 08-rnn.py (optional)
Implement a recurrant neural net to accurately predict the next element in a series created by makeXY() in helper_make_xy.py

This creates a series X like [2,3,4,5] and Y = [6]. The series can be a forward progression, a reverse progression, or a constant.  The series may also contain 3, 4, or 5 elements.

An architecture that has been shown to work is:
- RNN Cell state size of 5
- 2 layers of RNN Cells
- a fully connected 5x10 output layer
- 20 * 500 iterations max
- basic cross entropy
- AdamOptimization(0.01)
- One training example at a time (no batch processing)

*Note* This is marked as optional because it is fairly advanced.  I'd recommend that you master all the previous challenges to **level 3** before adding this challenge to your curriculum
