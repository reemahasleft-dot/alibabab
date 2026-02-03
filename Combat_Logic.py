I must clarify that creating a custom neural network input prediction algorithm for an NVIDIA RTX 5080 GPU in C++ would require a deep understanding of computer vision, machine learning, and GPU programming. Moreover, achieving a 500x reaction speed improvement compared to the baseline is a challenging task.

That being said, I'll provide you with a high-level outline of the steps involved in creating such an algorithm:

**Step 1: Data Collection and Preprocessing**

* Collect a dataset of input images and corresponding neural network predictions.
* Preprocess the data by resizing images, normalizing pixel values, and converting them to a suitable format for training.

**Step 2: Neural Network Architecture Design**

* Design a neural network architecture that can learn patterns in the input images and predict the corresponding neural network outputs.
* Consider using convolutional neural networks (CNNs) or recurrent neural networks (RNNs) depending on the nature of your data.

**Step 3: Training the Neural Network**

* Train the neural network using the collected dataset and a suitable optimization algorithm (e.g., stochastic gradient descent, Adam).
* Use a suitable loss function to measure the difference between predicted outputs and actual outputs.
* Monitor training progress and adjust hyperparameters as needed.

**Step 4: Implementing the Prediction Algorithm in C++**

* Write a C++ program that loads the trained neural network model and uses it to predict outputs for new input images.
* Utilize NVIDIA's CUDA toolkit to optimize your code for execution on an NVIDIA GPU, such as the RTX 5080.

**Step 5: Optimizing the Prediction Algorithm**

* Use NVIDIA's cuDNN library to accelerate neural network operations on the GPU.
* Optimize your code using techniques like loop unrolling