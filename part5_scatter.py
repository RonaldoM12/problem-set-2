'''
PART 5: SCATTER PLOTS
- Write functions for the tasks below
- Update main() in main.py to generate the plots and print statments when called
- All plots should be output as PNG files to `data/part5_plots`
'''
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Using lmplot, create a scatter plot where the x-axis is the prediction for felony and the y-axis the is prediction for a nonfelony, and hue this by whether the current charge is a felony. 
# 
# In a print statement, answer the following question: What can you say about the group of dots on the right side of the plot?
def scatterplot(df):
    sns.set(style="whitegrid")
    g = sns.lmplot(
        data= df,
        x= "p_felony",
        y="p_nonfelony",
        hue="has_felony_charge",
        fit_reg= False,
        height=6, 
        aspect=1
    )
    g.set_axis_labels("Predicted felony rearrest", "predicted non-felon rearrest")
    plt.title("Felony vs non-felony predictions by current felony charge")
    plt.savefig("./data/part5_plots/felony_vs_nonfelony.png")
    plt.close()

# 2. Create a scatterplot where the x-axis is prediction for felony rearrest and the y-axis is whether someone was actually rearrested.
# 
# In a print statement, answer the following question: Would you say based off of this plot if the model is calibrated or not?
def rearrest_scatterplot(df):
    sns.set(style="whitegrid")
    sns.scatterplot(
        data= df,
        x= "p_felony",
        y="p_nonfelony",
        alpha = 0.5

    )
    plt.xlabel("Predicted Probability of Felony Rearrest")
    plt.ylabel("Actual Felony rearrest (0 = No, 1 = Yes)")
    plt.title("Model Calibration: Predicted vs Actual Felony Rearrest")
    plt.savefig("./data/part5_plots/felony_prediction_vs_outcome.png")
    plt.close()

    print(
        "If the model is well-calibrated, we would expect to see a gradual increase in actual rearrest rates as the predicted probability increases.\n"
        "If the dots appear evenly scattered or inconsistent with the prediction values, the model may be poorly calibrated."
    )
