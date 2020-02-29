import json
from os import fspath
from skimage import io
from flask import request
from flask_restful import Resource
from keras.models import load_model
from config.application import storage_path
from yolo3.utils.utils import get_yolo_boxes


class PredictionController(Resource):

    net_h, net_w = 416, 416
    obj_thresh, nms_thresh = 0.5, 0.45

    model_compiled = {
        'model_1': fspath(storage_path.joinpath('model/yolo3_full_fault_1.h5')),
        'model_2': fspath(storage_path.joinpath('model/yolo3_full_fault_4.h5'))
    }

    model_config = {
        'model_1': fspath(storage_path.joinpath('model/config/config_full_yolo_fault_1_infer.json')),
        'model_2': fspath(storage_path.joinpath('model/config/config_full_yolo_fault_4_infer.json'))
    }

    model = dict()

    def __init__(self):
        self.model['model_1'] = load_model(self.model_compiled['model_1'])
        self.model['model_2'] = load_model(self.model_compiled['model_2'])

    def post(self):
        collection = request.get_json()
        images = [io.imread(item['url']) for item in collection]

        with open(self.model_config['model_1']) as config_buffer:
            config_1 = json.load(config_buffer)
        with open(self.model_config['model_2']) as config_buffer:
            config_2 = json.load(config_buffer)

        labels_1 = config_1['model']['labels']
        labels_2 = config_2['model']['labels']

        boxes_p_1 = get_yolo_boxes(
            self.model['model_1'],
            images,
            self.net_h,
            self.net_w, config_1['model']['anchors'],
            self.obj_thresh,
            self.nms_thresh)

        boxes_p_2 = get_yolo_boxes(
            self.model['model_2'],
            images,
            self.net_h,
            self.net_w,
            config_2['model']['anchors'],
            self.obj_thresh,
            self.nms_thresh)

        for index, item in enumerate(collection):
            item['objects'] = list()

            for boxes in boxes_p_1[index]:
                item['objects'].append({
                    'class': labels_1[boxes.label],
                    'label': 'Soiling Fault',
                    'score': boxes.score,
                    'xmax': boxes.xmax,
                    'xmin': boxes.xmin,
                    'ymax': boxes.ymax,
                    'ymin': boxes.ymax
                })

            for boxes in boxes_p_2[index]:
                item['objects'].append({
                    'class': labels_2[boxes.label],
                    'score': boxes.score,
                    'label': 'Diode Fault',
                    'xmax': boxes.xmax,
                    'xmin': boxes.xmin,
                    'ymax': boxes.ymax,
                    'ymin': boxes.ymax
                })

        return collection
