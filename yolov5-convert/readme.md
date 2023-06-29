**hb_mapper-checker result**
```shell
root@af23c3c673c9:/open_explorer# hb_mapper checker --model-type onnx --model model-sim2.onnx --march bayes --input-shape "input" "1x3x640x640"
2023-06-29 11:43:38,559 INFO log will be stored in /open_explorer/hb_mapper_checker.log
2023-06-29 11:43:38,559 INFO Start hb_mapper....
2023-06-29 11:43:38,559 INFO hbdk version 3.44.7
2023-06-29 11:43:38,559 INFO horizon_nn version 0.17.1
2023-06-29 11:43:38,559 INFO hb_mapper version 1.16.2
2023-06-29 11:43:38,586 INFO Model type: onnx
2023-06-29 11:43:38,586 INFO input names ['input']
2023-06-29 11:43:38,587 INFO input shapes {'input': [1, 3, 640, 640]}
2023-06-29 11:43:38,615 INFO Begin model checking....
2023-06-29 11:43:38,626 INFO [Thu Jun 29 11:43:38 2023] Start to Horizon NN Model Convert.
2023-06-29 11:43:38,626 INFO Loading horizon_nn debug methods:[]
2023-06-29 11:43:38,626 INFO Parsing the input parameter:{'input': {'input_shape': [1, 3, 640, 640]}}
2023-06-29 11:43:38,626 INFO Parsing the hbdk parameter:{'hbdk_pass_through_params': '--O0'}
2023-06-29 11:43:38,627 INFO HorizonNN version: 0.17.1
2023-06-29 11:43:38,627 INFO HBDK version: 3.44.7
2023-06-29 11:43:38,627 INFO [Thu Jun 29 11:43:38 2023] Start to parse the onnx model.
2023-06-29 11:43:38,642 INFO Input ONNX model infomation:
ONNX IR version:          6
Opset version:            [11]
Producer:                 pytorch1.8
Domain:                   none
Input name:               input, [1, 3, 640, 640]
Output name:              output, [1, 3, 80, 80, 85]
Output name:              663, [1, 3, 40, 40, 85]
Output name:              684, [1, 3, 20, 20, 85]
2023-06-29 11:43:38,801 INFO [Thu Jun 29 11:43:38 2023] End to parse the onnx model.
2023-06-29 11:43:38,801 INFO Model input names parsed from model: ['input']
2023-06-29 11:43:38,856 INFO Saving the original float model: ./.hb_check/original_float_model.onnx.
2023-06-29 11:43:38,856 INFO [Thu Jun 29 11:43:38 2023] Start to optimize the model.
2023-06-29 11:43:39,191 INFO [Thu Jun 29 11:43:39 2023] End to optimize the model.
2023-06-29 11:43:39,243 INFO Saving the optimized model: ./.hb_check/optimized_float_model.onnx.
2023-06-29 11:43:39,244 INFO [Thu Jun 29 11:43:39 2023] Start to calibrate the model.
2023-06-29 11:43:39,256 INFO There are 1 samples in the calibration data set.
2023-06-29 11:43:39,362 INFO Run calibration model with max method.
2023-06-29 11:43:39,528 INFO Calibration using batch 8
max calibration in progress: 100%|██████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  3.42it/s]
2023-06-29 11:43:40,328 INFO Saving the calibrated model: ./.hb_check/calibrated_model.onnx.
2023-06-29 11:43:40,328 INFO [Thu Jun 29 11:43:40 2023] End to calibrate the model.
2023-06-29 11:43:40,329 INFO [Thu Jun 29 11:43:40 2023] Start to quantize the model.
2023-06-29 11:43:42,542 INFO [Thu Jun 29 11:43:42 2023] End to quantize the model.
2023-06-29 11:43:42,830 INFO Saving the quantized model: ./.hb_check/quantized_model.onnx.
2023-06-29 11:43:43,705 INFO [Thu Jun 29 11:43:43 2023] Start to compile the model with march bayes.
2023-06-29 11:43:44,061 INFO Compile submodel: torch-jit-export_subgraph_0
2023-06-29 11:43:44,570 INFO hbdk-cc parameters:['--O0', '--input-layout', 'NHWC', '--output-layout', 'NHWC']
2023-06-29 11:43:45,723 INFO [Thu Jun 29 11:43:45 2023] End to compile the model with march bayes.
2023-06-29 11:43:45,725 INFO The converted model node information:
================================================================
Node                  ON   Subgraph  Type                       
----------------------------------------------------------------
Conv_0                BPU  id(0)     HzSQuantizedConv           
Mul_2                 BPU  id(0)     HzLut                      
Conv_3                BPU  id(0)     HzSQuantizedConv           
Mul_5                 BPU  id(0)     HzLut                      
Conv_6                BPU  id(0)     HzSQuantizedConv           
Mul_8                 BPU  id(0)     HzLut                      
Conv_9                BPU  id(0)     HzSQuantizedConv           
Mul_11                BPU  id(0)     HzLut                      
Conv_12               BPU  id(0)     HzSQuantizedConv           
Mul_14                BPU  id(0)     HzLut                      
UNIT_CONV_FOR_Add_15  BPU  id(0)     HzSQuantizedConv           
Conv_16               BPU  id(0)     HzSQuantizedConv           
Mul_18                BPU  id(0)     HzLut                      
373_Requantize        BPU  id(0)     HzRequantize               
Concat_19             BPU  id(0)     Concat                     
Conv_20               BPU  id(0)     HzSQuantizedConv           
Mul_22                BPU  id(0)     HzLut                      
Conv_23               BPU  id(0)     HzSQuantizedConv           
Mul_25                BPU  id(0)     HzLut                      
Conv_26               BPU  id(0)     HzSQuantizedConv           
Mul_28                BPU  id(0)     HzLut                      
Conv_29               BPU  id(0)     HzSQuantizedConv           
Mul_31                BPU  id(0)     HzLut                      
Conv_32               BPU  id(0)     HzSQuantizedConv           
Mul_34                BPU  id(0)     HzLut                      
UNIT_CONV_FOR_Add_35  BPU  id(0)     HzSQuantizedConv           
Conv_36               BPU  id(0)     HzSQuantizedConv           
Mul_38                BPU  id(0)     HzLut                      
Conv_39               BPU  id(0)     HzSQuantizedConv           
Mul_41                BPU  id(0)     HzLut                      
UNIT_CONV_FOR_Add_42  BPU  id(0)     HzSQuantizedConv           
Conv_43               BPU  id(0)     HzSQuantizedConv           
Mul_45                BPU  id(0)     HzLut                      
408_Requantize        BPU  id(0)     HzRequantize               
Concat_46             BPU  id(0)     Concat                     
Conv_47               BPU  id(0)     HzSQuantizedConv           
Mul_49                BPU  id(0)     HzLut                      
Conv_50               BPU  id(0)     HzSQuantizedConv           
Mul_52                BPU  id(0)     HzLut                      
Conv_53               BPU  id(0)     HzSQuantizedConv           
Mul_55                BPU  id(0)     HzLut                      
Conv_56               BPU  id(0)     HzSQuantizedConv           
Mul_58                BPU  id(0)     HzLut                      
Conv_59               BPU  id(0)     HzSQuantizedConv           
Mul_61                BPU  id(0)     HzLut                      
UNIT_CONV_FOR_Add_62  BPU  id(0)     HzSQuantizedConv           
Conv_63               BPU  id(0)     HzSQuantizedConv           
Mul_65                BPU  id(0)     HzLut                      
Conv_66               BPU  id(0)     HzSQuantizedConv           
Mul_68                BPU  id(0)     HzLut                      
UNIT_CONV_FOR_Add_69  BPU  id(0)     HzSQuantizedConv           
Conv_70               BPU  id(0)     HzSQuantizedConv           
Mul_72                BPU  id(0)     HzLut                      
Conv_73               BPU  id(0)     HzSQuantizedConv           
Mul_75                BPU  id(0)     HzLut                      
UNIT_CONV_FOR_Add_76  BPU  id(0)     HzSQuantizedConv           
Conv_77               BPU  id(0)     HzSQuantizedConv           
Mul_79                BPU  id(0)     HzLut                      
Concat_80             BPU  id(0)     Concat                     
Conv_81               BPU  id(0)     HzSQuantizedConv           
Mul_83                BPU  id(0)     HzLut                      
Conv_84               BPU  id(0)     HzSQuantizedConv           
Mul_86                BPU  id(0)     HzLut                      
Conv_87               BPU  id(0)     HzSQuantizedConv           
Mul_89                BPU  id(0)     HzLut                      
Conv_90               BPU  id(0)     HzSQuantizedConv           
Mul_92                BPU  id(0)     HzLut                      
Conv_93               BPU  id(0)     HzSQuantizedConv           
Mul_95                BPU  id(0)     HzLut                      
UNIT_CONV_FOR_Add_96  BPU  id(0)     HzSQuantizedConv           
Conv_97               BPU  id(0)     HzSQuantizedConv           
Mul_99                BPU  id(0)     HzLut                      
478_Requantize        BPU  id(0)     HzRequantize               
Concat_100            BPU  id(0)     Concat                     
Conv_101              BPU  id(0)     HzSQuantizedConv           
Mul_103               BPU  id(0)     HzLut                      
Conv_104              BPU  id(0)     HzSQuantizedConv           
Mul_106               BPU  id(0)     HzLut                      
MaxPool_107           BPU  id(0)     HzQuantizedMaxPool         
MaxPool_108           BPU  id(0)     HzQuantizedMaxPool         
MaxPool_109           BPU  id(0)     HzQuantizedMaxPool         
Concat_110            BPU  id(0)     Concat                     
Conv_111              BPU  id(0)     HzSQuantizedConv           
Mul_113               BPU  id(0)     HzLut                      
Conv_114              BPU  id(0)     HzSQuantizedConv           
Mul_116               BPU  id(0)     HzLut                      
Resize_125            BPU  id(0)     HzQuantizedResizeUpsample  
457_Requantize        BPU  id(0)     HzRequantize               
Concat_126            BPU  id(0)     Concat                     
Conv_127              BPU  id(0)     HzSQuantizedConv           
Mul_129               BPU  id(0)     HzLut                      
Conv_130              BPU  id(0)     HzSQuantizedConv           
Mul_132               BPU  id(0)     HzLut                      
Conv_133              BPU  id(0)     HzSQuantizedConv           
Mul_135               BPU  id(0)     HzLut                      
Conv_136              BPU  id(0)     HzSQuantizedConv           
Mul_138               BPU  id(0)     HzLut                      
523_Requantize        BPU  id(0)     HzRequantize               
527_Requantize        BPU  id(0)     HzRequantize               
Concat_139            BPU  id(0)     Concat                     
Conv_140              BPU  id(0)     HzSQuantizedConv           
Mul_142               BPU  id(0)     HzLut                      
Conv_143              BPU  id(0)     HzSQuantizedConv           
Mul_145               BPU  id(0)     HzLut                      
Resize_154            BPU  id(0)     HzQuantizedResizeUpsample  
547_Requantize        BPU  id(0)     HzRequantize               
Concat_155            BPU  id(0)     Concat                     
Conv_156              BPU  id(0)     HzSQuantizedConv           
Mul_158               BPU  id(0)     HzLut                      
Conv_159              BPU  id(0)     HzSQuantizedConv           
Mul_161               BPU  id(0)     HzLut                      
Conv_162              BPU  id(0)     HzSQuantizedConv           
Mul_164               BPU  id(0)     HzLut                      
Conv_165              BPU  id(0)     HzSQuantizedConv           
Mul_167               BPU  id(0)     HzLut                      
564_Requantize        BPU  id(0)     HzRequantize               
Concat_168            BPU  id(0)     Concat                     
Conv_169              BPU  id(0)     HzSQuantizedConv           
Mul_171               BPU  id(0)     HzLut                      
Conv_172              BPU  id(0)     HzSQuantizedConv           
Mul_174               BPU  id(0)     HzLut                      
573_Requantize        BPU  id(0)     HzRequantize               
536_Requantize        BPU  id(0)     HzRequantize               
Concat_175            BPU  id(0)     Concat                     
Conv_176              BPU  id(0)     HzSQuantizedConv           
Mul_178               BPU  id(0)     HzLut                      
Conv_179              BPU  id(0)     HzSQuantizedConv           
Mul_181               BPU  id(0)     HzLut                      
Conv_182              BPU  id(0)     HzSQuantizedConv           
Mul_184               BPU  id(0)     HzLut                      
Conv_185              BPU  id(0)     HzSQuantizedConv           
Mul_187               BPU  id(0)     HzLut                      
586_Requantize        BPU  id(0)     HzRequantize               
Concat_188            BPU  id(0)     Concat                     
Conv_189              BPU  id(0)     HzSQuantizedConv           
Mul_191               BPU  id(0)     HzLut                      
Conv_192              BPU  id(0)     HzSQuantizedConv           
Mul_194               BPU  id(0)     HzLut                      
599_Requantize        BPU  id(0)     HzRequantize               
Concat_195            BPU  id(0)     Concat                     
Conv_196              BPU  id(0)     HzSQuantizedConv           
Mul_198               BPU  id(0)     HzLut                      
Conv_199              BPU  id(0)     HzSQuantizedConv           
Mul_201               BPU  id(0)     HzLut                      
Conv_202              BPU  id(0)     HzSQuantizedConv           
Mul_204               BPU  id(0)     HzLut                      
Conv_205              BPU  id(0)     HzSQuantizedConv           
Mul_207               BPU  id(0)     HzLut                      
612_Requantize        BPU  id(0)     HzRequantize               
616_Requantize        BPU  id(0)     HzRequantize               
Concat_208            BPU  id(0)     Concat                     
Conv_209              BPU  id(0)     HzSQuantizedConv           
Mul_211               BPU  id(0)     HzLut                      
Conv_212              BPU  id(0)     HzSQuantizedConv           
Sigmoid_222           BPU  id(0)     HzLut                      
Reshape_227           BPU  id(0)     Reshape                    
Transpose_228         BPU  id(0)     Transpose                  
Conv_229              BPU  id(0)     HzSQuantizedConv           
Sigmoid_239           BPU  id(0)     HzLut                      
Reshape_244           BPU  id(0)     Reshape                    
Transpose_245         BPU  id(0)     Transpose                  
Conv_246              BPU  id(0)     HzSQuantizedConv           
Sigmoid_256           BPU  id(0)     HzLut                      
Reshape_261           BPU  id(0)     Reshape                    
Transpose_262         BPU  id(0)     Transpose
2023-06-29 11:43:45,726 INFO [Thu Jun 29 11:43:45 2023] End to Horizon NN Model Convert.
2023-06-29 11:43:45,735 INFO ONNX model output num : 3
2023-06-29 11:43:45,754 INFO End model checking....
```