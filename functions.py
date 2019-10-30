
import numpy as np
def distance(x0,x1,size):
	delta = np.abs(x0 - x1)
	delta = np.where(delta > 0.5 * 1, delta - 1, delta)
	return np.sqrt(((delta*np.array(size))**2).sum(axis=-1))
