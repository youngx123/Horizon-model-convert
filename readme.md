<!--
 * @Author: xyoung
 * @Date: 2023-06-21 18:21:55
 * @LastEditTime: 2023-06-29 13:53:11
-->
## Horizon api model convert 

以`nanodet-s 320x320` 和 `yolov5-s 640x640` 两个模型为基础，按照地平线官方文档，搭建docker
环境，使用 **hb_mapper** 工具对模型算子进行检查和模型格式转换。针对不支持的算子进行修改。

```python
|-- nanodet-convert
|   |-- calibration_data # 模型后量化用到的图片，并转为 bin 格式图片
|   |-- hb_mapper-makertbin_result # bin 文件转换过程中中间文件
|   |-- hb_perf_result #模型测试结果
|   |   |-- nanodet_320x320
|   |-- src_data
|-- yolov5-convert
    |-- calibration_data
    |-- hb_mapper-makertbin_result
    |-- hb_perf_result
    |-- onnx_convert # 转换onnx模型和测试代码
        |-- models
```
> 征程5官方模型转换文档
>https://developer.horizon.ai/api/v1/fileData/horizon_j5_open_explorer_cn_doc/oe_mapper/source/faststart.html

> 官方文档
>https://developer.horizon.ai/api/v1/fileData/horizon_j5_open_explorer_cn_doc/index.html#