<div align="center">
  <p>
    <a align="center" href="" target="_blank">
      <img
        width="850"
        src="https://media.roboflow.com/open-source/autodistill/autodistill-banner.png"
      >
    </a>
  </p>
</div>

# Autodistill AWS Rekognition Module

This repository contains the code supporting the [AWS Rekognition DetectLabels](https://docs.aws.amazon.com/rekognition/latest/dg/labels-detect-labels-image.html) base model for use with [Autodistill](https://github.com/autodistill/autodistill).

With this repository, you can label images using the AWS Rekognition DetectLabels API and train a fine-tuned model using the generated labels.

This is ideal if you want to train a model that you own on a custom dataset.

You can then use your trained model on your computer using Autodistill, or at the edge or in the cloud by deploying with [Roboflow Inference](https://inference.roboflow.com).

See our Autodistill modules for [GCP Vision](https://github.com/autodistill/autodistill-gcp-vision) and [Azure Custom Vision](https://github.com/autodistill/autodistill-azure-vision) if you are interested in using those services instead.

Read the full [Autodistill documentation](https://autodistill.github.io/autodistill/).

Read the [Autodistill AWS Rekognition documentation](https://autodistill.github.io/autodistill/base_models/aws_rekognition/).

## Installation

> [!NOTE]  
> Using this project will incur billing charges for API calls to the AWS Rekognition DetectLabels API. Refer to the [AWS Rekognition pricing](https://aws.amazon.com/rekognition/pricing/) for more information. This package makes one API call per image you want to label.

To use the AWS Rekognition DetectLabels API with autodistill, you need to install the following dependency:

```bash
pip install autodistill-rekognition
```

You will then need to authenticate with the `aws` CLI.

Learn [how to install the `aws` CLI](https://aws.amazon.com/cli/).

Learn [how to set up and authenticate with the `aws` CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html).

## Quickstart

_Note: You will need to install `python-opencv` to run the example below._

```python
from autodistill_rekognition import Rekognition
from autodistill.detection import CaptionOntology
import supervision as sv
import cv2

# define an ontology to map class names to our Rekognition prompt
# the ontology dictionary has the format {caption: class}
# where caption is the prompt sent to the base model, and class is the label that will
# be saved for that caption in the generated annotations
# then, load the model
base_model = Rekognition(
    ontology=CaptionOntology(
        {
            "Person": "Person",
            "a forklift": "forklift"
        }
    )
)

results = base_model.predict("image.jpeg")

# annotate predictions on an image
classes = base_model.ontology.classes()

box_annotator = sv.BoxAnnotator()

labels = [
	f"{classes[class_id]} {confidence:0.2f}"
	for _, _, confidence, class_id, _
	in detections
]

image = cv2.imread("image.jpeg")

annotated_frame = box_annotator.annotate(
	scene=image.copy(),
	detections=detections,
	labels=labels
)

sv.plot_image(image=annotated_frame, size=(16, 16))
```

## License

This project is licensed under an [MIT license](LICENSE).

## 🏆 Contributing

We love your input! Please see the core Autodistill [contributing guide](https://github.com/autodistill/autodistill/blob/main/CONTRIBUTING.md) to get started. Thank you 🙏 to all our contributors!