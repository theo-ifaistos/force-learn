from abc import abstractmethod

class BaseAgent:
    """
    Base class for RL agents.
    """

    @abstractmethod
    def _interact(self, env, observation, reward):
        pass

    def _learn(self, env, observation, reward):
        return self

    def interact(self, env, learn=True, render=True, **interaction_params):
        self.steps_results_ = [(env.reset(), 0.0, False, {})]
        for _ in range(interaction_params['n_steps']):
            if render:
                env.render()
            observation, reward, *_ = self.steps_results_[-1]
            if learn:
                self._learn(env, observation, reward)
            action = self._interact(env, observation, reward)
            step_result = env.step(action)
            self.steps_results_.append(step_result)
            *_, done, _ = step_result
            if done:
                self.steps_results_.append((env.reset(), 0.0, False, {}))
        env.close()
        return self


class RandomAgent(BaseAgent):
    """An agent taking random actions."""

    def _interact(self, env, observation, reward):
        return env.action_space.sample()


class ConstantAgent(BaseAgent):
    """An agent taking constant actions."""

    def __init__(self, action):
        self.action = action

    def _interact(self, env, observation, reward):
        return self.action
