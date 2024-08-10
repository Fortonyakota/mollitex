import spcm

# Assuming `card` and `channels` are defined somewhere earlier
card = 0  # Example card number
channels = [0, 1]  # Example list of channels

# Creating an instance of DDS using spcm module
dds = spcm.DDS(card, channels=channels)

# Now `dds` can be used to interact with the DDS functionality
