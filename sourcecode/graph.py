import matplotlib.pyplot as plt
import numpy as np

class Graph:
    """
    Class for graphing tests results & training data
    """

    def __init__(self, x, y, x_2=None, y_2=None, title='test title', x_label='x',
    y_label='y',legend=None):
        """
        Initializes Graph variables
        when x,x_2 are None, assumes y,y_2 are data signals
        """

        self.x = x
        self.y = y
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.legend = legend
        self.x_2 = x_2
        self.y_2 = y_2

    def build_double_line_graph(self):
        """
        Double line graph using x, y, x_2 and y_2
        
        if x, x_2 are None, assumes y,y_2 are signals 
        """

        if self.x == None and self.x_2 == None:
            plt.plot(self.y)
            plt.plot(self.y_2)
            plt.ylabel('accuracy')
            plt.xlabel('epoch')
            plt.title(self.title)
            plt.legend(self.legend, loc='upper left')
            plt.show()

    def build_line_graph(self):
        """
        Uses x and y to graph 
        """
        if self.x == None:
            for i in self.y:
                plt.plot(i)
        else:
            for i in self.x:
                plt.plot(self.x, self.y)
            
        plt.title(self.title)
        plt.ylabel(self.y_label)
        plt.xlabel(self.x_label)
        plt.legend(self.legend, loc='upper left')
        plt.show()
        pass
    
    def build_powerspectrum_graph(self):
        #plt.figure(212)
        #b.set_xscale('log')
        plt.psd(self.y, NFFT = 256,Fs=1)
        plt.show()

    def build_frequ_graph(self):
        x = list(range(0, len(self.y)))
        x = [float(i) for i in x]
        plt.figure(212)
        plt.plot(x,self.y)
        plt.show()

        """
        #y = np.sin(0.5 * np.pi * x * (1 + .1 * x))
        graph_2 = Graph(x,y)
        freq, psd = signal.welch(y)
        graph_3 = Graph(x, y)
        graph_3.build_powerspectrum_graph()
        graph_3.build_frequ_graph()
        """



