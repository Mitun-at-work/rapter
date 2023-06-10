# Importing packages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Rapter Class declaration

class Rapter:
    
    def __init__(self, stockCode) -> None:
        self.targetUrl =    "https://upstox.com/calculator/brokerage-calculator/"
        self.stockCode = stockCode
        self.defaultXpath = "/html/body/div[2]/section[1]/section[3]/div/div/form/div/div[2]/div/div[3]/"
        self.stockQuantityXpath = f"{self.defaultXpath}div[1]/input"
        self.buyPriceXpath    =   f"{self.defaultXpath}div[2]/input"
        self.sellPriceXpath   =   f"{self.defaultXpath}div[3]/input"
        self.deliveryXpath = "/html/body/div[2]/section[1]/section[3]/div/div/form/div/div[2]/div/div[1]/div/label[2]"
        self.netProfitXpath = "/html/body/div[2]/section[1]/section[3]/div/div/form/div/div[2]/div/div[4]/div[1]/div[4]/span/span"
        self.intraDayXpath = "/html/body/div[2]/section[1]/section[3]/div/div/form/div/div[2]/div/div[1]/div/label[1]"
        self.stockSearchPath =    "brokerage-scrip-search"
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
    def FireConnection(self):
        
        # Initialising Window
        self.driver.get(self.targetURL)
        
        # Fetch Input Fields
        self.stockQueryField = self.driver.find_element(By.ID, self.stockSearchPath)
        self.stockQuantityField = self.driver.find_element(By.XPATH, self.stockQuantityXpath)
        self.buyPriceField = self.driver.find_element.find_element(By.XPATH, self.buyPriceXpath)
        self.sellPriceField = self.driver.find_element.find_element(By.XPATH, self.sellPriceXpath)
        
        # Fetch IntraDay / delivery Options
        self.deliveryButton = self.driver.find_element.find_element(By.XPATH, self.deliveryXpath)
        self.intraButton = self.driver.find_element.find_element(By.XPATH, self.intraDayXpath)
        
        # Send the stock key as an input
        
        self.stockQuantityField.send_keys()

    def GenerateReport(self):
        pass
        
        
                
