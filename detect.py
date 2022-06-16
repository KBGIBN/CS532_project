import torch

# Model
#model = torch.hub.load('ultralytics/yolov5', 'custom', r'D:\UIT\CS532\final_project\yolov5\runs\train\yolov5s_results\weights\last.pt')  # or yolov5m, yolov5l, yolov5x, etc.
model = torch.hub.load('./yolov5', 'custom', path='./yolov5/runs/train/yolov5s_results/weights/last.pt', source='local')

# Images
im = './input/input.jpg'  # or file, Path, URL, PIL, OpenCV, numpy, list

# Inference
results = model(im)

# Results
#results.show()  # or .show(), .save(), .crop(), .pandas(), etc.

#results.xyxy[0]  # im predictions (tensor)
#print(results.pandas().xyxy[0])
results.crop(im)