# Importing packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from banner import RapterBanner
from raptor_charts import RaptorCharts

# Rapter Class declaration
class Rapter:
    def __init__(self, stockCode) -> None:
        RapterBanner()
        # Declaring baseUrl and stockcodes
        self.targetUrl =  "https://upstox.com/calculator/brokerage-calculator/"
        self.stockCode = stockCode
        self.yfinanceCode = f"{self.stockCode}.NS"
        
        # xpath
        self.defaultXpath = "/html/body/div[2]/section[1]/section[3]/div/div/form/div/div[2]/div/div[3]/"
        
        self.stockQuantityXpath = f"{self.defaultXpath}div[1]/input"
        self.buyPriceXpath    =   f"{self.defaultXpath}div[2]/input"
        self.sellPriceXpath   =   f"{self.defaultXpath}div[3]/input"
        
        
        # Xpath of Delivery Intra & netProfit  .
        self.deliveryXpath = "/html/body/div[2]/section[1]/section[3]/div/div/form/div/div[2]/div/div[1]/div/label[2]"
        self.netProfitXpath = "/html/body/div[2]/section[1]/section[3]/div/div/form/div/div[2]/div/div[4]/div[1]/div[4]/span"
        self.intraDayXpath = "/html/body/div[2]/section[1]/section[3]/div/div/form/div/div[2]/div/div[1]/div/label[1]"
        self.stockSearchPath =    "brokerage-scrip-search"
        
        
        # Driver declaration.
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
        self.raptorCharts = RaptorCharts(stockCode= stockCode)
        
    def FireConnection(self):
        # Initialising Window
        self.driver.get(self.targetUrl)
        
        # Fetch Input Fields
        self.stockQueryField = self.driver.find_element(By.ID, self.stockSearchPath)
        self.stockQuantityField = self.driver.find_element(By.XPATH, self.stockQuantityXpath)
        self.buyPriceField = self.driver.find_element(By.XPATH, self.buyPriceXpath)
        self.sellPriceField = self.driver.find_element(By.XPATH, self.sellPriceXpath)
        
        # Fetch IntraDay / Delivery Options
        self.deliveryButton = self.driver.find_element(By.XPATH, self.deliveryXpath)
        self.intraButton = self.driver.find_element(By.XPATH, self.intraDayXpath)
        self.netProfit = self.driver.find_element(By.XPATH, self.netProfitXpath)

        # Send the stock key as an input
        self.stockQueryField.send_keys(self.stockCode)
        input("")

    def GenerateReport(self, 
                       investment :int ,
                       acquirePrice : list,
                       sellPrice : list,
                       investmentScale : int,
                       minimumInvestment : int = 1000,
                       ):
        # Investment Amount Eg :  5000
        # Acquire Price Eg : 0.80
        # Sell Price Eg : 0.85
        # price Scale Eg : 500 (Linear Investment Range)
        
        stockDict = {}
        def analyseProfits(
            investment,
            buyPrice,
            sellPrice
        ):
            # Calculating Number of Stocks 
            total_stocks = (investment // buyPrice) 
            total_stocks = str(total_stocks)[:-2]
            
            # Clearing the prefilled values
            self.stockQuantityField.clear()
            self.buyPriceField.clear()
            self.sellPriceField.clear()
            
            # Sending keyStroke
            self.stockQuantityField.send_keys(f"{total_stocks}")
            self.buyPriceField.send_keys(f"{buyPrice}")
            self.sellPriceField.send_keys(f"{sellPrice}")
            
            # Reading Value
            self.intraButton.click() 
            intraDayProfit = self.netProfit.text[2:]
            self.deliveryButton.click()
            DeliveryProfit = self.netProfit.text[2:]
            # returning the analysed data
            return (total_stocks, intraDayProfit, DeliveryProfit)
        
        # Iterating over the investment 
        while investment >= minimumInvestment : 
            for primaryPoint in range(len(acquirePrice)) :
                for secondaryPoint in range(len(sellPrice)) :
                    if sellPrice[secondaryPoint] -   acquirePrice[primaryPoint] <= 0 : continue
                    generatedKey = f"{acquirePrice[primaryPoint]} - {sellPrice[secondaryPoint]}"
                    if generatedKey not in stockDict :  stockDict[generatedKey] = []
                    profitData  = analyseProfits(
                    investment,
                    acquirePrice[primaryPoint],
                    sellPrice[secondaryPoint],
                ),
                    # Temproary Dict to save into the stockDict 
                    dataDict = {
                        # Mapping Required Fields
                        'Investment' : investment,
                        'Stocks Acquired' : profitData[0][0],
                        'IntraDay Profits' : profitData[0][1],
                        'Delivery Profits' : profitData[0][2],
                    }
                    stockDict[generatedKey].append(dataDict)
            investment -= investmentScale
        # with open('report.json','w') as text : text.write(json.dumps(stockDict))
        self.raptorCharts.createChart(stockDict)
        return True
    
    
rap = Rapter(stockCode="GTLINRA")
rap.FireConnection()
rap.GenerateReport(
    investment = 10000,
    acquirePrice = [0.75, 0.80, 0.85],
    sellPrice = [0.80, 0.85 ,0.90],
    investmentScale = 500,
    minimumInvestment = 1000,
)