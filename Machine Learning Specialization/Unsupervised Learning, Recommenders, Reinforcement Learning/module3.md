# Reinforcement Learning Introduction

Let's start with an example. Let's say we have an autonomous helicopter and we want to make it fly by itself.

We can't use supervised learning since there is a lot of states (like the position, velocity, distance to objects) and actions to take (the ideal y)

* **Reward function**: a function that tells the helicopter how when it's doing well and when it's doing poorly

It's like training a dog. When it does something good, you say "good dog". Otherwise, you say "bad dog". Hopefully, it learns to do more of the good dog things and fewer of the bad dog things

It's a powerful algorithm since you have to tell it what to do rather than how to do it and specifying the reward function rather than the optimal action gives you a lot more flexibility in how you design the system

There are positive rewards and negative ones. When the helicopter flies well, you give it +1 "points"

When it flies poorly, you remove 1000 "points"

### Applications

* **Controlling robots**

* **Factory Optimization**

* **Financial (stock) trading**

* **Playing games**

Let's have as an example a simplified Mars Rover

Let's say the state 1 is more valuable for the scientists than the state 6, because they want the robot to sample more from that surface. The scientists are not interest in the other states. So, for instance, the state 1 has a reward of 100, state 6 has a reward of 40 and all the other ones have a reward of 0. But, since we started at state 4, the state 6 is closer to the robot

In each position, the robot can go to the left or to the right

Futhermore, we are going to call states 1 and 6 **terminal states**, that is, after the robot gets to one of these terminals, nothing more happens

The robot could go to the left, then to the right, then to the left and, after some time, decides to go to a terminal state and get its reward. He would do it because it doesn't change its points doing unnecessary moves since the reward of states 2, ..., 5 is 0

* **S**: the current state of the robot

* **a**: an action that the robot can take

* **R(s)**: a reward that the robot will take going to state S

* **S'**: new state the robot will be if it takes action a at state S

![mars-rover-example](./assets/module3/mars-rover-example1.png)

## Return

The concept of a return captures that rewards that you can get quicker are maybe more attractive than rewards that take you a long time to get to

* **Discount Factor γ**: it's a number a little bit less than 1 that the algorithm will weight each reward that you take powered by the how many actions you took so far. It makes the algorithm a little bit more impacient. So, getting rewards sooner results in a higher value for the total sum

    * Usually, it's 0.9, 0.99, 0.999

    * In financial case, the discount factor could be interpret as the "interest rate"

![mars-rover-example](./assets/module3/mars-rover-example2.png)

![mars-rover-example](./assets/module3/mars-rover-example3.png)

In the fist case above, we always go to the left. Starting at the state, we would get a return of 50

In the second case, we always go to the right

In the third case, what action we should take depends on the state that we start at. If we start at state 2, 3 or 4, we go to the left. If we start at state at 5, we go to the right

A state reward could be negative. So, the discount factor incentivizes the system to push out the negative rewards as far into the future as possible

Our **goal** is to come up with a function, which is called a **policy π**, whose job it is to take as input any state s and map it to some action a that it wants us to take

Find a policy π that tells you what action (a = π(s)) to take in every state s so as to maximize the return

### Examples

![reinforcement-examples](./assets/module3/reinforcement-examples.png)

The formalism above is called **Markov Decision Process (MDP)**

In Markov Decision Process, the future depends only where you are now not on how you got at the current state

The robot is our example could be called **agent**. If it takes an action a, something will happen in the **environment**

![markov-decision-process-diagram](./assets/module3/markov-decision-process.png)