import random
import time
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import scipy.stats as stats
from scipy.stats import shapiro
import numpy as np

class DiceRoller:
    def __init__(self):
        self.function_results = []
        self.cumulative_counts = Counter()

    def generate_numbers(self):
        return [random.randint(1, 6) for _ in range(7)]

    def dist_of_means(self, results):
        mean_value = sum(results) / len(results)
        return round(mean_value, 4)

    def prob_plot(self, ax):
        mean_values = [d['mean'] for d in self.function_results]
        stats.probplot(mean_values, dist="norm", plot=ax)

    def p_value(self, results):
        _, p_value = shapiro(results)
        return round(p_value, 4)

    def original_dist(self, results):
        self.cumulative_counts.update(results)
        return self.cumulative_counts

    def update(self, frame):
        results = self.generate_numbers()
        mean = self.dist_of_means(results)
        p_value = self.p_value(results)
        original_dist = self.original_dist(results)

        self.function_results.append({
            'trials': results,
            'mean': mean,
            'p_value': p_value,
            'original_dist': original_dist
        })

        # Histogram for distribution of means
        ax1.clear()
        hist_data = [d['mean'] for d in self.function_results]
        ax1.hist(hist_data, bins=np.arange(min(hist_data), max(hist_data) + 0.5, 0.5), color='skyblue', edgecolor='black')
        ax1.set_title('distribution of means')

        # Q-Q Plot
        ax2.clear()
        self.prob_plot(ax2)
        ax2.set_title('Probability Plot')

        # Normality Test P-Value
        ax3.clear()
        ax3.text(0.5, 0.5, f"p-value: {p_value}", fontsize=15, ha='center', va='center')
        ax3.set_title('normality test p-value')
        ax3.axis('off')

        # Original Distribution of outputs
        ax4.clear()
        bar_width = 1  # You can adjust this value as needed
        ax4.bar(list(range(1, 7)), [original_dist[i] for i in range(1, 7)], width=bar_width,color='skyblue', edgecolor='black')
        ax4.set_title('distribution of outputs')

        # Trial Count
        ax5.clear()
        ax5.text(0.5, 0.5, f"Trial Count: {len(self.function_results)}", fontsize=15, ha='center', va='center')
        ax5.axis('off')
        plt.draw()

    def run(self):
        fig = plt.figure(figsize=(18, 10))
        gs = fig.add_gridspec(2, 3)


        global ax1, ax2, ax3, ax4, ax5
        ax1 = fig.add_subplot(gs[0, 0])
        ax2 = fig.add_subplot(gs[0, 1])
        ax3 = fig.add_subplot(gs[1, 0])
        ax4 = fig.add_subplot(gs[:, 2])
        ax5 = fig.add_subplot(gs[1, 1])

        ani = FuncAnimation(fig, self.update, interval=500)
        plt.show()


dice_roller = DiceRoller()
dice_roller.run()
