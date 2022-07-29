# Smart IoT Library
import requests
import torchaudio 
import matplotlib.pyplot as plt
from IPython.display import Audio, display

def version():
  '''
    Shows smart IoT library version
  '''
  print('Smart IoT Library ver. 1.5.0')
  
def load_audio(url, fname):
  '''
  Regresa la señal de audio, sample-rate, metadata, byte-size
  '''
  r = requests.get(url)
  with open(fname, 'wb') as f:
    f.write(r.content)

  sz = len(r.content)
  meta = torchaudio.info(fname)
  wave, sr = torchaudio.load(fname)

  return (wave, sr, meta, sz)

def print_info(info, fname=None):
  if fname:
    print('-'*30)
    print('Filename: '+fname)
    print('-'*30)

  wave, sr, meta, sz= info
  channels, frames = wave.shape
  print(f'            Frames: {frames}')
  print(f'          Channels: {channels}')
  print(f'   Audio File Size: {sz} bytes')
  print(f'Tensor memory size: {wave.element_size() * channels * frames} bytes')
  print(f'             Dtype: {wave.dtype}')
  print(f'               Max: {wave.max().item():6.3f}')
  print(f'               Min: {wave.min().item():6.3f}')
  print(f'              Mean: {wave.mean().item():6.3f}')
  print(f'           Std Dev: {wave.max().std():6.3f}')
  print(wave)
  
def plot_wave(wave, torch=True):
  '''
    Graficar una señal de audio en PyTorch o Numpy 
  '''
  plt.figure()
  plt.plot(wave[0].numpy() if torch else wave)

def play_audio(waveform, sample_rate, torch=True):
  '''
    Reproducir una señal de audio.
  '''
  if torch:
    waveform = waveform.numpy()
    num_channels, num_frames = waveform.shape
  else:
    display(Audio(waveform, rate=sample_rate))
    return
  
  if num_channels == 1:
    display(Audio(waveform[0], rate=sample_rate))
  elif num_channels == 2:
    display(Audio((waveform[0], waveform[1]), rate=sample_rate))
  else:
    raise ValueError('Forma de la señal no soporta más de dos canales')

 def plot_fft(wave, max_freq=None):
  '''
    Graficar la señal transformada FFT desde 0 hasta la frecuencia máxima
  '''
  wave2 = wave[:max_freq] if max_freq else wave
  wave3 = np.abs(wave2.real)
  plt.figure()
  plt.plot(wave3, lw=1, color='green')
