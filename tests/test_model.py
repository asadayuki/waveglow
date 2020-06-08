import torch
import json
from src.model import Invertible1x1Conv, WaveGlow


CONFIG_FILE = 'src/config.json'

def test_invertible_conv():
    conv = Invertible1x1Conv(c=4)
    batch_size, group_size, n_of_groups  = 12, 4,100
    z = torch.rand(batch_size, group_size, n_of_groups)
    z_1, _ = conv.forward(z)
    z_2 = conv.forward(z_1, reverse=True)
    assert torch.allclose(z, z_2, rtol=1e-3) , "reverse convolution does not give original tensor"


def test_waveglow_forward_inbatch_independence():

    with open(CONFIG_FILE) as f:
        data = f.read()
    config = json.loads(data)
    waveglow_config = config["waveglow_config"]
    wg = WaveGlow(**waveglow_config)

    spect1  = torch.Tensor(1, waveglow_config['n_mel_channels'], 63)
    spect2  = torch.Tensor(1, waveglow_config['n_mel_channels'], 63)
    audio1 = torch.Tensor(1, 16000)
    audio2 = torch.Tensor(1,16000)
    spect_batch = torch.cat((spect1, spect2), 0)
    audio_batch = torch.cat((audio1, audio2), 0)

    output_audio, log_s_list, log_det_W_list = wg.forward((spect1, audio1))
    output_audio_batch, log_s_list_batch, log_det_W_list_batch = wg.forward((spect_batch, audio_batch))
    print(log_s_list[-1].size())
    print(log_s_list_batch[-1].size())

    assert torch.allclose(log_s_list[-1], log_s_list_batch[-1][0:1,:,:]) , "samples in batch interfer with each other"
    