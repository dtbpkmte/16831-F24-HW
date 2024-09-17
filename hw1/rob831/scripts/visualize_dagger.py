import csv
import matplotlib.pyplot as plt


if __name__ == "__main__":
    # Ant-v2 plots
    avg_returns = []
    std_returns = []
    with open('p2_q2_ant_mean.csv', mode='r') as f:
        reader = csv.reader(f)
        next(reader)
        avg_returns = [float(row[2]) for row in reader]
    with open('p2_q2_ant_std.csv', mode='r') as f:
        reader = csv.reader(f)
        next(reader)
        std_returns = [float(row[2]) for row in reader]

    # Plot the results
    x = range(len(avg_returns))
    plt.errorbar(x,
                 avg_returns,
                 yerr=std_returns,
                 fmt='o',
                 color='r')
    plt.plot(x, avg_returns, marker='o', color='b', linestyle='-', linewidth=3)

    # Expert's average return and std
    expert_avg_return = 4713.65
    plt.axhline(y=expert_avg_return,
                color='green',
                linestyle='--',
                linewidth=3,
                label='Expert\'s average return')

    # BC agent's average return and std
    bc_avg_return = 4676.64
    plt.axhline(y=bc_avg_return,
                color='purple',
                linestyle='--',
                linewidth=3,
                label='BC agent\'s average return')

    # Add labels and title
    plt.xlabel('iter', fontsize=24)
    plt.ylabel('Mean return', fontsize=24)
    plt.legend(fontsize=24)
    plt.tick_params(axis='both', which='major', labelsize=24)

    # Humanoid-v2 plots
    plt.figure()
    avg_returns = []
    std_returns = []
    with open('p2_q2_humanoid_mean.csv', mode='r') as f:
        reader = csv.reader(f)
        next(reader)
        avg_returns = [float(row[2]) for row in reader]
    with open('p2_q2_humanoid_std.csv', mode='r') as f:
        reader = csv.reader(f)
        next(reader)
        std_returns = [float(row[2]) for row in reader]

    # Plot the results
    x = range(len(avg_returns))
    plt.errorbar(x,
                 avg_returns,
                 yerr=std_returns,
                 fmt='o',
                 color='r')
    plt.plot(x, avg_returns, marker='o', color='b', linestyle='-', linewidth=3)

    # Expert's average return and std
    expert_avg_return = 10344.51
    plt.axhline(y=expert_avg_return,
                color='green',
                linestyle='--',
                linewidth=3,
                label='Expert\'s average return')

    # BC agent's average return and std
    bc_avg_return = 246.28
    plt.axhline(y=bc_avg_return,
                color='purple',
                linestyle='--',
                linewidth=3,
                label='BC agent\'s average return')

    # Add labels and title
    plt.xlabel('iter', fontsize=24)
    plt.ylabel('Mean return', fontsize=24)
    plt.legend(fontsize=24)
    plt.tick_params(axis='both', which='major', labelsize=24)

    plt.show()
