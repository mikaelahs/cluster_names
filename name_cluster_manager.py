'''
Created: May 25, 2017
@author mhoffmanstapleton@usfca.edu
'''

class name_cluster_manager(object):
    '''
    This class is the manager for the name cluster algorithm. It forms clusters and prints them. It contains four
    functions: __init__(), which initializes attributes, read_names(), which populates the self.names attribute, 
    cluster_names(), which assigns the names to clusters, and print_names(), which prints the names by cluster.
    '''

    def __init__(self, argv):
        '''
        Constructor
        '''
        self.names_file = argv[1]
        self.clusters_to_form = int(argv[2])
        self.names = []
        self.clusters = []

        # Call the read_names function right away
        self.read_names(False)

    def read_names(self, clear_names_first):
        '''
        This function reads the names from storage to memory. It assumes that self.names_file is a list of names, one per
        line. It populates self.names as a list of names read from the self.names_file.
        :param clear_names_first: True if any existing names should be flushed prior to filling self.names.
        :type clear_names_first: boolean 
        :return: does not return anything
        '''
        if clear_names_first:
            self.names = []
        with open(self.names_file) as f:
            for name in f:
                self.names.append(name.strip())

    def cluster_names(self):
        '''
        This function forms clusters according to the requirements. It converts the names to their soundex versions and 
        creates a matrix of levenshtein distances, where each entry is the distance between two soundex names. This matrix
        is used as the input for an agglomerative clustering model, which assigns each name to a cluster. It populates 
        self.clusters as a list of cluster assignments according to the output of the model.
        :return: does not return anything
        '''
        from sound import sound
        from hw1.linguistic_distance import linguistic_distance
        from sklearn.cluster import AgglomerativeClustering
        sound = sound()
        linguistic_distance = linguistic_distance()
        # Call get_soundex() from the sound class to get the soundex conversion for each name
        soundex = []
        for name in self.names:
            soundex.append(sound.get_soundex(name))
        # Call levenshtein() from the linguistic_distance class to get the matrix of distances
        distance = []
        for i in range(len(soundex)):
            row = []
            for j in range(len(soundex)):
                row.append(linguistic_distance.levenshtein(soundex[i], soundex[j]))
            distance.append(row)
        # Cluster the names using agglomerative clustering and populate self.clusters
        model = AgglomerativeClustering(n_clusters=self.clusters_to_form)
        model.fit(distance)
        self.clusters = model.labels_

    def print_names(self):
        '''
        This function prints the clusters formed. It creates a pandas dataframe and filters the rows to print names that 
        were assigned to the same cluster.
        :return: does not return anything
        '''
        import pandas as pd
        df = pd.DataFrame.from_items([('name', self.names), ('cluster', self.clusters)])
        # Print names associated with each cluster
        for cluster in df['cluster'].unique():
            df_filtered = df[df['cluster'] == cluster]
            print ' '.join(df_filtered['name'])
