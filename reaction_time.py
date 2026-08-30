
from harp.serial import open_device

import device as beh

COM_PORT = "COM3"

LED_PIN = beh.DigitalOutputs.DO_PORT0  # 1 or 0x01 also works...
INPUT_PIN = beh.DigitalInputs.DI_PORT0  # 1 or 0x01 also works...

with open_device(beh, port=COM_PORT) as this_device:
    led_on_msg = this_device.write(beh.OutputSet, LED_PIN)  # You can also use

    state = False
    msg = None
    while state is False:
        msg = this_device.read(beh.DigitalInputState)
        state = (msg.payload & INPUT_PIN) > 0

    rx = msg.timestamp - led_on_msg.timestamp
    print(f"Reaction time: {rx}")
    this_device.write(
        beh.OutputClear, LED_PIN
    )  # You can also use beh.DigitalOutputs.DO_PORT0
