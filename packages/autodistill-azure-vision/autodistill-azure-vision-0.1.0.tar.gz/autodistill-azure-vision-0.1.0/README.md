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

# Autodistill Azure Vision Module

This repository contains the code supporting the Azure Vision module for use with [Autodistill](https://github.com/autodistill/autodistill).

The [Azure Vision Image Analysis 4.0 API](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/how-to/call-analyze-image-40?tabs=csharp&pivots=programming-language-rest-api) enables you to detect objects in images.

With this package, you can use the API to automatically label data for use in training a fine-tuned computer vision model.

This is ideal if you want to train a model that you own on a custom dataset.

You can then use your trained model on your computer using Autodistill, or at the edge or in the cloud by deploying with [Roboflow Inference](https://inference.roboflow.com).

Read the full [Autodistill documentation](https://autodistill.github.io/autodistill/).

Read the [Autodistill Azure Vision documentation](https://autodistill.github.io/autodistill/base_models/azure_vision/).

## Installation

> [!NOTE]  
> Using this project will incur billing charges for API calls to the [Azure Vision Image Analysis 4.0 API](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/how-to/call-analyze-image-40?tabs=csharp&pivots=programming-language-rest-api).
> Refer to the [Azure Computer Vision pricing](https://azure.microsoft.com/en-gb/pricing/details/cognitive-services/computer-vision/) for more information and to calculate your expected pricing. This package makes one API call per image you want to label.

To use Azure Vision with autodistill, you need to install the following dependency:

```bash
pip install autodistill-azure-vision
```

Next, you will need to [create an Azure account](https://azure.microsoft.com/en-gb/get-started/azure-portal). Once you have an Azure account, create a "Computer vision" deployment in the "Azure AI services" dashboard in Azure.

This deployment will give you two API keys and an endpoint URL. You will need one of these API keys and the endpoint URL to use this Autodistill module.

Set your API key and endpoint URL in your environment:

```
export AZURE_VISION_SUBSCRIPTION_KEY=<your api key>
export AZURE_VISION_ENDPOINT=<your endpoint>
```

Use the quickstart below to start labeling images.

## Quickstart

### Label a Single Image

```python
from autodistill_azure_vision import AzureVision
from autodistill.detection import CaptionOntology

# define an ontology to map class names to our Azure Custom Vision prompt
# the ontology dictionary has the format {caption: class}
# where caption is the prompt sent to the base model, and class is the label that will
# be saved for that caption in the generated annotations
# then, load the model
base_model = AzureVision(
    ontology=CaptionOntology(
        {
            "animal": "animal",
            "a forklift": "forklift"
        }
    ),
    endpoint=os.environ["AZURE_VISION_ENDPOINT"],
    subscription_key=os.environ["AZURE_VISION_SUBSCRIPTION_KEY"]
)

results = base_model.predict("image.jpeg")

print(results)

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

### Label a Folder of Images


```python
from autodistill_azure_vision import AzureVision
from autodistill.detection import CaptionOntology

# define an ontology to map class names to our Azure Custom Vision prompt
# the ontology dictionary has the format {caption: class}
# where caption is the prompt sent to the base model, and class is the label that will
# be saved for that caption in the generated annotations
# then, load the model
base_model = AzureVision(
    ontology=CaptionOntology(
        {
            "animal": "animal",
            "a forklift": "forklift"
        }
    ),
    endpoint=os.environ["AZURE_VISION_ENDPOINT"],
    subscription_key=os.environ["AZURE_VISION_SUBSCRIPTION_KEY"]
)

base_model.label("./context_images", extension=".jpeg")
```

## License

This project is licensed under an [MIT license](LICENSE).

## 🏆 Contributing

We love your input! Please see the core Autodistill [contributing guide](https://github.com/autodistill/autodistill/blob/main/CONTRIBUTING.md) to get started. Thank you 🙏 to all our contributors!