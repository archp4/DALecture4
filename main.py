import pandas as pd
from data_plotting import plot_hist

admissions_df = pd.read_csv("./data/ADMISSIONS.csv")

# plot_hist(data=df, column="insurance", xLabel="Insurance", yLabel="Number of Patient",
#           title="Distribution of Patients per Insurance")
plot_hist(data=admissions_df, column="admission_type", xLabel="Admission Type", yLabel="Number of Patient",
          title="Admission Type of Patients")
