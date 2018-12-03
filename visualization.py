import utils
import seaborn as sns
import matplotlib.pyplot as plt


data = utils.get_data()

# Find the correlations between each pair of features with pairplot
sns.pairplot(data)
plt.show()

# TODO KHALED
