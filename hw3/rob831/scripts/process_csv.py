import pandas as pd


def process_csv(csv_files, output_name):
    value_series = [pd.read_csv(file)["Value"] for file in csv_files]

    values_df = pd.concat(value_series, axis=1)
    values_df.columns = ["Value1", "Value2", "Value3"]

    step_column = pd.read_csv(csv_files[0])["Step"]

    values_df["Average"] = values_df.mean(axis=1)
    values_df["Std"] = values_df.std(axis=1)

    result_df = pd.DataFrame({
        "Step": step_column,
        "Average": values_df["Average"],
        "Std": values_df["Std"]
    })

    result_df.to_csv(output_name, index=False)


if __name__ == "__main__":
    csv_files_1 = [
        "raw_csv/run-q1_doubledqn_1_LunarLander-v3_30-10-2024_15-01-24-tag-Train_AverageReturn.csv",
        "raw_csv/run-q1_doubledqn_2_LunarLander-v3_31-10-2024_22-14-44-tag-Train_AverageReturn.csv",
        "raw_csv/run-q1_doubledqn_3_LunarLander-v3_30-10-2024_16-18-10-tag-Train_AverageReturn.csv"
    ]
    csv_files_2 = [
        "raw_csv/run-q1_doubledqn_1_LunarLander-v3_30-10-2024_15-01-24-tag-Train_BestReturn.csv",
        "raw_csv/run-q1_doubledqn_2_LunarLander-v3_31-10-2024_22-14-44-tag-Train_BestReturn.csv",
        "raw_csv/run-q1_doubledqn_3_LunarLander-v3_30-10-2024_16-18-10-tag-Train_BestReturn.csv"
    ]
    csv_files_3 = [
        "raw_csv/run-q1_dqn_1_LunarLander-v3_31-10-2024_16-23-29-tag-Train_AverageReturn.csv",
        "raw_csv/run-q1_dqn_2_LunarLander-v3_31-10-2024_22-24-01-tag-Train_AverageReturn.csv",
        "raw_csv/run-q1_dqn_3_LunarLander-v3_31-10-2024_22-32-37-tag-Train_AverageReturn.csv"
    ]
    csv_files_4 = [
        "raw_csv/run-q1_dqn_1_LunarLander-v3_31-10-2024_16-23-29-tag-Train_BestReturn.csv",
        "raw_csv/run-q1_dqn_2_LunarLander-v3_31-10-2024_22-24-01-tag-Train_BestReturn.csv",
        "raw_csv/run-q1_dqn_3_LunarLander-v3_31-10-2024_22-32-37-tag-Train_BestReturn.csv"
    ]
    process_csv(csv_files_1, "q1_doubledqn_average.csv")
    process_csv(csv_files_2, "q1_doubledqn_best.csv")
    process_csv(csv_files_3, "q1_dqn_average.csv")
    process_csv(csv_files_4, "q1_dqn_best.csv")
