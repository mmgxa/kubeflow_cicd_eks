```
WARNING: sun.reflect.Reflection.getCallerClass is not supported. This will impact performance.
2023-11-12T07:59:50,972 [INFO ] main org.pytorch.serve.servingsdk.impl.PluginsManager - Initializing plugins manager...
2023-11-12T07:59:51,045 [INFO ] main org.pytorch.serve.ModelServer - 
Torchserve version: 0.7.0
TS Home: /usr/local/lib/python3.8/dist-packages
Current directory: /home/model-server
Temp directory: /home/model-server/tmp
Metrics config path: /usr/local/lib/python3.8/dist-packages/ts/configs/metrics.yaml
Number of GPUs: 1
Number of CPUs: 3
Max heap size: 1536 M
Python executable: /usr/bin/python3.8
Config file: /mnt/models/config/config.properties
Inference address: http://0.0.0.0:8085
Management address: http://0.0.0.0:8085
Metrics address: http://0.0.0.0:8082
Model Store: /mnt/models/model-store
Initial Models: N/A
Log dir: /home/model-server/logs
Metrics dir: /home/model-server/logs
Netty threads: 4
Netty client threads: 0
Default workers per model: 1
Blacklist Regex: N/A
Maximum Response Size: 655350000
Maximum Request Size: 6553500
Limit Maximum Image Pixels: true
Prefer direct buffer: false
Allowed Urls: [file://.*|http(s)?://.*]
Custom python dependency for model allowed: true
Metrics report format: prometheus
Enable metrics API: true
Workflow Store: /mnt/models/model-store
Model config: N/A
2023-11-12T07:59:51,051 [INFO ] main org.pytorch.serve.servingsdk.impl.PluginsManager -  Loading snapshot serializer plugin...
2023-11-12T07:59:51,072 [INFO ] main org.pytorch.serve.snapshot.SnapshotManager - Started restoring models from snapshot {"name":"startup.cfg","modelCount":1,"models":{"cifar10":{"1.0":{"defaultVersion":true,"marName":"cifar10_test.mar","minWorkers":1,"maxWorkers":5,"batchSize":1,"maxBatchDelay":5000,"responseTimeout":900}}}}
2023-11-12T07:59:51,078 [INFO ] main org.pytorch.serve.snapshot.SnapshotManager - Validating snapshot startup.cfg
2023-11-12T07:59:51,079 [INFO ] main org.pytorch.serve.snapshot.SnapshotManager - Snapshot startup.cfg validated successfully
2023-11-12T07:59:51,489 [DEBUG] main org.pytorch.serve.wlm.ModelVersionedRefs - Adding new version 1 for model cifar10
2023-11-12T07:59:51,489 [DEBUG] main org.pytorch.serve.wlm.ModelVersionedRefs - Setting default version to 1 for model cifar10
[I 231112 07:59:51 __main__:70] Wrapper : Model names ['cifar10'], inference address http//0.0.0.0:8085, management address http://0.0.0.0:8085, model store /mnt/models/model-store
[I 231112 07:59:51 TorchserveModel:52] kfmodel Predict URL set to 0.0.0.0:8085
[I 231112 07:59:51 TorchserveModel:54] kfmodel Explain URL set to 0.0.0.0:8085
[I 231112 07:59:51 storage:63] Copying contents of /mnt/models/model-store to local
[I 231112 07:59:51 TSModelRepository:27] TSModelRepo is initialized
[I 231112 07:59:51 model_server:150] Registering model: cifar10
[I 231112 07:59:51 model_server:123] Listening on port 8080
[I 231112 07:59:51 model_server:125] Will fork 1 workers
[I 231112 07:59:51 model_server:128] Setting max asyncio worker threads as 7
2023-11-12T08:03:17,539 [DEBUG] main org.pytorch.serve.wlm.ModelVersionedRefs - Setting default version to 1 for model cifar10
2023-11-12T08:03:17,550 [INFO ] main org.pytorch.serve.wlm.ModelManager - Model cifar10 loaded.
2023-11-12T08:03:17,550 [DEBUG] main org.pytorch.serve.wlm.ModelManager - updateModel: cifar10, count: 1
2023-11-12T08:03:17,563 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerLifeCycle - Worker cmdline: [/usr/bin/python3.8, /usr/local/lib/python3.8/dist-packages/ts/model_service_worker.py, --sock-type, unix, --sock-name, /home/model-server/tmp/.ts.sock.9000, --metrics-config, /usr/local/lib/python3.8/dist-packages/ts/configs/metrics.yaml]
2023-11-12T08:03:17,566 [INFO ] main org.pytorch.serve.ModelServer - Initialize Inference server with: EpollServerSocketChannel.
2023-11-12T08:03:17,677 [INFO ] main org.pytorch.serve.ModelServer - Inference API bind to: http://0.0.0.0:8085
2023-11-12T08:03:17,677 [INFO ] main org.pytorch.serve.ModelServer - Initialize Metrics server with: EpollServerSocketChannel.
2023-11-12T08:03:17,678 [INFO ] main org.pytorch.serve.ModelServer - Metrics API bind to: http://0.0.0.0:8082
Model server started.
2023-11-12T08:03:17,867 [WARN ] pool-3-thread-1 org.pytorch.serve.metrics.MetricCollector - worker pid is not available yet.
2023-11-12T08:03:18,337 [INFO ] pool-3-thread-1 TS_METRICS - CPUUtilization.Percent:0.0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776198
2023-11-12T08:03:18,338 [INFO ] pool-3-thread-1 TS_METRICS - DiskAvailable.Gigabytes:13.947399139404297|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776198
2023-11-12T08:03:18,338 [INFO ] pool-3-thread-1 TS_METRICS - DiskUsage.Gigabytes:46.040863037109375|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776198
2023-11-12T08:03:18,338 [INFO ] pool-3-thread-1 TS_METRICS - DiskUtilization.Percent:76.7|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776198
2023-11-12T08:03:18,339 [INFO ] pool-3-thread-1 TS_METRICS - GPUMemoryUtilization.Percent:0.0|#Level:Host,device_id:0|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776198
2023-11-12T08:03:18,339 [INFO ] pool-3-thread-1 TS_METRICS - GPUMemoryUsed.Megabytes:0|#Level:Host,device_id:0|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776198
2023-11-12T08:03:18,339 [INFO ] pool-3-thread-1 TS_METRICS - GPUUtilization.Percent:0|#Level:Host,device_id:0|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776198
2023-11-12T08:03:18,340 [INFO ] pool-3-thread-1 TS_METRICS - MemoryAvailable.Megabytes:29758.9296875|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776198
2023-11-12T08:03:18,340 [INFO ] pool-3-thread-1 TS_METRICS - MemoryUsed.Megabytes:1422.45703125|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776198
2023-11-12T08:03:18,341 [INFO ] pool-3-thread-1 TS_METRICS - MemoryUtilization.Percent:5.9|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776198
2023-11-12T08:03:26,688 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Listening on port: /home/model-server/tmp/.ts.sock.9000
2023-11-12T08:03:26,693 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Successfully loaded /usr/local/lib/python3.8/dist-packages/ts/configs/metrics.yaml.
2023-11-12T08:03:26,693 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - [PID]98
2023-11-12T08:03:26,694 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Torch worker started.
2023-11-12T08:03:26,694 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Python runtime: 3.8.10
2023-11-12T08:03:26,694 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - W-9000-cifar10_1 State change null -> WORKER_STARTED
2023-11-12T08:03:26,700 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Connecting to: /home/model-server/tmp/.ts.sock.9000
2023-11-12T08:03:26,708 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Connection accepted: /home/model-server/tmp/.ts.sock.9000.
2023-11-12T08:03:26,711 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776206711
2023-11-12T08:03:26,744 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - model_name: cifar10, batchSize: 1
2023-11-12T08:03:27,125 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - generated new fontManager
2023-11-12T08:03:28,371 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Model dir is /home/model-server/tmp/models/d37baf69a9c3423da8991a5388a9579a
2023-11-12T08:03:28,415 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Torch Version: 2.1.0+cu118
2023-11-12T08:03:28,415 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Using Device: cuda:0
2023-11-12T08:03:28,591 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Loading pretrained weights from Hugging Face hub (timm/vit_tiny_patch16_224.augreg_in21k_ft_in1k)
2023-11-12T08:03:28,787 [WARN ] W-9000-cifar10_1-stderr MODEL_LOG - 
2023-11-12T08:03:28,895 [WARN ] W-9000-cifar10_1-stderr MODEL_LOG - model.safetensors:   0%|          | 0.00/22.9M [00:00<?, ?B/s]
2023-11-12T08:03:28,906 [WARN ] W-9000-cifar10_1-stderr MODEL_LOG - model.safetensors:  92%|█████████▏| 21.0M/22.9M [00:00<00:00, 195MB/s]
2023-11-12T08:03:28,906 [WARN ] W-9000-cifar10_1-stderr MODEL_LOG - model.safetensors: 100%|██████████| 22.9M/22.9M [00:00<00:00, 193MB/s]
2023-11-12T08:03:28,907 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - [timm/vit_tiny_patch16_224.augreg_in21k_ft_in1k] Safe alternative available for 'pytorch_model.bin' (as 'model.safetensors'). Loading weights using safetensors.
2023-11-12T08:03:31,335 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - CIFAR10 model from path /home/model-server/tmp/models/d37baf69a9c3423da8991a5388a9579a loaded successfully
2023-11-12T08:03:31,336 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Mapping file present
2023-11-12T08:03:31,343 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 4599
2023-11-12T08:03:31,343 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - W-9000-cifar10_1 State change WORKER_STARTED -> WORKER_MODEL_LOADED
2023-11-12T08:03:31,343 [INFO ] W-9000-cifar10_1 TS_METRICS - W-9000-cifar10_1.ms:13783|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776211
2023-11-12T08:03:31,344 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:34|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776211
[I 231112 08:04:03 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:03,758 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776243758
2023-11-12T08:04:03,761 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776243
2023-11-12T08:04:05,413 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:1650.55|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:7071020c-3f9e-4f37-a8f5-b4f1089b1557,timestamp:1699776245
2023-11-12T08:04:05,413 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:1650.92|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:7071020c-3f9e-4f37-a8f5-b4f1089b1557,timestamp:1699776245
2023-11-12T08:04:05,413 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 1653
2023-11-12T08:04:05,415 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:56806 "POST /v1/models/cifar10:predict HTTP/1.1" 200 1664
2023-11-12T08:04:05,415 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:05,415 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 152193, Backend time ns: 1657233029
2023-11-12T08:04:05,415 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776245
2023-11-12T08:04:05,416 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:5|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776245
[I 231112 08:04:05 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 1726.72ms
[I 231112 08:04:05 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:05,733 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776245733
2023-11-12T08:04:05,735 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776245
2023-11-12T08:04:05,756 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.94|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:6c66bf51-e4e8-4c66-b346-c4dc763d35b6,timestamp:1699776245
2023-11-12T08:04:05,756 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.21|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:6c66bf51-e4e8-4c66-b346-c4dc763d35b6,timestamp:1699776245
2023-11-12T08:04:05,756 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:05,757 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:59978 "POST /v1/models/cifar10:predict HTTP/1.1" 200 25
2023-11-12T08:04:05,757 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:05,757 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 117221, Backend time ns: 24324800
2023-11-12T08:04:05,757 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776245
2023-11-12T08:04:05,757 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776245
[I 231112 08:04:05 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 74.16ms
[I 231112 08:04:05 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:05,939 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776245939
2023-11-12T08:04:05,941 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776245
2023-11-12T08:04:05,962 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.49|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:bddaf6c1-279c-4feb-b4c5-cfd908f7ab52,timestamp:1699776245
2023-11-12T08:04:05,963 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.76|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:bddaf6c1-279c-4feb-b4c5-cfd908f7ab52,timestamp:1699776245
2023-11-12T08:04:05,963 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 23
2023-11-12T08:04:05,963 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:59988 "POST /v1/models/cifar10:predict HTTP/1.1" 200 25
2023-11-12T08:04:05,963 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:05,964 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 106808, Backend time ns: 24558930
2023-11-12T08:04:05,964 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776245
2023-11-12T08:04:05,964 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776245
[I 231112 08:04:05 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 83.18ms
[I 231112 08:04:06 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:06,123 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776246123
2023-11-12T08:04:06,125 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776246
2023-11-12T08:04:06,145 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.47|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:eb3d83dc-a556-44fc-8436-c235b15e9993,timestamp:1699776246
2023-11-12T08:04:06,146 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.73|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:eb3d83dc-a556-44fc-8436-c235b15e9993,timestamp:1699776246
2023-11-12T08:04:06,146 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:06,146 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60002 "POST /v1/models/cifar10:predict HTTP/1.1" 200 24
2023-11-12T08:04:06,146 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:06,147 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 99657, Backend time ns: 24103295
2023-11-12T08:04:06,147 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776246
2023-11-12T08:04:06,147 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776246
[I 231112 08:04:06 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 60.64ms
[I 231112 08:04:06 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:06,283 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776246283
2023-11-12T08:04:06,285 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776246
2023-11-12T08:04:06,305 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.13|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:e9204c28-9fb7-47dc-b198-0c72184c81aa,timestamp:1699776246
2023-11-12T08:04:06,306 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.38|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:e9204c28-9fb7-47dc-b198-0c72184c81aa,timestamp:1699776246
2023-11-12T08:04:06,306 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:06,306 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60012 "POST /v1/models/cifar10:predict HTTP/1.1" 200 24
2023-11-12T08:04:06,306 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:06,307 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 98108, Backend time ns: 23768220
2023-11-12T08:04:06,307 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776246
2023-11-12T08:04:06,307 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776246
[I 231112 08:04:06 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 38.84ms
[I 231112 08:04:06 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:06,458 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776246458
2023-11-12T08:04:06,461 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776246
2023-11-12T08:04:06,481 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.47|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:6498440a-21c5-45fb-b48a-dbbefdb571ec,timestamp:1699776246
2023-11-12T08:04:06,482 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.76|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:6498440a-21c5-45fb-b48a-dbbefdb571ec,timestamp:1699776246
2023-11-12T08:04:06,482 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:06,482 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60020 "POST /v1/models/cifar10:predict HTTP/1.1" 200 24
2023-11-12T08:04:06,482 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:06,483 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 116287, Backend time ns: 24382067
2023-11-12T08:04:06,483 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776246
2023-11-12T08:04:06,483 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:3|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776246
[I 231112 08:04:06 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 43.82ms
[I 231112 08:04:06 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:06,651 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776246651
2023-11-12T08:04:06,653 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776246
2023-11-12T08:04:06,673 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.61|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:afd2decb-228a-40ba-9344-41039ea1fb52,timestamp:1699776246
2023-11-12T08:04:06,673 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.89|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:afd2decb-228a-40ba-9344-41039ea1fb52,timestamp:1699776246
2023-11-12T08:04:06,673 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:06,674 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60036 "POST /v1/models/cifar10:predict HTTP/1.1" 200 24
2023-11-12T08:04:06,674 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:06,674 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 97915, Backend time ns: 23470501
2023-11-12T08:04:06,675 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776246
2023-11-12T08:04:06,675 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:3|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776246
[I 231112 08:04:06 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 35.99ms
[I 231112 08:04:06 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:06,881 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776246881
2023-11-12T08:04:06,883 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776246
2023-11-12T08:04:06,903 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.23|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:43caafcc-c7c9-4d57-91da-d0cedea3a49c,timestamp:1699776246
2023-11-12T08:04:06,904 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.49|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:43caafcc-c7c9-4d57-91da-d0cedea3a49c,timestamp:1699776246
2023-11-12T08:04:06,904 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:06,904 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60038 "POST /v1/models/cifar10:predict HTTP/1.1" 200 24
2023-11-12T08:04:06,904 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:06,905 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 91294, Backend time ns: 23726751
2023-11-12T08:04:06,905 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776246
2023-11-12T08:04:06,905 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776246
[I 231112 08:04:06 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 36.45ms
[I 231112 08:04:07 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:07,060 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776247060
2023-11-12T08:04:07,062 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776247
2023-11-12T08:04:07,082 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.1|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:2a61d836-3624-41f6-b271-35b26f84d0c0,timestamp:1699776247
2023-11-12T08:04:07,083 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.36|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:2a61d836-3624-41f6-b271-35b26f84d0c0,timestamp:1699776247
2023-11-12T08:04:07,083 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:07,083 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60052 "POST /v1/models/cifar10:predict HTTP/1.1" 200 24
2023-11-12T08:04:07,083 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:07,083 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 84689, Backend time ns: 23507225
2023-11-12T08:04:07,084 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776247
2023-11-12T08:04:07,084 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776247
[I 231112 08:04:07 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 43.34ms
[I 231112 08:04:07 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:07,223 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776247223
2023-11-12T08:04:07,225 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776247
2023-11-12T08:04:07,245 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.17|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:df227b7a-491a-47ff-ac30-ae4eb13276d8,timestamp:1699776247
2023-11-12T08:04:07,246 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.42|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:df227b7a-491a-47ff-ac30-ae4eb13276d8,timestamp:1699776247
2023-11-12T08:04:07,246 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:07,246 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60056 "POST /v1/models/cifar10:predict HTTP/1.1" 200 24
2023-11-12T08:04:07,246 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:07,246 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 87393, Backend time ns: 23706790
2023-11-12T08:04:07,247 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776247
2023-11-12T08:04:07,247 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776247
[I 231112 08:04:07 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 33.94ms
[I 231112 08:04:07 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:07,388 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776247388
2023-11-12T08:04:07,390 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776247
2023-11-12T08:04:07,411 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.16|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:b8014968-753c-4654-a5cd-db4aac986ca8,timestamp:1699776247
2023-11-12T08:04:07,411 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.42|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:b8014968-753c-4654-a5cd-db4aac986ca8,timestamp:1699776247
2023-11-12T08:04:07,411 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:07,411 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60068 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:07,411 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:07,412 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 80162, Backend time ns: 23350482
2023-11-12T08:04:07,412 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776247
2023-11-12T08:04:07,412 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776247
[I 231112 08:04:07 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 35.50ms
[I 231112 08:04:07 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:07,575 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776247575
2023-11-12T08:04:07,577 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776247
2023-11-12T08:04:07,598 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.06|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:41b98abe-83dd-4934-a321-792bf7ae79c6,timestamp:1699776247
2023-11-12T08:04:07,598 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.3|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:41b98abe-83dd-4934-a321-792bf7ae79c6,timestamp:1699776247
2023-11-12T08:04:07,598 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:07,598 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60084 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:07,599 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:07,599 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 90210, Backend time ns: 23456032
2023-11-12T08:04:07,599 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776247
2023-11-12T08:04:07,599 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776247
[I 231112 08:04:07 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 42.77ms
[I 231112 08:04:07 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:07,749 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776247749
2023-11-12T08:04:07,751 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776247
2023-11-12T08:04:07,770 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.55|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:62c38a75-be3d-4ea4-932f-2ba289327178,timestamp:1699776247
2023-11-12T08:04:07,771 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.82|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:62c38a75-be3d-4ea4-932f-2ba289327178,timestamp:1699776247
2023-11-12T08:04:07,771 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:07,771 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60094 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:07,771 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:07,771 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 94178, Backend time ns: 22870815
2023-11-12T08:04:07,772 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776247
2023-11-12T08:04:07,772 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776247
[I 231112 08:04:07 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 34.53ms
[I 231112 08:04:07 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:07,949 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776247949
2023-11-12T08:04:07,951 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776247
2023-11-12T08:04:07,970 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.34|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:f3450021-b26a-4c36-b75a-229ec0454a19,timestamp:1699776247
2023-11-12T08:04:07,971 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.61|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:f3450021-b26a-4c36-b75a-229ec0454a19,timestamp:1699776247
2023-11-12T08:04:07,971 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:07,971 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60104 "POST /v1/models/cifar10:predict HTTP/1.1" 200 24
2023-11-12T08:04:07,971 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:07,971 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 80819, Backend time ns: 22806313
2023-11-12T08:04:07,972 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776247
2023-11-12T08:04:07,972 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776247
[I 231112 08:04:07 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 45.09ms
[I 231112 08:04:08 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:08,164 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776248164
2023-11-12T08:04:08,166 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776248
2023-11-12T08:04:08,186 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.54|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:4b84a216-e063-40b1-8937-365800ec416d,timestamp:1699776248
2023-11-12T08:04:08,187 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:08,187 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60120 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:08,187 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.8|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:4b84a216-e063-40b1-8937-365800ec416d,timestamp:1699776248
2023-11-12T08:04:08,187 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:08,187 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 88603, Backend time ns: 22887040
2023-11-12T08:04:08,187 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776248
2023-11-12T08:04:08,187 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776248
[I 231112 08:04:08 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 32.60ms
[I 231112 08:04:08 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:08,434 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776248433
2023-11-12T08:04:08,436 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776248
2023-11-12T08:04:08,456 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.13|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:eef0a310-711f-4c35-9296-808a532c0c3d,timestamp:1699776248
2023-11-12T08:04:08,456 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.42|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:eef0a310-711f-4c35-9296-808a532c0c3d,timestamp:1699776248
2023-11-12T08:04:08,456 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:08,457 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60126 "POST /v1/models/cifar10:predict HTTP/1.1" 200 24
2023-11-12T08:04:08,457 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:08,457 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 96264, Backend time ns: 23475665
2023-11-12T08:04:08,457 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776248
2023-11-12T08:04:08,457 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:3|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776248
[I 231112 08:04:08 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 44.46ms
[I 231112 08:04:08 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:08,624 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776248624
2023-11-12T08:04:08,627 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776248
2023-11-12T08:04:08,648 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:21.33|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:dddb405c-fd15-4abe-8a75-20979ec7a098,timestamp:1699776248
2023-11-12T08:04:08,649 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 24
2023-11-12T08:04:08,649 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:21.61|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:dddb405c-fd15-4abe-8a75-20979ec7a098,timestamp:1699776248
2023-11-12T08:04:08,649 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60132 "POST /v1/models/cifar10:predict HTTP/1.1" 200 26
2023-11-12T08:04:08,649 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:08,649 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 86770, Backend time ns: 25310654
2023-11-12T08:04:08,649 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776248
2023-11-12T08:04:08,650 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776248
[I 231112 08:04:08 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 38.79ms
[I 231112 08:04:08 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:08,826 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776248826
2023-11-12T08:04:08,828 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776248
2023-11-12T08:04:08,847 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.47|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:59ffb510-b600-47ee-8a03-165b5c94c2e1,timestamp:1699776248
2023-11-12T08:04:08,848 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:08,848 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.74|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:59ffb510-b600-47ee-8a03-165b5c94c2e1,timestamp:1699776248
2023-11-12T08:04:08,848 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60134 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:08,848 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:08,848 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 100231, Backend time ns: 22705496
2023-11-12T08:04:08,848 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776248
2023-11-12T08:04:08,849 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776248
[I 231112 08:04:08 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 32.47ms
[I 231112 08:04:09 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:09,030 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776249030
2023-11-12T08:04:09,032 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776249
2023-11-12T08:04:09,053 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.3|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:8b6f90b1-5c31-45b9-a38d-2537e7aca9af,timestamp:1699776249
2023-11-12T08:04:09,053 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.59|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:8b6f90b1-5c31-45b9-a38d-2537e7aca9af,timestamp:1699776249
2023-11-12T08:04:09,053 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:09,053 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60140 "POST /v1/models/cifar10:predict HTTP/1.1" 200 24
2023-11-12T08:04:09,053 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:09,054 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 101402, Backend time ns: 23777300
2023-11-12T08:04:09,054 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776249
2023-11-12T08:04:09,054 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776249
[I 231112 08:04:09 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 41.04ms
[I 231112 08:04:09 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:09,210 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776249210
2023-11-12T08:04:09,212 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776249
2023-11-12T08:04:09,232 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.4|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:c7f940e1-9e09-4b33-bd4c-58869da77545,timestamp:1699776249
2023-11-12T08:04:09,233 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.72|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:c7f940e1-9e09-4b33-bd4c-58869da77545,timestamp:1699776249
2023-11-12T08:04:09,233 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:09,233 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60150 "POST /v1/models/cifar10:predict HTTP/1.1" 200 24
2023-11-12T08:04:09,233 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:09,233 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 96873, Backend time ns: 23633104
2023-11-12T08:04:09,233 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776249
2023-11-12T08:04:09,233 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776249
[I 231112 08:04:09 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 36.28ms
[I 231112 08:04:09 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:09,414 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776249414
2023-11-12T08:04:09,416 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776249
2023-11-12T08:04:09,436 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.62|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:7b025381-477e-4582-9233-ec7104f56557,timestamp:1699776249
2023-11-12T08:04:09,436 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:09,436 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.9|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:7b025381-477e-4582-9233-ec7104f56557,timestamp:1699776249
2023-11-12T08:04:09,436 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60160 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:09,436 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:09,436 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 86890, Backend time ns: 22858509
2023-11-12T08:04:09,437 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776249
2023-11-12T08:04:09,437 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776249
[I 231112 08:04:09 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 32.31ms
[I 231112 08:04:09 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:09,595 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776249595
2023-11-12T08:04:09,597 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776249
2023-11-12T08:04:09,617 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.43|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:b5a31b7a-37bb-4278-b243-bd00af5ad4d8,timestamp:1699776249
2023-11-12T08:04:09,617 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.69|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:b5a31b7a-37bb-4278-b243-bd00af5ad4d8,timestamp:1699776249
2023-11-12T08:04:09,617 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:09,617 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60166 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:09,617 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:09,617 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 84004, Backend time ns: 22434384
2023-11-12T08:04:09,617 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776249
2023-11-12T08:04:09,617 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776249
[I 231112 08:04:09 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 43.75ms
[I 231112 08:04:09 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:09,768 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776249768
2023-11-12T08:04:09,770 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776249
2023-11-12T08:04:09,790 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.58|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:0a45fc3a-2aed-431a-be59-f1406f6a8a4b,timestamp:1699776249
2023-11-12T08:04:09,791 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.85|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:0a45fc3a-2aed-431a-be59-f1406f6a8a4b,timestamp:1699776249
2023-11-12T08:04:09,791 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:09,791 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60172 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:09,791 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:09,791 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 102733, Backend time ns: 22822572
2023-11-12T08:04:09,791 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776249
2023-11-12T08:04:09,791 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776249
[I 231112 08:04:09 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 36.73ms
[I 231112 08:04:09 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:09,967 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776249967
2023-11-12T08:04:09,969 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776249
2023-11-12T08:04:09,988 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.39|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:628a2c77-4ec9-4833-8a08-9d76812807ad,timestamp:1699776249
2023-11-12T08:04:09,989 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.68|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:628a2c77-4ec9-4833-8a08-9d76812807ad,timestamp:1699776249
2023-11-12T08:04:09,989 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:09,989 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60186 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:09,989 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:09,989 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 92537, Backend time ns: 22595762
2023-11-12T08:04:09,989 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776249
2023-11-12T08:04:09,989 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776249
[I 231112 08:04:09 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 32.53ms
[I 231112 08:04:10 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:10,159 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776250158
2023-11-12T08:04:10,160 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776250
2023-11-12T08:04:10,180 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.46|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:485a2a9e-889c-4921-90c7-346b58248211,timestamp:1699776250
2023-11-12T08:04:10,180 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.77|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:485a2a9e-889c-4921-90c7-346b58248211,timestamp:1699776250
2023-11-12T08:04:10,180 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:10,181 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60200 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:10,181 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:10,181 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 93735, Backend time ns: 22532280
2023-11-12T08:04:10,181 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776250
2023-11-12T08:04:10,181 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776250
[I 231112 08:04:10 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 33.81ms
[I 231112 08:04:10 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:10,345 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776250345
2023-11-12T08:04:10,347 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776250
2023-11-12T08:04:10,367 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.55|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:e7f427e9-bb60-40d4-88e3-a9cd8b832630,timestamp:1699776250
2023-11-12T08:04:10,367 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.83|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:e7f427e9-bb60-40d4-88e3-a9cd8b832630,timestamp:1699776250
2023-11-12T08:04:10,367 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:10,368 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60210 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:10,368 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:10,368 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 81224, Backend time ns: 22878007
2023-11-12T08:04:10,368 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776250
2023-11-12T08:04:10,368 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776250
[I 231112 08:04:10 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 32.08ms
[I 231112 08:04:10 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:10,542 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776250542
2023-11-12T08:04:10,544 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776250
2023-11-12T08:04:10,563 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.29|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:aa4c869c-f632-4796-a322-6c5db8ac83c8,timestamp:1699776250
2023-11-12T08:04:10,563 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.55|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:aa4c869c-f632-4796-a322-6c5db8ac83c8,timestamp:1699776250
2023-11-12T08:04:10,564 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:10,564 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60224 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:10,564 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:10,564 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 80990, Backend time ns: 22210270
2023-11-12T08:04:10,564 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776250
2023-11-12T08:04:10,564 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776250
[I 231112 08:04:10 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 40.96ms
[I 231112 08:04:10 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:10,746 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776250746
2023-11-12T08:04:10,748 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776250
2023-11-12T08:04:10,768 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.1|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:f1326238-b71f-4dfd-bc24-9a487f1e1434,timestamp:1699776250
2023-11-12T08:04:10,769 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.38|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:f1326238-b71f-4dfd-bc24-9a487f1e1434,timestamp:1699776250
2023-11-12T08:04:10,769 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:10,769 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60228 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:10,769 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:10,769 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 95494, Backend time ns: 23075070
2023-11-12T08:04:10,769 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776250
2023-11-12T08:04:10,769 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776250
[I 231112 08:04:10 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 41.20ms
[I 231112 08:04:10 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:10,953 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776250953
2023-11-12T08:04:10,955 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776250
2023-11-12T08:04:10,976 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.77|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:c8d2c615-3cfa-4eb8-8d6d-a3e28177c349,timestamp:1699776250
2023-11-12T08:04:10,977 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:21.05|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:c8d2c615-3cfa-4eb8-8d6d-a3e28177c349,timestamp:1699776250
2023-11-12T08:04:10,977 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 23
2023-11-12T08:04:10,977 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60234 "POST /v1/models/cifar10:predict HTTP/1.1" 200 24
2023-11-12T08:04:10,977 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:10,977 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 90178, Backend time ns: 24134050
2023-11-12T08:04:10,977 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776250
2023-11-12T08:04:10,977 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776250
[I 231112 08:04:10 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 34.18ms
[I 231112 08:04:11 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:11,127 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776251127
2023-11-12T08:04:11,129 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776251
2023-11-12T08:04:11,149 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.28|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:415f670b-9cea-45e1-a41f-a1fbcdf59357,timestamp:1699776251
2023-11-12T08:04:11,150 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.55|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:415f670b-9cea-45e1-a41f-a1fbcdf59357,timestamp:1699776251
2023-11-12T08:04:11,150 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:11,150 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60238 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:11,150 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:11,150 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 82007, Backend time ns: 23408404
2023-11-12T08:04:11,151 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776251
2023-11-12T08:04:11,151 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776251
[I 231112 08:04:11 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 32.94ms
[I 231112 08:04:11 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:11,297 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776251297
2023-11-12T08:04:11,299 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776251
2023-11-12T08:04:11,319 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.09|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:a19df52d-8957-4d0e-b505-b86be6c96c3b,timestamp:1699776251
2023-11-12T08:04:11,319 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.37|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:a19df52d-8957-4d0e-b505-b86be6c96c3b,timestamp:1699776251
2023-11-12T08:04:11,320 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:11,320 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60254 "POST /v1/models/cifar10:predict HTTP/1.1" 200 24
2023-11-12T08:04:11,320 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:11,320 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 73619, Backend time ns: 23583064
2023-11-12T08:04:11,320 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776251
[I 231112 08:04:11 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 34.51ms
2023-11-12T08:04:11,320 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776251
[I 231112 08:04:11 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:11,493 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776251493
2023-11-12T08:04:11,495 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776251
2023-11-12T08:04:11,514 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.28|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:0d025d77-201a-4271-b888-e5aa113b1dd7,timestamp:1699776251
2023-11-12T08:04:11,515 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.56|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:0d025d77-201a-4271-b888-e5aa113b1dd7,timestamp:1699776251
2023-11-12T08:04:11,515 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:11,515 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60256 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:11,515 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:11,515 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 97054, Backend time ns: 22372235
2023-11-12T08:04:11,515 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776251
2023-11-12T08:04:11,515 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776251
[I 231112 08:04:11 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 31.91ms
[I 231112 08:04:11 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:11,687 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776251687
2023-11-12T08:04:11,689 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776251
2023-11-12T08:04:11,708 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.33|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:584e8c55-fc83-4990-96c1-b98c82abd1f7,timestamp:1699776251
2023-11-12T08:04:11,708 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.59|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:584e8c55-fc83-4990-96c1-b98c82abd1f7,timestamp:1699776251
2023-11-12T08:04:11,709 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 20
[I 231112 08:04:11 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 31.75ms
2023-11-12T08:04:11,709 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60258 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:11,709 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:11,709 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 84290, Backend time ns: 22261977
2023-11-12T08:04:11,709 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776251
2023-11-12T08:04:11,709 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776251
[I 231112 08:04:11 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:11,855 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776251855
2023-11-12T08:04:11,857 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776251
2023-11-12T08:04:11,877 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.03|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:63fe0d4e-656b-4343-ab8b-d109c5f34aac,timestamp:1699776251
2023-11-12T08:04:11,877 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.29|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:63fe0d4e-656b-4343-ab8b-d109c5f34aac,timestamp:1699776251
2023-11-12T08:04:11,877 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:11,877 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60270 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:11,877 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:11,878 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 88255, Backend time ns: 22955709
2023-11-12T08:04:11,878 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776251
2023-11-12T08:04:11,878 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776251
[I 231112 08:04:11 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 35.82ms
[I 231112 08:04:12 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:12,052 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776252052
2023-11-12T08:04:12,054 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776252
2023-11-12T08:04:12,074 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.13|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:f70fcdd6-81c5-4360-8959-c9760adf618b,timestamp:1699776252
2023-11-12T08:04:12,074 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.39|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:f70fcdd6-81c5-4360-8959-c9760adf618b,timestamp:1699776252
2023-11-12T08:04:12,074 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:12,075 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60280 "POST /v1/models/cifar10:predict HTTP/1.1" 200 24
2023-11-12T08:04:12,075 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:12,075 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 114301, Backend time ns: 23158604
2023-11-12T08:04:12,075 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776252
2023-11-12T08:04:12,075 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776252
[I 231112 08:04:12 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 32.27ms
[I 231112 08:04:12 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:12,221 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776252221
2023-11-12T08:04:12,223 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776252
2023-11-12T08:04:12,243 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.09|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:c4a8adcd-d49d-45ed-9c95-1f2ec798b158,timestamp:1699776252
2023-11-12T08:04:12,244 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.34|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:c4a8adcd-d49d-45ed-9c95-1f2ec798b158,timestamp:1699776252
2023-11-12T08:04:12,244 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:12,244 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60294 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:12,244 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:12,244 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 94774, Backend time ns: 22892935
2023-11-12T08:04:12,244 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776252
2023-11-12T08:04:12,244 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776252
[I 231112 08:04:12 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 32.67ms
[I 231112 08:04:12 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:12,400 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776252400
2023-11-12T08:04:12,402 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776252
2023-11-12T08:04:12,422 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.99|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:a4f79920-f7c5-4e80-89ad-7e73eaaadd35,timestamp:1699776252
2023-11-12T08:04:12,422 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.25|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:a4f79920-f7c5-4e80-89ad-7e73eaaadd35,timestamp:1699776252
2023-11-12T08:04:12,422 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:12,422 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60296 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:12,423 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:12,423 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 72977, Backend time ns: 23025586
2023-11-12T08:04:12,423 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776252
2023-11-12T08:04:12,423 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776252
[I 231112 08:04:12 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 32.57ms
[I 231112 08:04:12 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:12,570 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776252570
2023-11-12T08:04:12,572 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776252
2023-11-12T08:04:12,592 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.45|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:7572ac4e-2b5d-4558-8310-b3548b0c54d8,timestamp:1699776252
2023-11-12T08:04:12,592 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.77|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:7572ac4e-2b5d-4558-8310-b3548b0c54d8,timestamp:1699776252
2023-11-12T08:04:12,593 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:12,593 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60298 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:12,593 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:12,593 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 87088, Backend time ns: 22624517
2023-11-12T08:04:12,593 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776252
2023-11-12T08:04:12,593 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776252
[I 231112 08:04:12 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 35.53ms
[I 231112 08:04:12 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:12,762 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776252762
2023-11-12T08:04:12,764 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776252
2023-11-12T08:04:12,783 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.46|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:2914406d-e65c-45bb-b718-0a3e5734eed7,timestamp:1699776252
2023-11-12T08:04:12,784 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.71|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:2914406d-e65c-45bb-b718-0a3e5734eed7,timestamp:1699776252
2023-11-12T08:04:12,784 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:12,784 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60310 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:12,784 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:12,784 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 112390, Backend time ns: 22254736
2023-11-12T08:04:12,784 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776252
2023-11-12T08:04:12,784 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776252
[I 231112 08:04:12 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 32.13ms
[I 231112 08:04:12 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:12,971 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776252971
2023-11-12T08:04:12,973 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776252
2023-11-12T08:04:12,994 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.17|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:daec93b0-8a19-4ac3-8330-89bcacc1e8b0,timestamp:1699776252
2023-11-12T08:04:12,994 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.44|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:daec93b0-8a19-4ac3-8330-89bcacc1e8b0,timestamp:1699776252
2023-11-12T08:04:12,994 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:12,994 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60318 "POST /v1/models/cifar10:predict HTTP/1.1" 200 26
2023-11-12T08:04:12,994 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:12,995 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 84543, Backend time ns: 23590678
2023-11-12T08:04:12,995 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776252
2023-11-12T08:04:12,995 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776252
[I 231112 08:04:12 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 45.01ms
[I 231112 08:04:13 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:13,172 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776253172
2023-11-12T08:04:13,173 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776253
2023-11-12T08:04:13,194 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.11|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:5e4e3647-7091-4b15-92b3-01da282698a5,timestamp:1699776253
2023-11-12T08:04:13,194 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.37|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:5e4e3647-7091-4b15-92b3-01da282698a5,timestamp:1699776253
2023-11-12T08:04:13,194 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:13,194 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60324 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:13,194 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:13,194 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 89113, Backend time ns: 22873769
2023-11-12T08:04:13,195 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776253
2023-11-12T08:04:13,195 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776253
[I 231112 08:04:13 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 39.15ms
[I 231112 08:04:13 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:13,337 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776253337
2023-11-12T08:04:13,339 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776253
2023-11-12T08:04:13,359 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.88|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:975c6939-5828-465c-a3f4-002a0f659c01,timestamp:1699776253
2023-11-12T08:04:13,360 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.15|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:975c6939-5828-465c-a3f4-002a0f659c01,timestamp:1699776253
2023-11-12T08:04:13,360 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:13,360 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60334 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:13,360 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:13,360 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 85405, Backend time ns: 22780152
2023-11-12T08:04:13,360 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776253
2023-11-12T08:04:13,360 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776253
[I 231112 08:04:13 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 32.51ms
[I 231112 08:04:13 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:13,515 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776253515
2023-11-12T08:04:13,517 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776253
2023-11-12T08:04:13,538 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.12|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:f6579265-d3b7-4b8b-b801-45989e76609a,timestamp:1699776253
2023-11-12T08:04:13,538 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.42|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:f6579265-d3b7-4b8b-b801-45989e76609a,timestamp:1699776253
2023-11-12T08:04:13,538 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:13,538 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60342 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:13,538 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:13,538 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 94154, Backend time ns: 23277188
2023-11-12T08:04:13,538 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776253
2023-11-12T08:04:13,538 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776253
[I 231112 08:04:13 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 42.53ms
[I 231112 08:04:13 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:13,682 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776253682
2023-11-12T08:04:13,684 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776253
2023-11-12T08:04:13,704 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.83|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:1490b3cc-5698-42d2-bff9-26041b6fe863,timestamp:1699776253
2023-11-12T08:04:13,705 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.1|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:1490b3cc-5698-42d2-bff9-26041b6fe863,timestamp:1699776253
2023-11-12T08:04:13,705 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:13,705 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60348 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:13,705 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:13,705 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 82210, Backend time ns: 22833763
2023-11-12T08:04:13,705 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776253
2023-11-12T08:04:13,705 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776253
[I 231112 08:04:13 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 32.85ms
[I 231112 08:04:13 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:13,863 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776253863
2023-11-12T08:04:13,865 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776253
2023-11-12T08:04:13,885 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.28|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:7a45c209-5454-4682-833d-978c2ef4e442,timestamp:1699776253
2023-11-12T08:04:13,885 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.55|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:7a45c209-5454-4682-833d-978c2ef4e442,timestamp:1699776253
2023-11-12T08:04:13,885 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:13,885 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60354 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:13,885 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:13,885 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 79043, Backend time ns: 22097245
2023-11-12T08:04:13,885 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776253
2023-11-12T08:04:13,885 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776253
[I 231112 08:04:13 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 31.24ms
[I 231112 08:04:14 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:14,053 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776254053
2023-11-12T08:04:14,055 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776254
2023-11-12T08:04:14,084 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:28.31|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:343ca7c9-dc03-4fd7-aa37-8b5651afb022,timestamp:1699776254
2023-11-12T08:04:14,084 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:28.57|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:343ca7c9-dc03-4fd7-aa37-8b5651afb022,timestamp:1699776254
2023-11-12T08:04:14,084 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 30
2023-11-12T08:04:14,084 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60362 "POST /v1/models/cifar10:predict HTTP/1.1" 200 32
2023-11-12T08:04:14,084 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:14,084 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 75677, Backend time ns: 31773221
2023-11-12T08:04:14,085 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776254
2023-11-12T08:04:14,085 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776254
[I 231112 08:04:14 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 41.53ms
[I 231112 08:04:14 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:14,236 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776254236
2023-11-12T08:04:14,238 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776254
2023-11-12T08:04:14,257 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.3|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:7b6a44f4-0a8c-4981-b084-64c6b23673e3,timestamp:1699776254
2023-11-12T08:04:14,258 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.55|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:7b6a44f4-0a8c-4981-b084-64c6b23673e3,timestamp:1699776254
2023-11-12T08:04:14,258 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:14,258 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60376 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:14,258 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:14,258 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 94633, Backend time ns: 22331217
2023-11-12T08:04:14,258 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776254
2023-11-12T08:04:14,258 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776254
[I 231112 08:04:14 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 31.56ms
[I 231112 08:04:14 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:14,394 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776254394
2023-11-12T08:04:14,396 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776254
2023-11-12T08:04:14,415 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.34|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:06595bcc-e23d-48dd-8802-5ab5c54c17d9,timestamp:1699776254
2023-11-12T08:04:14,416 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.6|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:06595bcc-e23d-48dd-8802-5ab5c54c17d9,timestamp:1699776254
2023-11-12T08:04:14,416 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:14,416 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60384 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:14,416 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:14,416 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 79499, Backend time ns: 22291871
2023-11-12T08:04:14,416 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776254
2023-11-12T08:04:14,416 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776254
[I 231112 08:04:14 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 32.18ms
[I 231112 08:04:14 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:14,563 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776254563
2023-11-12T08:04:14,565 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776254
2023-11-12T08:04:14,585 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.3|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:5f6a3854-e011-416c-bc5c-38c665026e55,timestamp:1699776254
2023-11-12T08:04:14,585 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.56|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:5f6a3854-e011-416c-bc5c-38c665026e55,timestamp:1699776254
2023-11-12T08:04:14,585 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:14,585 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60388 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:14,585 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:14,585 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 72971, Backend time ns: 22148703
2023-11-12T08:04:14,586 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776254
2023-11-12T08:04:14,586 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776254
[I 231112 08:04:14 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 37.47ms
[I 231112 08:04:14 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:14,745 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776254745
2023-11-12T08:04:14,747 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776254
2023-11-12T08:04:14,767 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.26|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:91fb848c-f712-4ac9-a8ff-5752a516a701,timestamp:1699776254
2023-11-12T08:04:14,768 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.52|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:91fb848c-f712-4ac9-a8ff-5752a516a701,timestamp:1699776254
2023-11-12T08:04:14,768 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:14,768 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:60394 "POST /v1/models/cifar10:predict HTTP/1.1" 200 24
2023-11-12T08:04:14,768 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:14,768 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 81603, Backend time ns: 23148025
2023-11-12T08:04:14,768 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776254
2023-11-12T08:04:14,768 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776254
[I 231112 08:04:14 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 32.55ms
[I 231112 08:04:14 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:14,966 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776254966
2023-11-12T08:04:14,968 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776254
2023-11-12T08:04:14,988 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.07|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:b689744e-2329-4a35-93a0-d8de56b04fed,timestamp:1699776254
2023-11-12T08:04:14,988 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.33|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:b689744e-2329-4a35-93a0-d8de56b04fed,timestamp:1699776254
2023-11-12T08:04:14,989 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:14,989 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55708 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:14,989 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:14,989 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 93987, Backend time ns: 22919714
2023-11-12T08:04:14,989 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776254
2023-11-12T08:04:14,989 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776254
[I 231112 08:04:14 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 32.01ms
[I 231112 08:04:15 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:15,122 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776255122
2023-11-12T08:04:15,124 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776255
2023-11-12T08:04:15,144 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.23|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:888df717-eec8-4714-84e4-4bd83b49a610,timestamp:1699776255
2023-11-12T08:04:15,144 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.49|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:888df717-eec8-4714-84e4-4bd83b49a610,timestamp:1699776255
2023-11-12T08:04:15,145 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:15,145 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55716 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:15,145 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:15,145 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 83625, Backend time ns: 23100213
2023-11-12T08:04:15,145 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776255
2023-11-12T08:04:15,145 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776255
[I 231112 08:04:15 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 32.07ms
[I 231112 08:04:15 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:15,296 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776255296
2023-11-12T08:04:15,298 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776255
2023-11-12T08:04:15,318 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.33|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:014a321a-e446-4759-9717-72ae12522d8b,timestamp:1699776255
2023-11-12T08:04:15,318 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.59|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:014a321a-e446-4759-9717-72ae12522d8b,timestamp:1699776255
2023-11-12T08:04:15,318 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:15,318 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55728 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:15,318 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:15,319 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 73468, Backend time ns: 22211716
2023-11-12T08:04:15,319 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776255
2023-11-12T08:04:15,319 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776255
[I 231112 08:04:15 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 31.04ms
[I 231112 08:04:15 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:15,464 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776255464
2023-11-12T08:04:15,466 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776255
2023-11-12T08:04:15,486 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.18|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:63ac29ca-ef43-4385-9f59-e9637b13e01c,timestamp:1699776255
2023-11-12T08:04:15,486 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.43|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:63ac29ca-ef43-4385-9f59-e9637b13e01c,timestamp:1699776255
2023-11-12T08:04:15,486 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:15,486 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55742 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:15,486 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:15,486 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 65595, Backend time ns: 21995339
2023-11-12T08:04:15,486 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776255
2023-11-12T08:04:15,487 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776255
[I 231112 08:04:15 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 31.05ms
[I 231112 08:04:15 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:15,669 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776255669
2023-11-12T08:04:15,671 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776255
2023-11-12T08:04:15,691 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.36|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:bccc40c3-4b1d-44c2-8590-a0cca291c3ad,timestamp:1699776255
2023-11-12T08:04:15,691 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.61|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:bccc40c3-4b1d-44c2-8590-a0cca291c3ad,timestamp:1699776255
2023-11-12T08:04:15,691 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:15,691 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55744 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:15,691 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:15,691 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 76606, Backend time ns: 22111064
2023-11-12T08:04:15,691 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776255
2023-11-12T08:04:15,691 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776255
[I 231112 08:04:15 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 35.32ms
[I 231112 08:04:15 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:15,870 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776255870
2023-11-12T08:04:15,872 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776255
2023-11-12T08:04:15,893 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.28|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:fbcc0c6e-d6f6-4e53-849a-af9c0a2d0e3d,timestamp:1699776255
2023-11-12T08:04:15,893 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.54|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:fbcc0c6e-d6f6-4e53-849a-af9c0a2d0e3d,timestamp:1699776255
2023-11-12T08:04:15,893 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:15,893 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55752 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:15,893 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:15,893 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 85388, Backend time ns: 23138628
2023-11-12T08:04:15,894 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776255
2023-11-12T08:04:15,894 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776255
[I 231112 08:04:15 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 33.29ms
[I 231112 08:04:16 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:16,021 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776256021
2023-11-12T08:04:16,022 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776256
2023-11-12T08:04:16,042 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.25|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:95749757-334e-4dc5-bf2f-045033d79b7e,timestamp:1699776256
2023-11-12T08:04:16,042 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.5|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:95749757-334e-4dc5-bf2f-045033d79b7e,timestamp:1699776256
2023-11-12T08:04:16,042 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:16,042 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55768 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:16,042 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:16,043 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 72365, Backend time ns: 21889890
2023-11-12T08:04:16,043 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776256
2023-11-12T08:04:16,043 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776256
[I 231112 08:04:16 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 31.06ms
[I 231112 08:04:16 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:16,205 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776256205
2023-11-12T08:04:16,207 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776256
2023-11-12T08:04:16,227 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.35|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:4f444274-8786-41d3-a57a-b95dfd2f1377,timestamp:1699776256
2023-11-12T08:04:16,227 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.6|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:4f444274-8786-41d3-a57a-b95dfd2f1377,timestamp:1699776256
2023-11-12T08:04:16,227 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:16,228 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55782 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:16,228 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:16,228 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 73369, Backend time ns: 22338084
2023-11-12T08:04:16,228 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776256
2023-11-12T08:04:16,228 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776256
[I 231112 08:04:16 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 34.26ms
[I 231112 08:04:16 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:16,365 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776256365
2023-11-12T08:04:16,367 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776256
2023-11-12T08:04:16,387 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.15|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:16f83765-1126-4f0f-861a-be3b4015082d,timestamp:1699776256
2023-11-12T08:04:16,387 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.42|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:16f83765-1126-4f0f-861a-be3b4015082d,timestamp:1699776256
2023-11-12T08:04:16,387 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:16,388 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55798 "POST /v1/models/cifar10:predict HTTP/1.1" 200 24
2023-11-12T08:04:16,388 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:16,388 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 75412, Backend time ns: 23046660
2023-11-12T08:04:16,388 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776256
2023-11-12T08:04:16,388 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776256
[I 231112 08:04:16 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 32.06ms
[I 231112 08:04:16 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:16,552 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776256552
2023-11-12T08:04:16,554 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776256
2023-11-12T08:04:16,574 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.31|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:d3f37eec-6382-44c2-bae9-74826fac6115,timestamp:1699776256
2023-11-12T08:04:16,575 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.61|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:d3f37eec-6382-44c2-bae9-74826fac6115,timestamp:1699776256
2023-11-12T08:04:16,575 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:16,575 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55802 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:16,575 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:16,575 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 71757, Backend time ns: 23213204
2023-11-12T08:04:16,575 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776256
2023-11-12T08:04:16,575 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776256
[I 231112 08:04:16 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 40.15ms
[I 231112 08:04:16 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:16,715 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776256715
2023-11-12T08:04:16,717 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776256
2023-11-12T08:04:16,737 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.24|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:2155b21e-0206-4ffd-8932-c43219ffc7a8,timestamp:1699776256
2023-11-12T08:04:16,738 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.53|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:2155b21e-0206-4ffd-8932-c43219ffc7a8,timestamp:1699776256
2023-11-12T08:04:16,738 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:16,738 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55814 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:16,738 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:16,738 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 94361, Backend time ns: 23101261
2023-11-12T08:04:16,738 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776256
2023-11-12T08:04:16,738 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776256
[I 231112 08:04:16 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 32.56ms
[I 231112 08:04:16 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:16,900 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776256900
2023-11-12T08:04:16,902 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776256
2023-11-12T08:04:16,923 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.25|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:67acfa61-0ff7-405b-b02e-681b307b6ede,timestamp:1699776256
2023-11-12T08:04:16,923 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.53|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:67acfa61-0ff7-405b-b02e-681b307b6ede,timestamp:1699776256
2023-11-12T08:04:16,923 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:16,923 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55822 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:16,923 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:16,923 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 80836, Backend time ns: 23112266
2023-11-12T08:04:16,923 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776256
2023-11-12T08:04:16,923 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776256
[I 231112 08:04:16 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 40.23ms
[I 231112 08:04:17 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:17,067 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776257067
2023-11-12T08:04:17,069 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776257
2023-11-12T08:04:17,089 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.19|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:0f35183d-aadd-453e-80d0-b27aa7c1c3b4,timestamp:1699776257
2023-11-12T08:04:17,090 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.48|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:0f35183d-aadd-453e-80d0-b27aa7c1c3b4,timestamp:1699776257
2023-11-12T08:04:17,090 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:17,090 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55828 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:17,090 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:17,090 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 92962, Backend time ns: 23159501
2023-11-12T08:04:17,090 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776257
2023-11-12T08:04:17,090 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776257
[I 231112 08:04:17 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 34.06ms
[I 231112 08:04:17 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:17,252 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776257252
2023-11-12T08:04:17,254 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776257
2023-11-12T08:04:17,275 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.28|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:ce99adf6-700a-43e9-9c25-26a115ee9de8,timestamp:1699776257
2023-11-12T08:04:17,275 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.58|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:ce99adf6-700a-43e9-9c25-26a115ee9de8,timestamp:1699776257
2023-11-12T08:04:17,275 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:17,275 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55834 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:17,275 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:17,275 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 94939, Backend time ns: 23297907
2023-11-12T08:04:17,275 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776257
2023-11-12T08:04:17,276 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776257
[I 231112 08:04:17 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 32.44ms
[I 231112 08:04:17 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:17,436 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776257436
2023-11-12T08:04:17,438 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776257
2023-11-12T08:04:17,459 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.08|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:032c7062-2b29-484f-bbf9-5a0eab1f2f54,timestamp:1699776257
2023-11-12T08:04:17,459 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.36|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:032c7062-2b29-484f-bbf9-5a0eab1f2f54,timestamp:1699776257
2023-11-12T08:04:17,459 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:17,459 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55836 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:17,459 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:17,459 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 71185, Backend time ns: 22905678
2023-11-12T08:04:17,459 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776257
2023-11-12T08:04:17,459 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776257
[I 231112 08:04:17 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 40.50ms
[I 231112 08:04:17 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:17,602 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776257602
2023-11-12T08:04:17,604 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776257
2023-11-12T08:04:17,624 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.11|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:6fd98f72-5c5e-49c5-8640-7ca965ed3a68,timestamp:1699776257
2023-11-12T08:04:17,624 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.39|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:6fd98f72-5c5e-49c5-8640-7ca965ed3a68,timestamp:1699776257
2023-11-12T08:04:17,624 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:17,625 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55852 "POST /v1/models/cifar10:predict HTTP/1.1" 200 24
2023-11-12T08:04:17,625 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:17,625 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 89429, Backend time ns: 22825602
2023-11-12T08:04:17,625 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776257
2023-11-12T08:04:17,625 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776257
[I 231112 08:04:17 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 31.90ms
[I 231112 08:04:17 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:17,787 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776257787
2023-11-12T08:04:17,789 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776257
2023-11-12T08:04:17,808 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.36|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:3bceee16-08cf-4132-8bf1-98a84da7cfaa,timestamp:1699776257
2023-11-12T08:04:17,809 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.62|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:3bceee16-08cf-4132-8bf1-98a84da7cfaa,timestamp:1699776257
2023-11-12T08:04:17,809 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:17,809 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55854 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:17,809 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:17,809 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 72194, Backend time ns: 22337792
2023-11-12T08:04:17,809 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776257
2023-11-12T08:04:17,809 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776257
[I 231112 08:04:17 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 34.99ms
[I 231112 08:04:17 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:17,973 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776257973
2023-11-12T08:04:17,987 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776257
2023-11-12T08:04:18,058 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:70.53|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:ef0238b0-9384-4d07-8dbe-510103bc8426,timestamp:1699776258
2023-11-12T08:04:18,058 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:70.81|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:ef0238b0-9384-4d07-8dbe-510103bc8426,timestamp:1699776258
2023-11-12T08:04:18,059 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 72
2023-11-12T08:04:18,059 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55862 "POST /v1/models/cifar10:predict HTTP/1.1" 200 87
2023-11-12T08:04:18,059 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:18,059 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 118815, Backend time ns: 86321415
2023-11-12T08:04:18,059 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776258
2023-11-12T08:04:18,059 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:14|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776258
[I 231112 08:04:18 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 99.92ms
[I 231112 08:04:18 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:18,267 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776258267
2023-11-12T08:04:18,269 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776258
2023-11-12T08:04:18,289 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.56|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:f08b5b38-4d8c-469d-a98b-642d1ab35153,timestamp:1699776258
2023-11-12T08:04:18,289 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.83|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:f08b5b38-4d8c-469d-a98b-642d1ab35153,timestamp:1699776258
2023-11-12T08:04:18,289 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:18,289 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55866 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:18,289 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:18,289 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 73297, Backend time ns: 22487447
2023-11-12T08:04:18,289 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776258
2023-11-12T08:04:18,289 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776258
[I 231112 08:04:18 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 41.26ms
2023-11-12T08:04:18,344 [INFO ] pool-3-thread-1 TS_METRICS - CPUUtilization.Percent:0.0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776258
2023-11-12T08:04:18,344 [INFO ] pool-3-thread-1 TS_METRICS - DiskAvailable.Gigabytes:14.067619323730469|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776258
2023-11-12T08:04:18,344 [INFO ] pool-3-thread-1 TS_METRICS - DiskUsage.Gigabytes:45.9206428527832|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776258
2023-11-12T08:04:18,344 [INFO ] pool-3-thread-1 TS_METRICS - DiskUtilization.Percent:76.5|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776258
2023-11-12T08:04:18,344 [INFO ] pool-3-thread-1 TS_METRICS - GPUMemoryUtilization.Percent:7.386326030842544|#Level:Host,device_id:0|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776258
2023-11-12T08:04:18,344 [INFO ] pool-3-thread-1 TS_METRICS - GPUMemoryUsed.Megabytes:1116|#Level:Host,device_id:0|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776258
2023-11-12T08:04:18,344 [INFO ] pool-3-thread-1 TS_METRICS - GPUUtilization.Percent:1|#Level:Host,device_id:0|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776258
2023-11-12T08:04:18,344 [INFO ] pool-3-thread-1 TS_METRICS - MemoryAvailable.Megabytes:27078.3203125|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776258
2023-11-12T08:04:18,344 [INFO ] pool-3-thread-1 TS_METRICS - MemoryUsed.Megabytes:4072.765625|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776258
2023-11-12T08:04:18,344 [INFO ] pool-3-thread-1 TS_METRICS - MemoryUtilization.Percent:14.4|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776258
[I 231112 08:04:18 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:18,494 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776258494
2023-11-12T08:04:18,496 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776258
2023-11-12T08:04:18,516 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.55|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:34f2fb20-e821-481c-bb6b-7b7aa1b19acc,timestamp:1699776258
2023-11-12T08:04:18,516 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.81|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:34f2fb20-e821-481c-bb6b-7b7aa1b19acc,timestamp:1699776258
2023-11-12T08:04:18,516 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:18,516 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55878 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:18,516 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:18,516 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 86012, Backend time ns: 22436863
2023-11-12T08:04:18,516 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776258
2023-11-12T08:04:18,516 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776258
[I 231112 08:04:18 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 31.29ms
[I 231112 08:04:18 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:18,713 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776258713
2023-11-12T08:04:18,714 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776258
2023-11-12T08:04:18,734 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.23|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:028ec0f7-3e44-463d-b3a0-6f1da955d1ac,timestamp:1699776258
2023-11-12T08:04:18,734 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.48|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:028ec0f7-3e44-463d-b3a0-6f1da955d1ac,timestamp:1699776258
2023-11-12T08:04:18,734 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:18,734 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55886 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:18,734 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:18,735 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 79504, Backend time ns: 21967749
2023-11-12T08:04:18,735 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776258
2023-11-12T08:04:18,735 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776258
[I 231112 08:04:18 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 31.37ms
[I 231112 08:04:18 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:18,940 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776258940
2023-11-12T08:04:18,941 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776258
2023-11-12T08:04:18,961 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.55|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:f06aa707-2d85-45d0-a265-b11f5dcb56b1,timestamp:1699776258
2023-11-12T08:04:18,961 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.83|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:f06aa707-2d85-45d0-a265-b11f5dcb56b1,timestamp:1699776258
2023-11-12T08:04:18,962 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:18,962 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55898 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:18,962 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:18,962 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 78787, Backend time ns: 22574020
2023-11-12T08:04:18,962 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776258
2023-11-12T08:04:18,962 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776258
[I 231112 08:04:18 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 37.36ms
[I 231112 08:04:19 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:19,146 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776259146
2023-11-12T08:04:19,148 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776259
2023-11-12T08:04:19,168 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.35|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:39847eef-50ba-49f9-b6b4-be5d6c535fc7,timestamp:1699776259
2023-11-12T08:04:19,168 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.63|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:39847eef-50ba-49f9-b6b4-be5d6c535fc7,timestamp:1699776259
2023-11-12T08:04:19,168 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:19,168 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55906 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:19,168 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:19,168 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 85221, Backend time ns: 22199250
2023-11-12T08:04:19,168 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776259
2023-11-12T08:04:19,168 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776259
[I 231112 08:04:19 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 34.46ms
[I 231112 08:04:19 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:19,345 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776259345
2023-11-12T08:04:19,346 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776259
2023-11-12T08:04:19,366 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.67|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:ebcc7ef4-16d2-4d6a-9f74-835bebdb5798,timestamp:1699776259
2023-11-12T08:04:19,366 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.95|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:ebcc7ef4-16d2-4d6a-9f74-835bebdb5798,timestamp:1699776259
2023-11-12T08:04:19,367 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:19,367 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55912 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:19,367 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:19,367 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 81336, Backend time ns: 22404106
2023-11-12T08:04:19,367 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776259
2023-11-12T08:04:19,367 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776259
[I 231112 08:04:19 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 31.90ms
[I 231112 08:04:19 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:19,563 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776259563
2023-11-12T08:04:19,565 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776259
2023-11-12T08:04:19,585 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.31|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:f7eb707e-9e19-4e08-9f87-6259c1a9d249,timestamp:1699776259
2023-11-12T08:04:19,585 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.56|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:f7eb707e-9e19-4e08-9f87-6259c1a9d249,timestamp:1699776259
2023-11-12T08:04:19,585 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:19,585 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55924 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:19,585 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:19,585 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 82888, Backend time ns: 22048681
2023-11-12T08:04:19,586 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776259
2023-11-12T08:04:19,586 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776259
[I 231112 08:04:19 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 30.80ms
[I 231112 08:04:19 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:19,768 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776259768
2023-11-12T08:04:19,770 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776259
2023-11-12T08:04:19,790 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.34|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:0c045475-7e1d-452e-b216-a1e9bc674b6c,timestamp:1699776259
2023-11-12T08:04:19,790 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.59|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:0c045475-7e1d-452e-b216-a1e9bc674b6c,timestamp:1699776259
2023-11-12T08:04:19,790 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:19,790 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55932 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:19,790 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:19,791 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 70270, Backend time ns: 22065429
2023-11-12T08:04:19,791 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776259
2023-11-12T08:04:19,791 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776259
[I 231112 08:04:19 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 30.69ms
[I 231112 08:04:19 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:20,002 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776260002
2023-11-12T08:04:20,004 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776260
2023-11-12T08:04:20,023 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.25|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:995d7656-f124-480e-9af5-9ff2b65fb1d3,timestamp:1699776260
2023-11-12T08:04:20,023 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.49|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:995d7656-f124-480e-9af5-9ff2b65fb1d3,timestamp:1699776260
2023-11-12T08:04:20,023 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 20
2023-11-12T08:04:20,024 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55936 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:20,024 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:20,024 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 76845, Backend time ns: 21938469
2023-11-12T08:04:20,024 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776260
2023-11-12T08:04:20,024 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776260
[I 231112 08:04:20 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 39.71ms
[I 231112 08:04:20 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:20,247 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776260247
2023-11-12T08:04:20,249 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776260
2023-11-12T08:04:20,269 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.41|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:054e25fd-0bd7-4467-871d-dfc896958529,timestamp:1699776260
2023-11-12T08:04:20,269 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.67|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:054e25fd-0bd7-4467-871d-dfc896958529,timestamp:1699776260
2023-11-12T08:04:20,269 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:20,269 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55942 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:20,269 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:20,270 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 62806, Backend time ns: 22253442
2023-11-12T08:04:20,270 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776260
2023-11-12T08:04:20,270 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776260
[I 231112 08:04:20 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 31.04ms
[I 231112 08:04:20 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:20,451 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776260451
2023-11-12T08:04:20,453 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776260
2023-11-12T08:04:20,473 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.48|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:d352e01a-9196-4f37-99d3-9bc0fd5a3675,timestamp:1699776260
2023-11-12T08:04:20,473 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.77|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:d352e01a-9196-4f37-99d3-9bc0fd5a3675,timestamp:1699776260
2023-11-12T08:04:20,473 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:20,473 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55954 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:20,473 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:20,473 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 71595, Backend time ns: 22094131
2023-11-12T08:04:20,473 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776260
2023-11-12T08:04:20,474 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776260
[I 231112 08:04:20 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 30.86ms
[I 231112 08:04:20 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:20,643 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776260642
2023-11-12T08:04:20,644 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776260
2023-11-12T08:04:20,665 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.14|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:df105984-99ef-40b7-bc60-f5232667d606,timestamp:1699776260
2023-11-12T08:04:20,665 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.41|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:df105984-99ef-40b7-bc60-f5232667d606,timestamp:1699776260
2023-11-12T08:04:20,665 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:20,665 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55956 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:20,665 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:20,665 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 82295, Backend time ns: 22826255
2023-11-12T08:04:20,665 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776260
2023-11-12T08:04:20,665 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776260
[I 231112 08:04:20 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 31.61ms
[I 231112 08:04:20 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:20,847 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776260847
2023-11-12T08:04:20,849 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776260
2023-11-12T08:04:20,870 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.25|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:2156f9fc-ec4c-425d-8e26-22e44b381d04,timestamp:1699776260
2023-11-12T08:04:20,870 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.52|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:2156f9fc-ec4c-425d-8e26-22e44b381d04,timestamp:1699776260
2023-11-12T08:04:20,870 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:20,870 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55972 "POST /v1/models/cifar10:predict HTTP/1.1" 200 24
2023-11-12T08:04:20,870 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:20,870 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 78480, Backend time ns: 23015811
2023-11-12T08:04:20,870 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776260
2023-11-12T08:04:20,870 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776260
[I 231112 08:04:20 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 32.32ms
[I 231112 08:04:21 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:21,050 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776261050
2023-11-12T08:04:21,052 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776261
2023-11-12T08:04:21,072 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.49|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:41aeef54-e594-4aba-970d-c75f213d9371,timestamp:1699776261
2023-11-12T08:04:21,072 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.77|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:41aeef54-e594-4aba-970d-c75f213d9371,timestamp:1699776261
2023-11-12T08:04:21,072 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:21,072 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:55986 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:21,072 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:21,072 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 75766, Backend time ns: 22309563
2023-11-12T08:04:21,072 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776261
2023-11-12T08:04:21,072 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776261
[I 231112 08:04:21 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 31.67ms
[I 231112 08:04:21 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:21,283 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776261283
2023-11-12T08:04:21,285 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776261
2023-11-12T08:04:21,304 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.3|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:04aaaba4-10f5-4ebe-944c-e3a5add26fcb,timestamp:1699776261
2023-11-12T08:04:21,304 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.56|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:04aaaba4-10f5-4ebe-944c-e3a5add26fcb,timestamp:1699776261
2023-11-12T08:04:21,305 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:21,305 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:56000 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:21,305 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:21,305 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 67806, Backend time ns: 22422229
2023-11-12T08:04:21,305 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776261
2023-11-12T08:04:21,305 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776261
[I 231112 08:04:21 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 34.94ms
[I 231112 08:04:21 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:21,470 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776261470
2023-11-12T08:04:21,472 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776261
2023-11-12T08:04:21,492 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.11|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:fbbdc6eb-b15d-4533-913b-05d833cf0e65,timestamp:1699776261
2023-11-12T08:04:21,493 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.37|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:fbbdc6eb-b15d-4533-913b-05d833cf0e65,timestamp:1699776261
2023-11-12T08:04:21,493 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:21,493 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:56016 "POST /v1/models/cifar10:predict HTTP/1.1" 200 24
2023-11-12T08:04:21,493 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:21,493 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 69818, Backend time ns: 22842188
2023-11-12T08:04:21,493 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776261
2023-11-12T08:04:21,493 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776261
[I 231112 08:04:21 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 32.18ms
[I 231112 08:04:21 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:21,674 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776261674
2023-11-12T08:04:21,676 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776261
2023-11-12T08:04:21,696 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.0|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:7e0ad941-e182-4bb2-9946-986a28e769a2,timestamp:1699776261
2023-11-12T08:04:21,696 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.25|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:7e0ad941-e182-4bb2-9946-986a28e769a2,timestamp:1699776261
2023-11-12T08:04:21,697 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:21,697 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:56032 "POST /v1/models/cifar10:predict HTTP/1.1" 200 24
2023-11-12T08:04:21,697 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:21,697 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 78401, Backend time ns: 22738923
2023-11-12T08:04:21,697 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776261
2023-11-12T08:04:21,697 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776261
[I 231112 08:04:21 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 32.63ms
[I 231112 08:04:21 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:21,890 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776261890
2023-11-12T08:04:21,892 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776261
2023-11-12T08:04:21,911 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.37|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:d67ff55a-67c7-463c-8b8f-0d9d24c3441f,timestamp:1699776261
2023-11-12T08:04:21,912 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.64|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:d67ff55a-67c7-463c-8b8f-0d9d24c3441f,timestamp:1699776261
2023-11-12T08:04:21,912 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:21,912 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:56036 "POST /v1/models/cifar10:predict HTTP/1.1" 200 24
2023-11-12T08:04:21,912 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:21,912 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 74580, Backend time ns: 22204885
2023-11-12T08:04:21,912 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776261
2023-11-12T08:04:21,912 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776261
[I 231112 08:04:21 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 33.22ms
[I 231112 08:04:22 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:22,114 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776262114
2023-11-12T08:04:22,116 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776262
2023-11-12T08:04:22,137 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.34|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:a96881ed-311d-4913-999a-62ef81ed011f,timestamp:1699776262
2023-11-12T08:04:22,137 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.62|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:a96881ed-311d-4913-999a-62ef81ed011f,timestamp:1699776262
2023-11-12T08:04:22,137 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:22,137 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:56038 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:22,137 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:22,137 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 89601, Backend time ns: 23123840
2023-11-12T08:04:22,137 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776262
2023-11-12T08:04:22,137 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776262
[I 231112 08:04:22 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 39.73ms
[I 231112 08:04:22 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:22,332 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776262332
2023-11-12T08:04:22,333 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776262
2023-11-12T08:04:22,354 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.44|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:8ec1cd0f-49be-4eb4-8d59-2cd46bd38eb2,timestamp:1699776262
2023-11-12T08:04:22,354 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.77|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:8ec1cd0f-49be-4eb4-8d59-2cd46bd38eb2,timestamp:1699776262
2023-11-12T08:04:22,355 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:22,355 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:56044 "POST /v1/models/cifar10:predict HTTP/1.1" 200 24
2023-11-12T08:04:22,355 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:22,355 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 77037, Backend time ns: 23218076
2023-11-12T08:04:22,355 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776262
2023-11-12T08:04:22,355 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776262
[I 231112 08:04:22 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 40.82ms
[I 231112 08:04:22 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:22,557 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776262557
2023-11-12T08:04:22,558 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776262
2023-11-12T08:04:22,579 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.1|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:b1ec0c1b-472a-4380-b2ec-685ca7e9770b,timestamp:1699776262
2023-11-12T08:04:22,579 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.38|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:b1ec0c1b-472a-4380-b2ec-685ca7e9770b,timestamp:1699776262
2023-11-12T08:04:22,579 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:22,579 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:56050 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:22,579 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:22,579 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 66976, Backend time ns: 22859256
2023-11-12T08:04:22,580 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776262
2023-11-12T08:04:22,580 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776262
[I 231112 08:04:22 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 36.55ms
[I 231112 08:04:22 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:22,727 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776262727
2023-11-12T08:04:22,729 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776262
2023-11-12T08:04:22,749 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.33|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:98cf0784-c63c-43ab-89b5-ad329c96e1ac,timestamp:1699776262
2023-11-12T08:04:22,750 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.61|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:98cf0784-c63c-43ab-89b5-ad329c96e1ac,timestamp:1699776262
2023-11-12T08:04:22,750 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:22,750 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:56060 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:22,750 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:22,750 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 73380, Backend time ns: 23168734
2023-11-12T08:04:22,750 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776262
2023-11-12T08:04:22,750 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776262
[I 231112 08:04:22 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 32.05ms
[I 231112 08:04:22 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:22,940 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776262940
2023-11-12T08:04:22,941 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776262
2023-11-12T08:04:22,962 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.15|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:681d2bcf-6a2e-4f0b-b4f5-c4b25c07e184,timestamp:1699776262
2023-11-12T08:04:22,962 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.42|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:681d2bcf-6a2e-4f0b-b4f5-c4b25c07e184,timestamp:1699776262
2023-11-12T08:04:22,962 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:22,962 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:56076 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:22,962 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:22,962 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 74325, Backend time ns: 22883408
2023-11-12T08:04:22,963 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776262
2023-11-12T08:04:22,963 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776262
[I 231112 08:04:22 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 31.69ms
[I 231112 08:04:23 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:23,147 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776263147
2023-11-12T08:04:23,149 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776263
2023-11-12T08:04:23,169 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.38|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:d68d0847-913d-43fb-8bc2-524891d72972,timestamp:1699776263
2023-11-12T08:04:23,169 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.66|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:d68d0847-913d-43fb-8bc2-524891d72972,timestamp:1699776263
2023-11-12T08:04:23,169 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:23,169 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:56082 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:23,169 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:23,169 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 71644, Backend time ns: 22030149
2023-11-12T08:04:23,170 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776263
2023-11-12T08:04:23,170 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776263
[I 231112 08:04:23 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 30.70ms
[I 231112 08:04:23 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:23,364 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776263364
2023-11-12T08:04:23,365 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776263
2023-11-12T08:04:23,385 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.48|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:74c5e2b3-5a1d-421b-b635-381910dfe4af,timestamp:1699776263
2023-11-12T08:04:23,385 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.76|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:74c5e2b3-5a1d-421b-b635-381910dfe4af,timestamp:1699776263
2023-11-12T08:04:23,386 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:23,386 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:56096 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:23,386 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:23,386 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 69363, Backend time ns: 22126078
2023-11-12T08:04:23,386 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776263
2023-11-12T08:04:23,386 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776263
[I 231112 08:04:23 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 33.50ms
[I 231112 08:04:23 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:23,590 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776263590
2023-11-12T08:04:23,592 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776263
2023-11-12T08:04:23,612 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.23|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:b329fe6f-2c35-41f6-8548-dca7b346f255,timestamp:1699776263
2023-11-12T08:04:23,612 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.51|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:b329fe6f-2c35-41f6-8548-dca7b346f255,timestamp:1699776263
2023-11-12T08:04:23,612 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:23,612 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:56100 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:23,612 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:23,613 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 87337, Backend time ns: 22075552
2023-11-12T08:04:23,613 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776263
2023-11-12T08:04:23,613 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776263
[I 231112 08:04:23 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 41.18ms
[I 231112 08:04:23 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:23,820 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776263820
2023-11-12T08:04:23,822 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776263
2023-11-12T08:04:23,842 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.53|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:000f21d4-2089-4382-8f87-302d603b8371,timestamp:1699776263
2023-11-12T08:04:23,842 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.8|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:000f21d4-2089-4382-8f87-302d603b8371,timestamp:1699776263
2023-11-12T08:04:23,842 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:23,843 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:56108 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:23,843 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:23,843 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 78268, Backend time ns: 22229067
2023-11-12T08:04:23,843 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776263
2023-11-12T08:04:23,843 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776263
[I 231112 08:04:23 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 31.23ms
[I 231112 08:04:24 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:24,060 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776264060
2023-11-12T08:04:24,061 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776264
2023-11-12T08:04:24,082 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.2|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:dd9aa597-27c3-4c49-9401-64dc312e3f30,timestamp:1699776264
2023-11-12T08:04:24,082 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.45|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:dd9aa597-27c3-4c49-9401-64dc312e3f30,timestamp:1699776264
2023-11-12T08:04:24,082 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:24,083 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:56118 "POST /v1/models/cifar10:predict HTTP/1.1" 200 24
2023-11-12T08:04:24,083 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:24,083 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 73300, Backend time ns: 23134211
2023-11-12T08:04:24,083 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776264
2023-11-12T08:04:24,083 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776264
[I 231112 08:04:24 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 44.64ms
[I 231112 08:04:24 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:24,272 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776264272
2023-11-12T08:04:24,274 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776264
2023-11-12T08:04:24,294 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.88|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:99a4f793-dccf-49d9-91c4-a617664e4684,timestamp:1699776264
2023-11-12T08:04:24,294 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.16|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:99a4f793-dccf-49d9-91c4-a617664e4684,timestamp:1699776264
2023-11-12T08:04:24,295 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:24,295 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:56128 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:24,295 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:24,295 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 65476, Backend time ns: 22608681
2023-11-12T08:04:24,295 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776264
2023-11-12T08:04:24,295 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776264
[I 231112 08:04:24 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 39.31ms
[I 231112 08:04:24 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:24,505 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776264505
2023-11-12T08:04:24,506 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776264
2023-11-12T08:04:24,526 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.2|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:4798f156-8ef9-4dbd-931d-d98bf1e728af,timestamp:1699776264
2023-11-12T08:04:24,526 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.46|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:4798f156-8ef9-4dbd-931d-d98bf1e728af,timestamp:1699776264
2023-11-12T08:04:24,526 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:24,526 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:56138 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:24,526 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:24,526 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 112788, Backend time ns: 21778768
2023-11-12T08:04:24,526 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776264
2023-11-12T08:04:24,527 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776264
[I 231112 08:04:24 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 43.03ms
[I 231112 08:04:24 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:24,733 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776264733
2023-11-12T08:04:24,735 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776264
2023-11-12T08:04:24,755 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.34|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:48411841-060c-4458-8a1f-8c589a99f997,timestamp:1699776264
2023-11-12T08:04:24,755 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.58|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:48411841-060c-4458-8a1f-8c589a99f997,timestamp:1699776264
2023-11-12T08:04:24,755 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:24,755 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:56150 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:24,755 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:24,755 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 79026, Backend time ns: 21903988
2023-11-12T08:04:24,755 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776264
2023-11-12T08:04:24,755 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776264
[I 231112 08:04:24 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 42.21ms
[I 231112 08:04:24 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:24,916 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776264916
2023-11-12T08:04:24,918 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776264
2023-11-12T08:04:24,938 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.29|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:02d9664e-bbe4-46da-baa1-e46258148bb8,timestamp:1699776264
2023-11-12T08:04:24,938 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.56|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:02d9664e-bbe4-46da-baa1-e46258148bb8,timestamp:1699776264
2023-11-12T08:04:24,938 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:24,938 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:53796 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:24,938 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:24,938 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 73263, Backend time ns: 21940868
2023-11-12T08:04:24,938 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776264
2023-11-12T08:04:24,938 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776264
[I 231112 08:04:24 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 30.95ms
[I 231112 08:04:25 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:25,116 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776265116
2023-11-12T08:04:25,118 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776265
2023-11-12T08:04:25,138 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.45|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:7511696a-324e-4b17-afea-ad5e8e2ffe8b,timestamp:1699776265
2023-11-12T08:04:25,138 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.7|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:7511696a-324e-4b17-afea-ad5e8e2ffe8b,timestamp:1699776265
2023-11-12T08:04:25,138 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:25,138 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:53808 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:25,138 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:25,138 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 83160, Backend time ns: 22123030
2023-11-12T08:04:25,138 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776265
2023-11-12T08:04:25,138 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776265
[I 231112 08:04:25 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 31.07ms
[I 231112 08:04:25 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:25,343 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776265343
2023-11-12T08:04:25,345 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776265
2023-11-12T08:04:25,365 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.27|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:156cb213-d445-40d8-aed3-2a08c2a73553,timestamp:1699776265
2023-11-12T08:04:25,366 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.53|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:156cb213-d445-40d8-aed3-2a08c2a73553,timestamp:1699776265
2023-11-12T08:04:25,366 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:25,366 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:53820 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:25,366 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:25,366 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 73131, Backend time ns: 22951111
2023-11-12T08:04:25,366 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776265
2023-11-12T08:04:25,366 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776265
[I 231112 08:04:25 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 31.62ms
[I 231112 08:04:25 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:25,544 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776265544
2023-11-12T08:04:25,546 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776265
2023-11-12T08:04:25,566 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.34|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:1efb253f-c810-45d8-9c02-092e4e1fcbf3,timestamp:1699776265
2023-11-12T08:04:25,566 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.6|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:1efb253f-c810-45d8-9c02-092e4e1fcbf3,timestamp:1699776265
2023-11-12T08:04:25,566 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:25,566 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:53828 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:25,566 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:25,566 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 75995, Backend time ns: 21977353
2023-11-12T08:04:25,566 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776265
2023-11-12T08:04:25,566 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776265
[I 231112 08:04:25 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 39.61ms
[I 231112 08:04:25 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:25,764 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776265764
2023-11-12T08:04:25,766 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776265
2023-11-12T08:04:25,785 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.42|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:299499f4-7b49-4017-8754-7afa2da9cbb5,timestamp:1699776265
2023-11-12T08:04:25,786 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.68|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:299499f4-7b49-4017-8754-7afa2da9cbb5,timestamp:1699776265
2023-11-12T08:04:25,786 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:25,786 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:53836 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:25,786 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:25,786 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 71120, Backend time ns: 22025175
2023-11-12T08:04:25,786 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776265
2023-11-12T08:04:25,786 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776265
[I 231112 08:04:25 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 33.12ms
[I 231112 08:04:25 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:25,972 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776265972
2023-11-12T08:04:25,973 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776265
2023-11-12T08:04:25,993 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.41|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:b577f3a1-f38e-4c74-a541-12dde296087a,timestamp:1699776265
2023-11-12T08:04:25,993 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.66|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:b577f3a1-f38e-4c74-a541-12dde296087a,timestamp:1699776265
2023-11-12T08:04:25,993 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 20
2023-11-12T08:04:25,994 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:53844 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:25,994 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:25,994 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 80023, Backend time ns: 22000578
2023-11-12T08:04:25,994 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776265
2023-11-12T08:04:25,994 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776265
[I 231112 08:04:25 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 39.53ms
[I 231112 08:04:26 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:26,171 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776266171
2023-11-12T08:04:26,172 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776266
2023-11-12T08:04:26,193 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.1|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:eb504b56-a1e8-4b5f-beb1-ffb05fb65657,timestamp:1699776266
2023-11-12T08:04:26,193 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.35|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:eb504b56-a1e8-4b5f-beb1-ffb05fb65657,timestamp:1699776266
2023-11-12T08:04:26,193 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:26,193 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:53856 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:26,193 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:26,193 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 72926, Backend time ns: 22580157
2023-11-12T08:04:26,193 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776266
2023-11-12T08:04:26,193 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776266
[I 231112 08:04:26 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 31.09ms
[I 231112 08:04:26 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:26,344 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776266344
2023-11-12T08:04:26,345 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776266
2023-11-12T08:04:26,365 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.75|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:cd2d620e-fdfe-4021-b833-72a8a67561c3,timestamp:1699776266
2023-11-12T08:04:26,365 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.0|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:cd2d620e-fdfe-4021-b833-72a8a67561c3,timestamp:1699776266
2023-11-12T08:04:26,366 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:26,366 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:53860 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:26,366 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:26,366 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 73054, Backend time ns: 22355129
2023-11-12T08:04:26,366 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776266
2023-11-12T08:04:26,366 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776266
[I 231112 08:04:26 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 31.02ms
[I 231112 08:04:26 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:26,602 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776266602
2023-11-12T08:04:26,604 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776266
2023-11-12T08:04:26,624 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.49|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:14986451-0197-4504-a915-0ea70f1abfcb,timestamp:1699776266
2023-11-12T08:04:26,624 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.78|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:14986451-0197-4504-a915-0ea70f1abfcb,timestamp:1699776266
2023-11-12T08:04:26,624 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:26,624 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:53862 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:26,624 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:26,624 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 74379, Backend time ns: 22115857
2023-11-12T08:04:26,624 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776266
2023-11-12T08:04:26,625 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776266
[I 231112 08:04:26 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 39.58ms
[I 231112 08:04:26 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:26,871 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776266871
2023-11-12T08:04:26,873 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776266
2023-11-12T08:04:26,893 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.42|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:2dc92336-f6a2-4d18-90c6-9c9787d8aab9,timestamp:1699776266
2023-11-12T08:04:26,893 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.68|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:2dc92336-f6a2-4d18-90c6-9c9787d8aab9,timestamp:1699776266
2023-11-12T08:04:26,893 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:26,893 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:53864 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:26,893 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:26,893 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 67501, Backend time ns: 22197555
2023-11-12T08:04:26,893 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776266
2023-11-12T08:04:26,893 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776266
[I 231112 08:04:26 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 35.27ms
[I 231112 08:04:27 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:27,094 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776267094
2023-11-12T08:04:27,096 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776267
2023-11-12T08:04:27,115 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.4|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:a844fc68-66aa-406a-ace0-6594b464e58e,timestamp:1699776267
2023-11-12T08:04:27,116 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.69|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:a844fc68-66aa-406a-ace0-6594b464e58e,timestamp:1699776267
2023-11-12T08:04:27,116 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:27,116 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:53876 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:27,116 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:27,116 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 67524, Backend time ns: 22228199
2023-11-12T08:04:27,116 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776267
2023-11-12T08:04:27,116 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776267
[I 231112 08:04:27 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 41.58ms
[I 231112 08:04:27 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:27,324 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776267324
2023-11-12T08:04:27,326 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776267
2023-11-12T08:04:27,346 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.45|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:1c29f30e-1c45-4fd8-9309-5c0dbcbce47e,timestamp:1699776267
2023-11-12T08:04:27,346 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.7|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:1c29f30e-1c45-4fd8-9309-5c0dbcbce47e,timestamp:1699776267
2023-11-12T08:04:27,346 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:27,346 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:53886 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:27,346 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:27,346 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 64477, Backend time ns: 22097910
2023-11-12T08:04:27,346 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776267
2023-11-12T08:04:27,347 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776267
[I 231112 08:04:27 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 31.73ms
[I 231112 08:04:27 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:27,525 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776267525
2023-11-12T08:04:27,527 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776267
2023-11-12T08:04:27,547 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.2|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:4324ead6-64ce-4e79-8c7f-5c2ae9731ffc,timestamp:1699776267
2023-11-12T08:04:27,547 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.45|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:4324ead6-64ce-4e79-8c7f-5c2ae9731ffc,timestamp:1699776267
2023-11-12T08:04:27,547 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:27,547 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:53894 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:27,547 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:27,547 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 69558, Backend time ns: 21822303
2023-11-12T08:04:27,547 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776267
2023-11-12T08:04:27,547 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776267
[I 231112 08:04:27 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 31.91ms
[I 231112 08:04:27 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:27,743 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776267743
2023-11-12T08:04:27,745 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776267
2023-11-12T08:04:27,766 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.26|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:efbac492-95f1-4327-827f-db6a85f0a584,timestamp:1699776267
2023-11-12T08:04:27,766 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.53|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:efbac492-95f1-4327-827f-db6a85f0a584,timestamp:1699776267
2023-11-12T08:04:27,766 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:27,766 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:53902 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:27,766 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:27,766 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 82856, Backend time ns: 22898621
2023-11-12T08:04:27,766 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776267
2023-11-12T08:04:27,766 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776267
[I 231112 08:04:27 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 49.04ms
[I 231112 08:04:27 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:27,961 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776267961
2023-11-12T08:04:27,962 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776267
2023-11-12T08:04:27,982 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.37|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:a083cf6d-a14a-4582-9541-1290274b2a8e,timestamp:1699776267
2023-11-12T08:04:27,982 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.64|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:a083cf6d-a14a-4582-9541-1290274b2a8e,timestamp:1699776267
2023-11-12T08:04:27,982 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:27,983 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:53914 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:27,983 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:27,983 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 79717, Backend time ns: 22101510
2023-11-12T08:04:27,983 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776267
2023-11-12T08:04:27,983 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776267
[I 231112 08:04:27 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 30.75ms
[I 231112 08:04:28 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:28,213 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776268213
2023-11-12T08:04:28,215 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776268
2023-11-12T08:04:28,235 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.44|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:407ce757-78ae-45b8-88fd-adcef1f18b0b,timestamp:1699776268
2023-11-12T08:04:28,235 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.74|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:407ce757-78ae-45b8-88fd-adcef1f18b0b,timestamp:1699776268
2023-11-12T08:04:28,235 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:28,235 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:53918 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:28,235 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:28,235 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 72118, Backend time ns: 22200905
2023-11-12T08:04:28,236 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776268
2023-11-12T08:04:28,236 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776268
[I 231112 08:04:28 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 31.18ms
[I 231112 08:04:28 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:28,455 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776268455
2023-11-12T08:04:28,457 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776268
2023-11-12T08:04:28,477 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.97|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:181e5a4e-fde5-44da-b3bd-554a9cf697a6,timestamp:1699776268
2023-11-12T08:04:28,477 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.23|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:181e5a4e-fde5-44da-b3bd-554a9cf697a6,timestamp:1699776268
2023-11-12T08:04:28,478 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:28,478 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:53934 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:28,478 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:28,478 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 82312, Backend time ns: 22661709
2023-11-12T08:04:28,478 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776268
2023-11-12T08:04:28,478 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776268
[I 231112 08:04:28 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 31.38ms
[I 231112 08:04:28 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:28,664 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776268664
2023-11-12T08:04:28,666 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776268
2023-11-12T08:04:28,686 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:20.18|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:831f3ca4-efc1-402d-9cec-43c3354031c0,timestamp:1699776268
2023-11-12T08:04:28,686 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:20.45|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:831f3ca4-efc1-402d-9cec-43c3354031c0,timestamp:1699776268
2023-11-12T08:04:28,687 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 22
2023-11-12T08:04:28,687 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:53940 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:28,687 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:28,687 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 68821, Backend time ns: 22902882
2023-11-12T08:04:28,687 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776268
2023-11-12T08:04:28,687 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776268
[I 231112 08:04:28 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 31.96ms
[I 231112 08:04:28 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:28,881 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776268881
2023-11-12T08:04:28,883 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776268
2023-11-12T08:04:28,902 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.29|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:385d97ef-70ab-46ed-bea9-1de2643f2026,timestamp:1699776268
2023-11-12T08:04:28,902 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.56|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:385d97ef-70ab-46ed-bea9-1de2643f2026,timestamp:1699776268
2023-11-12T08:04:28,902 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 20
2023-11-12T08:04:28,903 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:53954 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:28,903 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:28,903 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 98242, Backend time ns: 22016871
2023-11-12T08:04:28,903 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776268
2023-11-12T08:04:28,903 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776268
[I 231112 08:04:28 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 30.99ms
[I 231112 08:04:29 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:29,082 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776269082
2023-11-12T08:04:29,084 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776269
2023-11-12T08:04:29,104 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.33|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:382f76cb-daf6-41d7-97a3-b00cabb2edef,timestamp:1699776269
2023-11-12T08:04:29,104 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.6|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:382f76cb-daf6-41d7-97a3-b00cabb2edef,timestamp:1699776269
2023-11-12T08:04:29,104 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:29,104 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:53964 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:29,104 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:29,104 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 72141, Backend time ns: 21935884
2023-11-12T08:04:29,104 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776269
2023-11-12T08:04:29,104 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776269
[I 231112 08:04:29 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 34.43ms
[I 231112 08:04:29 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:29,266 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776269266
2023-11-12T08:04:29,268 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776269
2023-11-12T08:04:29,288 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.2|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:13a5eb3c-28f2-4093-b4a8-112dcb944b5e,timestamp:1699776269
2023-11-12T08:04:29,288 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.47|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:13a5eb3c-28f2-4093-b4a8-112dcb944b5e,timestamp:1699776269
2023-11-12T08:04:29,288 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:29,288 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:53978 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:29,288 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:29,288 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 82756, Backend time ns: 21949167
2023-11-12T08:04:29,288 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776269
2023-11-12T08:04:29,289 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776269
[I 231112 08:04:29 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 30.76ms
[I 231112 08:04:29 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:29,462 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776269462
2023-11-12T08:04:29,465 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776269
2023-11-12T08:04:29,486 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:21.2|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:83adef93-e3c9-440c-8158-21837a7c14ca,timestamp:1699776269
2023-11-12T08:04:29,486 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:21.46|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:83adef93-e3c9-440c-8158-21837a7c14ca,timestamp:1699776269
2023-11-12T08:04:29,487 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 24
2023-11-12T08:04:29,487 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:53988 "POST /v1/models/cifar10:predict HTTP/1.1" 200 25
2023-11-12T08:04:29,487 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:29,487 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 134901, Backend time ns: 25033037
2023-11-12T08:04:29,487 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776269
2023-11-12T08:04:29,488 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776269
[I 231112 08:04:29 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 35.09ms
[I 231112 08:04:29 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:29,747 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776269747
2023-11-12T08:04:29,749 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776269
2023-11-12T08:04:29,768 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.32|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:36d70337-eb16-4952-bf56-12d07311a013,timestamp:1699776269
2023-11-12T08:04:29,769 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.6|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:36d70337-eb16-4952-bf56-12d07311a013,timestamp:1699776269
2023-11-12T08:04:29,769 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:29,769 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:53998 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:29,769 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:29,769 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 92992, Backend time ns: 22011651
2023-11-12T08:04:29,769 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776269
2023-11-12T08:04:29,769 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776269
[I 231112 08:04:29 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 32.43ms
[I 231112 08:04:29 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:29,948 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776269948
2023-11-12T08:04:29,950 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776269
2023-11-12T08:04:29,969 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.3|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:951955e7-7633-48ef-a6b5-90bb54b36a21,timestamp:1699776269
2023-11-12T08:04:29,970 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.55|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:951955e7-7633-48ef-a6b5-90bb54b36a21,timestamp:1699776269
2023-11-12T08:04:29,970 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:29,970 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:54000 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:04:29,970 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:29,970 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 79148, Backend time ns: 21832424
2023-11-12T08:04:29,970 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776269
2023-11-12T08:04:29,970 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776269
[I 231112 08:04:29 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 30.86ms
[I 231112 08:04:50 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:04:50,566 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776290566
2023-11-12T08:04:50,568 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776290
2023-11-12T08:04:50,588 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.59|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:539fa943-127c-4ec8-9388-04f6821d580e,timestamp:1699776290
2023-11-12T08:04:50,588 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.92|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:539fa943-127c-4ec8-9388-04f6821d580e,timestamp:1699776290
2023-11-12T08:04:50,588 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:04:50,589 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:56316 "POST /v1/models/cifar10:predict HTTP/1.1" 200 23
2023-11-12T08:04:50,589 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:04:50,589 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 147487, Backend time ns: 22402767
2023-11-12T08:04:50,589 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776290
2023-11-12T08:04:50,589 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776290
[I 231112 08:04:50 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 40.86ms
2023-11-12T08:05:18,333 [INFO ] pool-3-thread-2 TS_METRICS - CPUUtilization.Percent:0.0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776318
2023-11-12T08:05:18,334 [INFO ] pool-3-thread-2 TS_METRICS - DiskAvailable.Gigabytes:14.067066192626953|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776318
2023-11-12T08:05:18,334 [INFO ] pool-3-thread-2 TS_METRICS - DiskUsage.Gigabytes:45.92119598388672|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776318
2023-11-12T08:05:18,334 [INFO ] pool-3-thread-2 TS_METRICS - DiskUtilization.Percent:76.6|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776318
2023-11-12T08:05:18,334 [INFO ] pool-3-thread-2 TS_METRICS - GPUMemoryUtilization.Percent:7.386326030842544|#Level:Host,device_id:0|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776318
2023-11-12T08:05:18,334 [INFO ] pool-3-thread-2 TS_METRICS - GPUMemoryUsed.Megabytes:1116|#Level:Host,device_id:0|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776318
2023-11-12T08:05:18,334 [INFO ] pool-3-thread-2 TS_METRICS - GPUUtilization.Percent:0|#Level:Host,device_id:0|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776318
2023-11-12T08:05:18,334 [INFO ] pool-3-thread-2 TS_METRICS - MemoryAvailable.Megabytes:27076.88671875|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776318
2023-11-12T08:05:18,334 [INFO ] pool-3-thread-2 TS_METRICS - MemoryUsed.Megabytes:4074.91015625|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776318
2023-11-12T08:05:18,334 [INFO ] pool-3-thread-2 TS_METRICS - MemoryUtilization.Percent:14.4|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776318
2023-11-12T08:06:18,323 [INFO ] pool-3-thread-2 TS_METRICS - CPUUtilization.Percent:0.0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776378
2023-11-12T08:06:18,323 [INFO ] pool-3-thread-2 TS_METRICS - DiskAvailable.Gigabytes:14.06728744506836|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776378
2023-11-12T08:06:18,323 [INFO ] pool-3-thread-2 TS_METRICS - DiskUsage.Gigabytes:45.92097473144531|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776378
2023-11-12T08:06:18,323 [INFO ] pool-3-thread-2 TS_METRICS - DiskUtilization.Percent:76.5|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776378
2023-11-12T08:06:18,323 [INFO ] pool-3-thread-2 TS_METRICS - GPUMemoryUtilization.Percent:7.386326030842544|#Level:Host,device_id:0|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776378
2023-11-12T08:06:18,323 [INFO ] pool-3-thread-2 TS_METRICS - GPUMemoryUsed.Megabytes:1116|#Level:Host,device_id:0|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776378
2023-11-12T08:06:18,323 [INFO ] pool-3-thread-2 TS_METRICS - GPUUtilization.Percent:0|#Level:Host,device_id:0|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776378
2023-11-12T08:06:18,323 [INFO ] pool-3-thread-2 TS_METRICS - MemoryAvailable.Megabytes:27071.38671875|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776378
2023-11-12T08:06:18,323 [INFO ] pool-3-thread-2 TS_METRICS - MemoryUsed.Megabytes:4080.109375|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776378
2023-11-12T08:06:18,323 [INFO ] pool-3-thread-2 TS_METRICS - MemoryUtilization.Percent:14.4|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776378
[W 231112 08:06:23 web:2271] 404 POST /v2/models/ (127.0.0.1) 0.46ms
[W 231112 08:06:32 web:2271] 404 GET /v2/models/ (127.0.0.1) 0.43ms
[I 231112 08:06:37 web:2271] 200 GET /v2/models (127.0.0.1) 0.61ms
2023-11-12T08:07:18,327 [INFO ] pool-3-thread-2 TS_METRICS - CPUUtilization.Percent:0.0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776438
2023-11-12T08:07:18,328 [INFO ] pool-3-thread-2 TS_METRICS - DiskAvailable.Gigabytes:14.066795349121094|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776438
2023-11-12T08:07:18,328 [INFO ] pool-3-thread-2 TS_METRICS - DiskUsage.Gigabytes:45.92146682739258|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776438
2023-11-12T08:07:18,328 [INFO ] pool-3-thread-2 TS_METRICS - DiskUtilization.Percent:76.6|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776438
2023-11-12T08:07:18,328 [INFO ] pool-3-thread-2 TS_METRICS - GPUMemoryUtilization.Percent:7.386326030842544|#Level:Host,device_id:0|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776438
2023-11-12T08:07:18,328 [INFO ] pool-3-thread-2 TS_METRICS - GPUMemoryUsed.Megabytes:1116|#Level:Host,device_id:0|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776438
2023-11-12T08:07:18,328 [INFO ] pool-3-thread-2 TS_METRICS - GPUUtilization.Percent:0|#Level:Host,device_id:0|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776438
2023-11-12T08:07:18,328 [INFO ] pool-3-thread-2 TS_METRICS - MemoryAvailable.Megabytes:27074.11328125|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776438
2023-11-12T08:07:18,328 [INFO ] pool-3-thread-2 TS_METRICS - MemoryUsed.Megabytes:4077.47265625|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776438
2023-11-12T08:07:18,328 [INFO ] pool-3-thread-2 TS_METRICS - MemoryUtilization.Percent:14.4|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776438
[I 231112 08:07:32 web:2271] 200 GET /v2/models (127.0.0.1) 0.43ms
[I 231112 08:07:39 TorchserveModel:76] PREDICTOR_HOST : 0.0.0.0:8085
2023-11-12T08:07:39,826 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Flushing req. to backend at: 1699776459826
2023-11-12T08:07:39,828 [INFO ] W-9000-cifar10_1-stdout MODEL_LOG - Backend received inference at: 1699776459
2023-11-12T08:07:39,848 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - HandlerTime.Milliseconds:19.42|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:6fe5e907-e8be-4b12-936f-44a45b2c5724,timestamp:1699776459
2023-11-12T08:07:39,848 [INFO ] W-9000-cifar10_1-stdout MODEL_METRICS - PredictionTime.Milliseconds:19.72|#ModelName:cifar10,Level:Model|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,requestID:6fe5e907-e8be-4b12-936f-44a45b2c5724,timestamp:1699776459
2023-11-12T08:07:39,848 [INFO ] W-9000-cifar10_1 org.pytorch.serve.wlm.WorkerThread - Backend response time: 21
2023-11-12T08:07:39,848 [INFO ] W-9000-cifar10_1 ACCESS_LOG - /127.0.0.1:34550 "POST /v1/models/cifar10:predict HTTP/1.1" 200 22
2023-11-12T08:07:39,848 [INFO ] W-9000-cifar10_1 TS_METRICS - Requests2XX.Count:1|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776243
2023-11-12T08:07:39,848 [DEBUG] W-9000-cifar10_1 org.pytorch.serve.job.Job - Waiting time ns: 99253, Backend time ns: 22192367
2023-11-12T08:07:39,849 [INFO ] W-9000-cifar10_1 TS_METRICS - QueueTime.ms:0|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776459
2023-11-12T08:07:39,849 [INFO ] W-9000-cifar10_1 TS_METRICS - WorkerThreadTime.ms:2|#Level:Host|#hostname:torchserve-predictor-default-00001-deployment-7d79b49884-p8ggm,timestamp:1699776459
[I 231112 08:07:39 web:2271] 200 POST /v2/models/cifar10/infer (127.0.0.1) 32.79ms
```
