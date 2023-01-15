from gym_puyopuyo import register
register()

import gym


# env = gym.make("PuyoPuyoEndlessNormal-v2")
env = gym.make("PuyoPuyoEndlessBoxedNormal-v1")
# env = gym.make("PuyoPuyoEndlessBoxedSmall-v1")
# env = gym.make("PuyoPuyoEndlessSmall-v2")
# env = gym.make("PuyoPuyoEndlessTsu-v2")

env.reset()

obs_list = []
reward_list = []

for i in range(100):
    observation, reward, done, info = env.step(env.action_space.sample())
    obs_list.append(observation)
    reward_list.append(reward)
    print('---------------------------------------------------')
    print(f'action_apace:{env.action_space.n}')
    print(f"observation:{observation}")
    print(f"reward:{reward}")
    print(f"done:{done}")
    print(f"info:{info}")
    # if reward >=1:
    #     print(f'reward:{reward}')

    if done:
        break