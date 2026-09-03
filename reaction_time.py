import time

from harp.device import core
from harp.serial import open_device

import device as beh

COM_PORT = "COM11"
TIMEOUT_S = 3.0

LED_PIN = beh.DigitalOutputs.DO_PORT0  # 1 or 0x01 also works...
INPUT_PIN = beh.DigitalInputs.DI_PORT0  # 1 or 0x01 also works...

with open_device(beh, port=COM_PORT) as this_device:

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

    led_on_msg = this_device.write(beh.OutputSet, LED_PIN)  # You can also use
    print(f"Led turned on at {led_on_msg.timestamp}")

    start_time = time.monotonic()
    while True:
        msg = this_device.read(beh.DigitalInputState)
        if msg.payload & INPUT_PIN > 0:
            break
        if time.monotonic() - start_time > TIMEOUT_S:
            print("Timeout: no response within 3 seconds")
            break

    if msg.payload & INPUT_PIN > 0:
        rx = msg.timestamp - led_on_msg.timestamp
        print(f"Reaction time: {rx}")
    else:
        print("No response detected")
    r = this_device.write(
        beh.OutputClear, LED_PIN
    )  # You can also use beh.DigitalOutputs.DO_PORT0
    print(f"Led turned off at {r.timestamp}")
