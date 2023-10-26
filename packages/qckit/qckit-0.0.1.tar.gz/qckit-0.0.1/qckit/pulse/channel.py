from qiskit.pulse.channels import Channel, DriveChannel, ControlChannel, MeasureChannel, AcquireChannel



def channel_to_str(channel):
    """
    Converts a channel object to a string representation.

    Args:
        channel (Channel): The channel object to convert.

    Returns:
        str: The string representation of the channel object.
    """
    if isinstance(channel, DriveChannel):
        channel_str = "d" + str(channel.index)
    elif isinstance(channel, ControlChannel):
        channel_str = "u" + str(channel.index)
    elif isinstance(channel, MeasureChannel):
        channel_str = "m" + str(channel.index)
    elif isinstance(channel, AcquireChannel):
        channel_str = "a" + str(channel.index)
    elif isinstance(channel, str) and channel[0] in ['d', 'u', 'm', 'a']:
        try:
            int(channel[1:])
            channel_str = channel
        except Exception as exp:
            raise exp
    else:
        raise ValueError("Input must be one of the qiskit.pulse.channels.Channel objects.")
    return channel_str



def str_to_channel(channel_str):
    """
    Converts a string representation of a channel to a channel object.

    Args:
        channel_str (str): The string representation of the channel.

    Returns:
        Channel: The channel object.
    """
    if channel_str[0] == 'd':
        channel = DriveChannel(int(channel_str[1:]))
    elif channel_str[0] == 'u':
        channel = ControlChannel(int(channel_str[1:]))
    elif channel_str[0] == 'm':
        channel = MeasureChannel(int(channel_str[1:]))
    elif channel_str[0] == 'a':
        channel = AcquireChannel(int(channel_str[1:]))
    elif isinstance(channel_str, Channel):
        channel = channel_str
    else:
        raise ValueError("Input must be a string representation of a qiskit.pulse.channels.Channel object.")
    return channel



def channel_rep(channel, use_channel = False):
    """
    Converts a channel object to a string representation or a string representation to a channel object.

    Args:
        channel (Union[Channel, str]): The channel object or string representation to convert.
        use_channel (bool): If True, converts a string representation to a channel object. If False, converts a channel object
            to a string representation.

    Returns:
        Union[Channel, str]: The converted channel object or string representation.
    """
    if use_channel and isinstance(channel, str):
        return str_to_channel(channel)
    else:
        return channel_to_str(channel)
