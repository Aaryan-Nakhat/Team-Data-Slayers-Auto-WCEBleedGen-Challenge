# Team-Data-Slayers-Auto-WCEBleedGen-Challenge
A robust implementation of Auto-WCEBleedGen Classification and Detection

## Achieved Metrics of Classification and Detection on the Validation Dataset

| Accuracy | Recall | F1-Score | Average Precision | Mean-Average Precision | Intersection over Union(IoU)) |
|:--------:|:------:|----------|-------------------|------------------------|-------------------------------|
|    1.0   |   1.0  | 1.0      | 0.814             | 0.814                  | 0.709                         |

## Screenshots of 10 images from the validation dataset showcasing classification and detection

![sample](miscellaneous/validation_results_screenshots/example_1.jpg)
![sample](miscellaneous/validation_results_screenshots/example_2.jpg)
![sample](miscellaneous/validation_results_screenshots/example_3.jpg)
![sample](miscellaneous/validation_results_screenshots/example_4.jpg)
![sample](miscellaneous/validation_results_screenshots/example_5.jpg)
![sample](miscellaneous/validation_results_screenshots/example_6.jpg)
![sample](miscellaneous/validation_results_screenshots/example_7.jpg)
![sample](miscellaneous/validation_results_screenshots/example_8.jpg)
![sample](miscellaneous/validation_results_screenshots/example_9.jpg)
![sample](miscellaneous/validation_results_screenshots/example_10.jpg)

## Screenshots of 5 images from the test dataset 1 showcasing classification and detection

![sample](miscellaneous/test_data_1_results_screenshots/example_1.jpg)
![sample](miscellaneous/test_data_1_results_screenshots/example_2.jpg)
![sample](miscellaneous/test_data_1_results_screenshots/example_3.jpg)
![sample](miscellaneous/test_data_1_results_screenshots/example_4.jpg)
![sample](miscellaneous/test_data_1_results_screenshots/example_5.jpg)

## Screenshots of 5 images from the test dataset 2 showcasing classification and detection

![sample](miscellaneous/test_data_2_results_screenshots/example_1.jpg)
![sample](miscellaneous/test_data_2_results_screenshots/example_2.jpg)
![sample](miscellaneous/test_data_2_results_screenshots/example_3.jpg)
![sample](miscellaneous/test_data_2_results_screenshots/example_4.jpg)
![sample](miscellaneous/test_data_2_results_screenshots/example_5.jpg)

## Interpretability plots on the Validation Dataset

1) Receiver Operating Characteristic Curve
   ![sample](miscellaneous/Interpretability_plots/ROC_Curve_validation_set.png)

2) Precision Recall Curve
   ![sample](miscellaneous/interpretability_plots/Precision_Recall_Curve_validation_set.png)

3) Confusion Matrix
   ![sample](miscellaneous/interpretability_plots/confusion_matrix_validation_set.png)

## Running classification inference on test data

- Firstly run <code>pip install -r requirements.txt</code> to install all dependencies.
- Then run:
  
  <code>python classification_inference_on_test_datasets.py --image_folders "<path_to_test_data_1>" "<path_to_test_data_2>"</code>

This will save the results of inference on the test data in an excel file with a default name of "test_data_predictions_combined.xlsx". You can also change the name of the excel file by giving <code>--output_file</code> as a command line argument.

The inference is already run and the classification results on the test datasets are present in <code>test_data_predictions_combined.xlsx</code> file.

## Demo

Following video shows a demo of our classification model:

![Demo](miscellaneous/classification_demo.gif)

You can try yourself at: [classification_demo](https://huggingface.co/Aaryan333/convnext-tiny-finetuned-misahub-auto-wce)
