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
        self.entryPrice

        self.period = timedelta(31)

        #Will track when we sshould reenter our long SPY position
        #We init this to the current time since we want to start investing right away
        self.nextEntryTime = self.Time 


    #OnData method runs everytime we get new data
    def OnData(self, data):
        pass