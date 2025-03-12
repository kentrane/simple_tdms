# Description: Read data from a TDMS file using the nptdms library
# Author: Kenneth Petersen
from nptdms import TdmsFile
import numpy as np

def read_tdms_file(file_path):
    try:
        # read the TDMS file into memory
        tdms_file = TdmsFile.read(file_path)
        
        # Get all groups in the file
        groups = tdms_file.groups()
        print(groups.name)
        
        data = {}
        for group in groups:
            # Get all channels in the group
            channels = group.channels()
            print(channels.name)

            # Store data for each channel
            group_data = {}
            for channel in channels:
                
                # Read channel data into numpy array
                channel_data = channel[:]
                
                # Store channel data and properties
                group_data[channel.name] = {
                    'data': channel_data,
                    'properties': channel.properties
                }
            
            data[group.name] = group_data
            
        return data
    
    except Exception as e:
        print(f"Error reading TDMS file: {e}")
        return None

if __name__ == "__main__":
    file_path = "datafile.tdms"
    data = read_tdms_file(file_path)
    
    if data:
        print("Successfully read TDMS file")