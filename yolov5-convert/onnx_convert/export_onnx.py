# -*- coding: utf-8 -*-
# @Author : xyoung
# @Time : 14:28  2021-12-22
"""
According to the given yolo v5 6.0 version yamL file of any network,
construct the corresponding network structure and load the pre-training weights
img_size = 640
"""
import torch

from models.yolo import *

import onnxsim
import onnx


def export_onnx(model, input_size, file_name="model", simplify=True):
    input_name = "input"
    output_name = "output"
    input_data = torch.Tensor(1, input_size[0], input_size[1], input_size[2])
    print("input data shape : ", input_data.shape)
    onnx_name = file_name + ".onnx"
    torch.onnx.export(
        model,
        input_data,
        onnx_name,
        input_names=[input_name],
        output_names=[output_name],
        opset_version=11,
    )

    # Checks
    model_onnx = onnx.load(onnx_name)  # load onnx model
    onnx.checker.check_model(model_onnx)  # check onnx model
    if simplify:
        try:
            import onnxsim

            print(f'{onnx_name} simplifying with onnx-simplifier {onnxsim.__version__}...')
            model_onnx, check = onnxsim.simplify(
                model_onnx,
            )
            assert check, 'assert check failed'
            onnx_sim_name = file_name + "-sim.onnx"
            onnx.save(model_onnx, onnx_sim_name)
        except Exception as e:
            print(f'{onnx_name} simplifier failure: {e}')

        print(f'{onnx_name} export success, saved as {onnx_sim_name}')


if __name__ == '__main__':
    netName = "./yolov5s"
    model = Model(netName + ".yaml")
    model.eval()
    model_static = model.state_dict()

    # load pretrained model
    pretrained = netName + ".pt"
    model_dict = torch.load(pretrained)

    pretrained_state_dict = model_dict["model"].state_dict()
    del pretrained_state_dict['model.24.anchors']
    del pretrained_state_dict['model.24.anchor_grid']

    for id, (a, b, namea, nameb) in enumerate(
            zip(pretrained_state_dict.values(), model_static.values(), pretrained_state_dict.keys(),
                model_static.keys())):
        if namea.find('anchor') > -1:
            continue
        if not operator.eq(a.shape, b.shape):
            pass
        else:
            model_static[nameb].copy_(a)

    model.load_state_dict(model_static)
    export_onnx(model, [3, 640, 640])
    # for test
    filepath = "bus.jpg"  # bus
    srcimg0 = cv2.imread(filepath)
    srcimg = cv2.resize(srcimg0, (640, 640)) / 255.0
    srcimg = srcimg[np.newaxis, ...]
    srcimg = srcimg.transpose(0, 3, 1, 2)
    srcimg = torch.from_numpy(srcimg).float()
    outs = model(srcimg)

    z = []  # inference output
    for i in range(3):
        y = outs[i].detach().numpy()
        bs, _, _, _, _ = y.shape
        z.append(y.reshape(bs, -1, 85))
    z = np.concatenate(z, axis=1)

    # post processing
    frame = postprocess(srcimg0, z)
    # save result
    cv2.imwrite(netName + "1.png", frame)
