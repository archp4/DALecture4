import pandas as pd
from data_plotting import plot_hist
from data_transformation import replace_missing_value_with_mean

admissions_df = pd.read_csv("./data/ADMISSIONS.csv", parse_dates=['admittime'])


# plot_hist(data=df, column="insurance", xLabel="Insurance", yLabel="Number of Patient",
#           title="Distribution of Patients per Insurance")
plot_hist(data=admissions_df, column="admission_type", xLabel="Admission Type", yLabel="Number of Patient",
          title="Admission Type of Patients")


chartEvent_df = pd.read_csv("./data/CHARTEVENTS.csv", low_memory=False)

# Transforming Data // pivoting table // rotating table by switch column value to column title
pivoted_chartEvents = pd.pivot_table(
    data=chartEvent_df,
    index=['hadm_id', 'charttime'],
    columns=['itemid'],
    values='valuenum'
).reset_index() # reset index will
#
# # Saving DF as CSV
# new_formated_chartEvents.to_csv("Formated_CHARTEVENTS.csv", index=True)

# To replace missing we can is avg of column to replace missing value if value based column we used mean if category based column use mod

# mean for column
# print(admissions_df['hospital_expire_flag'].value_counts())
#
# mod


print("--------------------------------------------------------------------------------------------")

# Merging to table
merged_df = pd.merge(left=admissions_df,right=pivoted_chartEvents,on=["hadm_id"], how="inner")
# merged_df.to_csv("merged_data.csv")

print(merged_df['hospital_expire_flag'].value_counts())

print(merged_df['22045'].isnull().values().any())

merged_df = replace_missing_value_with_mean(merged_df, label='hospital_expire_flag', column=2)

print(merged_df['hospital_expire_flag'].head(50))
