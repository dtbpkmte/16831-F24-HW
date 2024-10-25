import os

b_list = [10000, 30000, 50000]
r_list = [0.005, 0.01, 0.02]

# Base command
base_cmd = (
    "python rob831/scripts/run_hw2.py --env_name HalfCheetah-v4 --ep_len 150 "
    "--discount 0.95 -n 100 -l 2 -s 32 -b {b} -lr {r} -rtg --nn_baseline "
    "--exp_name q4_search_b{b}_lr{r}_rtg_nnbaseline"
)

for b in b_list:
    for r in r_list:
        print(f"Running: b = {b}, r = {r}")
        cmd = base_cmd.format(b=b, r=r)
        os.system(cmd)
