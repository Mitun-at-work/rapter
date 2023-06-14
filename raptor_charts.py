import matplotlib.pyplot as plt 
import numpy as np

# Chart Plotting Functions
class RaptorCharts:        
    
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
            
            sequenceLength = len(investedAmount)
            
            initialPoint, seondaryPoint, intrevalLength = 0, 5, 5
            
            while seondaryPoint <= sequenceLength : 
                # Framing Data
                dataScale = 5
                
                # Mapping the data recieved
                plotData = {
                    "Investment" : investedAmount[initialPoint : intrevalLength + 1],
                    "IntraDay Profits" : intraDayProfits[initialPoint : intrevalLength + 1],
                    "Delivery Profits" : deliveryProfits[initialPoint : intrevalLength + 1],
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
                ax.set_title(plotTitle)
                ax.set_xticks(x + width, plotData)
                ax.legend(loc='upper left', ncols=3)
                plt.savefig(f"demo.png")
                initialPoint += intrevalLength
                seondaryPoint += intrevalLength
        
        # Initialising & modifiying Inputs    
        # Iterating over the stock keys to frame the data
        for stockKeys in stockData.keys() :
            currentDict = stockData[stockKeys]
            investedAmount = [x['Investment'] for  x in currentDict]
            intraDayProfit = [ float(x['IntraDay Profits'].replace(',','')  ) for  x in currentDict] 
            deliveryProfit = [ float(x['Delivery Profits'].replace(',','')  ) for  x in currentDict]
            drawChart(
                plotTitle = stockKeys,
                investedAmount = investedAmount,
                intraDayProfits = intraDayProfit,
                deliveryProfits = deliveryProfit
            )
            
            
            
        
            