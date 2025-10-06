def generate_webgazer_dataframe(df):
    df1 = df[df["trial_type"] == "html-keyboard-response"]
    df_webgazer = df1[~df1["webgazer_data"].isna()]
    dfs = []
    for row in range(len(df_webgazer)):
        json_data = df_webgazer["webgazer_data"].iloc[row].replace("'", "\"")
        print(json_data)
        data_list = json.loads(json_data)
        df_tmp = pd.DataFrame(data_list)
        df_tmp["trial"] = row + 1
        dfs.append(df_tmp)
    return pd.concat(dfs)
