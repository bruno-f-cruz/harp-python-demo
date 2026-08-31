
from harp.data import open_dataset, parse_to_dataframe

import device as beh

dataset = open_dataset("dataset.harp")


#  dataset = open_dataset("dataset.harp", device_module=beh)  # If you dont want to infer


df_analog = dataset.read(beh.AnalogData)
# df_analog = dataset.read("AnalogData")
# df_analog = dataset.read(dataset.device_module.AnalogData)
print(df_analog)

df_digital_state = dataset.read(beh.DigitalInputState)
print(df_digital_state)

df_digital_state = dataset.read("DigitalInputState", demux_bit_masks=True)
print(df_digital_state)

df_no_dataset = parse_to_dataframe(beh.AnalogData, "./dataset.harp/Behavior_44.bin")
print(df_no_dataset)
