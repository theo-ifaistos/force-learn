from gym import env
from flearn.agent import ConstantAgent

if __name__ =='__main__':

    env = gym.make('CartPole-v0')
    constant_agent = ConstantAgent(action=1)
    constant_agent.interact(env, n_steps=500)