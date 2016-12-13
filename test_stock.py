import rrl2
import csv
import matplotlib.pyplot as plt

with open('AAPL_test.csv') as csvfile:
    testData = csv.reader(csvfile, delimiter=',')
    priceList = []
    for row in testData:
        priceList.append(float(row[1]))


# print(rrl2.increList)
weight = rrl2.learning(21, 200)
rrl2.n = len(priceList)
rrl2.increList = rrl2.increment(priceList)
# rrl2.increList = [x * 5 for x in rrl2.increment(priceList)]
tradeSig = rrl2.posVector(weight, 21)
sumsr, sumsrsq, total = rrl2.sumReturn(tradeSig, rrl2.increList)
#plt.plot(tradeSig.transpose())
#plt.ylabel('Trading Signal')
#plt.show()
#print(total)
plt.plot(total.transpose())
plt.xlabel('Date')
plt.ylabel('Total Return')
plt.title('AAPL')
plt.show()
