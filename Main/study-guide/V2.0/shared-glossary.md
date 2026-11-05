Shared Glossary
Babi Guling – AI Overview | Markdown V2.0 | 2026-11-05
This is the single glossary of the module. Each term has one meaning in all four chapters. The last column shows the chapters whose glossary lists the term. If you find a chapter that uses a term differently, change the chapter, not this file, and tell the team.
It lists 138 terms. It was built from the four chapter glossaries by a script that compares the wording; no term has two different wordings.
Term	Meaning	Chapters
A* search	An informed search that uses cost so far plus an estimate of the remaining cost.	2
Accuracy	The share of decisions that a model gets right on test examples.	1
Action	A choice the agent can make.	4
Activation function	The function that turns a neuron's sum into its output.	3
Admissible heuristic	An estimate of the remaining cost that never exceeds the true cost.	2
Agent	Something that perceives its environment and acts on it to reach a goal.	1, 4
Algorithm	A step-by-step procedure for solving a problem.	1
Alpha-beta pruning	A way to speed up minimax by skipping branches that cannot change the result.	2
Architecture	The pattern in which the neurons of a network are connected.	3
Artificial Intelligence (AI)	The field of making machines perform tasks that normally need intelligence.	1
Attention	A mechanism in which every part of the input weighs how much every other part matters.	3
Backpropagation	The method that works out each weight's share of the error.	3
Backward chaining	Reasoning that starts from a goal and looks for rules and facts that prove it.	2
Batch processing	Processing a large group of data at once, with a result after minutes or hours.	3
Bellman idea	The value of a state equals the immediate reward plus the discounted value of the next state.	4
Bias (fairness)	Unfair patterns in data or results.	3
Bias (in a neuron)	A number added to the weighted sum.	3
Big Data	Data too large, fast, or varied for ordinary tools.	3
Binary	A number system that uses only 0 and 1.	1
Binary search	A search on a sorted list that checks the middle item and discards half of the remaining items each time.	1
Bit	One binary digit, 0 or 1.	1
Breadth-first search	Search that explores all nodes at one depth before the next.	2
Break-even γ	The discount factor at which two choices have equal value.	4
Classification	Predicting a category for an item.	1
Clustering	Grouping similar items without labels.	1
CNN	Convolutional neural network, suited to images.	3
Computer Science (CS)	The study of computation, information, and computing systems.	1
Conflict resolution	A strategy for choosing which rule to use when two rules give different advice, such as priority, specificity, or recency.	2
Confusion matrix	A table that counts true positives, false negatives, false positives, and true negatives.	1
Contrapositive	The statement “if not q then not p”, which is equivalent to “if p then q”.	2
Converse	The statement “if q then p”, which is not equivalent to “if p then q”.	2
Credit assignment	Deciding which earlier action deserves credit for a later reward.	4
Data	Facts recorded in a form a computer can use.	1
Data lake / warehouse	Stores for raw data / for organised data used in reports.	3
Data pipeline	The steps from collecting data to analysing it: collect, clean, store, process, analyse.	3
Deep learning	Neural networks with many hidden layers.	3
Deep reinforcement learning	Reinforcement learning in which a neural network estimates the values or the policy.	4
Default knowledge	A fact assumed true unless an exception is known, such as "birds can fly".	2
Depth-first search	Search that follows one branch as deep as possible before backtracking.	2
Discount factor (γ)	A number between 0 and 1 that reduces the weight of future rewards.	4
Distributed file system	Storage that cuts files into blocks and keeps copies on many computers.	3
Embedding	A list of numbers that represents a word or an image so that similar items are close together.	3
Encoding	An agreement about which numbers stand for which letters, pictures, or sounds.	1
Environment	Everything the agent interacts with.	4
Episode	One run from start to finish.	4
Epoch	One pass through all the training examples.	3
Equivalent statements	Statements that have the same truth value in every row of the truth table.	2
ETL	Extract, transform, load: preparing data for analysis.	3
Exception	A case in which a general rule does not hold, such as a penguin among birds.	2
Expected value	The sum of (probability × reward) over the possible outcomes of an action.	4
Experience replay	Storing past experiences and learning from random samples of them.	4
Expert system	A system that copies the decision-making of a human expert in a narrow domain.	2
Exploitation	Choosing the action that looks best from what is already known.	4
Exploration	Trying an action that may turn out better.	4
F1 score	A single number that combines precision and recall.	1
Feature	A measurable property of an example that a model looks at, such as size or sourness.	1
Five Vs	Volume, velocity, variety, veracity, and value: the challenges of Big Data.	3
Forward chaining	Reasoning from known facts, applying rules until no new fact appears.	2
Forward pass	Sending an input through the layers of a network to get an output.	3
Frame	A data structure with slots describing a typical object or situation.	2
Game tree	A tree of the positions that can occur in a game, with a branch for each legal move.	2
Goal state	The state a search is trying to reach.	2
GOFAI	Good Old-Fashioned AI, another name for Symbolic AI.	2
Gradient descent	Repeated small weight changes that reduce the loss.	3
Heuristic	A rule of thumb that estimates how good a state or choice is.	2
Hidden layer	A layer between the input and the output of a neural network.	3
Hybrid system	A system that combines learned parts and hand-written rules.	3
Inference	Using a trained model on new input to get an output.	1
Inference engine	The part of a system that applies rules to knowledge to reach conclusions.	2
Inheritance	In a semantic network, passing a property from a general concept to a more specific one.	2
k-anonymity	A table where every combination of identifying-looking columns is shared by at least k people.	3
Knowledge base	The facts and rules that a symbolic system reasons with.	1, 2
Label	The correct answer attached to a training example.	1
Learning rate	The size of each step in gradient descent.	3
Linear search	A search that checks the items one by one.	1
Loss	A number that measures how wrong a prediction is.	3
Machine learning (ML)	A way for programs to improve at a task by learning from data.	1
MapReduce	A way to process big data in parallel by mapping then reducing.	3
Markov property	The next state depends only on the current state and action, not on the whole history.	4
MDP	Markov Decision Process: states, actions, transitions, rewards, and discount.	4
Model	What a machine-learning method produces by learning: numbers plus the procedure that turns an input into an output.	1
Modus ponens / tollens	Valid inference rules: from p → q and p conclude q; from p → q and ¬q conclude ¬p.	2
Narrow AI	An AI system that is good at specific tasks only.	1
Nearest neighbour	A simple learning method that gives a new item the label of the most similar training example.	1
Neural network	A model made of connected neurons arranged in layers.	3
NoSQL database	A database that stores flexible data (key-value, document, column, or graph) instead of fixed tables.	3
Ontology	A formal description of the concepts in a domain and how they relate.	2
Overfitting	When a model has memorised its training examples and does not work well on new ones.	1, 3
Parameter	A number the network learns, such as a weight or a bias.	3
Pattern matching	Comparing text with a template to decide which rule applies.	2
Perceptron rule	Change each weight by (target − output) × input whenever the neuron is wrong.	3
Pixel	One tiny square of a picture.	1
Policy	A rule that chooses an action in each state.	4
Precision	Of the items a model called positive, the share that really were positive.	1
Predicate	A statement with variables that is true or false depending on their values.	2
Proposition	A sentence that is either true or false.	2
Q-learning	A value-based RL method that learns Q(s, a).	4
Q-value	Q(state, action): how good it is to take that action in that state.	4
Quantifier	∀ ("for all") or ∃ ("there exists").	2
Quasi-identifier	A column such as ZIP code or birth year that does not name a person but can help identify one when combined.	3
Re-identification	Finding out who a record belongs to by combining facts in a dataset without names.	3
Recall	Of the items that really were positive, the share that the model found.	1
Regression	Predicting a number.	1
Reinforcement learning	Learning to act by receiving rewards.	1
ReLU	An activation function that gives 0 for negative numbers and the number itself for positive ones.	3
Return	The total future reward an agent tries to maximise, usually discounted by γ.	4
Reward	A number that tells an agent how good the result of its last action was.	1, 4
Reward hacking	Raising the reward by exploiting a loophole instead of doing the intended task.	4
RLHF	Reinforcement learning from human feedback: human rankings or ratings serve as the reward.	4
Rule	An IF–THEN statement written by a person.	1
Rule-based system	A system whose knowledge is a set of IF–THEN rules that an inference engine applies.	2
Sample inefficiency	The need for a very large number of trials before an agent learns well.	4
SARSA	A Q-learning variant that updates with the action the agent actually takes next.	4
Script	A sequence of frames describing a typical event.	2
Self-play	An agent improves by playing against copies of itself.	4
Semantic network	A graph of concepts (nodes) and relationships (links).	2
Sigmoid	A smooth activation function that gives values between 0 and 1.	3
Simulation gap	The difference between a simulated world and the real world, which can make learned skills fail.	4
State	A complete description of the situation at one moment, for example in a search problem (Chapter 2) or a reinforcement learning problem (Chapter 4).	2, 4
State space	The set of all states a system can be in.	2
Stream processing	Processing each event as it arrives, with a result in seconds or less.	3
Subsumption architecture	A robot design with layers of simple behaviours, where higher-priority layers override lower ones.	4
Supervised learning	Learning from labelled examples.	1
Test data	Examples kept apart from training, used to check a model.	1
Test set	Data that the model never saw during training, used for a fair final check.	3
Training	Adjusting a model, using examples or rewards, so that it does a task better.	1
Training example	One piece of data used to teach a model.	1
Transfer learning	Starting from a model trained on a big task and adjusting it to a smaller one.	3
Transformer	A network architecture based on attention, used in language models.	3
Transition	The chance of reaching each next state after an action.	4
Unsupervised learning	Finding structure in data that has no labels.	1
Validation data	Examples kept apart from training, used to tune a model and decide when to stop.	3
Value	Expected total future reward.	4
Value iteration	Computing the value of every state by repeating the Bellman update until the values stop changing.	4
Vanishing gradient	A problem in which the slope shrinks as it is passed back through many layers, so early layers learn very slowly.	3
Weight	The strength of a connection between two neurons.	3
XOR	"Exclusive or": true when exactly one of two inputs is true.	3
ε-greedy	With probability ε pick a random action, otherwise pick the best-known one.	4
