import time
class BruteForce:
    def __init__(self, mainStr, searchStr):
        self._mainStr=mainStr
        self._searchStr=searchStr
    
    def search(self)->int:
        searchLen=len(self._searchStr)
        mainLen=len(self._mainStr)
        if mainLen==0 or mainLen<searchLen:
            return -1

        i=0
        while i<=mainLen-searchLen:
            if self._mainStr[i:i+searchLen]==self._searchStr:
                return i
            i=i+1

        return -1

def test_BruteForce():
    mainStr='神光财经表示，今日上午沪指震荡下行，小幅下跌，农业种植板块逆势大涨，领涨两市，神农科技等4股涨停，稀土板块继续大涨，板块掀涨停潮，金力永磁等9股涨停，带动小金属、有色、黄金等板块大涨，建筑装饰板块继续保持强势，建研院等7股涨停，5G概念表现活跃，欣天科技等6股涨停，分散染料领跌两市，汽车整车、白酒、医药、家电等白马股集体下跌，跌幅居前。从盘面表现看，股市目前在低位震荡盘整，下跌空间有限，所以大家不必太过担心，短期随时都可能会走出一轮反弹行情，所以大家可以选择优质个股逢低买入，但是要控制好仓位，耐心持股待涨。'
    searchStr='持股XX待涨。'
    start=time.time()
    bf=BruteForce(mainStr, searchStr)
    end=time.time()
    print(end-start)
    index=bf.search()
    print('查找到位置是:'+str(index))

if __name__=="__main__":
    test_BruteForce()
