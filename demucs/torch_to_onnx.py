# %% Taken from pytorch example - Test that things work

import torch
import torchvision

dummy_input = torch.randn(10, 3, 224, 224, device="cpu")
model = torchvision.models.alexnet(pretrained=True)

# Providing input and output names sets the display names for values
# within the model's graph. Setting these does not change the semantics
# of the graph; it is only for readability.
#
# The inputs to the network consist of the flat list of inputs (i.e.
# the values you would pass to the forward() method) followed by the
# flat list of parameters. You can partially specify names, i.e. provide
# a list here shorter than the number of inputs to the model, and we will
# only set that subset of names, starting from the beginning.
input_names = ["actual_input_1"] + ["learned_%d" % i for i in range(16)]
output_names = ["output1"]

torch.onnx.export(
    model,
    dummy_input,
    "alexnet.onnx",
    verbose=True,
    input_names=input_names,
    output_names=output_names,
)


# %%

import torch as th
from torch.nn import functional as F

from demucs.audio import AudioFile
from demucs.utils import load_model


# %%

# Create the model and load the weights
model = load_model("./models/demucs_extra.th")

# %%

# print(model)
shape_of_first_layer = list(model.parameters())[0].shape
print(shape_of_first_layer)

dummy_input = th.zeros(shape_of_first_layer)
print(dummy_input)


# %%

device = "cpu"

mix = (
    AudioFile("../Song/Resources/mix1.mp3")
    .read(streams=0, samplerate=44100, channels=2)
    .to(device)
)

channels, length = mix.size()

# From utils.apply_model
valid_length = model.valid_length(length)
delta = valid_length - length
padded = F.pad(mix, (delta // 2, delta - delta // 2))

dummy_input = padded.unsqueeze(0)

# %%

# Define input / output names
input_names = ["my_input"]
output_names = ["my_output"]

# Convert the PyTorch model to ONNX
with th.no_grad():
    th.onnx.export(
        model,
        dummy_input,
        "./models/demucs_extra.onnx",
        verbose=True,
        input_names=input_names,
        output_names=output_names,
        opset_version=11,
        use_external_data_format=True,
    )

# %%
