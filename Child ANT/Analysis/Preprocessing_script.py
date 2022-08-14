# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import sem

# Read file path
filename = "../data/999_childANT_2022.csv"


# Skip rows that correspond to practise trials (1-25 rows)
rows_to_skip = [*range(1, 26, 1)]


# Read the main file
datafile = pd.read_csv(filename, skiprows= rows_to_skip)


# Keep only necessary columns
columns_to_keep = ["Cue",
                   "Target_side",
                   "response.corr",
                   "response.rt",
                   "participant"]

datafile = datafile[datafile.columns[datafile.columns.isin(columns_to_keep)]]


# Remove rows where Accuracy = 0, as they are not included in the calculation
# of reaction times (RT)
RT_df = datafile[datafile["response.corr"] == 1]
descriptives = ['min', 'max', 'median', 'std', 'sem']
scores = RT_df.groupby("Cue")["response.rt"].agg(descriptives)

# Calculate Alerting Network score: RT for No Cue - RT for Double Cue Trials
no_cue_RT = scores.iloc[2,2]
double_cue_RT = scores.iloc[1,2]
alerting_RT_median = no_cue_RT - double_cue_RT

# Visualize Alerting Network scores
fig = plt.figure(figsize = (11, 6))
plt.bar(scores.index ,
        scores.iloc[:,2],
        color ='maroon',
        yerr = scores.iloc[:,4],
        width = 0.4,
        capsize = 10)

plt.xlabel("Condition")
plt.ylabel("Reaction Time (in ms)")
plt.title("Alerting network score")
plt.show()

# Calculate Orienting Network score: RT for Central Cue - RT for Spatial Cue
central_cue_RT = scores.iloc[0,2]
spatial_cue_RT = scores.iloc[3,2]
orienting_RT_median = central_cue_RT - spatial_cue_RT

# Calculate Executive Network score: RT for Incogruent - RT for Congruent
executive =  RT_df.groupby("Target_side")["response.rt"].agg(descriptives)

congruent_RT = executive.iloc[0,2]
incogruent_RT = executive.iloc[1,2]
executive_RT_median = incogruent_RT - congruent_RT

#TO DO: Add calculation for alerting network.
