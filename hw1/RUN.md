#1. Behavioral Cloning

##Question 2:

###Ant-v2:
```
python rob831/scripts/run_hw1.py \
--expert_policy_file rob831/policies/experts/Ant.pkl \
--env_name Ant-v2 --exp_name bc_ant --n_iter 1 \
--expert_data rob831/expert_data/expert_data_Ant-v2.pkl \
--video_log_freq -1 \
--ep_len 1000
```

###Humanoid-v2:
```
python rob831/scripts/run_hw1.py \
--expert_policy_file rob831/policies/experts/Humanoid.pkl \
--env_name Humanoid-v2 --exp_name bc_humanoid --n_iter 1 \
--expert_data rob831/expert_data/expert_data_Humanoid-v2.pkl \
--video_log_freq -1 \
--ep_len 1000
```

###Walker2d-v2:
```
python rob831/scripts/run_hw1.py \
--expert_policy_file rob831/policies/experts/Walker2d.pkl \
--env_name Walker2d-v2 --exp_name bc_walker2d --n_iter 1 \
--expert_data rob831/expert_data/expert_data_Walker2d-v2.pkl \
--video_log_freq -1 \
--ep_len 1000
```

###Hopper-v2:
```
python rob831/scripts/run_hw1.py \
--expert_policy_file rob831/policies/experts/Hopper.pkl \
--env_name Hopper-v2 --exp_name bc_hopper --n_iter 1 \
--expert_data rob831/expert_data/expert_data_Hopper-v2.pkl \
--video_log_freq -1 \
--ep_len 1000
```

###HalfCheetah-v2:
```
python rob831/scripts/run_hw1.py \
--expert_policy_file rob831/policies/experts/HalfCheetah.pkl \
--env_name HalfCheetah-v2 --exp_name bc_halfcheetah --n_iter 1 \
--expert_data rob831/expert_data/expert_data_HalfCheetah-v2.pkl \
--video_log_freq -1 \
--ep_len 1000
```

##Question 3:

###Ant-v2:
```
python rob831/scripts/run_hw1.py \
--expert_policy_file rob831/policies/experts/Ant.pkl \
--env_name Ant-v2 --exp_name bc_ant --n_iter 1 \
--expert_data rob831/expert_data/expert_data_Ant-v2.pkl \
--video_log_freq -1 \
--ep_len 1000 \
--num_agent_train_steps_per_iter 1000 \
--eval_batch_size 5000
```

###Humanoid-v2:
```
python rob831/scripts/run_hw1.py \
--expert_policy_file rob831/policies/experts/Humanoid.pkl \
--env_name Humanoid-v2 --exp_name bc_humanoid --n_iter 1 \
--expert_data rob831/expert_data/expert_data_Humanoid-v2.pkl \
--video_log_freq -1 \
--ep_len 1000 \
--num_agent_train_steps_per_iter 1000 \
--eval_batch_size 5000
```

##Question 4:

To run experiments with varying `num_agent_train_steps_per_iter`:
```
python rob831/scripts/run_hw1_part1_q4.py --run_exp
```

To visualize the results:
```
python rob831/scripts/run_hw1_part1_q4.py
```

#2. DAgger
###Ant-v2:
```
python rob831/scripts/run_hw1.py \
--expert_policy_file rob831/policies/experts/Ant.pkl \
--env_name Ant-v2 --exp_name dagger_ant --n_iter 10 \
--do_dagger --expert_data rob831/expert_data/expert_data_Ant-v2.pkl \
--video_log_freq -1 \
--ep_len 1000 \
--num_agent_train_steps_per_iter 500 \
--eval_batch_size 10000
```

###Humanoid-v2:
```
python rob831/scripts/run_hw1.py \
--expert_policy_file rob831/policies/experts/Humanoid.pkl \
--env_name Humanoid-v2 --exp_name dagger_humanoid --n_iter 40 \
--do_dagger --expert_data rob831/expert_data/expert_data_Humanoid-v2.pkl \
--video_log_freq -1 \
--ep_len 1000 \
--num_agent_train_steps_per_iter 1000 \
--eval_batch_size 10000
```

###To generate 2 plots for question 2:
``
python rob831/scripts/visualize_dagger.py
```
