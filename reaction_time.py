
from harp.device import core
from harp.serial import open_device

import device as beh

COM_PORT = "COM3"

LED_PIN = beh.DigitalOutputs.DO_PORT0  # 1 or 0x01 also works...
INPUT_PIN = beh.DigitalInputs.DI_PORT0  # 1 or 0x01 also works...

with open_device(beh, port=COM_PORT) as this_device:
    led_on_msg = this_device.write(beh.OutputSet, LED_PIN)  # You can also use

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
    rx = msg.timestamp - led_on_msg.timestamp
    print(f"Reaction time: {rx}")
    this_device.write(
        beh.OutputClear, LED_PIN
    )  # You can also use beh.DigitalOutputs.DO_PORT0
