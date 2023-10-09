import os
import pandas as pd
from transformers import AutoFeatureExtractor, AutoModelForImageClassification, pipeline
from PIL import Image
import argparse
from tqdm import tqdm

def main():
    parser = argparse.ArgumentParser(description="Image Classification CLI")
    parser.add_argument("--model_name", type=str, default="Aaryan333/convnext-tiny-finetuned-misahub-auto-wce",
                        help="Name of the model")
    parser.add_argument("--output_file", type=str, default="test_data_predictions_combined.xlsx",
                        help="Output Excel file name")
    parser.add_argument("--image_folders", nargs='+', required=True,
                        help="List of folders containing images")

    args = parser.parse_args()

    # Initialize the image classification pipeline
    print("\nLoading the fine-tuned model...")
    classifier = pipeline("image-classification", model=args.model_name)

    # Create a list to store predictions
    predictions_list = []

    # Process each image from each folder and make predictions
    for folder_count, image_folder in tqdm(enumerate(args.image_folders)):
        image_paths = [os.path.join(image_folder, filename) for filename in os.listdir(image_folder)]
        print(f"\n\nProcessing images in folder {folder_count+1}...")

        for image_path in tqdm(image_paths):
            image_name = os.path.basename(image_path)
            image = Image.open(image_path)

            # Use the pipeline to classify the image
            result = classifier(image)

            predicted_class = result[0]["label"]

            # Append the prediction to the list
            predictions_list.append({"Image name": image_name.replace(".png", ""), "Predicted Class label": predicted_class.title().replace("_", "-")})

    # Create a DataFrame from the predictions list
    predictions_df = pd.DataFrame(predictions_list)

    # Save the DataFrame to an Excel file
    predictions_df.to_excel(args.output_file, index=False)

    print("\nDone!!!")

if __name__ == "__main__":
    main()