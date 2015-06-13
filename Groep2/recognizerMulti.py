'''
Shell of the handwriting recognition system.
Pre-processes specified .ppms, extracts features from them,
trains several classifiers on those and tests them as well.

Next, a similar approach is used on 'novel' pictures.
'''

import sys, os

import cv2

from preprocessing import prepImage
from segmentation import char_segmentation as cs
from features import featExtraction
from classification import classification

# Parallel packages
from multiprocessing import Pool
import time

def unwrap_self_wordParallel(arg, **kwarg):
    return Recognizer.wordParallel(*arg, **kwarg)

class Recognizer:
    """
    Recognizer class
    """

    def wordParallel(self, word):

        ## Character segmentation
        cuts, chars = cs.segment(word[0])

        segs = cs.annotate(cuts, word[2])

        assert len(chars) == len(segs) #Safety check did the segmenting go correctly

        # Feature extraction
        word = list(word)
        word.append([])     # Add empty list for features and classes

        # Obtain features of all segments
        for char, s in zip(chars, segs):
            word[3].append((feat.hog(char), s[1]))

        return word

    # Trains one classifier on all images and words in specified folders
    def fullTrain(self, ppm_folder, words_folder):

        for file in os.listdir(ppm_folder):
            if file.endswith('.ppm') or file.endswith('.jpg'):
                print file
                ## Read and preprocess
                ppm = ppm_folder + '/' + file   # ENTIRE path of course..
                inwords = words_folder + '/' + os.path.splitext(file)[0] + '.words'
                words = self.prepper.prep(ppm, inwords)

                # Iterate through words
                for word in words:
                    ## Character segmentation
                    cuts, chars = cs.segment(word[0])  # Make segments
                    segs = cs.annotate(cuts, word[2]) # Give annotations to segments

                    assert len(chars) == len(segs) #Safety check did the segmenting go correctly

                    ## Feature extraction
                    # Extract features from each segment
                    for char, seg in zip(chars, segs):
                        features.append(feat.hog(char))
                        classes.append(seg[1])
                        # NOTE: these are in order! Do not shuffle or you lose correspondence.
                        # zip() is also possible of course, but I simply do not feel the need. :)

        ## Classification
        # Fully train specified classifier on data set
        self.cls.fullTrain('RF', features, classes)   # Note to set this to best classifier!!

    # One run using all files in an images and a words folder
    def folders(self, ppm_folder, words_folder):

        for file in os.listdir(ppm_folder):
            print file
            if file.endswith('.ppm') or file.endswith('.jpg'):
                ## Read and preprocess
                ppm = ppm_folder + '/' + file   # ENTIRE path of course..
                inwords = words_folder + '/' + os.path.splitext(file)[0] + '.words'
                wordsInter = prepper.prep(ppm, inwords)

                ## Prarallel feature extraction.
                jobs = pool.map(unwrap_self_wordParallel, zip([self]*len(wordsInter), wordsInter))

        ## Classification
        cls.fullPass(jobs)  # A full run on the characters

    # Trains and tests on a single image
    def singleFile(self, ppm, inwords):

        ## Preprocessing
        wordsInter = prepper.prep(ppm, inwords)

        ## Prarallel feature extraction.
        jobs = pool.map(unwrap_self_wordParallel, zip([self]*len(wordsInter), wordsInter))

        ## Classification
        cls.fullPass(jobs)


    # Go through folder, train and test on each file
    def oneFolder(self, ppm_folder, words_folder):

        # Iterate through all files in the image folder
        for file in os.listdir(ppm_folder):
            # Print which file is currently worked on
            print file
            if file.endswith('.ppm') or file.endswith('.jpg'):
                ## Pass on to single file procedure
                ppm = ppm_folder + '/' + file   # ENTIRE path of course..
                inwords = words_folder + '/' + os.path.splitext(file)[0] + '.words'
                self.singleFile(ppm, inwords)

    # Standard run for validation by instructors
    def validate(self, ppm, inwords, outwords):
        ## Preprocessing
        words = prepper.wordPrep(ppm, inwords)

        predictions = []    # Empty list to contain all predictions

        # Go through all words
        for word in words:
            ## Character segmentation
            cuts, chars = cs.segment(word)

            # Go through all characters
            for c in chars:
                ## Feature extraction
                features = feat.hog(c)

                ## Classification
                pred = cls.classify('RF', features)
                predictions.append(pred)    # Store prediction

        prepper.saveXML(predictions, inwords, outwords)



if __name__ == "__main__":

    # Initializes the recognizer by initializing all parts of the pipeline
    # Initialize pipeline
    prepper = prepImage.PreProcessor()     # Preprocessor
    cs = cs.segmenter()                    # Character segmentation
    feat = featExtraction.Features()       # Feature extraction
    cls = classification.Classification()  # Classification
    features = []                          # List containing all features
    classes = []                           # List containing class (word) features belong to
    words = []                             # Complete word container for experiments
    pool = Pool(processes=4)               # Initialize pool with 8 processes

    r = Recognizer()

    # Number of arguments indicates how to run the program
    if len(sys.argv) < 4:
        # Too little, you screwed up..
        print "Usage: %s <image> <.words file> <output file>" % sys.argv[0]
        sys.exit(1)
    elif len(sys.argv) > 4:
        if sys.argv[1] == 'dev':
            # You know how to treat our program, all its little secrets...
            if sys.argv[2] == 'train':
                # Train on full data set
                r.fullTrain(sys.argv[3], sys.argv[4])
            elif sys.argv[2] == 'single':
                # Train and test on one file
                r.singleFile(sys.argv[3], sys.argv[4])
            elif sys.argv[2] == 'onefolder':
                # Train and test on each file in a folder
                r.oneFolder(sys.argv[3], sys.argv[4])
            elif sys.argv[2] == 'experiment':
                # Run our experiment
                r.folders(sys.argv[3], sys.argv[4])
            else:
                # Dum dum is trying to be cheeky
                print "Usage: %s -dev <version> <image_folder> <.words_folder>" % sys.argv[0]
        else:
            # Dum dum put in too many arguments
            print "Usage: %s <image> <.words file> <output file>" % sys.argv[0]
    else:
        # You are an instructor, who runs our program in the standardized format
        r.validate(sys.argv[1], sys.argv[2], sys.argv[3])

    pool.close()
    pool.join()

