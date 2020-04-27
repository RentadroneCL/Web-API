import numpy as np


def get_yolo_boxes(model, images, net_h, net_w, anchors, obj_thresh, nms_thresh):
    image_h, image_w, _ = images[0].shape
    nb_images = len(images)
    batch_input = np.zeros((nb_images, net_h, net_w, 3))

    # preprocess the input
    for i in range(nb_images):
        batch_input[i] = preprocess_input(images[i], net_h, net_w)

    # run the prediction
    batch_output = model.predict_on_batch(batch_input)
    batch_boxes = [None] * nb_images

    for i in range(nb_images):
        yolos = [batch_output[0][i], batch_output[1][i], batch_output[2][i]]
        boxes = []

        # decode the output of the network
        for j in range(len(yolos)):
            yolo_anchors = anchors[
                (2 - j) * 6 : (3 - j) * 6
            ]  # config['model']['anchors']
            boxes += decode_netout(yolos[j], yolo_anchors, obj_thresh, net_h, net_w)

        # correct the sizes of the bounding boxes
        correct_yolo_boxes(boxes, image_h, image_w, net_h, net_w)

        # suppress non-maximal boxes
        do_nms(boxes, nms_thresh)

        batch_boxes[i] = boxes

    return batch_boxes


def disconnected(image, boxes, obj_thresh=0.5, area_min=400, merge=0, z_thresh=1.8):
    new_boxes = []
    for num, box in enumerate(boxes):

        xmin = box.xmin + merge
        xmax = box.xmax - merge
        ymin = box.ymin + merge
        ymax = box.ymax - merge

        if (
            xmin > 0
            and ymin > 0
            and xmax < image.shape[1]
            and ymax < image.shape[0]
            and box.get_score() > obj_thresh
        ):

            area = (ymax - ymin) * (xmax - xmin)
            z_score = (
                np.sum(image[np.int(ymin) : np.int(ymax), np.int(xmin) : np.int(xmax)])
                / area
            )

            if area > area_min:

                box.z_score = z_score
                new_boxes.append(box)
                # boxes_area_score[str(num)] = {'xmin': xmin, 'xmax': xmax, 'ymin': ymin, 'ymax': ymax, 'score' : score, 'area' : area}

    mean_score = np.mean([box.z_score for box in new_boxes])
    sd_score = np.std([box.z_score for box in new_boxes])

    new_boxes = [
        box for box in new_boxes if (box.z_score - mean_score) / sd_score > z_thresh
    ]

    for box in new_boxes:

        z_score = (box.z_score - mean_score) / sd_score
        box.classes[0] = min((z_score - z_thresh) * 0.5 / (3 - z_thresh) + 0.5, 1)

    return new_boxes
