import matplotlib.pyplot as pyplot
import numpy

pyplot.plot([1, 5, 3, 9])
pyplot.ylabel('y-axis')
pyplot.show()

pyplot.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro') # x-axis, y-axis, red circle to represent each function point
pyplot.axis((0, 6, 0, 20)) # x-axis range from 0 to 6, y-axis range from 0 to 20
pyplot.ylabel('y-axis')
pyplot.xlabel('x-axis')
pyplot.show()

two = numpy.arange(0., 2., 0.1)
# red line, blue square, green triangle and line width 2.5
pyplot.plot(two, two**2, 'r-', two, two**3, 'bs', two, two**4, 'g^', linewidth=2.5)
# common function representation chars:
# '-', '--', '-.', ':', 'o', 's', '^', 'x', '+', '*', 'D', 'd', 'h', 'H', 'p', '<', '>', '|', '_'
pyplot.xlabel('time (sec)')
pyplot.ylabel('amplitude')
pyplot.title('Powers of two')
pyplot.show()

x_function = numpy.linspace(0, 6 * numpy.pi, 300)
y_function = 5 * numpy.cos(x_function)

pyplot.figure(1) # Create a new figure with number 1
pyplot.plot(x_function, y_function)
pyplot.show()

t_function = numpy.linspace(-4, 4, 1000)

pyplot.figure()

x1_function = 5 * numpy.cos(2 * numpy.pi * 6 * t_function)
x2_function = 3 * numpy.sin(2 * numpy.pi * 4 * t_function)
x3_function = numpy.cos(2 * numpy.pi * 2 * t_function)

# rendering three functions in the same figure
pyplot.plot(t_function, x1_function, 'r-', t_function, x2_function, 'g-', t_function, x3_function, 'b-')
pyplot.show()
pyplot.close()

# rendering multiple functions in multiple figures and sub-plots
def f_function(m_function):
    tao = 0.4
    division = 1 / (1 * tao)

    return numpy.exp(-m_function / tao) * numpy.cos(2 * numpy.pi * division * m_function)

t1_function = numpy.arange(0., 2., 0.02)
t2_function = numpy.arange(0., 2., 0.1)

pyplot.figure(1)
pyplot.subplot(211) # two rows with one column rendering figure 1
pyplot.title('damped sinusoidal (top), sinusoidal (bottom)')
pyplot.plot(t1_function, f_function(t1_function), 'bo', t2_function, f_function(t2_function), 'k')
pyplot.ylabel('amplitude')
pyplot.subplot(212) # two rows with one column rendering figure 2
pyplot.plot(t2_function, numpy.cos(2 * numpy.pi * t2_function), '-r')
pyplot.xlabel('time (sec)')
pyplot.ylabel('amplitude')
pyplot.show()

# rendering multiple subplots in the same figure
pyplot.figure(1)
pyplot.subplot(211)
pyplot.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
pyplot.title('linear (top) and linear in sections (bottom)')
pyplot.ylabel('y-axis')
pyplot.subplot(212)
pyplot.plot([4, 5, 6,9, 10, 11, 14, 15, 18, 20])
pyplot.xlabel('x-axis')
pyplot.ylabel('y-axis')
pyplot.show()

pyplot.figure(2)
pyplot.plot([4, 5, 6, 8, 9, 10, 15, 16, 17, 22, 23])
pyplot.title('figure 2')
pyplot.xlabel('x-axis')
pyplot.ylabel('y-axis')
pyplot.show()

pyplot.figure(1)
pyplot.subplot(211)
pyplot.plot([1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9])
pyplot.title('Multiple figure')
pyplot.ylabel('y-axis')
pyplot.subplot(212)
pyplot.plot([1., 1.2, 1.3, 0.4, 0.6, 1.6, 1.7, 1.8, 0.9, 2.0, 2.1, 2.2])
pyplot.xlabel('x-axis')
pyplot.ylabel('y-axis')
pyplot.show()

pyplot.clf() # clear current figure
pyplot.cla() # clear current axis
pyplot.close(1) # clean memory for figure 1

# rendering text in figures
numpy.random.seed(123)
mu, sigma = 50, 10 # average and standard deviation
x_function = mu + sigma * numpy.random.randn(6000) # list of 6000 random number using normal distribution
num_sub_intervals_x_axis = 50
n, bins, patches = pyplot.hist(x_function, num_sub_intervals_x_axis, density=True, facecolor='g', alpha=0.75)
# better gaussian function
g_function = ((1 / (numpy.sqrt(2 * numpy.pi) * sigma)) * numpy.exp(-0.5 * (1 / sigma * (bins - mu)) ** 2))

pyplot.plot(bins, g_function, '-')
print('Values for n: ', n) # values generated per each interval
print('Values for patches: ', patches)
pyplot.xlabel('Values', fontsize=14, color='red')
pyplot.ylabel('Probability')
pyplot.title('Histogram')

m_function = max(n)

pyplot.text(20, .85 * m_function, r'$\mu=50, sigma=10$')
pyplot.axis((10, 90, 0, 1.1 * m_function))
pyplot.grid(True)
pyplot.show()

# two functions in the same figure using tags
frequency = 2
t_function = numpy.linspace(0, 2, 1000) # timeline
x1_function = numpy.exp(-t_function) * numpy.sin(2 * numpy.pi * frequency * t_function)
x2_function = numpy.exp(-2 * t_function) * numpy.sin(2 * numpy.pi * 2 * frequency * t_function)

pyplot.figure()
pyplot.plot(t_function, x1_function, 'k-', linewidth=1.5, label='x1_function')
pyplot.plot(t_function, x2_function, 'r--', linewidth=1, label='x2_function')
pyplot.legend(loc=2)
pyplot.xlabel(r"$x (\mu seg) $", fontsize=10, color=(1, 0, 0))
pyplot.ylabel('Amplitude')

pyplot.text(x = 1.5, y = 0.6, s = u'frec = 2', fontsize = 10)
pyplot.grid(True)
pyplot.grid(color = '0.5', linestyle = '--', linewidth = 1)
pyplot.axis('tight')
pyplot.title('Impulse response', fontsize = 10, color = '0.75')
pyplot.savefig('Impulseresponse.png')
pyplot.show()

# no lineal scales
pyplot.figure(1)
x_function = numpy.arange(0, 100, 0.01)
y1_function = 10 * x_function
y2_function = 2 * (x_function ** 2)

# lineal representation
pyplot.subplot(3, 1, 1)
pyplot.plot(x_function, y1_function)
pyplot.plot(x_function, y2_function)
pyplot.title('Lineal')
pyplot.grid()

# semi-logarithmic representation
pyplot.subplot(3, 1, 2)
pyplot.xscale('log')
pyplot.plot(x_function, y1_function)
pyplot.plot(x_function, y2_function)
pyplot.title('Semi-logarithmic')
pyplot.grid()

# logarithmic representation
pyplot.subplot(3, 1, 3)
pyplot.xscale('log')
pyplot.yscale('log')
pyplot.plot(x_function, y1_function)
pyplot.plot(x_function, y2_function)
pyplot.title('Logarithmic')
pyplot.grid()
pyplot.show()
