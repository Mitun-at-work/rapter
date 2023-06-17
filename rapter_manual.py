import pandas as pd

class RaptorManual :
    def __init__(self, stockCode) -> None:
        self.stockCode = stockCode
        self.pandasDataFrame = []
        
    def generateManual(self,
                       stockKey : str,
                       investment : list[float],
                       intraDayProfits : list[float],
                       deliveryProfits : list[float],
                       ):
        initStart = 0
        initEnd = stockKey[stockKey.index('-')]
        sellPrice = initEnd + 1
        buyPrice, sellPrice = 1,1
        dataFrame = pd.DataFrame()
        dataFrame['Investment Amount']
        dataFrame['IntraDay Profit']
        dataFrame['Delivery Profit']
        dataFrame['Buy Price']
        dataFrame['Sell Price']
        dataFrame['Intra Profit Percentage']
        dataFrame['Delivery Profit Percentage']
        self.pandasDataFrame.append(dataFrame)
