import numpy as np
import os
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_pdf import PdfPages


# Chart Plotting Functions
class RaptorCharts:        
    def __init__(self, stockCode) -> None:
        self.stockCode = stockCode
        self.imgDirectory = f"{os.curdir}/reports"
        self.plots = []
        self.count = 1
        
        
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
                ax.set_xticks(x + width, plotData["Investment"] )
                ax.legend(loc='upper left', ncols=3)
                ax.set_ylim(0,investedAmount[initialPoint : seondaryPoint][0] + 2500)
                self.plots.append(fig)
                initialPoint += intrevalLength
                seondaryPoint += intrevalLength
                self.count +=1
                
            # Plotting the MatplotLib Graphs
            with PdfPages(f'reports/{self.stockCode}.pdf') as pdf:
                for plot in self.plots:
                    pdf.savefig(plot)
        
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
            print("Executed")
            return True
            
keys = {
    "0.75 - 0.8": [
        {
            "Investment": 10000,
            "Stocks Acquired": "13333",
            "IntraDay Profits": "650.63",
            "Delivery Profits": "574.59"
        },
        {
            "Investment": 9500,
            "Stocks Acquired": "12666",
            "IntraDay Profits": "618.08",
            "Delivery Profits": "542.39"
        },
        {
            "Investment": 9000,
            "Stocks Acquired": "12000",
            "IntraDay Profits": "585.58",
            "Delivery Profits": "510.24"
        },
        {
            "Investment": 8500,
            "Stocks Acquired": "11333",
            "IntraDay Profits": "553.03",
            "Delivery Profits": "478.04"
        },
        {
            "Investment": 8000,
            "Stocks Acquired": "10666",
            "IntraDay Profits": "520.48",
            "Delivery Profits": "445.84"
        },
        {
            "Investment": 7500,
            "Stocks Acquired": "10000",
            "IntraDay Profits": "487.98",
            "Delivery Profits": "413.69"
        },
        {
            "Investment": 7000,
            "Stocks Acquired": "9333",
            "IntraDay Profits": "455.44",
            "Delivery Profits": "381.50"
        },
        {
            "Investment": 6500,
            "Stocks Acquired": "8666",
            "IntraDay Profits": "422.89",
            "Delivery Profits": "349.31"
        },
        {
            "Investment": 6000,
            "Stocks Acquired": "8000",
            "IntraDay Profits": "390.38",
            "Delivery Profits": "317.15"
        },
        {
            "Investment": 5500,
            "Stocks Acquired": "7333",
            "IntraDay Profits": "357.83",
            "Delivery Profits": "284.95"
        },
        {
            "Investment": 5000,
            "Stocks Acquired": "6666",
            "IntraDay Profits": "325.28",
            "Delivery Profits": "252.75"
        },
        {
            "Investment": 4500,
            "Stocks Acquired": "6000",
            "IntraDay Profits": "292.78",
            "Delivery Profits": "220.60"
        },
        {
            "Investment": 4000,
            "Stocks Acquired": "5333",
            "IntraDay Profits": "260.23",
            "Delivery Profits": "188.40"
        },
        {
            "Investment": 3500,
            "Stocks Acquired": "4666",
            "IntraDay Profits": "227.68",
            "Delivery Profits": "156.21"
        },
        {
            "Investment": 3000,
            "Stocks Acquired": "4000",
            "IntraDay Profits": "195.19",
            "Delivery Profits": "124.06"
        },
        {
            "Investment": 2500,
            "Stocks Acquired": "3333",
            "IntraDay Profits": "162.63",
            "Delivery Profits": "91.85"
        },
        {
            "Investment": 2000,
            "Stocks Acquired": "2666",
            "IntraDay Profits": "130.10",
            "Delivery Profits": "59.67"
        },
        {
            "Investment": 1500,
            "Stocks Acquired": "2000",
            "IntraDay Profits": "97.59",
            "Delivery Profits": "27.51"
        },
        {
            "Investment": 1000,
            "Stocks Acquired": "1333",
            "IntraDay Profits": "65.05",
            "Delivery Profits": "-4.68"
        },
       
    ],} 
            
        
rapc = RaptorCharts(
    stockCode= "GTLINFRA",
)

rapc.createChart(stockData=keys)
