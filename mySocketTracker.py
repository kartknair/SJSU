
import psutil
import csv
from collections import Counter

class SocketSniffer:
    def demo(self):
        socketdetails = psutil.net_connections("tcp")
        neworderlist = []
        for socketdetail in socketdetails:
            newsockdetail =  (socketdetail[6], socketdetail[3], socketdetail[4], socketdetail[5])
            neworderlist.append(newsockdetail)

        sortedsocketlist =  Counter(element[0] for element in neworderlist).most_common()

        finallist = []
        for x in sortedsocketlist:
           for y in neworderlist:
               if y[0] == x[0]:
                    finallist.append(y)

        with open('sortedSocketList.csv', 'wb') as outwriter:
            csvout = csv.writer(outwriter)
            csvout.writerow(['pid', 'laddr', 'raddr', 'status'])
            for row in finallist:
                csvout.writerow(row)

    demo(2)