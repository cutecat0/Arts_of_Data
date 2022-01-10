pip install gym
pip install pyglet

# Install additional packages for visualization
sudo apt-get install -y xvfb python-opengl > /dev/null 2>&1
pip install pyvirtualdisplay > /dev/null 2>&1
pip install git+https://github.com/tensorflow/docs > /dev/null 2>&1

参考文献：
https://blog.tensorflow.org/2018/07/deep-reinforcement-learning-keras-eager-execution.html

Asynchronous Advantage Actor Critic (A3C).

Learn how to train a model that is able to win at the simple game CartPole using deep reinforcement learning.
We’ll use tf.keras and OpenAI’s gym to train an agent using a technique known as Asynchronous Advantage Actor Critic (A3C).

