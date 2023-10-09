# Team-Data-Slayers-Auto-WCEBleedGen-Challenge

## Running inference on test data

- Firstly run <code>pip install -r requirements.txt</code> to install all dependencies.
- Then run:
  
  <code>python classification_inference.py --image_folders "<path_to_test_data_1>" "<path_to_test_data_2>"</code>

This will save the results of inference on the test data in an excel file with a default name of "test_data_predictions_combined.xlsx". You can also change the name of the excel file by giving <code>--output_file</code> as a command line argument.
