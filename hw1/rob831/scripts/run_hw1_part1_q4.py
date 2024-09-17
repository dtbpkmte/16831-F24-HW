import csv
import matplotlib.pyplot as plt
from run_hw1 import main


if __name__ == "__main__":
    # This file runs run_hw1 for the Ant-v2 environment with varying
    # number of training steps to see how this hyperparameter affects
    # the BC agent's performance.
    train_steps = list(range(1, 50, 10)) + \
                  list(range(50, 1000, 100)) + \
                  list(range(1000, 15000, 1000)) + \
                  list(range(15000, 50000, 5000))

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--run_exp', action='store_true')
    args = parser.parse_args()

    if args.run_exp:
        print("Experiment mode")
        for s in train_steps:
            main(['--expert_policy_file', 'rob831/policies/experts/Ant.pkl',
                  '--env_name', 'Ant-v2',
                  '--exp_name', 'bc_ant',
                  '--n_iter', '1',
                  '--expert_data', 'rob831/expert_data/expert_data_Ant-v2.pkl',
                  '--video_log_freq', '-1',
                  '--ep_len', '1000',
                  '--num_agent_train_steps_per_iter', str(s),
                  '--eval_batch_size', '10000'])
    else:
        print("Visualization mode")
        avg_returns = []
        std_returns = []
        with open('p1_q4.csv', mode='r') as f:
            reader = csv.reader(f)
            for row in reader:
                avg_returns.append(float(row[0]))
                std_returns.append(float(row[1]))

        # Plot the results
        # plt.bar(train_steps, avg_returns, width=1, color='b')
        plt.errorbar(train_steps,
                     avg_returns,
                     yerr=std_returns,
                     fmt='o',
                     color='r')
        plt.plot(train_steps, avg_returns, marker='o', color='b', linestyle='-')

        # Expert's average return and std
        expert_avg_return = 4713.65
        expert_std_return = 12.2
        plt.axhline(y=expert_avg_return, color='green', linestyle='--', label='Expert\'s average return')
        plt.fill_between(train_steps,
                         expert_avg_return - expert_std_return,
                         expert_avg_return + expert_std_return,
                         color='green', alpha=0.5)

        # Add labels and title
        plt.xlabel('num_agent_train_steps_per_iter', fontsize=20)
        plt.ylabel('Mean Values', fontsize=20)
        plt.legend(fontsize=20)
        plt.tick_params(axis='both', which='major', labelsize=20)

        plt.show()
