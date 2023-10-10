## Overview

- The notebook titled <code>Classification_Model_for_training_and_validation.ipynb</code> contains the code for the classification model and <code>Segmentation_Model_for_training_and_validation.ipynb</code> contains the code for the segmentation model.

- The notebook titled <code>Save_Classification_Model_Preds_Only_Bleeding.ipynb</code> contains the code for saving bleeding predicted train and validation samples in a new folder, which will serve as inputs for the segmentation task.

- Meanwhile, notebooks titled <code>inference-val-data-for-screenshots.ipynb</code>, <code>inference-test-data-1-for-screenshots.ipynb</code>, and <code>inference-test-data-2-for-screenshots.ipynb</code> contain the code for inferring screenshots from the validation, test dataset, and test dataset 2, respectively, which are used on the homepage of this repository.


## Order of execution:

1) <code>Classification_Model_for_training_and_validation.ipynb</code> for training and validating the classification model

2) <code>Save_Classification_Model_Preds_Only_Bleeding.ipynb</code> for saving bleeding predicted train and validation samples in a folder which will be used in the next step for segmentation

3) <code>Segmentation_Model_for_training_and_validation.ipynb</code> for training and validating the segmentation model

4) Running the <code>classification_inference_on_test_datasets.py</code> script by following the steps described in the homepage's README.md file. This will create an excel in the specified format

5) Running <code>inference-val-data-for-screenshots.ipynb</code>, <code>inference-test-data-1-for-screenshots.ipynb</code> and <code>inference-test-data-2-for-screenshots.ipynb</code> for getting inference screenshots from the validation dataset, test dataset, and test dataset 2, respectively.
