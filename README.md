# YOLOv8

- PC dependencies
- Training
- Export `onnx`
- Run model on the PC

## Dependencies

```bash
python3 -m venv env
source ./env/bin/activate
pip install -r ./requirements.txt
```

## Training.

I used [VisDrone](https://github.com/VisDrone/VisDrone-Dataset?tab=readme-ov-file) dataset. You can use any another.

Download, move it to `model_train/datasets/VisDrone`. 

Python sript `ann2yolo.py` converts annotations to labels for YOLO. Execute the script. Dataset is ready to train YOLO.

`VisDrone.yaml` is smth like pointers to data and classes. We refer to it in the file `train.py`.

Next, in the `train.py` script, we set the file&dir paths and training parameters. All possible training parameters are described in the Ultralytics [documentation for training](https://docs.ultralytics.com/modes/train/).

We cross our fingers for enough memory and execute. If there is not enough memory, we reduce the batch size.

```bash
python3 train.py
```

If you have an Nvidia GPU, then let's go have coffee, otherwise, you can go to bed, this will take a long time.

Table for understanding:
```
|   device | memory | BATCH_SIZE | time for 1 epoch |
| RTX 3060 |   12GB |         16 |            ~1min |
| i5 11400 |   32GB |         16 |           ~20min |
```

The higher we get the `mAP` parameter, the better.

After training, copy `last.pt` from `./save/VisDrone/run/weights` to `./train_result`. Rename it as we please.

#Export ONNX

We export the model to `onnx` using `pt2onnx.py`, having previously specified the model name in the script. All possible export parameters are described in the Ultralytics [documentation for export](https://docs.ultralytics.com/modes/export/).

```bash
python3 pt2onnx.py
```

## Run model on th PC.

I'll add it the future.