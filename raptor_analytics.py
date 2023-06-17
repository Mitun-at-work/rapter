import os
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_pdf import PdfPages
from rapter_manual import RaptorManual

# Chart Plotting Functions
class RaptorAnalytics:        
    def __init__(self, stockCode) -> None:
        self.stockCode = stockCode
        self.plots = []
        self.raptorManual = RaptorManual(stockCode= stockCode)
        self.imgDirectory = f"{os.curdir}/reports"

    # Creating charts to the data
    def createChart(
        self,
        stockData : dict,
    ) :
        def drawChart(
            plotTitle : str,
            investedAmount : list,
            intraDayProfits : list,
            deliveryProfits : list,
        ):
            plt.style.use("Solarize_Light2")
            sequenceLength = len(investedAmount)
            initialPoint, seondaryPoint, intrevalLength = 0, 3, 3
            while seondaryPoint <= sequenceLength : 
                # Framing Data
                plotData = {
                    "Investment" : investedAmount[ initialPoint : seondaryPoint ],
                    "IntraDay Profits" : intraDayProfits[ initialPoint : seondaryPoint ],
                    "Delivery Profits" : deliveryProfits[ initialPoint : seondaryPoint ],
                }
                # Framing Scales
                x = np.arange(3)  # the label locations
                width = 0.20  # the width of the bars
                multiplier = 0
                fig, ax = plt.subplots(layout='constrained')
                # Plotting Data
                for attribute, measurement in plotData.items():
                    offset = width * multiplier
                    rects = ax.bar(x + offset, measurement, width, label=attribute)
                    ax.bar_label(rects, padding=3)
                    multiplier += 1.5
                # ax.set_title(plotTitle)
                ax.set_title(plotTitle)
                ax.set_xticks(x + width, plotData["Investment"] )
                ax.legend(loc='upper left', ncols=3)
                ax.set_ylim(0, plotData['Investment'][0] + 2000)
                self.plots.append(fig)
                initialPoint += intrevalLength
                seondaryPoint += intrevalLength
                self.count +=1
        # Initialising & modifiying Inputs    
        # Iterating over the stock keys to frame the data
        for stockKeys in stockData.keys() :
            currentDict = stockData[stockKeys]
            investedAmount = [ x['Investment'] for  x in currentDict ]
            intraDayProfit = [ float(x['IntraDay Profits'].replace(',','')  ) for  x in currentDict ] 
            deliveryProfit = [ float(x['Delivery Profits'].replace(',','')  ) for  x in currentDict ]
            drawChart(
                plotTitle = stockKeys,
                investedAmount = investedAmount,
                intraDayProfits = intraDayProfit,
                deliveryProfits = deliveryProfit
            )
            self.raptorManual.generateManual(
                
            )
        with PdfPages(f'reports/{self.stockCode}.pdf') as pdf:
            for plot in self.plots:
                pdf.savefig(plot)
            return True
 