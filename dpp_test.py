from dpp import *

import time
times_1=0

beemsizes=[2,3,4,5,6,7,8]
times_beem={}
for i in beemsizes:
    times_beem[i]=0
score_1=0
score_beem={}
for i in beemsizes:
    score_beem[i]=0
for p in range(10000):
    item_size = 100
    feature_dimension = 100
    max_length = 8

    scores = np.exp(0.01 * np.random.randn(item_size) + 0.2)
    feature_vectors = np.random.randn(item_size, feature_dimension)

    feature_vectors /= np.linalg.norm(feature_vectors, axis=1, keepdims=True)
    similarities = np.dot(feature_vectors, feature_vectors.T)
    #print(similarities.shape)
    kernel_matrix = scores.reshape((item_size, 1)) * similarities * scores.reshape((1, item_size))
    #print(kernel_matrix.shape)
    #print('kernel matrix generated!')


    def cala(result):
        global scores,feature_vectors,max_length
        S=np.zeros(len(result))
        Feature_vectors=np.zeros((len(result), feature_dimension))
        #print(Feature_vectors)
        for i in range(len(result)):
            S[i]=scores[result[i]]
            #print(feature_vectors[result[i]])
            Feature_vectors[i]=feature_vectors[result[i]]
        Similarities =np.dot(Feature_vectors, Feature_vectors.T)
        Kernel_matrix = S.reshape((len(result), 1)) * Similarities * S.reshape((1, len(result)))

        return np.linalg.det(Kernel_matrix)
    t = time.time()
    result = dpp(kernel_matrix, max_length)
    #print ('algorithm running time: ' + '\t' + "{0:.4e}".format(time.time() - t))
    times_1+=time.time() - t
    #print(result)
    score_1+=cala(result)
    # window_size = 5
    # t = time.time()
    # result_sw = dpp_sw(kernel_matrix, window_size, max_length)
    # print(result_sw)
    # print ('sw algorithm running time: ' + '\t' + "{0:.4e}".format(time.time() - t))
    #print(result)
    for i in beemsizes:
        t = time.time()
        result_beem=dpp_beemserach(kernel_matrix, max_length,beemsize=i)
        #if(i==2):
           #print(result_beem)
        times_beem[i] += time.time() - t
        # print(result)
        score_beem[i]+= cala(result_beem)
    # print(result_beem)
    # print ('beem algorithm running time: ' + '\t' + "{0:.4e}".format(time.time() - t))
    if(p%1000==0):print(p)

print ('algorithm running avg time: ' + '\t' + "{0:.4e}".format(times_1/10000))
print ('algorithm running avg score: ' + '\t' + "{0:.4e}".format(score_1/10000))
for i in beemsizes:
    print ('beem'+str(i)+' algorithm running avg time: ' + '\t' + "{0:.4e}".format(times_beem[i]/10000))
    print('beem' + str(i) + ' algorithm running avg score: ' + '\t' + "{0:.4e}".format(score_beem[i] / 10000))