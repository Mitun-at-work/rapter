import matplotlib.pyplot as plt 
import numpy as np

# Chart Plotting Functions
class RaptorCharts:
    def __init__(self) -> None:
        self.count = 1
        
    def drawChart(
        self,
        buyPrice,
        sellPrice,
        depositList,
        withdrawList,
        quantityList,
        profitList,
    ):
        
        # Framing Data
        dataScale = len(depositList)
        profitList = [withdrawList[i] - depositList[i] for i in range(dataScale)]
        plotData = {
            "Deposited Amount" : depositList,
            "Withdraw Amount" : withdrawList,
            "Profit Recieved" : profitList,
        }
        
        # Framing Scales
        x = np.arange(dataScale)  # the label locations
        width = 0.25  # the width of the bars
        multiplier = 0
        fig, ax = plt.subplots(layout='constrained',squeeze=True)
        
        # Plotting Data
        for attribute, measurement in plotData.items():
            offset = width * multiplier
            rects = ax.bar(x + offset, measurement, width, label=attribute)
            ax.bar_label(rects, padding=2)
            multiplier += 1

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_title(f'Buy Price : {buyPrice}  Sell Price : {sellPrice}')
        ax.set_xticks(x + width, plotData)
        ax.legend(loc='upper left', ncols=3)
        plt.savefig(f"img{self.count}")
        self.count +=1