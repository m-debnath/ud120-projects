""" quiz materials for feature scaling clustering """

### FYI, the most straightforward implementation might
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!
### why would you rescale it?  Or even use it at all?
def featureScaling(arr):

    arr_max = max(arr)
    arr_min = min(arr)
    data_scaled = [round((arr[ii] - arr_min)/float(arr_max - arr_min), 3) for ii in range(0, len(arr))]
    return data_scaled

# tests of your feature scaler--line below is input data
data = [3285., 1000000., 34348384.]
print featureScaling(data)