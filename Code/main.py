class EnergeticGreenCaterpillar(QCAlgorithm):
    
    def Initialize(self):
        
        #Setting the Start and End dates for backtesting 
        self.SetStartDate(2020, 1, 1)
        self.SetEndDate(2021, 1, 1)
        
        #Starting cash balance, real life this would be taken from your brokerage account
        self.SetCash(100000) 

        #Adding the data for the security our Algo will trade
        #Since we want to trade SPY we use AddEquity and the SPY ticker symbol
        #As the second argument the AddEquity method takes in a Resolution
        #Lowest is tick resolution(tick/mili second)
        spy = self.AddEquity("SPY", Resolution.Daily)

        #Data adjustment Mode
        #Options only allow raw data so 'DataNormalizationMode.Raw off
        #Here we are changing the data mode

        spy.SetDataNormalizationMode(DataNormalizationMode.Raw)

        #Saving the symbol object of SPY to a new variable
        #Symbol objects hold more information than tickers which can help with unwanted ambiguity when referencing a ticker symbol
        self.spy = spy.Symbol

        #Setting a benchmark
        #This will automatically generate a chart when backtesting
        #This helps with analyzing the performance of our algo
        self.SetBenchmark("SPY")

        #Allows us to set different brokerage models so that our algo best accounts for the brokerages fee structure and account type
        self.SetBrokerageModel(BrokerageName.InteractiveBrokersBrokerage, AccountType.Margin)

        #Three custom helper variables

        #entryPrice will track the entry price of our SPY position
        self.entryPrice = 0

        self.period = timedelta(31)

        #Will track when we sshould reenter our long SPY position
        #We init this to the current time since we want to start investing right away
        self.nextEntryTime = self.Time 


    #OnData method runs everytime we get new data
    def OnData(self, data):
        
        #We need to check if the data already exists before anything
        if not self.spy in data:
            return

        #Firstly we would want to save the current price of SPY
        #directly indexing the data variable, this will return a trade bar object that we can use to find the last close price
        price = data[self.spy].Close

        #Implementing the trade logic
        #Firstly we want to check if our bot is already invested

        #This bot is supposed to buy and hold SPY until SPY drops or rises a certain amount
        #After we stay in cash for one month until we buy and hold again

        #To account fot the one month wait time we can use self.Time to access the current time and then check if its greater or equal to the next entry time


        if not self.Portfolio.Invested:
            if self.nextEntryTime <= self.Time:
                self.SetHoldings(self.spy, 1)
                # self.MarketOrder(self.spy, int(self.Portfolio.Cash / price) )
                self.Log("BUY SPY @" + str(price))
                self.entryPrice = price
        
        elif self.entryPrice * 1.1 < price or self.entryPrice * 0.90 > price:
            self.Liquidate()
            self.Log("SELL SPY @" + str(price))
            self.nextEntryTime = self.Time + self.period