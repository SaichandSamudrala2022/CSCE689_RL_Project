import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
#import seaborn as sns
mpl.style.use('seaborn')

def running_avg(arr,window):
    running_avg = np.zeros(len(arr))
    std_dev = np.zeros(len(arr))
    for i in range(len(running_avg)):
        running_avg[i] = np.mean(arr[max(0, i-window):(i+1)])
        std_dev[i] = np.std(arr[max(0, i-window):(i+1)])
    return running_avg, std_dev

RL_algos = ['DQN','PPO','A2C','TRPO']
rews = {}
rts = {}

for idx in range(10):
    rts[idx]={}
    rews[idx] = {}
    #plt.figure()
    for RL_algo in RL_algos:
        if RL_algo == 'DQN':
            with open("../GlobalRoutingRL/logs/"+RL_algo+"_benchmark_"+str(idx+1),'r') as f:
                lines = f.readlines()
        else:
            with open("./logs/"+RL_algo+"_benchmark_"+str(idx+1),'r') as f:
                lines = f.readlines()
        
        rts[idx][RL_algo] = None
        rews[idx][RL_algo]= []
        for i in range(len((lines))):
            if "Reward: " in lines[i]:
                rews[idx][RL_algo].append(float(lines[i].split(":")[-1].strip()))
            elif "Runtime: " in lines[i]:
                rts[idx][RL_algo] = np.around(float(lines[i].split(":")[-1].strip()),2)
        '''
        #plt.plot(rews[idx],label=RL_algo)
        runn_avg, std_dev = running_avg(rews[idx][RL_algo],100)
        plt.plot(runn_avg,label=RL_algo)
        plt.fill_between(range(len(runn_avg)),runn_avg+std_dev,runn_avg-std_dev,alpha=0.3)
        #sns.lineplot(data=rews[idx], errorbar='sd')
        '''
    '''
    plt.legend(loc='lower right')
    plt.title("Benchmark"+str(idx+1))
    plt.xlabel("Episode")
    plt.ylabel("Reward")
    plt.savefig("./logs/Benchmark"+str(idx+1)+"_reward_plots.pdf")
    '''
#print(rts)


fig, axs = plt.subplots(2, 5,sharey=True,sharex=True, figsize=(10,4))
idx = 0
#print(rews[0])
for ax in axs.flat:
    ax.set_title("Benchmark"+str(idx+1))
    for RL_algo in rews[idx]:
        runn_avg, std_dev = running_avg(rews[idx][RL_algo],100)
        if idx == 0:
            ax.plot(runn_avg,label=RL_algo)
            ax.fill_between(range(len(runn_avg)),runn_avg+std_dev,runn_avg-std_dev,alpha=0.3)
        else:
            ax.plot(runn_avg)
            ax.fill_between(range(len(runn_avg)),runn_avg+std_dev,runn_avg-std_dev,alpha=0.3)
    idx+=1

fig.text(0.5, 0.01, 'Episodes', ha='center')
fig.text(0.04, 0.5, 'Reward', va='center', rotation='vertical')
fig.legend(loc='upper center',ncol=len(RL_algos))
plt.savefig("./logs/all_benchmarks_reward_plots.pdf")
    