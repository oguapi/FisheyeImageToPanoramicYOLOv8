# FisheyeImageToPanoramicYOLOv8detection
Fisheye image to Panoramic + Yolov8 object detection !

## Requirements
  * Python 3.9
  * requirements.txt

## Fisheye to Panoramic
We are working with the metod present in [this video](https://www.youtube.com/watch?v=QThcz7XQQPU&ab_channel=robotmania). Here we use the next:

![Algoritm used][lil-relation-url]

Just needed select the center point and the maxim radio accord to the input, for the example 1 is 280

![Input 1][lil-input1-url]

The panoramit result is 

![Outpu 1][lil-output1-url]

For the example 2 is 353

![Input 2][lil-input2-url]

The panoramit result is 

![Outpu 2][lil-output2-url]

## YOLOv8
We use YOLOv8 to do the detections. See the official repository [here](https://github.com/ultralytics/ultralytics)
where we download the pre-trained model yolov8n.pt. The result is the next:

![Detections][lil-dect-url]

[lil-relation-url]: https://raw.githubusercontent.com/oguapi/FisheyeImageToPanoramicYOLOv8/master/assets/relation.png
[lil-dect-url]: https://raw.githubusercontent.com/oguapi/FisheyeImageToPanoramicYOLOv8/master/assets/detectionsResult.png
[lil-input1-url]: https://raw.githubusercontent.com/oguapi/FisheyeImageToPanoramicYOLOv8/master/data/fisheyePhoto.jpg
[lil-output1-url]: https://raw.githubusercontent.com/oguapi/FisheyeImageToPanoramicYOLOv8/master/out.png
[lil-input2-url]: https://raw.githubusercontent.com/oguapi/FisheyeImageToPanoramicYOLOv8/master/data/fisheyePhoto2.jpg
[lil-output2-url]: https://raw.githubusercontent.com/oguapi/FisheyeImageToPanoramicYOLOv8/master/out2.png