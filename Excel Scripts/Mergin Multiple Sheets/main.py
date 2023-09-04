import pandas as pd


def merge_sheets(file_path, output_file_path):
    xls = pd.ExcelFile(file_path)
    df = pd.DataFrame()

    for sheet_name in xls.sheet_names:
        sheet_df = pd.read_excel(xls, sheet_name)
        df = df.append(sheet_df)
        df.to_excel(output_file_path, index=False)
