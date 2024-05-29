import pandas as pd
from data_plotting import plot_hist

admissions_df = pd.read_csv("./data/ADMISSIONS.csv")

# plot_hist(data=df, column="insurance", xLabel="Insurance", yLabel="Number of Patient",
#           title="Distribution of Patients per Insurance")
plot_hist(data=admissions_df, column="admission_type", xLabel="Admission Type", yLabel="Number of Patient",
          title="Admission Type of Patients")


chartEvent_df = pd.read_csv("./data/CHARTEVENTS.csv", low_memory=False)

# Transforming Data // pivoting table // rotating table by switch column value to column title
new_formated_chartEvents = pd.pivot_table(
    data=chartEvent_df,
    index=['hadm_id', 'charttime'],
    columns=['itemid'],
    values='valuenum'
)

# Saving DF as CSV
new_formated_chartEvents.to_csv("Formated_CHARTEVENTS.csv", index=True)
