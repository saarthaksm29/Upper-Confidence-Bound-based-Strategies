import random
import math

period=int(input("Enter the time period: "))
alpha=int(input("Enter the value of alpha: "))
channel_vacancy={'1':0.20,'2':0.35,'3':0.50,'4':0.65,'5':0.95}
num_channel=[1,2,3,4,5]
channel_selected=random.choice(num_channel)
times_played = {'1':1,'2':1,'3':1,'4':1,'5':1}
reward_arms = {'1':0,'2':0,'3':0,'4':0,'5':0}
regret_arms = {'1':0,'2':0,'3':0,'4':0,'5':0}
X_bar = {'1':0,'2':0,'3':0,'4':0,'5':0}
A_bias = {'1':0,'2':0,'3':0,'4':0,'5':0}
B_index = {'1':0,'2':0,'3':0,'4':0,'5':0}
rnd=round(random.uniform(0,1),2)

a = 0
max_achievable = 0

for key,value in channel_vacancy.items():
    if value >= a:
        max_achievable = value
    else:
        max_achievable = a

vacant=0
t=len(num_channel)+1
particular_channel=[]

while t<period+1:
   particular_channel.append(channel_selected)
   z=[x for x in num_channel if x!=channel_selected]
   for ch in z:
       reward_arms[str(ch)] += 0
       X_bar[str(ch)] = reward_arms[str(ch)]/times_played[str(ch)]
       A_bias[str(ch)] = math.sqrt(alpha*math.log(t)/times_played[str(ch)])
       B_index[str(ch)] += X_bar[str(ch)]+A_bias[str(ch)]   
       if rnd<=channel_vacancy[str(channel_selected)]:
        vacant=1
        times_played[str(channel_selected)] += 1
        reward_arms[str(channel_selected)] += 1
        X_bar[str(channel_selected)] = reward_arms[str(channel_selected)]/times_played[str(channel_selected)]
        A_bias[str(channel_selected)] = math.sqrt(alpha*math.log(t)/times_played[str(channel_selected)])
        B_index[str(channel_selected)] += X_bar[str(channel_selected)]+A_bias[str(channel_selected)]       
        regret_arms[str(channel_selected)] += max_achievable - channel_vacancy[str(channel_selected)]      
        a=0 
        b=0
       for i in num_channel:
           if B_index[str(i)]>=a:
               a=B_index[str(i)]
               b=i
       channel_selected=b
       rnd=round(random.uniform(0,1),2)
       t+=1
   else:
       vacant=0
       times_played[str(channel_selected)] += 1
       reward_arms[str(channel_selected)] += 0
       X_bar[str(channel_selected)] = reward_arms[str(channel_selected)]/times_played[str(channel_selected)]
       A_bias[str(channel_selected)] = math.sqrt(alpha*math.log(t)/times_played[str(channel_selected)])
       B_index[str(channel_selected)] += X_bar[str(channel_selected)]+A_bias[str(channel_selected)]       
       regret_arms[str(channel_selected)] += max_achievable - 0       
       a=0 
       b=0
       for i in num_channel:
           if B_index[str(i)]>=a:
               a=B_index[str(i)]
               b=i
       channel_selected=b
       rnd=round(random.uniform(0,1),2)
       t+=1

print("The sum of rewards for each channel is: ",reward_arms)
print(particular_channel)
print("Number of times played for each channel is: ",times_played)
print("The B index for each channel is: ",B_index)
print(regret_arms)
print(max_achievable)

print("The mean sample of rewards is: ",X_bar)
print("The bias term for each channel is: ",A_bias)

for key,value in X_bar.items():
    X_bar[key]=value/times_played[key]

max_key=max(B_index,key=B_index.get)

################################REWARD_CALCULATION#############################
max_achievable=0.8
channel_rewards=[0.2,0.5,0.7,0.8,0.1]
regret=[]
for i in range(len(channel_rewards)):
        regret.append(max_achievable-channel_rewards[i])
print(regret)