from gym import env
from flearn.agent import RandomAgent

if __name__ =='__main__':

    env = gym.make('CartPole-v0')
    constant_agent = RandomAgent()
    constant_agent.interact(env, n_steps=500)