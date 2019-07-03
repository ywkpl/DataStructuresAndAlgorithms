from datetime import datetime, timedelta
if __name__=="__main__":
    begin = datetime(2018, 11, 1)
    end = datetime(2019, 6, 18)
    times=end-begin
    print('天数：')
    print(times.days)
    print('月数余天数：')
    print(str(times.days//30)+'月'+str(times.days%30)+'天')
   