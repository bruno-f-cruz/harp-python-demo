
from harp.protocol import HarpMessage
from harp.serial import open_device
from harp.device import core
import device as beh
from time import sleep

COM_PORT = "COM11"

global is_done
is_done = False

def print_encoder(message: HarpMessage[beh.AnalogDataPayload]):
    print(f"Encoder value: {message.payload.encoder}@{message.timestamp}")
    if message.payload.encoder > 1000:
        global is_done
        is_done = True

with open_device(beh, port=COM_PORT) as this_device:
    led_on_msg = this_device.write(beh.EnableEncoders, beh.EncoderInputs.ENCODER_PORT2)
    this_device.write(beh.EncoderReset,  beh.EncoderInputs.ENCODER_PORT2)
    with this_device.subscribe(beh.AnalogData, print_encoder):
        this_device.write(
            core.OperationControl,
            core.OperationControlPayload(
                operation_mode=core.OperationMode.ACTIVE,
                dump_registers=True,
                heartbeat=True,
                mute_replies=False,
                visual_indicators=True,
                operation_led=True,
            ),
        )
        while not is_done:
            sleep(0.1)
