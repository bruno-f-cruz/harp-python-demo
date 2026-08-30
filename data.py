
from harp.data import open_dataset, parse_to_dataframe

import device as beh

dataset = open_dataset("dataset.harp")
df_analog = dataset.read(beh.AnalogData)
print(df_analog)

df_digital_state = dataset.read(beh.DigitalInputState)
print(df_digital_state)

df_no_dataset = parse_to_dataframe(beh.AnalogData, "./dataset.harp/Behavior_44.bin")
print(df_no_dataset)
