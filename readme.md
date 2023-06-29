<!--
 * @Author: xyoung
 * @Date: 2023-06-21 18:21:55
 * @LastEditTime: 2023-06-29 11:56:32
-->
## Horizon api model convert 

以nanodet-s 320x320 和yolov5-s 640x640 两个模型为基础，按照地平线官方文档，搭建docker
环境，使用hb_mapper 工具对模型算子进行检查和模型格式转换。针对不支持的算子进行修改。