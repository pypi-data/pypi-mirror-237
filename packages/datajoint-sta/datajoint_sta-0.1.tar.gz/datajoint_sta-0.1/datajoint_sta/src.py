import numpy as np
from matplotlib import pyplot as plt
import pickle as pkl

class Neurons():

    def __init__(self, datapkl='../data/ret1_data.pkl') -> None:
        with open(datapkl, 'rb') as datapath:
            self.data = pkl.load(datapath)

    
    
    def calc_sta(self, exp_num, delay=0):
        'calculates spike-trigerred-average of neuron number exp_num with a backward delay(s)'

        #sample = next(item for item in self.data if item["sample_number"] == sample_num)
        sample = self.data[exp_num]
        spike_times = sample['stimulations'][0]['spikes'][0]
        fps = sample['stimulations'][0]['fps']
        stim_onset = sample['stimulations'][0]['stimulus_onset']
        movie = sample['stimulations'][0]['movie']

        frame_nums = np.round((spike_times - stim_onset - delay) * fps).astype(int)
        frame_nums = frame_nums[frame_nums > 0]
        selected_frames = movie[:,:,frame_nums]
        sta = np.mean(selected_frames, axis=2)

        return sta

    def visualize_stim(self, stim, x_size=640, y_size=480):
        'visualized a stimulus'
        
        plt.figure()
        plt.imshow(stim.T, extent=(0,x_size,0,y_size), cmap='gray', vmin=-1, vmax=1)

    
    def visualize_frame(self, sample_num, frame_num):
        'visualizes the stimulus with frame_num in sample sample_num'

        sample = next(item for item in self.data if item["sample_number"] == sample_num)
        x_size = sample['stimulations'][0]['stim_width']
        y_size = sample['stimulations'][0]['stim_height']
        stim = sample['stimulations'][0]['movie'][:,:,frame_num]
        self.visualize_stim(stim, x_size, y_size)

    def visualize_sta(self, exp_num, delay=0):
        sta = self.calc_sta(exp_num, delay)
        self.visualize_stim(sta)
