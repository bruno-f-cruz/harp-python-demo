from time import sleep

from harp.device import core
from harp.protocol import HarpMessage, MessageType, RegisterU16
from harp.serial import open_device

import device as beh

COM_PORT = "COM3"


def handler(message: HarpMessage):
    print(f"Received message: {message}")


def specific_handler(message: HarpMessage[beh.DigitalInputs]):
    print(f"The state of the digital inputs is: {message.payload}")


with open_device(beh, port=COM_PORT) as this_device:
    print("Device connected")

    # Get Core registers
    whoami_response = this_device.read(core.WhoAmI)
    print(f"HarpMessage: {whoami_response}")
    print(f"WhoAmI: {whoami_response.payload}")
    device_name = this_device.read(core.DeviceName).payload
    print(f"Device Name: {device_name}")

    # Direct raw register access (mostly for development)
    whoami_raw_response = this_device.read(RegisterU16(0x00))
    print(f"Raw WhoAmI: {whoami_raw_response.payload}")

    with this_device.subscribe_all(
        handler, message_types=(MessageType.Read, MessageType.Write)
    ):
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
        sleep(1)

    with this_device.subscribe(
        register=beh.DigitalInputState,
        handler=specific_handler,
        message_types=(MessageType.Read, MessageType.Write),
    ):
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
        sleep(1)
