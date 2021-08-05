class EnergeticGreenCaterpillar(QCAlgorithm):
    
    def Initialize(self):
        
        #Setting the Start and End dates for backtesting 
        self.SetStartDate(2020, 1, 1)
        self.SetEndDate(2021, 1, 1)
        
        #Starting cash balance, real life this would be taken from your brokerage account
        self.SetCash(100000) 

        #Adding the data for the security our Algo will trade
        #Since we want to trade SPY we use AddEquity and the SPY ticker symbol
        #As the econd argument the AddEquity method takes in a Resolution
        #Lowest is tick resolution(tick/mili second)
        spy = self.AddEquity("SPY", Resolution.Daily)

    #OnData method runs everytime we get new data
    def OnData(self, data):
        pass