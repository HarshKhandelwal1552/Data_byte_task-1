import numpy as np

class MPNeuron:
    
    # constructor for MPNeuron 
    def __init__(self):
        self.n = [1, 1, 1] #initailizing n
        self.weight = [1, 1, 1] # initializing weights
        self.threshold = 2.5  # initializing threshold

    # the below function is to take or accept inputs given by user
    def MP_Neuron_Input(self, n, weights, threshold):
        self.n = n
        self.weights = weights 
        self.threshold = threshold
    
    def MP_Neuron_Evaluate(self):
        x_trans = np.array(self.n).reshape(1,-1)  #converting the entries into a row  
        w = np.array(self.weight).reshape(-1,1)         #converting the weights into column(length,1) to remove shape like(lenght,)
        y_pred = np.dot(x_trans, w)   # getting outputs from dot product
        if y_pred > self.threshold:   # thresholding the outputs for cut split
            return 1
        return 0

def NAND(x1, x2, x3):
    y = MPNeuron() # creating the instance of MPNeuron
    y.MP_Neuron_Input([-x1, -x2, -x3], [1, 1, 1], -3) 
    return y.MP_Neuron_Evaluate()
    



y_out = NAND(1,1,1)
print(y_out)
