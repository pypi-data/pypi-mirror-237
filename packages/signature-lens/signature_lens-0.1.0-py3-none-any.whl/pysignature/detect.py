from pathlib import Path

import numpy as np
import torch
from ultralytics.utils.plotting import save_one_box

from pysignature.models.common import DetectMultiBackend
from pysignature.utils.augmentations import letterbox
from pysignature.utils.general import (
    Profile,
    check_img_size,
    non_max_suppression,
    scale_boxes,
)
from pysignature.utils.torch_utils import select_device, smart_inference_mode


WEIGHTS = Path("weights.pt")


@smart_inference_mode()
def run(
    image_: np.ndarray,
    padding: int | None = None,
    weights: Path = WEIGHTS,  # model path or triton URL
    imgsz: tuple = (640, 640),  # inference size (height, width)
    conf_thres: float = 0.25,  # confidence threshold
    iou_thres: float = 0.45,  # NMS IOU threshold
    device: str = "",  # cuda device, i.e. 0 or 0,1,2,3 or cpu
    agnostic_nms: bool = False,  # class-agnostic NMS
    augment: bool = False,  # augmented inference
    half: bool = False,  # use FP16 half-precision inference
    dnn: bool = False,  # use OpenCV DNN for ONNX inference
) -> np.ndarray:
    """Detect signature and return the corresponding cropped image"""
    # Load model
    device = select_device(device)
    model = DetectMultiBackend(weights, device=device, dnn=dnn, data=None, fp16=half)
    stride, pt = model.stride, model.pt
    imgsz = check_img_size(imgsz, s=stride)  # check image size

    # Dataloader
    bs = 1  # batch_size

    # Run inference
    model.warmup(imgsz=(1 if pt or model.triton else bs, 3, *imgsz))  # warmup
    dt = (Profile(), Profile(), Profile())
    im = letterbox(image_, imgsz, stride=stride, auto=pt)[0]  # padded resize
    im = im.transpose((2, 0, 1))[::-1]  # HWC to CHW, BGR to RGB
    im = np.ascontiguousarray(im)
    # for path, im, im0s, _, s in dataset:
    with dt[0]:
        im = torch.from_numpy(im).to(model.device)
        im = im.half() if model.fp16 else im.float()  # uint8 to fp16/32
        im /= 255  # 0 - 255 to 0.0 - 1.0
        if len(im.shape) == 3:
            im = im[None]  # expand for batch dim

    # Inference
    with dt[1]:
        pred = model(im, augment=augment, visualize=False)
    # NMS
    with dt[2]:
        pred = non_max_suppression(pred, conf_thres, iou_thres, 1, agnostic_nms, max_det=1)[0]

    # Process prediction
    imc = image_.copy()  # for save_crop
    if len(pred):
        # Rescale boxes from img_size to im0 size
        pred[:, :4] = scale_boxes(im.shape[2:], pred[:, :4], image_.shape).round()

        # Write results
        *xyxy, _, _ = list(reversed(pred))[0]
        if padding:
            xyxy[0] = xyxy[0] - padding
            xyxy[1] = xyxy[1] - padding
            xyxy[2] = xyxy[2] + padding
            xyxy[3] = xyxy[3] + padding
        result = save_one_box(xyxy, imc, BGR=True, save=False)
        return result
