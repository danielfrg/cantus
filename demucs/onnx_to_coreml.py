# %%

import torch as th
from torch.nn import functional as F

import coremltools as ct
from coremltools.converters.mil import Builder as mb
from coremltools.converters.mil import register_torch_op
from coremltools.converters.mil.frontend.torch.ops import _get_inputs, _np

from demucs.audio import AudioFile
from demucs.utils import load_model


# %%

# Load the torch model
model = load_model("./models/demucs_extra.th")
model.eval()


# %%

# Create example input

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

example_input = padded.unsqueeze(0)

# %%

# Trace model for CoreML Tools
traced_model = th.jit.trace(model, example_input)


# %%


@register_torch_op(override=True)
def glu(context, node):
    # inputs = _get_inputs(context, node, expected=2)
    inputs = [context[name] for name in node.inputs]

    input_ = inputs[0]
    dim = inputs[1].val

    print(input_.shape)
    new_size = int(input_.shape[dim] / 2)
    begin_1 = [0, 0, 0]
    end_1 = list(input_.shape)
    end_1[dim] = new_size

    begin_2 = [0, 0, 0]
    begin_2[dim] = new_size
    end_2 = input_.shape

    print(begin_1)
    print(end_1)
    print(begin_2)
    print(end_2)

    # x = inputs[0]
    first_half = mb.slice_by_index(x=input_, begin=begin_1, end=end_1)
    second_half = mb.slice_by_index(x=input_, begin=begin_2, end=end_2)

    # print("!!!!")
    # print(context)
    # print(node)
    # print(node.inputs)
    # print(context["input.4"])
    # print(inputs)
    # print(inputs[0])
    # print(inputs[0].shape)
    # print(inputs[1])
    # print(inputs[1].shape)

    # res = mb.relu(x=inputs[0], name=node.name)

    second_half_sigmoid = mb.sigmoid(x=second_half)
    res = mb.mul(x=first_half, y=second_half_sigmoid, name=node.name)
    print(res)
    context.add(res)


# Convert to Core ML using the Unified Conversion API
model = ct.convert(
    traced_model, inputs=[ct.TensorType(name="input", shape=example_input.shape)]
)


# %%
