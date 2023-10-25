# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hindsight']

package_data = \
{'': ['*']}

install_requires = \
['einops', 'torch']

setup_kwargs = {
    'name': 'hindsight-replay',
    'version': '0.0.1',
    'description': 'Hindsight - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n# Hindsight Experience Replay (HER)\n=================================\n\nHindsight Experience Replay (HER) is a reinforcement learning technique that makes use of failed experiences to learn how to achieve goals. It does this by storing additional transitions in the replay buffer where the goal is replaced with the achieved state. This allows the agent to learn from a hindsight perspective, as if it had intended to reach the achieved state from the beginning.\n\n## Implementation\n--------------\n\nThis repository contains a Python implementation of HER using PyTorch. The main class is\xa0`HindsightExperienceReplay`, which represents a replay buffer that stores transitions and allows for sampling mini-batches of transitions.\n\nThe\xa0`HindsightExperienceReplay`\xa0class takes the following arguments:\n\n-   `state_dim`: The dimension of the state space.\n-   `action_dim`: The dimension of the action space.\n-   `buffer_size`: The maximum size of the replay buffer.\n-   `batch_size`: The size of the mini-batches to sample.\n-   `goal_sampling_strategy`: A function that takes a tensor of goals and returns a tensor of goals. This function is used to dynamically sample goals for replay.\n\nThe\xa0`HindsightExperienceReplay`\xa0class has the following methods:\n\n-   `store_transition(state, action, reward, next_state, done, goal)`: Stores a transition and an additional transition where the goal is replaced with the achieved state in the replay buffer.\n-   `sample()`: Samples a mini-batch of transitions from the replay buffer and applies the goal sampling strategy to the goals.\n-   `__len__()`: Returns the current size of the replay buffer.\n\n## Usage\n-----\n\nHere is an example of how to use the\xa0`HindsightExperienceReplay`\xa0class:\n\n```python\n# Define a goal sampling strategy\ndef goal_sampling_strategy(goals):\n    noise = torch.randn_like(goals) * 0.1\n    return goals + noise\n\n# Define the dimensions of the state and action spaces, the buffer size, and the batch size\nstate_dim = 10\naction_dim = 2\nbuffer_size = 10000\nbatch_size = 64\n\n# Create an instance of the HindsightExperienceReplay class\nher = HindsightExperienceReplay(state_dim, action_dim, buffer_size, batch_size, goal_sampling_strategy)\n\n# Store a transition\nstate = np.random.rand(state_dim)\naction = np.random.rand(action_dim)\nreward = np.random.rand()\nnext_state = np.random.rand(state_dim)\ndone = False\ngoal = np.random.rand(state_dim)\nher.store_transition(state, action, reward, next_state, done, goal)\n\n# Sample a mini-batch of transitions\nsampled_transitions = her.sample()\nif sampled_transitions is not None:\n    states, actions, rewards, next_states, dones, goals = sampled_transitions\n```\n\n\nIn this example, we first define a goal sampling strategy function and the dimensions of the state and action spaces, the buffer size, and the batch size. We then create an instance of the\xa0`HindsightExperienceReplay`\xa0class, store a transition, and sample a mini-batch of transitions. The states, actions, rewards, next states, done flags, and goals are returned as separate tensors.\n\n## Customizing the Goal Sampling Strategy\n--------------------------------------\n\nThe\xa0`HindsightExperienceReplay`\xa0class allows you to define your own goal sampling strategy by passing a function to the constructor. This function should take a tensor of goals and return a tensor of goals.\n\nHere is an example of a goal sampling strategy function that adds random noise to the goals:\n\n```\ndef goal_sampling_strategy(goals):\n    noise = torch.randn_like(goals) * 0.1\n    return goals + noise\n```\n\nIn this example, the function adds Gaussian noise with a standard deviation of 0.1 to the goals. You can customize this function to implement any goal sampling strategy that suits your needs.\n\n## Contributing\n------------\n\nContributions to this project are welcome. If you find a bug or think of a feature that would be nice to have, please open an issue. If you want to contribute code, please fork the repository and submit a pull request.\n\n## License\n-------\n\nThis project is licensed under the MIT License. See the\xa0[LICENSE](https://domain.apac.ai/LICENSE)\xa0file for details.',
    'author': 'Kye Gomez',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/HindsightReplay',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
