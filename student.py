import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go
import statistics
df = pd.read_csv('studentsPerformance.csv')
data = df['reading score'].tolist()
mean = sum(data) / len(data)
stdDeviation = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)
firstStdDeviationStart, firstStdDeviationEnd = mean - stdDeviation, mean + stdDeviation
secondStdDeviationStart, secondStdDeviationEnd = mean - (2 * stdDeviation), mean + (2 * stdDeviation)
thirdStdDeviationStart, thirdStdDeviationEnd = mean - (3 * stdDeviation), mean + (3 * stdDeviation)
fig = ff.create_distplot([data], ['reading score'], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = 'lines', name = 'MEAN'))
fig.add_trace(go.Scatter(x = [firstStdDeviationStart, firstStdDeviationStart], y = [0, 0.17], mode = 'lines', name = 'STANDARD DEVIATION 1'))
fig.add_trace(go.Scatter(x = [firstStdDeviationEnd, firstStdDeviationEnd], y = [0, 0.17], mode = 'lines', name = 'STANDARD DEVIATION 1'))
fig.add_trace(go.Scatter(x = [secondStdDeviationStart, secondStdDeviationStart], y = [0, 0.17], mode = 'lines', name = 'STANDARD DEVIATION 2'))
fig.add_trace(go.Scatter(x = [secondStdDeviationEnd, secondStdDeviationEnd], y = [0, 0.17], mode = 'lines', name = 'STANDARD DEVIATION 2'))
fig.show()
listOfDataWithin1StdDeviation = [result for result in data if result > firstStdDeviationStart and result < firstStdDeviationEnd]
listOfDataWithin2StdDeviation = [result for result in data if result > secondStdDeviationStart and result < secondStdDeviationEnd]
listOfDataWithin3StdDeviation = [result for result in data if result > thirdStdDeviationStart and result < thirdStdDeviationEnd]
print('Mean of this data is ' + str(mean))
print('Median of this data is ' + str(median))
print('Mode of this data is ' + str(mode))
print('Standard deviation of this data is ' + str(stdDeviation))
print('{}% of data lies within 1 standard deviation'.format(len(listOfDataWithin1StdDeviation) * 100.0 / len(data)))
print('{}% of data lies within 2 standard deviation'.format(len(listOfDataWithin2StdDeviation) * 100.0 / len(data)))
print('{}% of data lies within 3 standard deviation'.format(len(listOfDataWithin3StdDeviation) * 100.0 / len(data)))